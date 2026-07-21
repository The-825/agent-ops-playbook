# SESSION_STATE.md · living handoff

Refresh this file when Jovan says "checkpoint". A new session reads this first to pick
up mid-flight. Keep it current, keep it short.

## Active branch

`claude/style-rulings`: capture the two style rulings as D-5 and D-6 and mark the
matching handoff lines settled. The sole open PR.

## Merged so far

- Wave 1: companion content and components (PRs #3, #5, #7) plus the public-reference
  sanitize pass (PR #4).
- Wave 2, merged 2026-07-21: PRs #9-#15. Decision-capture guide + conclusions store
  starter (#9), blueprint template + four founding docs + day-one mandates (#10), the
  companion-only reframe per D-4 (#11), the rules spine (#12), the in-process test
  harness skeleton (#13), the command starter set (#14), and the promotion drafts (#15).
- Wave 3, merged 2026-07-21: PRs #17-#22. Staging promotion model + reset skeleton
  (#17), merge-lane companion workflows (#18), command batch 2 + agent preamble +
  incident template (#19), session operating discipline docs (#20), ledger provenance +
  staleness tools (#21), and the second-generation automerge decision gate + migrations
  policy kit (#22).
- Also merged 2026-07-21: PR #8 (identifier cleanup + the previous version of this
  handoff) and PR #16 (mechanical-facts template + model playbook). Nothing from the
  build waves remains open. The add/add overlap on docs/model-playbook.md was resolved
  on the other branch before merge, so main carries PR #16's version of that doc.
- PR #23, the post-merge continuity sweep, merged 2026-07-21: squash c831f37, greenlight
  label applied on Jovan's gl instruction, merged directly (no live automerge in this
  repo). The tree is self-consistent: index tables current, the gotcha count reads ten
  everywhere, the book pointer line sits below the H1 in every file that carries it.

## In-flight work

- This branch's PR (`claude/style-rulings`): D-5 and D-6 appended to the decisions
  ledger plus this handoff touch-up. Nothing else is in flight.

## Next steps

1. Wave 4 candidates, each with its trigger: the standing-agent substrate (the flagship
   kit; trigger: the operator asks for the fleet wave), the authority ledger + citation
   guard (trigger: the pattern survives a few more weeks of production use), and the
   batch-cadence stop hook (trigger: a hooks/settings bundle wave, which is also the
   README's one remaining "upcoming" item).
2. At launch: fill the Amazon link placeholder in README.md (ROADMAP item 3).
3. KI #1: refresh CLAUDE.md's own repo map and mission wording in a dedicated docs PR.

## Pending decisions (need Jovan)

- Style rulings: settled 2026-07-21. The labeled model examples stand (D-5) and the
  anonymized war-story numbers stand (D-6); see planning/DECISIONS.md.
- Publication decision points 1-5, shipped with de-facto answers that still want an
  explicit confirm: automerge variants (the maturity ladder in AUTOMERGE_GOTCHAS.md
  keeps the choice open per repo), skills layout (commands shipped as files under
  templates/commands/; that README still calls the location provisional), CI-kit split
  (single repo), war stories vs blank templates (anonymized labeled callouts in use,
  confirmed at D-6), operator-habits profile (not published).

## Where the full record lives

This build was a coordinated multi-session effort. The operator-side working notes,
including the publication denylist and the per-PR history, live in the team memory files
playbook-wave1-state-and-decisions, playbook-wave2-shipped, playbook-wave3-shipped, and
the playbook-publication-audit set. This public file carries only what the next session
needs.
