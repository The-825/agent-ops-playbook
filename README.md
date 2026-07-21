# agent-ops-playbook

Run one coding agent against a repo that matters and you can read every diff yourself.
Run several a day, solo, and the operating problems show up fast: a merge lands that no
human reviewed, the docs quietly fall behind the code, a decision gets made in one
session and is invisible to the next, and every new session starts blind because the
context lived in the last one's window.

This repo is the working operating system for that job, extracted from two years of
running Claude Code against a production system that handles regulated PII for real
users, with every domain identifier removed: copy-and-adapt templates, a CI kit with
self-tested guards, command skills, and pattern docs, all MIT licensed and written in
this repo's own words. It is for analysts leveling up to data and solution architects,
and for anyone running coding agents against a codebase that matters.

The premise behind all of it: a rule that lives only in a doc gets violated silently; a
rule with a guard, a gate, or a template becomes structurally hard to break. This repo
ships the guards, gates, and templates.

**Start with the [one-afternoon adoption path](#start-in-one-afternoon):** an issue
ledger, a session handoff file, and a label-gated merge give agent work a memory and a
brake in the first hour. The CI kit comes after.

## The book

This repo is the code companion to **From Archivist to Architect**, Book 1 of The
Architect's Blueprint series, by Jovan Smith, 825 Consulting. The book is out,
published July 21, 2026. It tells the story; this repo is the practice.

> On Amazon: **[SWAP-ON-ASIN]** <!-- swap this placeholder for the live Amazon listing URL once the ASIN exists -->

## Three ways in

- **I read the book.** Start with the memory starter:
  [CLAUDE](templates/CLAUDE_TEMPLATE.md),
  [SESSION_STATE](templates/SESSION_STATE_TEMPLATE.md), and
  [DECISIONS](templates/DECISIONS_TEMPLATE.md) in `templates/`, then the automerge
  gate in [`ci-kit/workflows/`](ci-kit/workflows/).
- **I want the templates.** [`templates/`](templates/) plus
  [`checklists/`](checklists/): copy the file, fill the placeholders, adapt.
- **I run agents on a real repo.** [`ci-kit/`](ci-kit/) first (guards, migrations,
  workflows), then [`docs/`](docs/) for the reasoning behind each piece.

## The map

One line per directory; the sections and READMEs below each one carry the depth.

- [`templates/`](templates/): copy-and-adapt working files (agent rules file, session
  handoff, decision and authority ledgers, rebuild blueprint, parity contract) plus
  slash commands, a test harness, and ledger tools
- [`ci-kit/`](ci-kit/): the runnable enforcement kit: self-tested lint guards, a
  migration runner with policy checks, and CI workflow templates around a fail-closed
  automerge gate
- [`skills/`](skills/): paste-able rule sets for your own agent rules file, from
  data-truth rules to forward-only migrations
- [`checklists/`](checklists/): two-minute operational checklists: PR discipline,
  pre-push verification, the continuity sweep
- [`docs/`](docs/): the method guides behind the templates, from day-one mandates and
  the rules spine to the context budget and the model playbook
- [`playbook/`](playbook/): the connective essays: the agent-ops operating model and
  the doc-sync agent pattern
- [`planning/`](planning/): this repo's own roadmap and decisions ledger
- [`marketing/`](marketing/): draft posts the author publishes by hand; nothing here
  auto-posts

## Who this is for

- Analysts leveling up to data and solution architects who want the working files, not
  another essay about them.
- Teams running coding agents (Claude Code or similar) against a codebase that matters,
  where "the agent moved fast" is not an acceptable root cause.
- Anyone rebuilding a legacy system and determined not to rebuild its debt along with it.
- Solo operators who want production discipline without a platform team: everything here
  is stdlib Python, bash, and GitHub Actions.

## The three over-arching principles

1. **Every PR ships infrastructure OR a user-visible improvement, never both.**
   Force-multiplier work and feature work decompose into separate PRs; mixing them buries each.
2. **Patterns over snowflakes.** Codify a pattern once (a renderer, a route shape, a SQL
   idiom, a flag, a spec); new features become "compose the existing pieces." If you are
   reinventing markup, a route shape, or an idiom, stop and extract.
3. **Catch regressions at the lowest layer that can catch them.** Parse-time first, then lint
   guards, then runtime tests, then data assertions, then unit tests. Each layer runs cheaply
   on every PR forever.

## Start in one afternoon

The highest-return first hour is not the CI kit. It is three small pieces that give agent
work a memory and a brake:

1. **An issue ledger.** Number every known issue (`KI #1`, `KI #2`, ...) in one file with
   the date found, the evidence, and the status; move fixed entries to Resolved with the
   fix reference, and never silently drop one. The starter section lives inside
   `templates/CLAUDE_TEMPLATE.md`.
2. **A session handoff file.** Copy `templates/SESSION_STATE_TEMPLATE.md` and refresh it
   on a trigger word, so the next session picks up mid-flight instead of starting blind.
3. **A label-gated merge.** Adopt `ci-kit/workflows/automerge.yml` with the
   operator-label gate described in `AUTOMERGE_GOTCHAS.md`: an agent PR merges only when
   every required check is green AND a human has applied the approval label. Nothing
   lands unreviewed while you sleep.

Then adopt the full CI kit:

1. Copy `ci-kit/` into your repo.
2. Edit the configuration block at the top of each guard (scanned paths, config-registry
   filename, approved fetch wrapper, institutional email domain and ID digit length).
3. Copy `ci-kit/workflows/checks.yml` to `.github/workflows/` and point its steps at your
   trees.
4. Run `bash ci-kit/run_guards.sh` locally until clean, then let the workflow gate every PR.

And when you are starting a disciplined rebuild:

1. Copy `templates/DECISIONS_TEMPLATE.md` and fill the right column of the rebuild tables
   from your own retrospective. If you cannot name the failure a decision prevents, cut the
   decision.
2. Copy `templates/PARITY_TEMPLATE.md` and enumerate the old surface across all eight
   buckets before writing code.
3. Lay the floor first: guards, tests, migration runner, CI gates. Features come after, and
   compose the patterns.

## Inside `ci-kit/`

The kit is meant to be copied into your repo and wired to CI the same day.

- `guards/`: seven parameterized lint guards, each stdlib-only, under two seconds, and its
  own testable unit. Six are path scanners (no inline style/script, env reads only in the
  config registry, no raw fetch, no hardcoded SQL LIMIT, no raw CREATE VIEW, no PII in
  fixtures): no args scans the repo (CI mode), an explicit path skips exclusions (self-test
  mode). The seventh checks that authority-ledger citations in a PR body resolve to real,
  unexpired grants, and that the ledger itself stays parseable.
- `guards/tests/`: the "prove they bite" self-tests. Every guard is run against a
  deliberately-bad fixture (must fail) and a clean fixture (must pass). A guard that never
  fails is worse than no guard.
- `run_guards.sh`: the aggregate gate CI calls. The guard registry lives in one array, and
  guards do not short-circuit, so an author sees all violations at once.
- `migrations/`: the migration runner, a tool instead of a loose folder. Refuses duplicate
  numbers and out-of-order apply before any SQL reaches a database; tracks applied-per-tenant
  in a JSON ledger. Ledger management only by design; the apply layer is separable. Its
  `policy_checks.py` adds the merge-time content lints (forward-only, risky defaults ship
  OFF, the claim-first number ledger) the automerge gate runs on migration PRs.
- `workflows/`: the CI floor as one workflow with two required-check jobs (`checks.yml`), a
  fail-closed automerge for agent PRs (`automerge.yml`), and `AUTOMERGE_GOTCHAS.md`, the ten
  non-obvious failure modes a naive automerge hits, each one paid for in production. Around
  that gate: `decision_script.py`, the second-generation merge decision as unit-tested pure
  functions, plus the merge-lane companion workflows, mapped in
  [`MERGE_LANE_COMPANIONS.md`](ci-kit/workflows/MERGE_LANE_COMPANIONS.md), and the
  staging-first reset button.
- `pull_request_template.md`: the judgment-only PR body template: Summary / Versions /
  Test plan / What's NOT in scope, prose answers for the calls robots cannot check,
  deliberately no checkboxes.

## Inside `templates/`

Copy the file, fill the placeholders, commit it to your own repo. The full set covers the
agent rules file, the session handoff, the conclusions store, the authority ledger, a
one-page ADR format, the shared agent-prompt preamble, the incident postmortem, and the
anti-rot mechanical-facts pattern; see [templates/README.md](templates/README.md). Highlights:

- `DECISIONS_TEMPLATE.md`: the append-only decisions ledger, plus the rebuild variant where
  every day-one rule is paired with the specific past failure it prevents, so abstract
  rules earn their place.
- `PARITY_TEMPLATE.md`: the zero-regression parity contract. Every old-surface
  capability is a tracked row, bucketed and checked with evidence; nothing ships until
  its row is checked.
- `commands/`: copy-paste slash-command definitions for Claude Code, from `/sprint` and
  `/ship` to `/land` and `/close-out`, each a markdown file with frontmatter.
- `test-harness/`: the in-process test harness skeleton: boot the real app in the
  test process, fake only the edges, prove route behavior on every PR in seconds.
- `ledger-tools/`: keeping a long-lived conclusions ledger trustworthy: provenance
  tiers, a staleness auditor, the capture nudge, and union-merge hygiene.

## What was deliberately left out

No book content, no domain content, no filled instances. The private repos this kit was
extracted from contain schemas, reports, regulated-domain record handling, staff
references, and operational state; none of that ships, in whole or in scrubbed part.
Templates here are authored fresh from the documented skeletons rather than scrubbed from
filled instances, because scrubbing risks residue and fresh authoring does not. Where an
incident makes a rule land, it appears as an anonymized war story in a clearly labeled
callout.

## Who made this

Jovan Smith, 825 Consulting. I built and ran these systems as
an operator inside a real program before writing about them. The material here is what I
actually use, cleaned up so you can use it too.

## Using this repo

Everything here is MIT licensed. See [LICENSE](LICENSE). Take it, adapt it, ship it. If
something is unclear or broken, open an issue; if you want to send a fix,
[CONTRIBUTING.md](CONTRIBUTING.md) is the short read.
