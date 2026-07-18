# agent-ops-playbook

The hands-on companion repo for **From Archivist to Architect**, Book 1 of the
Architect's Blueprint series.

The book is for analysts who are done being the person who just pulls the data. It walks
the path from report-writer to data and solution architect: how to design systems instead
of one-off queries, how to put AI agents to work on real operations, and how to build the
habits that make the work hold up after you ship it.

This repo is where the book's ideas become files you can actually use. No theory rehash,
no summaries of chapters you already read. Just the working artifacts, extracted from two
years of running Claude Code against a production system that handles regulated PII for
real users. Patterns, not product: the runnable CI enforcement kit, the templates, and
the hard-won gotchas, with every domain identifier removed.

The premise behind all of it: a rule that lives only in a doc gets violated silently; a
rule with a guard, a gate, or a template becomes structurally hard to break. This repo
ships the guards, gates, and templates.

## Who this is for

- Analysts leveling up to data and solution architects, following the book chapter by
  chapter.
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

## Map of the repo

Book-keyed artifact folders (content lands as chapters finish):

- **`skills/`** · reusable AI skill definitions you can drop into your own agent setup
- **`templates/`** · copy-and-adapt templates for the documents and workflows the book covers
- **`checklists/`** · the operational checklists, ready to run

Everything is keyed to the book's chapters, so when a chapter says "the template for this
is in the repo," this is the repo.

What has landed so far:

- **`ci-kit/`**: the runnable enforcement kit. Copy it into your repo.
  - `guards/`: six parameterized lint guards (no inline style/script, env reads only in the
    config registry, no raw fetch, no hardcoded SQL LIMIT, no raw CREATE VIEW, no PII in
    fixtures). Each is stdlib-only, runs in under two seconds, and doubles as its own testable
    unit: no args scans the repo (CI mode), an explicit path skips exclusions (self-test mode).
  - `guards/tests/`: the "prove they bite" self-tests. Every guard is run against a
    deliberately-bad fixture (must fail) and a clean fixture (must pass). A guard that never
    fails is worse than no guard.
  - `run_guards.sh`: the aggregate gate CI calls. The guard registry lives in one array, and
    guards do not short-circuit, so an author sees all violations at once.
  - `migrations/`: the migration runner, a tool instead of a loose folder. Refuses duplicate
    numbers and out-of-order apply before any SQL reaches a database; tracks applied-per-tenant
    in a JSON ledger. Ledger management only by design; the apply layer is separable.
  - `workflows/`: the CI floor as one workflow with two required-check jobs (`checks.yml`), a
    fail-closed automerge for agent PRs (`automerge.yml`), and `AUTOMERGE_GOTCHAS.md`, the six
    non-obvious failure modes a naive automerge hits, each one paid for in production.
- **`docs/rebuild-method/`**: templates from the legacy-rebuild methodology.
  - `DECISIONS_TEMPLATE.md`: the decision ledger. Every day-one rule paired with the specific
    past failure it prevents, so abstract rules earn their place.
  - `PARITY_TEMPLATE.md`: the zero-regression parity contract. Every old-surface capability is
    a tracked row across eight buckets; nothing ships until its row is checked.

Upcoming waves will add the rest of the playbook: the founding-doc templates (operating rules,
phased build order), session-memory and handoff templates, the in-process test harness
skeleton, model-ops docs, and the skills/hooks/settings bundle for the agent harness itself.

## Quick starts

**Adopt the CI kit in an afternoon.**

1. Copy `ci-kit/` into your repo.
2. Edit the configuration block at the top of each guard (scanned paths, config-registry
   filename, approved fetch wrapper, institutional email domain and ID digit length).
3. Copy `ci-kit/workflows/checks.yml` to `.github/workflows/` and point its steps at your
   trees.
4. Run `bash ci-kit/run_guards.sh` locally until clean, then let the workflow gate every PR.
5. Optional: adopt `automerge.yml` for agent PRs, but read `AUTOMERGE_GOTCHAS.md` first.

**Start a disciplined rebuild.**

1. Copy `DECISIONS_TEMPLATE.md` and fill the right column from your own retrospective. If you
   cannot name the failure a decision prevents, cut the decision.
2. Copy `PARITY_TEMPLATE.md` and enumerate the old surface across all eight buckets before
   writing code.
3. Lay the floor first: guards, tests, migration runner, CI gates. Features come after, and
   compose the patterns.

## Get the book

> **[Amazon link goes here at launch]** <!-- PLACEHOLDER: fill with the Amazon listing URL at launch -->

## What was deliberately left out

No domain content and no filled instances. The private repos this kit was extracted from
contain schemas, reports, regulated-domain record handling, staff references, and operational state; none
of that ships, in whole or in scrubbed part. Templates here are authored fresh from the
documented skeletons rather than scrubbed from filled instances, because scrubbing risks
residue and fresh authoring does not. Where an incident makes a rule land, it appears as an
anonymized war story in a clearly labeled callout.

## Who made this

Jovan Smith, 825 Consulting. I built and ran these systems as
an operator inside a real program before writing about them. The material here is what I
actually use, cleaned up so you can use it too.

## Using this repo

Everything here is MIT licensed. See [LICENSE](LICENSE). Take it, adapt it, ship it. If
something is unclear or broken, open an issue.
