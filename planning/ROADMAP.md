# ROADMAP · agent-ops-playbook (public companion repo)

The book pipeline (manuscript, formatting, cover, metadata, launch) lives in the private
book repo. This roadmap covers only the public companion.

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Repo split: strip book-side content, re-scope docs to the companion mission | Done | Merged (PR #2); public-reference cleanup followed in PR #4. Ruled in DECISIONS D-3. |
| 2 | Populate `skills/`, `templates/`, `checklists/` | Done | First component batch merged (PR #5); waves 2 and 3 (PRs #9-#22) merged 2026-07-21, adding `docs/`, the ci-kit growth, `templates/commands/`, `test-harness/`, `ledger-tools/`, and `marketing/` drafts. Wave 4 (PRs #26-#38) merged 2026-07-21 (main tip 051d95a); companion content is complete through wave 4, and every artifact the book points readers to is live. |
| 3 | Add the Amazon link to README.md | Pending launch | Book is finished but not yet published (awaiting the launch chain; book-repo KI #2). README now reads "listing coming at launch"; swap in the ASIN link the day Amazon assigns it. |
| 4 | Post-launch upkeep | Active | Keep artifacts in sync with the book; fix issues readers open. |
| 5 | Adoption `doctor` / `init` script | Idea | Suggested by the 2026-07-23 Codex review: a script that validates common placeholder edits (scanned paths, check names, label names, authority-ledger paths) so an adopter catches a missed config edit before CI does. |
