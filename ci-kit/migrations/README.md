> Part of the companion kit for *From Archivist to Architect* (The Architect's Blueprint, Book 1).

# Migrations kit: numbering integrity, apply ledger, merge-time policy

Two tools guard the same folder at two different layers:

- **`runner.py`**: repo-state integrity plus the applied-per-tenant ledger. It refuses a
  duplicate migration number anywhere in the folder and an out-of-order apply, and it tracks
  what has been applied where. It runs in your checks workflow on every PR. See its docstring
  for the CLI.
- **`policy_checks.py`**: merge-time content lints over the PR diff, called by the automerge
  gate (`ci-kit/workflows/decision_script.py`). It sees what the runner cannot: the base
  branch vs the PR head, so it can judge the change itself, not just the resulting folder.

They overlap on duplicate numbers on purpose. Catch the regression at the lowest layer that
can catch it, then catch it again at merge time with the context only the gate has.

## The pattern: a content lint replaces a blanket human gate

When an automerge gate first goes label-free (the maturity ladder in
`ci-kit/workflows/AUTOMERGE_GOTCHAS.md`), the migrations folder is exactly the kind of path
family that stays on the protected list: high blast radius, easy to get subtly wrong, and the
operator's label was buying a real review. The graduation move is not "trust the agent more."
It is: write down what the operator was actually checking, as code, and let the label go only
for PRs that pass those checks. A violation does not fail the PR; it re-attaches the label
requirement, and the label remains the explicit override for legitimately destructive work.

`policy_checks.py` encodes three such lints:

1. **Forward-only.** No `DROP TABLE`, `DROP COLUMN`, or `TRUNCATE`; no `DELETE FROM` against
   a protected table (your canonical, archive-do-not-lose stores, named in
   `PROTECTED_TABLE_TOKENS`). Verified-safe row deletes on ordinary operational tables stay
   allowed. Comments and string literals are stripped first, so prose that mentions a
   forbidden statement does not false-positive.
2. **Risky defaults ship OFF.** A numbered migration seeding the flag table with an
   enabled/true default is blocked unless the file header carries
   `APPROVED-DEFAULT-ON:` followed by the operator's quoted instruction. The approval
   travels in the file, greppable forever, instead of living in a chat message. Unnumbered
   snapshot re-dumps of live state are exempt by construction: they are records, not
   migrations.
3. **Duplicate-number guard.** A new numbered file is blocked when its number is already
   taken on the base branch, repeats within the same PR, or was never claimed in this
   README's ledger line (below). Deleting or renaming an existing migration is also blocked:
   the applied history is an audit trail.

Fail-closed floor: a missing base tree, a missing head tree, or an unparseable ledger line is
a violation, never a pass. If the check cannot see the thing it gates, the PR waits for the
label.

## The claim-first ledger

This folder keeps a single ledger line, parsed by the duplicate-number guard:

**The single current next-free number is `001`** (update this line, and only this line, when
claiming a number).

The rule is claim first, author second. A number is claimed by bumping the ledger line, in
the same PR as the new file or an earlier merged one, never by just using it. "Check the
folder for the highest number and take the next" looks equivalent and is not: it races.

> **Incident (anonymized).** In the production repo this pattern comes from, three PRs opened
> in the same fan-out wave all claimed the same migration number, because each worker checked
> the folder before the others' PRs existed. Two duplicate seeds reached the integration
> branch and had to be adjudicated and renumbered by hand.

For parallel fan-out, two additions: the orchestrator pre-assigns one number per worker in
the task prompt (each worker still re-verifies at write time against the base branch and the
open PRs), and the ledger line is treated as a single-writer resource during the wave, one
session owning every bump. If a race lands anyway, the earliest-opened PR keeps the contested
number and later claimants renumber.

## Parameterize before adopting

All knobs sit in the configuration block at the top of `policy_checks.py`: `MIGRATIONS_DIR`
(keep identical to the prefix registered in the gate), `PROTECTED_TABLE_TOKENS`, `FLAG_TABLE`,
`SEED_OVERRIDE_MARKER`, and the numbered-file regex (three digits by convention, matching
`runner.py`; widen both together if you outgrow 999).

## Wiring into the merge gate

```python
# in decision_script.py
from policy_checks import policy_violations
CONTENT_POLICIES = (("migrations/", policy_violations),)
```

The gate hands the policy the PR's changed paths under the prefix, a checkout of the PR head
(the contents that would merge), and a checkout of the base branch (the trusted tree plus the
existing numbers). Tests for both tools live in `tests/` and run with
`python3 -m unittest discover -s ci-kit/migrations/tests`.
