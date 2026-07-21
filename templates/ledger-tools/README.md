# Ledger tools

> Part of the companion kit for *From Archivist to Architect* (The Architect's Blueprint, Book 1).

The capture habit gets a conclusions ledger written ([docs/decision-capture.md](../../docs/decision-capture.md), base line format in [CONCLUSIONS_TEMPLATE.md](../CONCLUSIONS_TEMPLATE.md)). This directory is about the harder half: keeping the ledger trustworthy after months of entries, several writing surfaces, and a codebase that keeps moving underneath it.

| File | What it is |
|---|---|
| [PROVENANCE.md](PROVENANCE.md) | Three optional provenance fields (`src`, `verified`, `by`) extending the base entry format |
| [conclusions_audit.py](conclusions_audit.py) | Staleness auditor: classifies every entry STALE / AGING / SPECIAL / OK and checks `obsoleted_by` chains |
| [sample_conclusions.jsonl](sample_conclusions.jsonl) | Synthetic six-line fixture that demonstrates every verdict |
| [capture_nudge.py](capture_nudge.py) + [capture-nudge.md](capture-nudge.md) | UserPromptSubmit hook that injects a same-turn capture reminder when a prompt contains ruling-shaped language |
| [union-merge.md](union-merge.md) | The `merge=union` gitattributes setting for parallel appenders, with the cases where it is unsafe |

The four pieces cover a ledger entry's whole life: it gets written at all (the nudge), it carries its origin and last-checked date (provenance), its decay gets measured instead of discovered (the auditor), and parallel writers stop fighting over the end of the file (union merge).

## Try it

From the repo root:

```
python3 templates/ledger-tools/conclusions_audit.py templates/ledger-tools/sample_conclusions.jsonl --root .
python3 templates/ledger-tools/conclusions_audit.py --selftest
```

The first command audits the sample fixture against this repo's tree and reports one STALE entry, one AGING entry, one skipped special path, and one dangling `obsoleted_by` pointer, by design. The second runs the auditor's offline fixture tests.

## Adopting

Copy `conclusions_audit.py` anywhere in your repo (it takes the ledger path as an argument and resolves entry paths against `--root`), copy `capture_nudge.py` into `.claude/hooks/` and register it per [capture-nudge.md](capture-nudge.md), and add the one-line `.gitattributes` entry once your ledger has parallel writers. The auditor is a report, not a gate: it exits 0 whatever it finds, so it fits a scheduled job or a manual sweep without blocking anything. Its `--file-tasks` flag is a stub seam for wiring findings into your issue tracker.
