# SESSION_STATE.md · living handoff

Refresh this file when Jovan says "checkpoint". A new session reads this first to pick
up mid-flight. Keep it current, keep it short.

## Where things stand

- End of the 2026-07-21 full-throttle window: merges #26, #27, #29, #30, #31, #32,
  #34, #35, and #36 landed today, plus PR #33 (launch flip + end-of-window reconcile)
  closing the window. `git log` is the record; this file does not restate it.
- The wave-4 candidates shipped (authority-ledger kit, build story, launch drafts,
  front door, standing-agent substrate, hooks bundle).
- **The book is published.** From Archivist to Architect went live on KDP 2026-07-21.
  ASIN pending.
- KI ledger is clean. No wave PRs open besides #33.

## Open items

1. ASIN swap when Amazon assigns it: the README and the `marketing/launch/` drafts
   carry the `[SWAP-ON-ASIN]` slot. ROADMAP item 3.
2. Repo description and topics still unset (owner-in-UI action).
3. Authority-kit hardening ports: `planning/PARKED.md`, port when the kit is next
   touched.

## Pending decisions (need Jovan)

- Unchanged: the commands layout (`templates/commands/`) is still provisional pending a
  repo-layout decision; if it moves, it is one `git mv`.
