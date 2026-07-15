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
