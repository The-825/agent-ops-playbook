# The model playbook: per-tier operating rules

> Part of the companion kit for *From Archivist to Architect* (The Architect's Blueprint, Book 1).

One repo, one set of binding rules, several tiers of model running sessions against them. A deep model can infer its way to the right file and the right caveat; a cheaper model gets the same accuracy at lower cost only if the repo substitutes deterministic routing for open-ended inference. That substitution is the whole design brief of this playbook: the boot protocol supplies the routing, the guardrails pin the facts, and the per-tier counter-rules name each tier's characteristic failure and its counter.

Write the playbook as a file in the repo, and have every session read it once at start. It is the one doc where the reader's identity changes the instructions.

## Tiers, not model names

Frame everything in capability tiers, because model lineups and prices change faster than operating rules do:

- **Fast tier**: the cheapest model you run. Lookups, status pulls, mechanical single-file edits.
- **Mid tier**: the daily driver. Bounded feature work, doc edits, well-specified fixes.
- **Deep tier**: the strongest model you pay for. Undecided approaches, mystery debugging, architecture, multi-PR arcs.

| Tier | Your model (edit this column) | Typical work |
|---|---|---|
| Fast | `<fast-model>` | Lookups, log reads, yes/no checks, CI watching |
| Mid | `<default-model>` | Feature work, single PRs, doc edits, known-cause fixes |
| Deep | `<deep-model>` | Debugging with unknown cause, refactors, design, long arcs |

Example ladder, for calibration only: at the time of writing, one production setup mapped the tiers to Haiku (fast), Sonnet (mid), and Opus (deep), with a frontier model above the ladder for judgment-heavy synthesis. Treat that as the shape of a ladder, not a prescription; fill the column from your provider's current lineup, and update it when the lineup moves.

## Boot protocol, all tiers

Each step exists to prevent a specific waste pattern.

1. **Never re-read the auto-attached rules file.** The harness loads it at session start; a second read pays its full length for zero new information.
2. **Resuming mid-workstream? Read the session handoff file first.** Active branch, in-flight work, pending decisions. It is short on purpose ([templates/SESSION_STATE_TEMPLATE.md](../templates/SESSION_STATE_TEMPLATE.md)).
3. **Route, do not explore.** Follow the kernel-to-catalog-to-stamp shape from [context-budget.md](context-budget.md): the rules kernel names the destination class, the catalog names the file and anchor, the target file's stamp confirms the hop. For fast- and mid-tier sessions this is the *entire* boot read set: kernel plus catalog route, nothing else until a route demands it. Deep-tier sessions add one read of the full-system mental-model doc when the task genuinely spans systems, and skip it for everything narrower. The deep tier can afford to reconstruct the big picture from scattered reads; buying it pre-assembled is still cheaper.
4. **Open only the narrow cited source.** Grep to locate, then read the specific line range. Reference docs are grep targets, not cover-to-cover reads, on every tier.
5. **Use the committed commands for recurring workflows** (cut a branch, ship a PR, run the continuity sweep). Each one encodes conventions a session would otherwise re-derive at full price.
6. **Verify against the live system before authoring changes to it.** A thirty-second schema or endpoint check before writing a migration or citing a figure. Assumed-absent things that existed have cost real rework on every tier.

## Accuracy guardrails, all tiers

The guardrails bind every tier equally. Cheaper tiers hit them more often; that changes the frequency of the check, never the rule.

1. **Every reported figure names its canonical source.** Mirror the query the production surface runs; never hand-roll an aggregation off raw tables. If you cannot name the source, you have not looked it up. (The full rule set: [skills/data-truth-rules.md](../skills/data-truth-rules.md).)
2. **Blank is not missing.** Check the data dictionary or run a value-distribution query before calling any field sparse. In many schemas a blank is a meaningful value, not a gap.
3. **Domain semantics are quoted, not paraphrased.** Status vocabularies, category definitions, threshold values: quote the canonical doc verbatim. A confident paraphrase that drops one nuance is the costliest class of error, because it reads as correct.
4. **Two failed lookups means stop and say so.** "Not found; I need a pointer to the source" beats a synthesized answer every time. The operator resolves a pointer in seconds; unwinding a fabricated one costs a session.
5. **Verify before write.** Parse checks before push, schema checks before SQL, a live read before changing any displayed number. The cheapest regression layer that covers the change, every time ([checklists/pre-push.md](../checklists/pre-push.md)).
6. **Push, never merge.** The merge gate owns merges; sessions open PRs on feature branches and stop there ([checklists/pr-discipline.md](../checklists/pr-discipline.md)).

## Per-tier counter-rules

Each tier fails in a characteristic direction. The counter-rules are written against the direction, not against the tier's competence.

### Deep tier: spends too much

The deep tier's failure mode is cost, not correctness. It reads broadly to be safe, re-verifies what the repo already pins, and narrates.

- **Grep first, read narrow, one research agent per question.** Parallel agents on overlapping questions duplicate tokens for no added coverage.
- **Verify a live value once, then trust it for the session.** Thresholds and invariants the index files already pin do not need re-derivation.
- **No narration.** Run the tool instead of announcing it. Two-sentence turn summaries. One-sentence corrections.
- **Hold scope in long arcs.** Before every push: re-read the diff, run the cheapest covering check, confirm the diff matches the PR's stated scope and nothing more.
- **Plan first for multi-file work; skip the ceremony for two-file edits.**

### Mid tier: guesses too plausibly

The mid tier's failure mode is the confident answer assembled from pattern instead of lookup. Its counter-rules are all forms of "show your source."

- **Never assert a figure without naming the endpoint or view it came from.** Unable to name it? Run the routing lookup first.
- **The repo's gotcha list is a mandatory pre-flight** before schema, git, or data-diagnosis work. Every entry is a trap a prior session actually fell into.
- **Quote, do not reconstruct, domain semantics** (guardrail 3 binds hardest here).
- **The escalation valve is a rule, not an admission.** A debugging arc still guessing after thirty minutes on what looked like a five-minute fix says so explicitly and recommends restarting the task on the deep tier. More dead-end turns on the mid tier cost more than the escalation.

### Fast tier: must not decide alone

The fast tier is bounded by an allow-list, because its failure mode is doing plausible-looking damage quickly.

- **Allowed:** status pulls, single-file lookups, log reads, yes/no checks, watching CI.
- **Never:** schema changes, migrations, deletions, auth-touching code, multi-file edits, debugging real failures, authoring anything that states figures about regulated data.
- **The tell:** a fast-tier session editing its second file is the signal to stop and escalate. Not finish the edit, stop.
- **Escalation is the success path.** A fast-tier session that says "this is above my lane" has done its job. A wrong confident answer has not.

## Switching tiers mid-arc

Start cheaper, escalate on a wall. Before switching, refresh the session handoff file so the next tier boots from written state instead of re-deriving (or compacting away) the conversation. Switch at task boundaries, never mid-debug: the context the old session holds does not transfer, and rebuilding it mid-problem costs more than the tier arbitrage saves. The on-demand classifier that recommends a tier from a task description ships as a command in this kit ([templates/commands/model-check.md](../templates/commands/model-check.md)).

## Operator side: the first message is tier-tuned

- **To the mid tier:** name the target file, the pattern to mirror ("like the existing one in X"), and the acceptance criterion in message one. State edge cases and scope up front; each clarifying round is a full turn.
- **To the deep tier:** give the goal, the constraints, and what is explicitly out of scope, then let it plan. Do not over-specify the how.
- **To every tier:** batch related asks into one message, reference code by path and line, front-load any operational nuance that changes the data model, and when correcting a number, name the canonical source so the fix hits the root.

## Maintenance

Update the playbook when the model lineup changes, and when a new recurring error mode gets documented: the new mode goes in the guardrails table and in the repo's gotcha list, in the same PR. A playbook that lags the lineup misroutes every session that trusts it.
