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

Ruling: Repo split. 8two5/agent-ops-playbook [repo now lives at The-825, 2026-07-18; see
D-7] becomes the public companion holding only
shareable artifacts (skills, templates, checklists, playbook pages); the manuscript, KDP
metadata, and launch planning move to a private repo, proposed
8two5/archivist-to-architect-book [repo now lives at The-825, 2026-07-18; see D-7].
Why: KDP Select exclusivity and sales mean the book content never sits public.
Source: Jovan's "yes split" approval, session 2026-07-18.

## D-4 · 2026-07-21 · Repo scope: code-only companion to the book

Ruling: This repo is only a companion to From Archivist to Architect. No book prose, chapters, excerpts, or paraphrased chapter content ships here. The public surface is the working code: templates, CI kit, command skills, workflows, and pattern docs written in this repo's own words. The book is referenced as a pointer, never summarized.
Why: Freely public book content risks Amazon KDP demonetization. The repo sells the practice, the book sells the story.
Source: Jovan ruling, 2026-07-21, relayed via the coordinator session.

## D-5 · 2026-07-21 · Labeled model examples stand

Ruling: Concrete model names may appear in public playbook content when they sit inside an explicitly labeled, calibration-only example (the model-playbook ladder, the model-check fill-in table). The no-model-identifiers rule governs committed artifacts such as commit messages and machine-stamped files, not labeled teaching examples.
Why: An example ladder with real names is what makes the tier frame usable; the label plus fill-in placeholders keep it replaceable.
Source: Jovan ruling, 2026-07-21, in session.

## D-6 · 2026-07-21 · Anonymized war-story numbers stand

Ruling: Figure-bearing anonymized production callouts stay in (the context-diet line counts, the staging cost-neutral note, and the labeled-callout class generally). Callouts stay labeled, name no repo, and carry no identifying detail.
Why: The measured numbers are the credibility of the pattern; anonymization already strips what matters.
Source: Jovan ruling, 2026-07-21, in session.

## D-7 · 2026-07-21 · Org home of the public repo

Ruling: The public companion repo lives at The-825/agent-ops-playbook. The former
8two5/agent-ops-playbook path redirects; ledger entries citing 8two5 are historical and
stay verbatim.
Why: The repo was transferred to The-825 on 2026-07-18; recording the current home here
beats silently rewriting older entries.
Source: repo transfer 2026-07-18; captured during the 2026-07-21 full-throttle pass.

## D-8 · 2026-07-22 · the825.co site source home

Ruling: The the825.co site source lives in this repo under site/, recovered byte-identical from the production Netlify deploy (6a600ee43a684999b523e743). A root netlify.toml declares publish = "site" with no build step, mirroring the counselorai netlify.toml convention Jovan named as the reference. Netlify keeps serving the existing deploy until Jovan links the Netlify site the825co (id c08f6890-f852-472a-b2d4-d438d6beda59) to this repo.
Why: Jovan ruled the playbook repo is the public home for the site alongside the companion kit; the site is public content already live at https://the825.co.
Source: session, Jovan's instruction 2026-07-22.
