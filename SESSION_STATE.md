# SESSION_STATE.md · living handoff

Refresh this file when Jovan says "checkpoint". A new session reads this first to pick
up mid-flight. Keep it current, keep it short.

## Active branch

`claude/redact-cleanup`: finishes the public-reference cleanup on top of the merged
sanitize pass and refreshes this handoff.

## Merged so far

- Wave 1 companion content merged (PR #3).
- Companion components (skills, templates, checklists, playbook pages) merged (PR #5).
- Public-reference sanitize pass merged (PR #4).

## In-flight work

- This cleanup PR: the last residual identifier fixes main still needed after PR #4
  (stale branch pointers in planning/ROADMAP.md and planning/DECISIONS.md) plus this
  SESSION_STATE.md refresh.

## Next steps

1. Wave 2 content: founding-doc template and session-memory template.
2. At launch: fill the Amazon link placeholder in README.md (ROADMAP item 3).

## Pending decisions (need Jovan)

(none for this repo right now)
