# Parked from wave 4

> Part of the companion kit for *From Archivist to Architect* (The Architect's Blueprint, Book 1).

Everything here was deferred deliberately during the wave-4 build and is logged so nothing drops silently.

Shipped since: the grant-aware wiring of the merge-gate decision script (the first row of the original table) landed once its upstream wiring earned production mileage; see docs/authority-ledger.md Phase 2.

| Item | Why parked |
|---|---|
| A compact reference CLI for the a2a task bus | The honest version does not compress under ~150 lines; the protocol doc is the contract |
| Registry/index templates for a catalog-routed doc architecture (agent index, atlas, doctrine, and the separated-doc-set essay) | Audit wave-4 backlog; needs fresh authoring |
| Deploy inert-until-wired workflow skeleton | Audit wave-4 backlog |
| The five repo-pathed diagnostic skills rebuilt as templates (debug sweeps, flag graduation, screenshot review, migration steward) | Audit wave-4 backlog |
| Harness settings template (deny floor + allow list) | Audit wave-4 backlog |

## Authority-kit hardening (from the wave-4 parallel draft, superseded by #27; port when the kit is next touched)

- The citation guard scans repo file surfaces (`.md`/`.yml` under configurable paths with excludes) for grant citations, not just the PR body, and fails an unparseable expiry as a ledger-integrity error, with fixture-backed unittests.
- The ledger template shows a revoked/status-flipped example line, not only active grants.
- `grant.md` gains a refuse-vague-scope gate (pin the action class and surface before writing) and whole-ledger re-validation after append.
- The pattern doc names repo-file citation surfaces.
