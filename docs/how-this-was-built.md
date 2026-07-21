# How this was built: the launch build story

> Part of the companion kit for *From Archivist to Architect* (The Architect's Blueprint, Book 1).

On Tuesday, July 21, 2026, I uploaded *From Archivist to Architect* to Amazon KDP. The repo it shipped from had existed since the previous Friday evening. The book had existed much longer than that.

That gap is the honest center of this story. I drafted the book over months, into May 2026, and then stalled. The manuscript sat in Google Drive, reviewed as publication-ready, and did not move. What happened in July was not a book written in four days. It was a finished draft recovered and shipped in four days, by me working with a coordinated set of Claude Code agent sessions, on the machinery this repo now hands you. This page is the record of how, including the parts that went sideways.

## Friday night to Tuesday afternoon

**Friday, July 17.** I created the private book repo in the evening. First commit: a license and a one-line README. Nothing else existed on the repo side.

**Saturday, July 18.** The recovery day. The sessions searched my Google Drive and Gmail and found the manuscript: a Google Doc last modified May 22, 2026. The discovery inventory written that day recorded the headline finding: the book already existed and had been reviewed as publication-ready back in May, so the remaining work was launch execution, not drafting. The same day, the split ruling landed (this public companion repo on one side, the private book repo on the other), and by night the decisions ledger held rulings on the subtitle, the cover concept, pricing, and distribution.

**Sunday, July 19.** The walkthrough. I read the manuscript with a session and ruled on the open questions, including 28 approved voice edits. No commits landed that day; the work was staged and committed Monday.

**Monday, July 20.** The manuscript moved from Drive into the repo, verified byte-exact against the source: 118,035 bytes, 18,649 words at that point. With it came a fact-check table covering 66 claims. Eight came back contradicted and were fixed before the manuscript landed. That night I had a 10pm launch target. It slipped.

**Overnight into Tuesday.** The QA session started around 1:30am and ran the gauntlet: a mechanical proofread that applied 19 fixes, a full reader pass that logged 28 stalls, and a visual QA verdict on every figure. Five figures picked up touch-up flags for a later pass; all were judged shippable at Kindle scale, and the flags are on file. In parallel, another session wrote the final chapter.

**Tuesday, July 21.** I ruled that v1.0 ships with that chapter. The ten-chapter build came together: 21,546 words, 18 figures built in Canva, validated with EPUBCheck 5.1.0 at zero errors and zero warnings. I completed the KDP upload that afternoon.

## The chapter that documents itself

Chapter 10 is called The Force Multiplier, and it covers the working method that produced the book: the rules file, the check ladder, the ledgers, the human gate. Its closing section is titled The Proof You Are Holding, and the title is literal. The chapter about the workflow was written on launch night by one of the sessions running that workflow, put through the same fact-check discipline as the rest of the manuscript, and held to the same merge gate as every other change.

I am not going to give you a session count, because I did not run this as a headcount. I ran it as roles. One session coordinated. Others fact-checked claims, built and exported the figures, ran the proofread and reader passes, cut the EPUB build, and wrote that launch-night chapter. Each one booted cold, read the rules file, and picked up exactly where the ledgers said things stood.

## The machinery that held

Four mechanisms did the real work, and all four ship in this repo.

**A rules file every session boots from.** Both repos carry a binding rules file: the integrity floor, the voice rules, the branch and PR conventions. A session starting cold at 1:30am gets the same floor as one starting fresh on a Saturday morning. The pattern is [templates/CLAUDE_TEMPLATE.md](../templates/CLAUDE_TEMPLATE.md), and the long-form guide is [rules-spine.md](rules-spine.md).

**A decisions ledger, written the same turn.** Every durable call got a numbered entry the turn I made it, not reconstructed later. By upload time the book ledger read D-1 through D-15: the title, the subtitle, the cover, pricing, distribution, the AI-content disclosure, down to the launch-night call that v1.0 ships with Chapter 10. When I reversed an earlier call (a nine-chapter upload had been ruled that same day), the old entry stayed in the file with a superseded-by line. The ledger holds the reversal; nothing gets rewritten. Template: [templates/DECISIONS_TEMPLATE.md](../templates/DECISIONS_TEMPLATE.md).

**Human gates.** In both repos, the greenlight label is my explicit merge instruction. In this one, a PR also waits on green CI. The book repo had no CI and no automerge at all, so every merge there was my manual click, all eight of them. And the dashboard run ended at a hard stop written into the upload runbook itself: the Publish button is my click alone. The sessions staged every field and stopped at the button.

**Verify against live.** Every claim in the book that describes a system was checked against the thing it describes, never against vibes. The fact-check table ran 66 claims to verdicts: 34 verified, 9 mostly true, 15 kicked up to me, 8 contradicted and fixed. The statistics were reproduced read-only from the live aggregate data they summarize. Platform mechanics were re-verified against the platform's own current help pages. The production system the book draws on is one I built and run for an Honors program at a major public research university in California, and claims about it were verified against its actual repos, not my memory of them.

## What went wrong, and what caught it

A build story that only lists wins is marketing. Here is the other column.

**The deadline slipped.** The 10pm Monday target came and went, and the QA session ran overnight instead. The honest cause: the gauntlet was not optional and it was not fast. What kept the slip from becoming a quality problem is that the gauntlet is mechanical. The proofread log ties evidence to every fix, and the reader pass numbers every stall. Checklists do not get tired at 3am.

**A stale duplicate PR raced in.** In this repo, a leftover draft PR (#6) carried the same title as the already-merged PR #1 and described the same content. It was closed as superseded within three minutes, unmerged, because the check run before closing was a content diff against main: what does this add, not does the title look plausible. The same pattern repeated in the book repo, where PR #9's figure work had already landed through the ten-chapter branch (PR #7), so #9 closed unmerged minutes after #7 merged. The diff is the mechanism; titles lie, diffs do not.

**A merge-order scramble.** On launch night, the QA branch and the Chapter 10 branch were in flight at once, and the PR opened first had to merge second. The fix was boring and written down: a rebase protocol recorded in both PR descriptions, the chapter branch rebased onto the QA result, and the ledger entries renumbered in that rebase so both branches' rulings landed in order. The order held, QA merging at 6:01am and the chapter at 6:03am. The ledger discipline is what caught it; with every ruling already numbered and on file, a scramble is a rebase, not an archaeology dig.

**The harness told me no.** More than once, a session was refused an action because my authorization had been relayed secondhand instead of said by me directly. Pushes were denied. Four of five builder-session launches were refused in one wave until I said go, in-session, myself. Each wall cost real time on a launch night, and each was the system working as designed. A relayed yes is not my yes, and a machine that refuses to act on hearsay about my intent is exactly the machine I want holding my repos.

## Run it yourself

Nothing above is exotic. It is a rules file, two ledgers, a handoff file, CI guards, and a label a human applies. This repo carries all of it: the enforcement kit in [ci-kit/](../ci-kit/), the operating model in [playbook/](../playbook/), the pattern essays in this directory (docs/), paste-able skill definitions in [skills/](../skills/), the working-file templates in [templates/](../templates/), and the runnable checklists in [checklists/](../checklists/).

The book took months to write and four days to finish. Copy the kit, and go finish the thing you stalled on.
