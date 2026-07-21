# Substack series · Fleet of One

## Concept

Working title: **Fleet of One**

One-line promise: field notes from running a fleet of AI coding agents as one operator,
on production systems that have to hold up.

The angle: not model reviews, not prompt tips. The operations layer. What a single
person needs in place (memory, enforcement, release control) once agents write most of
the code and the human becomes the institution. Every post teaches one lesson in full
and pairs it with an artifact the reader can copy from the companion repo. Per the
rules in `marketing/README.md`: the repo linked once per post, the book as one pointer
line, nothing else.

## The arc, eight posts

Solo dev to fleet operator, one lesson per post, each paired with the repo artifact
that ships it.

| # | Post title | The lesson | Pairs with |
|---|---|---|---|
| 1 | The day I stopped being the only person in my repo | The role change nobody names: you become a manager of staff with no memory, and rules have to move from docs into guards, gates, and templates | `playbook/agent-ops-operating-model.md` |
| 2 | Sessions die. Plan for it. | In-flight state dies with the session unless a living handoff file catches it; refresh on a trigger word, because "keep it updated" means never | `templates/SESSION_STATE_TEMPLATE.md` |
| 3 | Write the ruling down the turn it lands | Decisions that live only in transcripts get re-litigated; the numbered ledger and same-turn capture | `templates/DECISIONS_TEMPLATE.md` |
| 4 | What the fleet already knows | Settled facts go in a machine-readable store read at session start, so no session pays twice to re-derive them | `templates/CONCLUSIONS_TEMPLATE.md` |
| 5 | A guard that never fails is worse than no guard | Every CI guard ships with a deliberately-bad fixture it must fail; test the tests | `ci-kit/guards/` and its `tests/` |
| 6 | Letting the agents merge | The fail-closed automerge: head-SHA verification, the one-workflow trap, the token recursion guard, and a label as the human release valve | `ci-kit/workflows/automerge.yml` + `AUTOMERGE_GOTCHAS.md` |
| 7 | Forward-only or nothing | Migrations as a tool with a ledger; destructive paths removed rather than discouraged | `skills/forward-only-migrations.md` + `ci-kit/migrations/` |
| 8 | The bus factor was already one | Docs drift unless something owns them; a doc-sync agent on a cadence, and a numbered known-issues ledger that never silently drops an entry | `playbook/doc-sync-agent.md` + `templates/CLAUDE_TEMPLATE.md` |

## Post 1, full draft

Title: The day I stopped being the only person in my repo

> For most of my career, the repo and I were the same organism. If code got written, I
> wrote it. If a migration ran out of order, I did that too. Working solo has obvious
> costs, but it comes with one enormous hidden subsidy: perfect institutional memory.
> Every decision, every half-finished branch, every "don't touch that table, it's
> weirder than it looks" lived in one head, and that head was always in the room.
>
> Then I started running coding agents against my repos. Several sessions a day,
> sometimes several at once, against a production system that handles regulated PII
> for real users. The thing nobody warned me about was not code quality. The agents
> write decent code most days, and when they don't, review catches it. The thing
> nobody warned me about is that I had quietly become a manager. My staff happened to
> be software: tireless, literal, fast, and completely without memory.
>
> A new session starts cold. It has not read the argument we settled last Tuesday. It
> does not know that the API's updated-date field lies, or that the one scary table is
> scary. It will re-derive whatever it needs, and re-derivation is where the trouble
> lives, because a session that re-derives a fact sometimes derives it differently,
> and a session that never saw a decision will occasionally reverse it with total
> confidence and a clean diff.
>
> For a while I handled this the way every solo dev handles everything: personally. I
> re-explained context at the top of each session. I reviewed every line. I was the
> memory, the reviewer, the merge button, and the alarm system. Which worked, in the
> sense that nothing burned down, and failed, in the sense that I had hired a fleet
> and then made myself the bottleneck it queued behind.
>
> The turn came when I noticed which problems repeated. Not exotic ones. An agent
> violating a convention I had written down. A session contradicting a ruling from an
> earlier session. A pull request that was fine except for the one invariant nobody
> re-checked. Every repeat had the same shape: the rule existed, the rule was written
> in a doc, and the doc was not in the loop.
>
> That gave me the premise I now run everything on. A rule that lives only in a doc
> gets violated silently. A rule with a guard, a gate, or a template is structurally
> hard to break. The whole job of the operator, it turns out, is moving rules from the
> first category to the second, one incident at a time.
>
> Concretely, the machinery sorts into three piles.
>
> Memory. A living handoff file at repo root that holds only what is in flight: the
> branch, the open PR, the half-done edits, the next three steps. It gets rewritten
> when I say the word "checkpoint", which means it gets rewritten at the moments that
> matter instead of never. Next to it, a numbered ledger of decisions, where a ruling
> is captured in the same turn it lands, because a ruling that lives only in a
> transcript gets re-litigated. And a small machine-readable file of settled facts
> sessions have proven, so no session pays to re-derive them.
>
> Enforcement. Lint guards for the invariants I actually care about, each one a small
> script that runs on every PR. The part I refuse to compromise on anymore: every
> guard ships with a test proving it can fail, a deliberately-bad fixture the guard
> must reject. It is embarrassingly easy to write a guard that never fires and then
> trust it for months. A guard that never fails is worse than no guard, because you
> stop looking. Same pile: a migration runner that refuses duplicate numbers and
> out-of-order applies before any SQL reaches a database. Two agents opening
> migrations on the same afternoon will eventually collide; a tool should catch that,
> not a human, and definitely not the database.
>
> Release. The merge is where autonomy gets real, so it is where I kept a dial
> instead of a switch. Agent PRs merge themselves only when every required check is
> green on the exact head commit, fail-closed, and for the production branch, only
> after I add a label. The label is one manual action, and it is my explicit release:
> checks green is the machine's opinion, the label is mine. Lower-stakes work merges
> on green alone. Getting this workflow right took more attempts than I want to
> admit, and the failure modes were nothing like what I would have guessed. That
> story gets its own post.
>
> Two honest caveats. First, none of this machinery is glamorous. It is handoff files
> and lint scripts and a JSON ledger, the plumbing of a very small institution. I did
> not build it out of foresight; almost every piece was paid for by a specific
> incident, and I have tried to keep the receipts attached, because a rule that
> cannot name the failure it prevents tends to get deleted by whoever inherits it,
> including future me. Second, you do not need all of it on day one. I didn't have it
> on day one. The order in which it earned its way in is roughly the order of this
> series.
>
> Which is what Fleet of One is. Eight posts, one lesson each, from solo dev to
> whatever this role actually is now. Operator is the closest word I have found: less
> time writing code, more time designing the system that writes it, and keeping that
> system honest. Next post: why sessions dying is a fact of life, and the one file
> that makes it stop mattering.
>
> Every artifact this series mentions, the templates, the guards with their must-fail
> fixtures, the merge workflow and its gotchas doc, lives in a public MIT repo,
> scrubbed of domain and ready to copy: https://github.com/The-825/agent-ops-playbook
>
> The repo is the companion to my book, From Archivist to Architect, a field guide for
> data analysts becoming architects, first in a planned series. It is out now on
> Amazon: [SWAP-ON-ASIN]

## Post 1 publishing checklist

One-time publication setup, before the first post:

1. Publication name: Fleet of One. One-line description: field notes from running a
   fleet of AI coding agents as one operator, on production systems that have to
   hold up. Both under Settings · Basics.
2. Write the About page: two or three paragraphs, same ground as the one-liner plus
   who it is for (working data people and solo builders operating agents).
3. Customize the free-subscriber welcome email (Settings · Emails): two sentences,
   what the series is and what arrives next.
4. Optional: claim a subdomain with your name or the series name while it is free.

Per-post steps for post 1:

1. Title: The day I stopped being the only person in my repo
2. Subtitle: Fleet of One, part 1. What changes when AI agents write most of the
   code and you become the institution.
3. Paste the post body from this file. Read it aloud once, end to end, before
   publishing (the binding rule in marketing/README.md).
4. Tags, in the draft's settings: AI, AI Agents, Software Engineering, Data
   Engineering. Four is plenty.
5. Social preview, same settings panel: a plain 1200x630 title card if one exists;
   otherwise skip it, the default text card is fine for post 1.
6. Publish now rather than schedule on launch day; the runbook sequences the hour.
7. Right after publishing, restack the post to Notes with one added line in your own
   words. Restacks reach Home feeds and are not emailed, so there is no double-send.
8. The other channels carry the repo link, not the Substack link. If a commenter
   wants the longer story, the Substack link goes in a reply, never in the post.
