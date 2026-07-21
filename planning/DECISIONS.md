# DECISIONS · rulings ledger

Persist a ruling the same turn it lands (CLAUDE.md, DECISION CAPTURE). One entry per
decision, newest last. Superseded entries stay, with a "Superseded by D-<n>" line added.
Never silently rewrite an entry.

Format:

```
## D-<n> · <date> · <topic>
Ruling: <the decision, one or two sentences>
Why: <one line of rationale>
Source: <where it landed: session, PR #, email>
```

---

## D-1 · 2026-07-15 · Repo layout for the eBook workstream (example entry, real decision)

Ruling: The eBook lives in this repo under manuscript/, marketing/, kdp-metadata/,
assets/, and planning/. kdp-metadata/ is the source of truth over the KDP dashboard.
Why: One versioned home for everything the listing depends on; dashboard-only edits
drift and get lost.
Source: Workstream setup PR (claude/ebook-claude-md).

## D-2 · 2026-07-15 · Book title

Ruling: The book title is "From Archivist to Architect" (Book 1 of the Architect's
Blueprint series). The earlier analyst-phrased working title is retired; do not use it
in any doc, metadata, or copy.
Why: Jovan's ruling; matches the manuscript and series naming in the 2026-05 series
review.
Source: Jovan in-session, 2026-07-15.

## D-3 · 2026-07-18 · Repo split: public companion vs private book repo

Ruling: Repo split. 8two5/agent-ops-playbook becomes the public companion holding only
shareable artifacts (skills, templates, checklists, playbook pages); the manuscript, KDP
metadata, and launch planning move to a private repo, proposed
8two5/archivist-to-architect-book.
Why: KDP Select exclusivity and sales mean the book content never sits public.
Source: Jovan's "yes split" approval, session 2026-07-18.

## D-4 · 2026-07-21 · Repo scope: code-only companion to the book

Ruling: This repo is only a companion to From Archivist to Architect. No book prose, chapters, excerpts, or paraphrased chapter content ships here. The public surface is the working code: templates, CI kit, command skills, workflows, and pattern docs written in this repo's own words. The book is referenced as a pointer, never summarized.
Why: Freely public book content risks Amazon KDP demonetization. The repo sells the practice, the book sells the story.
Source: Jovan ruling, 2026-07-21, relayed via the coordinator session.
