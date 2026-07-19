# CLAUDE.md · agent-ops-playbook (public companion repo)

> Resuming work? Read `SESSION_STATE.md` (repo root) FIRST: the living handoff (active
> branch, in-flight work, next steps, pending decisions). Refresh it when Jovan says
> "checkpoint". It complements these rules, it does not replace them.

This file is the single source of behavioral truth for Claude Code operating in this repo.
Read it top to bottom before touching anything.

**This repo is public.** Everything committed here is world-readable the moment it lands.
Book-side rules (manuscript, KDP, launch) live in the private book repo.

---

## WHO YOU WORK WITH

**Jovan Smith**, owner, 825 Consulting LLC. Email: jovan@the825.co.

This is an 825 Consulting workstream. Hard constraint: keep 825 Consulting work and the
owner's university client work in completely separate contexts unless Jovan explicitly
bridges them. Never pull content from the university repos, live institutional data, or
anything FERPA-covered into this repo.

Brand context lives in the BetterMe repo: `business-825-v3.md` (company profile),
`brand-825-consulting.md` (brand guide).

---

## WHAT THIS REPO IS

The public companion repo for **From Archivist to Architect** (Book 1 of the Architect's
Blueprint series). Readers land here from the book. The mission: free, shareable artifacts
keyed to the book's chapters, i.e. the skills, templates, checklists, and playbook pages the
book teaches, ready to use. The funnel: book -> repo -> 825 Consulting.

**Audience:** analysts leveling up to data and solution architects. Professional but
approachable. Not academic, not dumbed down.

What lives here: `skills/`, `templates/`, `checklists/`, playbook pages, and the planning
docs for this repo itself. What never lives here: the manuscript, KDP metadata, launch
planning, sales copy drafts, or anything else that belongs to the private book repo.

---

## BINDING RULES

Commit-time rules. Every PR is judged against them. The integrity floor never decays,
including on "small" fixes and work done by subagents. If a rule has to break, stop and
ask Jovan first.

**Integrity floor (never decays)**
1. **No plagiarized or unattributed content.** Quotes and data points carry sources,
   cited at the point of claim.
2. **No student data, client PII, or institution-identifying detail** anywhere in this repo.
3. **Confirm before deleting anything** (files, branches, published content). Flag
   irreversible actions before taking them.

**Brand and voice**
4. **Brand-voice compliance per the 825 brand guide** (`brand-825-consulting.md` in
   BetterMe): direct, human, expertise-first. Never salesy, hustle-culture, generic AI
   company, or hype-driven. Anchor framing: built by an operator, not a vendor. Anything
   public-facing is conversational, credible, human, nothing that sounds generated.

**Repo hygiene**
5. **No "fix it next PR" TODOs.** Fix in-PR or log it in the KI ledger.

---

## BRANCH / PR CONVENTIONS

- Feature branches are `claude/<feature-slug>`, named after the work (like
  `claude/chapter-3-templates`). Never push a session-named or auto-generated branch
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
- One concern per PR: a content addition OR repo infrastructure, not a mix.

---

## DECISION CAPTURE

**Persist a ruling the same turn it lands.** When Jovan decides anything durable about
this repo (structure, naming, what ships public, licensing), append it to
`planning/DECISIONS.md` in that turn, before moving on. A ruling that lives only in a
transcript gets re-litigated.

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

After any change to companion content or positioning, sweep the public surfaces that cite
the changed thing for drift before you finish: the README, the companion content
(`skills/`, `templates/`, `checklists/`, playbook pages), and the series positioning. A
renamed artifact, a restructured directory, or a reworded pitch must match everywhere it
appears.

Fix only the impacted files, never touch consistent ones. If everything is consistent,
report "no drift" and change nothing. Drift found but out of scope for the current PR
goes in the KI ledger, not a silent pass.

---

## KNOWN ISSUES

Numbered ledger, kept in this file under this section. Log an entry as `KI-<n>` with
the date found, the evidence, and its status. Move fixed entries to Resolved with the
fix reference (PR or commit). Never silently drop an entry.

### Active

(none yet)

### Resolved

(none yet)

---

## OPERATOR PREFERENCES (Jovan, binding for everything written here)

Applies to chat replies, companion content, PR bodies, commit messages, and every stub
file.

- No em-dashes, ever, in anything newly written. Use commas, periods, or parentheticals.
- Plain, casual, direct English. Lead with the answer, then context if needed.
- No filler, no motivation, no affirmation, no over-complimenting.
- Give a recommendation, not a list of options. If it is genuinely a toss-up, say so
  and why, briefly.
- See a problem with the ask? Say it BEFORE executing, not at the end.
- Confirm before deleting anything. Flag irreversible actions before taking them.
- If clarification is needed, ask ONE specific question, not a list.
- Public-facing copy is conversational, credible, human, nothing that sounds generated.
- Walk through complex topics step by step, not everything dumped at once.

---

## SESSION EFFICIENCY

- Read narrow line ranges: grep to locate, then read just those lines. Don't read a
  whole file when 30 lines answer the question.
- Never re-read a file in the same session; the harness tracks file state.
- Cap tool output (`| head -30`, `--limit`).
- End-of-turn summary: 2 sentences or less. Corrections: 1 sentence.
- Prose over headers for short answers.
- No "let me check X" preface before tool calls. Run the tool.

---

## REPO MAP

```
README.md                    Public landing page: the companion pitch + book link
LICENSE                      MIT
CLAUDE.md                    This file
SESSION_STATE.md             Living handoff (refresh on "checkpoint")
planning/
  ROADMAP.md                 Companion-repo roadmap
  DECISIONS.md               The decisions ledger (format defined above)
skills/                      Reusable AI skill definitions, keyed to book chapters
templates/                   Copy-and-adapt templates, keyed to book chapters
checklists/                  Operational checklists, keyed to book chapters
```

---

## DOCUMENTATION MAINTENANCE

| When | Update |
|---|---|
| Jovan says "checkpoint" | `SESSION_STATE.md` (full refresh: branch, in-flight work, next steps, pending decisions) |
| A roadmap item completes | `planning/ROADMAP.md` |
| A ruling lands | `planning/DECISIONS.md`, same turn |
| An issue is discovered | KI ledger in this file, same session |
| Companion content or positioning changes | Run the continuity check before finishing |
