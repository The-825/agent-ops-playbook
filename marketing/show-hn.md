# Show HN draft (optional channel)

An optional submission. Honest and technical or not at all: Show HN threads reward
plain speech and punish anything that smells like marketing.

## Fit, and the warning that matters

Show HN requires something people can try, and reading material is explicitly off
topic (https://news.ycombinator.com/showhn.html, checked 2026-07-21). This repo
qualifies through the runnable kit, so the submission leads with that: the CI guards
with their must-fail fixtures, the migration runner, the fail-closed automerge
workflow. If the framing drifts toward "a playbook to read", the post is off topic
and will get flagged.

Rules that bind, from the Show HN page and the site guidelines:

- The title must start with "Show HN:" and stay plain. No superlatives, no all-caps,
  no exclamation points, under 80 characters.
- Submit from your personal account, be around for the thread, and never ask anyone
  to upvote or comment. Vote-ring detection is real and unforgiving.
- Retype the comment below in your own words before posting; do not paste it. HN
  readers are sharply tuned to generated text right now, and the words should be
  yours anyway.

## Submission

- Type: link submission. URL: https://github.com/The-825/agent-ops-playbook
- Title: Show HN: CI guards and fail-closed automerge for AI-agent PRs
- Fallback title if that reads too narrow on the day: Show HN: The ops files I use
  to run AI coding agents solo against production

## First comment (substance to retype, not text to paste)

> For the last two years, most of the PRs on the production system I run (regulated
> PII, real users, one human: me) have been opened by AI coding agents, several
> sessions a day. The repo is the operating layer that keeps that from going wrong.
>
> What is in it: six small stdlib-Python lint guards that run on every PR, each
> shipping with a deliberately-bad fixture it must fail and a clean one it must
> pass, so CI proves the guards still bite. A migration runner that refuses
> duplicate numbers and out-of-order applies before any SQL reaches a database,
> with an applied-where ledger. A fail-closed automerge workflow: agent PRs merge
> only when every required check is green on the exact head SHA, and the production
> branch also waits for a human-applied label. A companion doc walks six failure
> modes of the naive automerge, each one hit in production first. Plus templates
> for the memory layer: a session handoff file, a decision ledger, and a
> machine-readable settled-facts store.
>
> MIT, no signup, no product. It pairs with a book I am finishing on the
> analyst-to-architect path; the repo stands alone and the book is a pointer in the
> README.
>
> One honest disclosure: agents helped build the repo itself. Nearly every rule in
> it exists because an agent broke something first. The automerge gotchas doc is
> the part I would most like challenged.

## Posting notes

- Weekday morning Pacific, on a day you can watch the thread for a few hours.
- Show HN entries start on the new and shownew feeds and need a few points to reach
  the Show front page. Slow starts are the median outcome, not a failure.
- Reply to every technical question. Concede fair criticism in one sentence, then
  add the detail. Never argue tone.
- If it sinks, one repost weeks later with a sharper title is within site norms;
  more than that is not.
