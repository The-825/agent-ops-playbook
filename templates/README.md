# Templates

Copy-paste starting points for the working files an agent-assisted repo needs. To adopt one: copy the file, fill the angle-bracket placeholders, delete what does not apply, and commit it to your repo root or docs directory. Each template's intro explains the failure it prevents, so read that before deciding whether you need it.

| File | What it is |
|---|---|
| [CLAUDE_TEMPLATE.md](CLAUDE_TEMPLATE.md) | Starter rules file for any agent-assisted repo: operating tier, binding rules, PR conventions, known-issues ledger |
| [SESSION_STATE_TEMPLATE.md](SESSION_STATE_TEMPLATE.md) | The living handoff file, refreshed on "checkpoint", so a new session picks up mid-flight |
| [DECISIONS_TEMPLATE.md](DECISIONS_TEMPLATE.md) | Append-only decisions ledger: durable rulings captured the turn they land, plus the rebuild variant pairing each day-one decision with the failure it prevents |
| [CONCLUSIONS_TEMPLATE.md](CONCLUSIONS_TEMPLATE.md) | JSONL store of settled facts, keyed by path, read at session start so knowledge survives sessions |
| [PARITY_TEMPLATE.md](PARITY_TEMPLATE.md) | Zero-regression parity inventory for a rebuild or migration, bucketed and checked with evidence |
| [ADR_TEMPLATE.md](ADR_TEMPLATE.md) | One-page architecture decision records, framed for data platforms, with a filled example |

The templates reference each other (the rules file points at the state file, the ledger, and the conclusions store). They work fine alone, but they were designed as a set.

CONCLUSIONS_TEMPLATE.md pairs with [conclusions.jsonl](conclusions.jsonl), a ready-to-copy starter store, and the same-turn capture practice behind the ledger and the store is written up in [docs/decision-capture.md](../docs/decision-capture.md).
