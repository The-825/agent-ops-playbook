# Reddit drafts

Three value-first text posts. The lesson is complete in each post body. The repo appears
exactly once per post, in the body or in a first comment depending on the sub's norms.
The book appears at most as one pointer line. Fill `[REPO LINK]` at posting time.

On verification: Reddit blocks rule reads from the drafting environment, so the approach
notes below combine what was verifiable secondhand at drafting time with the
conservative default (all value in the post, minimal linking). Re-read each sub's
sidebar rules on posting day. If the rules or a mod point to a designated showcase
thread or a required flair, follow that over these notes.

---

## Post 1 · r/ClaudeAI

Why here: the home crowd for Claude Code workflow write-ups, and session memory is a
pain everyone in the sub has hit. Concrete posts with real files do well; bare repo
links do not.

Approach: text post, full lesson in the body, repo link once at the end. Pick whatever
flair fits project or workflow shares on posting day. Stay in the comments for the
first hour and answer specifics.

Suggested title: My Claude Code sessions kept forgetting everything, so I gave the repo
the memory instead. Three plain files.

Body:

> The longest-running problem I had with Claude Code was not code quality. It was
> amnesia. A session hits the context limit and compacts, or I close the laptop
> mid-task, and the next session starts cold. It re-derives things an earlier session
> already worked out, sometimes differently. Once in a while it reverses a decision I
> made two weeks earlier, confidently, with a clean diff, because it never saw the
> decision.
>
> I run multiple sessions a day against a production repo that handles regulated PII,
> so "the agent forgot" is not an acceptable root cause for anything. What fixed it was
> not a memory product and not an MCP server. It was three plain files in the repo,
> each with a rule about when it gets written.
>
> SESSION_STATE.md, the living handoff. Repo root. It holds only what is in flight:
> active branch, open PR, half-done edits listed by file, next steps in order,
> decisions I still owe. The rule that makes it work is the trigger. I say
> "checkpoint" and the session rewrites the file to match reality. That makes the
> refresh event-driven, so it happens right before the moments that matter (end of
> day, a risky compaction, switching models) instead of never. "Keep the doc updated"
> means never.
>
> DECISIONS.md, the rulings ledger. Numbered entries, newest last: the ruling in a
> sentence or two, one line of why, where it landed. The binding rule is same-turn
> capture. When I make a durable call mid-session, the entry gets written before the
> session moves on to the work the call unblocked. A ruling that lives only in a
> transcript gets re-litigated by the next session. Every time.
>
> CONCLUSIONS.jsonl, settled knowledge. One JSON object per line: path, date, the
> fact, the evidence (a PR number or a commit). The test for adding a line is "would a
> fresh session pay real time to re-derive this, or get it wrong". Sessions read it at
> start. A session-start hook that injects only the lines matching the files being
> touched is the nice version; a plain read instruction in CLAUDE.md works too.
>
> The split matters more than the formats. Rolling state in the handoff. Human rulings
> in the ledger. Facts sessions proved in the conclusions store. When one file tries
> to be all three, it turns into a log nobody reads.
>
> Blank templates for all three, with the usage rules written in, are in the companion
> repo I maintain: [REPO LINK]. They came out of two years of running Claude Code
> against that production system, and they are the files I actually use, with the
> domain scrubbed out.
>
> (The repo pairs with a book I am finishing on the analyst-to-architect path, first
> in a planned series. Pointer in the repo README.)

---

## Post 2 · r/AI_Agents

Why here: the sub tolerates builders talking about their own work when they show up
with substance, and "here is what I built and what broke" is a recognized post shape
there (verified at drafting time). This crowd knows the difference between an agent
demo and production operations, which is exactly the gap the post covers.

Approach: text post, lesson in the body, repo link once at the end, book as one pointer
line. Engage in the comments; drive-by links get called out in this sub.

Suggested title: Letting my coding agents merge their own PRs without burning
production: what the naive automerge gets wrong

Body:

> I run several coding agent sessions a day against one production repo, solo. The
> throughput win is real, and the bottleneck moves exactly where you would expect: the
> merge queue, meaning me. So I built the thing everyone eventually builds, an
> automerge for agent PRs. The naive version has more failure modes than I would have
> guessed, and I hit them in production before the current version existed.
>
> The core that survived: one fail-closed gate. A single check runs on every trigger
> path and asks whether every named required check is completed and successful on the
> PR's head SHA. Anything missing, pending, or failed means no merge. There is no
> exceptions path.
>
> Head SHA, not workflow conclusion. If the gate trusts the triggering workflow's
> conclusion, every required check that lives outside that workflow silently stops
> gating anything. Verify actual check runs on the actual commit.
>
> Keep the required checks as jobs in one workflow. If your e2e job lives in its own
> workflow, the completion event for the first workflow fires while e2e is still
> pending, the gate correctly skips, and nothing ever re-fires when e2e goes green.
> The PR sits unmerged forever with everything passing. Fail-closed logic plus a
> missing re-trigger equals a queue that stalls silently.
>
> Draft-to-ready re-fires nothing by default. A PR that went green while in draft
> never re-evaluates unless ready_for_review is wired as a trigger running the
> identical gate.
>
> The token recursion guard will get you. A squash merge performed with the default CI
> token does not fire push-event workflows on the target branch. That is the
> platform's own infinite-loop protection, and it means deploy-on-push does not run
> for auto-merged PRs. Mine did not, silently, until the workflow was extended to
> dispatch the deploy explicitly after each merge.
>
> Autonomy is a dial, not a switch. For my production branch, checks green is not
> enough: the PR also waits for a label I apply by hand. One click, and it is my
> explicit release, separate from the machine's opinion. Lower-stakes branches merge
> on green alone. A missing labels array counts as unlabeled, which counts as no.
>
> The workflow file, plus a doc walking six of these failure modes with the incident
> behind each one, is in the public playbook repo I keep. MIT, copy freely:
> [REPO LINK]. The shipped template defaults to the hands-free version and documents
> the label gate as the trade-off it is.
>
> (Context, since people ask: the repo is the companion to a book I am finishing on
> going from analyst to architect, first in a planned series. Details in the repo
> README.)

---

## Post 3 · r/dataengineering

Why here: the repo's audience in one place, working data people who are being handed AI
agents whether they asked for them or not. The sub is strict about vendor content and
blog spam, so the value has to live entirely in the post.

Approach: text post, no link in the body. The repo link goes in a first comment with a
one-line disclosure, posted immediately after publishing. If the sidebar or a mod
points promotion at a designated thread, use that instead. The book stays out of the
post entirely; it rides in the comment.

Suggested title: AI agents write most of my PRs now. The CI floor that keeps them from
wrecking the warehouse.

Body:

> I operate a production system with a warehouse behind it. Regulated PII, real users,
> one human (me). Over the last two years most of the code has come from coding
> agents. The question that turned out to matter is not "can the model write SQL", it
> is "what stops PR number one thousand from quietly breaking an invariant a human
> would have caught on PR number ten". These four pieces earned their keep.
>
> Guards that have to prove they bite. The boring invariants are enforced by small
> stdlib-only lint scripts that run on every PR: no raw CREATE VIEW outside the
> versioned view layer, no hardcoded LIMIT buried in query code, env reads only in the
> config registry, no PII shapes in test fixtures. The rule I will not compromise on
> anymore: every guard also runs in CI against a deliberately-bad fixture it must fail
> and a clean fixture it must pass. It is embarrassingly easy to ship a guard with a
> regex that never fires and then trust it for months. A guard that never fails is
> worse than no guard, because you stop looking.
>
> Migrations as a tool, not a folder. The runner refuses duplicate migration numbers
> and out-of-order applies before any SQL reaches a database, and tracks what has been
> applied where in a ledger. Two agents cutting migrations the same afternoon will
> eventually collide on a number. A script catching that costs nothing; the warehouse
> catching it costs a weekend.
>
> Forward-only, structurally. Schema rolls forward, replaced columns keep a
> deprecation note, lifecycle state is soft-delete so history stays queryable. Agents
> are perfectly literal. If a destructive path exists, some session will eventually
> take it for a locally sensible reason. The fix is not a warning in the docs, it is
> removing the path.
>
> Report every violation at once. The guard registry does not short-circuit: all
> guards run, all findings come back in one pass. One violation per CI round-trip is
> how a five-minute fix becomes an afternoon, for an agent or a person.
>
> The honest summary is that none of this is agent-specific. It is the discipline we
> all claim to keep, made structural, because agents multiplied how often it gets
> tested. A rule that lives only in a doc gets violated silently. A rule with a guard
> is hard to break.
>
> Happy to go deeper on any piece in the comments.

First comment (post immediately after publishing):

> Disclosure: the runnable versions of all of the above (the guards with their
> fixtures, the migration runner, the CI wiring) live in a public MIT repo I maintain,
> domain scrubbed: [REPO LINK]. It doubles as the companion to a book I am finishing
> on the analyst-to-architect path, first in a planned series; pointer in the README
> if you want it.
