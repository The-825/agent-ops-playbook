#!/usr/bin/env python3
"""Merge-decision logic for an agent-PR automerge gate. Second generation.

TEMPLATE. Copy to your workflow-scripts directory (conventionally
`.github/scripts/decision_script.py`) and edit the configuration block
below. Read AUTOMERGE_GOTCHAS.md first, especially "The second generation:
extract the decision, then graduate trust", which explains this file's
design and the maturity ladder it supports. The shipped `automerge.yml` in
this directory is the single-file starting point; this script is what that
workflow grows into when you add an operator label, protected paths, or
label-free lanes.

Pure functions. No network, no GitHub context, no side effects at import:
the workflow gathers the inputs (base branch, head branch, labels, draft
state, changed files, check runs, mergeable state) and calls this script;
unit tests (tests/test_decision_script.py) exercise the same functions
directly. That split is the point. The merge decision becomes testable
code instead of YAML conditionals, and every fail-closed guarantee below
is provable in a test instead of asserted in a comment.

Two phases, matching the two workflow steps that call this:

  lane   -> may this PR merge at all once checks are green?
            (branch lanes, draft guard, approval-label override,
            protected paths, content-policy lanes)
  checks -> are the checks and mergeable state good enough RIGHT NOW?
            (required checks green, nothing failing, zero-runs
            fail-closed, mergeable state clean)

Verdicts, printed as a trailing "verdict=..." line the workflow parses:

  merge -> proceed
  wait  -> do not merge, exit green; a later event (synchronize, labeled,
           ready_for_review, reopened) re-evaluates
  fail  -> a check is red; exit the job red so the failure is visible

THE ONE RULE THAT SHAPES THE PROTECTED LIST: a PR that edits its own merge
gate must never self-merge. Whatever else you trim from PROTECTED_PATHS,
the gate's own moving parts (this script, the automerge workflow, any
labeler workflows, the file that grants CI its token scopes) keep the
human gate. And the workflow must run the BASE branch's copy of this
script, so a PR's edit to the gate cannot influence its own gate run.

Calling shape, sketched (the gate step of your automerge workflow):

    # Check out the BASE branch: the trusted copy of this script. The
    # default pull_request checkout is the merge ref, i.e. PR content.
    - uses: actions/checkout@v4
      with:
        ref: ${{ github.event.pull_request.base.ref }}
    - name: Merge gate
      run: |
        # A crash of this script must go RED, never read as merge=false.
        # See AUTOMERGE_GOTCHAS.md gotchas 8 and 9.
        set -o pipefail
        test -f .github/scripts/decision_script.py || {
          echo "decision script missing from the base branch; waiting loudly"
          exit 1
        }
        # Paginate the files listing and count renames as BOTH paths; on
        # any listing failure pass --files-error (gotcha 10, fail closed).
        gh api "repos/$REPO/pulls/$PR/files" --paginate \
          --jq '.[] | .filename, (.previous_filename // empty)' \
          > files.txt || FILES_ERR="--files-error"
        python3 .github/scripts/decision_script.py lane \
          --base "$BASE" --head "$HEAD" --labels-json "$LABELS_JSON" \
          --draft "$IS_DRAFT" --files-file files.txt ${FILES_ERR:-} \
          | tee lane_out.txt
        VERDICT=$(grep -o '^verdict=.*' lane_out.txt | cut -d= -f2)

The script itself exits 0 for every COMPUTED verdict ("wait" is a green
outcome: the PR is waiting, not broken), so pipefail only bites real
failures.

Fail-closed floor (all encoded below, all unit-tested, kept on EVERY rung
of the maturity ladder):
  * a DRAFT PR never merges;
  * ZERO check runs on the head SHA never merge (a missed event delivery
    must not become a silent merge);
  * a FAILING check never merges, and returns "fail" so the job goes red;
  * DIRTY or UNKNOWN mergeable state never merges;
  * an UNLISTABLE changed-file set never merges label-free (if you cannot
    see what changed, you cannot clear it);
  * a content-policy lane with no head/base tree to inspect never merges
    label-free.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

# ---------------------------------------------------------------------------
# Configuration. EDIT ME: every constant here is a convention to adapt.
# ---------------------------------------------------------------------------

# The only base branch this gate merges into. Everything else waits.
MAIN_BRANCH = "main"

# Branch namespaces eligible for automerge at all.
AGENT_PREFIXES = ("agent/",)

# The operator's release label. Its role depends on REQUIRE_LABEL: on rung
# one it is the gate (nothing merges without it); on rung two it is the
# universal override (a labeled PR skips the protected-path and
# content-policy checks). Placeholder on purpose; pick a short word your
# operator can type on a phone.
APPROVAL_LABEL = "<approval-label>"

# The maturity-ladder rung switch (AUTOMERGE_GOTCHAS.md, "second
# generation"). True = rung one: every merge is released by the operator's
# label. False = rung two: agent PRs self-merge on green unless they touch
# a protected path or fail a content policy. Which rung is right for your
# repo is an operator decision, not a default this kit can make for you.
# The kit ships rung one; graduate deliberately.
REQUIRE_LABEL = True

# Paths that keep the human gate even on the label-free rung. A trailing
# slash means "the whole tree"; no trailing slash means an exact file
# match. Machinery first: an agent PR that edits its own merge gate must
# never self-merge. Also keep high-blast-radius trees that have no CI
# policy lane (for example infrastructure-as-code with no plan step in PR
# context): a policy check that cannot run cannot fail closed.
PROTECTED_PATHS = [
    ".github/workflows/automerge.yml",
    ".github/scripts/decision_script.py",  # this file, at its deployed path
    # "<labeler-workflow>.yml",            # any workflow that applies APPROVAL_LABEL
    # "<ci-permissions-file>",             # whatever grants CI its token scopes
    # "<high-blast-radius-infra>/",        # e.g. your IaC tree, until it has a plan lane
]

# Check names that must be completed + success on the head SHA for every
# PR. Names match your checks workflow's job names. Matching is substring
# and case-insensitive because check-run names sometimes carry workflow
# prefixes or matrix suffixes.
ALWAYS_REQUIRED_CHECKS = ("Static checks", "E2E checks")

# Path-conditional checks: (name, relevance regex) pairs. The check is
# required only when a changed path matches its regex. The regex MUST
# mirror the producing workflow's `on.paths` filter exactly; when the two
# drift, a PR either merges without a check that should gate it or waits
# forever for a run that never comes. An unlistable file set makes every
# conditional check required (fail closed). Example:
#   CONDITIONAL_CHECKS = (("E2E checks", re.compile(r"^(static/|tests/e2e/)")),)
CONDITIONAL_CHECKS = ()

# Content-policy lanes: (path prefix, policy function) pairs. A path
# family may leave PROTECTED_PATHS only when a content lint replaces the
# judgment the label was buying. policy_fn(scoped_paths, head_root,
# base_root) returns a list of violation strings; any violation makes the
# PR wait for the label. See ci-kit/migrations/policy_checks.py for the
# worked example; wired it looks like:
#   from policy_checks import policy_violations
#   CONTENT_POLICIES = (("migrations/", policy_violations),)
CONTENT_POLICIES = ()

# Check-run conclusions that block a merge outright.
FAILING_CONCLUSIONS = {"failure", "cancelled", "timed_out", "action_required"}

# This gate's own job appears as a check run on the same SHA; a failed
# earlier attempt must not deadlock the next one. Match your job name.
SELF_CHECK_RE = re.compile(r"squash merge|auto-?merge", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Phase one: the lane decision.
# ---------------------------------------------------------------------------

def is_protected(path, protected=None):
    """True when path is on the protected list (exact file, or inside a
    trailing-slash tree entry)."""
    protected = PROTECTED_PATHS if protected is None else protected
    for p in protected:
        if p.endswith("/"):
            if path.startswith(p):
                return True
        elif path == p:
            return True
    return False


def lane_decision(base, head, labels, draft, files,
                  head_root=None, base_root=None,
                  require_label=None, content_policies=None, protected=None):
    """May this PR merge at all once checks are green?

    files is the changed-path list (renames contribute BOTH paths), or
    None when the listing failed: every label-free decision then fails
    closed. head_root/base_root are filesystem checkouts of the PR head
    and the base branch, consumed by content policies; None when
    unavailable (fail closed for any PR a content policy covers).

    Returns (verdict, reason) with verdict in {"merge", "wait"}.
    """
    require_label = REQUIRE_LABEL if require_label is None else require_label
    content_policies = CONTENT_POLICIES if content_policies is None else content_policies

    if draft:
        return "wait", "draft PR; automerge never merges drafts"
    if base != MAIN_BRANCH:
        return "wait", f"base branch {base!r} is not {MAIN_BRANCH!r}; not this gate's business"
    if not head.startswith(AGENT_PREFIXES):
        return "wait", f"head branch {head!r} is not an agent branch; not this gate's business"
    if APPROVAL_LABEL in labels:
        # The operator's explicit release. It overrides protected paths and
        # content policies (and a failed file listing): the human looked.
        return "merge", "approval label present: explicit operator release, merges on green"
    if require_label:
        return "wait", "rung one: every merge is released by the approval label; waiting"

    # Label-free rung. From here, every decision needs the file list.
    if files is None:
        return "wait", "could not list changed files; failing closed, PR waits for the label"
    hits = sorted({f for f in files if is_protected(f, protected)})
    if hits:
        return "wait", "protected paths require the approval label: " + ", ".join(hits)
    for prefix, policy in content_policies:
        scoped = sorted({f for f in files if f.startswith(prefix)})
        if not scoped:
            continue
        if head_root is None or base_root is None:
            return "wait", (f"changed files under {prefix} but no head/base checkout for "
                            "the content policy; failing closed, PR waits for the label")
        violations = policy(scoped, head_root, base_root)
        if violations:
            return "wait", ("content-policy violations require the approval label: "
                            + "; ".join(violations))
    return "merge", "label-free rung: no protected paths, content policies clean, merges on green"


# ---------------------------------------------------------------------------
# Phase two: the checks decision.
# ---------------------------------------------------------------------------

def checks_decision(checks, merge_state, files=None,
                    always_required=None, conditional=None):
    """Are the checks and mergeable state good enough to merge RIGHT NOW?

    checks: list of {"name", "status", "conclusion"} dicts for the head
    SHA. merge_state: the platform's mergeable-state string (CLEAN, DIRTY,
    UNKNOWN, ...). files: changed paths, or None when the listing failed
    (which makes every conditional check required, fail closed).

    Returns (verdict, reason) with verdict in {"merge", "wait", "fail"}.
    """
    always_required = ALWAYS_REQUIRED_CHECKS if always_required is None else always_required
    conditional = CONDITIONAL_CHECKS if conditional is None else conditional

    checks = [c for c in checks if not SELF_CHECK_RE.search(c.get("name") or "")]
    if not checks:
        return "wait", "zero check runs for this SHA; failing closed (no merge without CI evidence)"

    for c in checks:
        if c.get("status") == "completed" and (c.get("conclusion") or "") in FAILING_CONCLUSIONS:
            return "fail", f"check failing: {c.get('name')} = {c.get('conclusion')}"

    def runs_matching(name):
        needle = name.lower()
        return [c for c in checks if needle in (c.get("name") or "").lower()]

    required = [(name, runs_matching(name)) for name in always_required]
    for name, relevance in conditional:
        if files is None or any(relevance.match(f) for f in files):
            required.append((name, runs_matching(name)))
    for name, runs in required:
        if not runs:
            return "wait", f"required check {name!r} has no run yet for this SHA"
        if not any(c.get("status") == "completed" and c.get("conclusion") == "success"
                   for c in runs):
            return "wait", f"required check {name!r} is not green yet"

    ms = (merge_state or "").upper()
    if ms == "DIRTY":
        return "wait", "merge conflict (mergeable state DIRTY); resolve on the feature branch"
    if ms in ("", "UNKNOWN"):
        return "wait", "mergeable state UNKNOWN; not merging until the platform reports it"
    return "merge", f"required checks green, nothing failing, mergeable state {ms}"


# ---------------------------------------------------------------------------
# CLI: the workflow-facing contract.
# ---------------------------------------------------------------------------

def _read_files_arg(args):
    """None means the listing failed or was not provided (fail closed)."""
    if args.files_error or not args.files_file:
        return None
    with open(args.files_file, "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip()]


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="automerge decision gate (see the module docstring)")
    sub = ap.add_subparsers(dest="phase", required=True)

    lane = sub.add_parser("lane", help="branch lane + label + protected paths + content policy")
    lane.add_argument("--base", required=True)
    lane.add_argument("--head", required=True)
    lane.add_argument("--labels-json", required=True, help="JSON array of label names")
    lane.add_argument("--draft", required=True, choices=["true", "false"])
    lane.add_argument("--files-file", help="newline-separated changed paths")
    lane.add_argument("--files-error", action="store_true",
                      help="the file listing failed; fail closed")
    lane.add_argument("--head-root", help="checkout of the PR head (content-policy file contents)")
    lane.add_argument("--base-root", help="checkout of the base branch (the trusted tree)")

    checks = sub.add_parser("checks", help="check runs + mergeable state")
    checks.add_argument("--checks-json-file", required=True,
                        help='path to a JSON array of {"name","status","conclusion"}')
    checks.add_argument("--merge-state", required=True)
    checks.add_argument("--files-file", help="newline-separated changed paths")
    checks.add_argument("--files-error", action="store_true")

    args = ap.parse_args(argv)

    if args.phase == "lane":
        verdict, reason = lane_decision(
            args.base, args.head, json.loads(args.labels_json),
            args.draft == "true", _read_files_arg(args),
            head_root=args.head_root, base_root=args.base_root)
    else:
        with open(args.checks_json_file, "r", encoding="utf-8") as fh:
            check_runs = json.load(fh)
        verdict, reason = checks_decision(check_runs, args.merge_state,
                                          _read_files_arg(args))

    # Exit 0 for every computed verdict: "wait" is a green outcome (the PR
    # is waiting, not broken). Only real crashes exit non-zero, and the
    # calling step's pipefail turns those red instead of silent.
    print(f"reason: {reason}")
    print(f"verdict={verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
