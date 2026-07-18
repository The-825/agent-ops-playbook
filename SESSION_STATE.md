# SESSION_STATE.md · living handoff

Refresh this file when Jovan says "checkpoint". A new session reads this first to pick
up mid-flight. Keep it current, keep it short.

## Active branch

`claude/companion-split` (pushed to the private fork;
Jovan opens the cross-account PR into `8two5/agent-ops-playbook` himself from the
compare link, because the Claude GitHub App is not installed on the 8two5 account).

## In-flight work

- Repo split in progress (DECISIONS D-3): this repo becomes the public companion
  (skills, templates, checklists, playbook pages only). Book-side content removed:
  planning/LAUNCH_CHECKLIST.md and PROJECT_INSTRUCTIONS_8K.md deleted here, they move
  to the private book repo.
- Stub indexes created for `skills/`, `templates/`, `checklists/`. A sibling session is
  building the actual content components on a `claude/playbook-components` branch.

## Next steps

1. Jovan creates the private book repo (proposed `8two5/archivist-to-architect-book`)
   and moves the manuscript, KDP metadata, and launch planning there.
2. Jovan opens and merges the cross-account PR for this split.
3. Merge in the playbook components from the sibling branch as they land.
4. At launch: fill the Amazon link placeholder in README.md.

## Pending decisions (need Jovan)

- Confirm the private repo name (`archivist-to-architect-book` is the proposal).
- Whether to install the Claude GitHub App on the 8two5 account (until then, all writes
  route through the private fork).

## Coordinate Closet (irreplaceable exact values)

- Public repo: 8two5/agent-ops-playbook, default branch `main`.
- Write path: push branches to the private fork; direct
  writes to 8two5 return 403 (no app install).
- Private book repo (pending creation): proposed 8two5/archivist-to-architect-book.
- Brand guide: BetterMe repo, `brand-825-consulting.md`.
- Split ruling: planning/DECISIONS.md D-3 (2026-07-18).
