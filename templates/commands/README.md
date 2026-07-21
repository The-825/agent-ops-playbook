# Command starter set

Thirteen copy-paste slash-command definitions for Claude Code, extracted from a production agent-ops setup and generalized. Each is a markdown file with YAML frontmatter; the body is the instruction the model follows when the command is invoked. They pair with the templates one directory up (the session-state and conclusions-store templates especially), but each works alone.

Note: this location is provisional pending a repo-layout decision on how command artifacts are packaged; if they move, it is one `git mv` and the files themselves do not change.

## Install

1. Copy the files you want into your repo's `.claude/commands/` directory. The filename becomes the command: `ship.md` installs `/ship`.
2. Fill the angle-bracket placeholders (`<main-branch>`, `<branch-prefix>`, `<conclusions-store>`, `<your-health-endpoint>`, and so on). They are all visible inline, and the more configurable files list theirs in a fill-these line near the top of the body.
3. Delete what does not apply to your repo. A command that references a file you do not keep should lose that step, not keep a dead pointer.

Frontmatter fields: `description` (shown in the command picker), `argument-hint` (shown as you type; arguments land in the body wherever `$ARGUMENTS` appears), `allowed-tools` (the tools the command is allowed to run), and optionally `model` (pin a command to a specific model). All are optional; a plain markdown body still works as a command, but `description` keeps the picker legible and `allowed-tools` scopes what the command can do.

## The commands

| Command | What it does · when to run it |
|---|---|
| [sprint.md](sprint.md) | Cuts a fresh feature branch from the default base on the `<branch-prefix>/<feature-slug>` convention. Run at the start of any coherent unit of work. |
| [ship.md](ship.md) | Commits, runs the pre-push checks and the adversarial pass, pushes, and opens a ready-for-review PR with a structured body. Run when the work is ready for review. |
| [adversarial-verify.md](adversarial-verify.md) | Spawns a subagent whose only job is to refute the current diff, then triages findings by severity and confidence. `/ship` runs it automatically; run it standalone for a second opinion on any diff. |
| [tiered-review.md](tiered-review.md) | Reviews a change set with a model-tier ladder: cheap draft pass, stronger adversarial verify pass, whole-change reconcile pass only when the change is wide. Run on large or risky change sets. |
| [model-check.md](model-check.md) | Classifies a task description (LOOKUP / SHIP / COMPLEX) and recommends a model tier from a table you fill in. Run before starting work when the right tier is not obvious. |
| [status.md](status.md) | One-screen snapshot: open PRs, local tree, what awaits the operator, what is blocked, next recommended action. Run at session start or after time away. |
| [checkpoint.md](checkpoint.md) | Rewrites `SESSION_STATE.md`, the living handoff file, from current reality, preserving the irreplaceable-values section verbatim. Run on the operator's "checkpoint" trigger, and before any model or session switch. |
| [warp.md](warp.md) | Answers "what do we know about X?" from the conclusions store, the repo index, and recent git history, without re-deriving from source. Run before touching an area you have not worked in recently. |
| [pending.md](pending.md) | Sweeps the repo for every deferred idea and follow-up, and reports each with its current status (delivered, ripe, blocked, invalidated, recurring). Run periodically so deferred work resurfaces instead of dying. |
| [scout.md](scout.md) | Evaluates an external URL against your repo with a have / borrow / adopt / skip verdict per concept, and persists a dated report. Run when someone sends you a tool or repo worth a look. |
| [optimize.md](optimize.md) | Five-phase performance review (baseline, frontend, transport, backend runtime, regression guards) with evidence-only findings. Run a few times a year or after a slow-feeling stretch. |
| [session-cost.md](session-cost.md) | Prints a per-model token and estimated-cost table for a saved session transcript, via a small stdlib-only helper script included in the file. Run when you want to know what a session cost. |
| [verify-deploy.md](verify-deploy.md) | Confirms a merge actually rolled out by checking the deploy workflow's runs and the health endpoint's version contract. Run after a merge you care about, mindful of batched deploy windows. |

## Safety posture

These commands are deliberately one-sided about write authority. `/sprint` creates a local branch and stops. `/ship` opens the PR and stops: it never merges, never enables auto-merge, and never applies an approval or merge-gate label, because authorizing a merge is the operator's act. `/status`, `/warp`, `/pending`, `/verify-deploy`, and `/model-check` read and report only. Keep that boundary when you adapt them; a command that can both open and approve its own PR removes the one human checkpoint in an agent-driven flow.

Part of the companion repo for From Archivist to Architect.
