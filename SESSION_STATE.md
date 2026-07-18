# SESSION_STATE.md · living handoff

Refresh this file when Jovan says "checkpoint". A new session reads this first to pick
up mid-flight. Keep it current, keep it short.

## Active branch

`claude/ebook-claude-md` (draft PR open: project instructions + planning stubs).

## In-flight work

- First PR of the workstream: CLAUDE.md, this file, planning/ROADMAP.md,
  planning/LAUNCH_CHECKLIST.md, planning/DECISIONS.md, PROJECT_INSTRUCTIONS_8K.md.
  Awaiting Jovan's review and `greenlight`.

## Next steps

1. Jovan reviews the draft PR, marks ready, greenlights.
2. Decide the manuscript import path: which edition file becomes `manuscript/` content
   (the 2026-05 review recommends the Consulting Press edition as the single SKU).
3. Stand up `kdp-metadata/` from the existing KDP metadata package, applying the fixes
   flagged in BetterMe `ebook-series-review.md` section 1 (royalty-tier pricing, bundle
   language removal, KENPC math).
4. Update README.md with the companion-repo pitch.

## Pending decisions (need Jovan)

- Confirm the single-edition call (Consulting Press edition to KDP, trade foreword
  repurposed as launch essay). Log in planning/DECISIONS.md when ruled.
- Book 1 launch price and the review-threshold price step. Log when ruled.
- Title/subtitle final wording (subtitle trim suggested in the review, section 4.4).

## Coordinate Closet (irreplaceable exact values)

- Repo: 8two5/agent-ops-playbook, default branch `main`.
- Strategy baseline doc: BetterMe repo, `ebook-series-review.md` (2026-05-18 review).
- Brand guide: BetterMe repo, `brand-825-consulting.md`.
- Quality-gate skill definitions: BetterMe repo, `skills-v2.md` (humanizer, fact-checker).
- KDP 70% royalty cap: $9.99 (as of the 2026-05 review; re-verify before pricing).
