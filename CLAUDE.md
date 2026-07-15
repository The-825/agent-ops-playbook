# CLAUDE.md · Analyst to Architect eBook + agent-ops-playbook

> Resuming work? Read `SESSION_STATE.md` (repo root) FIRST: the living handoff (active
> branch, in-flight work, next steps, pending decisions). Refresh it when Jovan says
> "checkpoint". It complements these rules, it does not replace them.

This file is the single source of behavioral truth for Claude Code operating in this repo.
Read it top to bottom before touching anything.

---

## WHO YOU WORK WITH

**Jovan Smith**, owner, 825 Consulting LLC. Email: jovans@ucr.edu.

This is an 825 Consulting workstream. Hard constraint: keep UCR and 825 Consulting in
completely separate contexts unless Jovan explicitly bridges them. Never pull content from
the UCR repos, live UCR data, or anything FERPA-covered into the manuscript, marketing
copy, or this repo. Case-study material comes only from what Jovan has already written
into the manuscript himself.

Brand context lives in the BetterMe repo: `business-825-v3.md` (company profile),
`brand-825-consulting.md` (brand guide), `ebook-series-review.md` (the series strategy
review, the launch-strategy baseline), `skills-v2.md` (humanizer and fact-checker skill
definitions the quality gate references).

---

## WHAT THIS PROJECT IS

The workstream: finish the **Analyst to Architect** eBook, publish it on Kindle (KDP),
and sell it well. This repo (`agent-ops-playbook`) is the hands-on companion repo readers
land on from the book, and the working home for the manuscript, marketing assets, and
KDP metadata.

**Audience:** analysts leveling up to data and solution architects. Professional but
approachable. Not academic, not dumbed down (per the 825 brand guide reading level).

**Pipeline stages:** manuscript -> edit passes -> formatting (KDP/EPUB) -> cover ->
metadata (title, subtitle, keywords, categories) -> launch -> marketing -> reviews ->
iterate. Current stage and status live in `planning/ROADMAP.md`.

---

## BINDING RULES

Commit-time rules. Every PR is judged against them. The integrity floor never decays,
including on "small" fixes and work done by subagents. If a rule has to break, stop and
ask Jovan first.

**Integrity floor (never decays)**
1. **No fabricated testimonials, reviews, endorsements, or credentials. Ever.** Not as
   placeholders, not as drafts, not "to be replaced later."
2. **No plagiarized or unattributed content.** Quotes and data points carry sources,
   cited at the point of claim.
3. **Review solicitation complies with Amazon TOS.** Never incentivized, never fake,
   never review-swapped. ARC copies are fine; paying or trading for reviews is not.
4. **No publishing-irreversible action without Jovan's explicit go-ahead**, recorded in
   the decisions ledger: hitting Publish on KDP, price changes, category or keyword
   changes on the live listing, unpublishing. Flag the irreversibility BEFORE acting.
5. **No student data, client PII, or UCR-identifying detail** anywhere in this repo.

**Brand and quality**
6. **Brand-voice compliance per the 825 brand guide** (`brand-825-consulting.md` in
   BetterMe): direct, human, expertise-first. Never salesy, hustle-culture, generic AI
   company, or hype-driven. Anchor framing: built by an operator, not a vendor. Marketing
   copy is conversational, credible, human, nothing that sounds generated.
7. **Quality gate: every chapter gets a humanizer pass, a fact-checker pass, and a
   reading-level check before it is marked done. No chapter merges without the gate.**
   What each pass checks (full definitions in BetterMe `skills-v2.md`):
   - *Humanizer:* strips AI-writing residue. Cuts hollow openers and closers, rewrites
     any sentence using the blocked hype vocabulary (delve, leverage, transformative,
     robust, seamlessly, and the rest of the list) with concrete specifics, fixes
     structural tells (em-dashes, stacked tricolons, "not only... but also", restating
     conclusions), and restores voice variation (mixed sentence length, broken
     parallelism). Self-check ends at zero em-dashes and ends on the strongest sentence.
   - *Fact-checker:* extracts every factual claim (stats, dates, capabilities,
     citations, comparative claims) and issues a per-claim verdict: Verified, Mostly
     true, Unverifiable, or Contradicted, with a suggested fix for the last two. Claims
     about Jovan's own products or systems verify against the actual code or Jovan
     directly, never web search. Nothing ships with an unresolved Contradicted verdict.
   - *Reading-level check:* confirm the chapter reads for a working analyst, not an
     academic paper and not a dummies guide. Jargon gets defined on first use or cut.
8. **No magic claims.** Never state a number in the book or marketing copy you cannot
   source. KDP mechanics claims (royalty tiers, KENPC, pre-order rules) get re-verified
   against current KDP terms before they ship; the 2026-05 review caught three of these.

**Metadata and research discipline**
9. **KDP metadata is versioned in-repo (`kdp-metadata/`), never edited only on the KDP
   dashboard.** Dashboard state and repo state must match; the repo is the source of
   truth. Any dashboard change lands in the repo the same day, and any repo change to
   live-listing metadata needs Jovan's go-ahead first (rule 4).
10. **Keyword and category research is documented in-repo BEFORE metadata decisions.**
    Research files live in `kdp-metadata/research/`; the decision itself lands in the
    decisions ledger. Same for launch pricing: the strategy is logged before the price
    is set. Baseline facts to respect: the 70% royalty tier caps at $9.99, and KDP does
    not sell ebook bundles (series-page linking only).
11. **Nothing launches until its item in `planning/LAUNCH_CHECKLIST.md` is checked.**
    See KDP PUBLISHING DISCIPLINE below.

**Repo hygiene**
12. **Confirm before deleting anything** (files, branches, listing content). Flag
    irreversible actions before taking them.
13. **No "fix it next PR" TODOs.** Fix in-PR or log it in the KI ledger.

---

## BRANCH / PR CONVENTIONS

- Feature branches are `claude/<feature-slug>`, named after the work (like
  `claude/chapter-3-edit`). Never push a session-named or auto-generated branch
  (`ccr-*`, random hashes). Cut the feature branch first thing.
- PR titles carry intent tags: `feat:` / `fix:` / `docs:` / `chore:` / `refactor:`.
  The title names the work, not the session.
- PR body template: **Summary / Test plan / What's NOT in scope.** The last section
  forces scope discipline.
- **Greenlight merge discipline:** the `greenlight` label is Jovan's explicit merge
  instruction. Without it, the PR waits. Never merge by hand.
- **Verify before you push:** re-read the full diff, run the cheapest check that covers
  the change (spell/em-dash grep for prose, parse checks for anything executable),
  confirm the diff matches the PR's stated scope. No "push then clean up."
- One concern per PR: a chapter edit OR a metadata change OR repo infrastructure,
  not a mix.

---

## DECISION CAPTURE

**Persist a ruling the same turn it lands.** When Jovan decides anything durable
(pricing, title, subtitle, cover choice, categories, keywords, launch date, edition
strategy), append it to `planning/DECISIONS.md` in that turn, before moving on. A ruling
that lives only in a transcript gets re-litigated.

Ledger format, one entry per decision, newest last:

```
## D-<n> · <date> · <topic>
Ruling: <the decision, one or two sentences>
Why: <one line of rationale>
Source: <where it landed: session, PR #, email>
```

Superseded decisions stay in the ledger with a "Superseded by D-<n>" line added.
Never silently rewrite an entry.

---

## CONTINUITY CHECK

After any change to manuscript content, marketing copy, or metadata, sweep every surface
that cites the changed thing for drift before you finish: the blurb, the Amazon
description draft, landing page copy, this repo's README, sample chapters, and series
positioning. A renamed chapter, a changed price, a reworded value proposition, or a new
subtitle must match everywhere it appears.

Fix only the impacted files, never touch consistent ones. If everything is consistent,
report "no drift" and change nothing. Drift found but out of scope for the current PR
goes in the KI ledger, not a silent pass.

---

## KNOWN ISSUES

Numbered ledger, kept in this file under this section. Log an entry as `KI #<n>` with
the date found, the evidence, and its status. Move fixed entries to Resolved with the
fix reference (PR or commit). Never silently drop an entry.

### Active

(none yet)

### Resolved

(none yet)

---

## OPERATOR PREFERENCES (Jovan, binding for everything written here)

Applies to chat replies, the manuscript, marketing copy, PR bodies, commit messages,
and every stub file.

- No em-dashes, ever, in anything newly written. Use commas, periods, or parentheticals.
- Plain, casual, direct English. Lead with the answer, then context if needed.
- No filler, no motivation, no affirmation, no over-complimenting.
- Give a recommendation, not a list of options. If it is genuinely a toss-up, say so
  and why, briefly.
- See a problem with the ask? Say it BEFORE executing, not at the end.
- Confirm before deleting anything. Flag irreversible actions before taking them.
- If clarification is needed, ask ONE specific question, not a list.
- Marketing copy is conversational, credible, human, nothing that sounds generated.
- Walk through complex topics step by step, not everything dumped at once.

---

## SESSION EFFICIENCY

- Read narrow line ranges: grep to locate, then read just those lines. Don't read a
  whole manuscript file when 30 lines answer the question.
- Never re-read a file in the same session; the harness tracks file state.
- Cap tool output (`| head -30`, `--limit`).
- End-of-turn summary: 2 sentences or less. Corrections: 1 sentence.
- Prose over headers for short answers.
- No "let me check X" preface before tool calls. Run the tool.

---

## REPO MAP

Exists now:

```
README.md                    Repo landing page (currently a stub, needs the companion-repo pitch)
LICENSE                      MIT
CLAUDE.md                    This file
SESSION_STATE.md             Living handoff (refresh on "checkpoint")
planning/
  ROADMAP.md                 Pipeline stages as a status table, current stage marked
  LAUNCH_CHECKLIST.md        The launch gate: nothing publishes until its item is checked
  DECISIONS.md               The decisions ledger (format defined above)
```

Target layout (create directories as their first real content lands, not before):

```
manuscript/                  Chapter files, one file per chapter, front and back matter
marketing/                   Blurb, Amazon description drafts, landing page copy, launch posts, ARC outreach
kdp-metadata/                Title, subtitle, keywords, categories, pricing (source of truth vs the dashboard)
  research/                  Keyword and category research, logged BEFORE decisions
assets/                      Cover files, interior images, diagrams (KDP spec versions and sources)
```

Companion-repo content (the playbook material readers come here for) lives at the root
or under a directory Jovan names when that work starts; propose the structure in a PR,
don't invent it silently.

---

## KDP PUBLISHING DISCIPLINE + LAUNCH

`planning/LAUNCH_CHECKLIST.md` is the launch gate, the parity file for this project.
**Nothing launches until its item is checked.** Checking an item requires the evidence
named on the item (a ledger entry, a validated file, Jovan's recorded go-ahead).

Standing KDP facts (re-verify against current KDP terms before relying on them):
- 70% royalty tier caps at $9.99; $10.00 and up drops to 35% plus delivery fees.
- KDP sells no ebook bundles; the Series feature only links books on a series page.
- Ebook pre-orders run up to 90 days; no paperback pre-order.
- Formatting is validated in Kindle Previewer before the manuscript is called final.

The full launch-strategy baseline (ARC plan, pre-order window, AMS budget, category
picks, pricing rationale) is BetterMe `ebook-series-review.md`. Treat it as the strategy
source; port decisions from it into the decisions ledger as they are confirmed.

---

## DOCUMENTATION MAINTENANCE

| When | Update |
|---|---|
| Jovan says "checkpoint" | `SESSION_STATE.md` (full refresh: branch, in-flight work, next steps, pending decisions) |
| A pipeline stage completes | `planning/ROADMAP.md` status table |
| A ruling lands | `planning/DECISIONS.md`, same turn |
| An issue is discovered | KI ledger in this file, same session |
| A launch item is satisfied | `planning/LAUNCH_CHECKLIST.md`, check the box with evidence |
| Manuscript, marketing, or metadata changes | Run the continuity check before finishing |
