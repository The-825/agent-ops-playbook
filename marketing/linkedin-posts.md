# LinkedIn drafts

Three short lesson posts, 100 to 200 words each, final text below. Each post stands
without its link; if reach visibly suffers with the link in the body, cut it from the
body and paste it as the first comment instead (the line to move is the last one of
each post).

## Cadence plan

- One post a week for three consecutive weeks, in the order below.
- Mid-week, Tuesday to Thursday, between 7 and 9am Pacific.
- Post 1 goes out on launch day (LAUNCH_RUNBOOK.md slots it into the hour). Posts 2
  and 3 follow at one-week intervals in the same window.
- Watch which post lands hardest; that picks the next newsletter topic. Reply to
  every substantive comment the same day; the first two hours matter most for reach.

---

## Post 1 · Test the tests

> A CI rule I now apply everywhere: every lint guard has to prove it can fail.
>
> Each guard in my repos runs twice in CI. Once against a deliberately-bad fixture,
> where it must fail, and once against a clean fixture, where it must pass. If the bad
> fixture ever passes, the build breaks, because the guard has stopped guarding.
>
> I added this after realizing how easy it is to write a check that never fires (one
> wrong regex will do it) and then trust it for months. With AI agents opening most of
> my PRs, that trust gets tested far more often than it used to.
>
> A guard that never fails is worse than no guard. You stop looking at the thing it
> was supposed to watch.
>
> The six guards I run, with their fixtures and self-tests, are in the public playbook
> repo: https://github.com/The-825/agent-ops-playbook
>
> #ContinuousIntegration #AIAgents

---

## Post 2 · Sessions die. Plan for it.

> AI coding sessions die constantly. Context fills up and compacts, laptops close
> mid-task, tomorrow's session starts cold. Early on I treated that as an annoyance.
> It is actually an operations problem, and it has an operations fix.
>
> There is one file at the root of every repo I run agents in: SESSION_STATE.md. It
> holds only what is in flight right now. Active branch, open PR, half-done edits by
> file, the next three steps, the decisions I still owe. When I say "checkpoint", the
> session rewrites it to match reality.
>
> The trigger word is the whole trick. "Keep the doc updated" means never. An explicit
> refresh at the moments that matter means the next session, or the next model, or me
> after a weekend, picks up mid-flight instead of re-deriving everything.
>
> It works for human handoffs too. That part should probably have been obvious.
>
> Template with the usage rules written in: https://github.com/The-825/agent-ops-playbook
>
> #AIAgents #DeveloperExperience

---

## Post 3 · Autonomy is a dial

> My coding agents merge their own pull requests. People hear that and picture
> recklessness, so here is the actual mechanism.
>
> A merge happens only when every required check is green on the exact head commit,
> fail-closed: anything missing, pending, or unclear means no merge. And for the
> production branch there is one more gate. Me. A PR merges only after I add a label
> to it. One click. The checks are the machine's opinion that the change is safe; the
> label is mine.
>
> Autonomy is a dial, not a switch. Low-stakes branches merge on green alone.
> Production waits for the label. Nothing merges on vibes.
>
> The naive version of this workflow has at least six failure modes, and I hit them in
> production before the current version existed. The workflow, plus the write-up of
> all six: https://github.com/The-825/agent-ops-playbook
>
> #AIAgents #SoftwareEngineering
