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
Source: Workstream setup PR, 2026-07-15 (the eBook workstream has since moved to the
private book repo, see D-3).

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
