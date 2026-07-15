# Automerge gotchas: six failure modes a naive automerge hits

`automerge.yml` squash-merges an agent PR only when every required check is green on the PR
head SHA, fail-closed. It stands in for GitHub's paid auto-merge feature on Free-plan private
repos. The workflow looks simple. It is not. Every gotcha below is a real failure mode that was
hit in production use of this pattern; the shipped file already encodes the fix for each one.
Read this before adapting the template, and re-read it before "simplifying" it.

The reusable core is a single `requiredChecksGreen(headSha)` gate driven by an explicit
`REQUIRED_CHECKS` list. Each named check must be completed + success on the head SHA; anything
missing, pending, or failed returns false and skips the merge.

## Gotcha 1: `checks: read` permission is required or the gate 403s

Without `checks: read` in the workflow's `permissions:` block, `checks.listForRef` returns 403
and the gate can never confirm green, so nothing ever merges. The failure is silent from the
PR's point of view: checks are green, the PR just sits there.

> **Incident (anonymized).** In the production repo this pattern was extracted from, the
> missing `checks: read` scope was discovered only after green PRs stopped merging, and it took
> a dedicated fix PR to close it.

## Gotcha 2: draft-to-ready must re-fire the gate

Flipping a draft PR to ready-for-review fires no new check run. A PR whose checks went green
during the draft window never re-evaluates, so it sits unmerged until someone hand-merges it.
Fix: a second trigger, `pull_request: [ready_for_review]`, running the identical gate.

## Gotcha 3: verify required checks on the head SHA, never the workflow_run conclusion

The gate calls `checks.listForRef({ ref: pr.head.sha })` and requires every named check to be
completed + success there. Trusting `workflow_run.conclusion` instead means only the triggering
workflow gates the merge; any required check that lives outside it silently stops being a gate.
Verifying the head SHA makes every required check a real gate on every trigger path.

## Gotcha 4: automerge does not fire on `synchronize`

New commits on the PR branch do not re-trigger this workflow directly. Re-evaluation comes only
via the checks workflow's `workflow_run` completion (and the ready_for_review path). This is
fine, and it is worth understanding why: a push (including a merge of main into the branch)
re-fires the checks workflow, and that workflow's completion re-drives the merge gate. If you
add trigger types, keep the gate identical on every path.

## Gotcha 5: an explicit `permissions:` block zeroes all unlisted scopes

Declaring `permissions:` at all switches the token from default scopes to exactly what you
list. Every scope the script needs must be enumerated: `contents: write` (the squash merge),
`pull-requests: write` (the merge API), `checks: read` (the gate). Forgetting one does not fail
the workflow at parse time; it silently breaks the corresponding API call at run time.

## Gotcha 6: both required checks must be jobs in ONE workflow (the separate-workflow never-merge trap)

The check names in `REQUIRED_CHECKS` ("Static checks", "E2E checks") are job names inside one
workflow ("Required checks") on purpose. If the e2e job lived in its own workflow, the
`workflow_run` trigger keyed on the first workflow would fire when it finished, the head-SHA
gate would (correctly, fail-closed) skip because e2e was still pending, and nothing would ever
re-fire once e2e went green. The PR would sit unmerged forever with all checks passing.
Co-locating the jobs makes one `workflow_run` completion cover both. If you must keep separate
workflows, add a `workflow_run` trigger per checks workflow; the head-SHA gate stays correct
either way, but every checks workflow needs to be able to re-drive the merge.

## Design trade-offs from two generations of this workflow

The shipped file is the second, simplified generation. An earlier, more elaborate production
variant of the same pattern made three choices worth knowing about before you adopt.

### The operator-label gate

The earlier variant required an operator-applied label (its convention: a "greenlight" label)
on PRs from the primary agent's branch namespace before they could merge to the production
branch. Checks-green alone was not enough; a human explicitly released each merge, and the gate
failed closed (a PR with no labels never merged). Other, lower-stakes agent namespaces merged
on green checks alone. The version shipped here drops the label gate for a faster hands-free
flow.

This is a genuine trade-off, not a recommendation: the label gate buys a human in the loop
before production at the cost of one manual action per PR. If you adopt it, add
`pull_request: [labeled]` as a third trigger running the identical gate, so applying the label
to an already-green PR merges it without waiting for another checks run, and treat a missing
labels array as unlabeled (fail closed).

### The GITHUB_TOKEN recursion-guard trap

A squash-merge performed with the default `GITHUB_TOKEN` does not trigger push-event workflows
on the target branch. That is GitHub's deliberate infinite-loop guard, and it means your
deploy-on-push and smoke-test-on-push workflows DO NOT RUN for auto-merged PRs.

> **Incident (anonymized).** In the earlier production variant, every auto-merged PR reached
> the production branch with no deploy and no smoke run, silently, until the workflow was
> extended to explicitly `workflow_dispatch` the deploy and smoke workflows after a successful
> merge. The dispatch API is the recursion guard's one exemption.

If your automerge target branch has push-triggered workflows, either dispatch them explicitly
post-merge or switch the merge to a PAT/GitHub App token (which re-introduces loop risk you
must then guard yourself). The template shipped here does not include a post-merge dispatch
because it assumes no push-triggered deploy; add one if you have one.

### Poll-loop vs event-driven

The earlier variant polled check-run status in a wait loop after its trigger fired, and had to
mirror the lint workflow's path filters exactly; when the filters drifted, a docs-only PR could
merge without waiting for a required scan (a documented hole in that repo). The event-driven
head-SHA gate shipped here removes both needs: no polling, no filter mirroring, because the
gate re-evaluates on every checks-workflow completion and verifies actual check runs. Use the
poll loop only if you genuinely cannot restructure your required checks into one workflow.
