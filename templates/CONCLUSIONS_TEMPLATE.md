# Conclusions store template

> Part of the companion kit for *From Archivist to Architect* (The Architect's Blueprint, Book 1). Pairs with section 10.6 (The Ledger and the Live Check).

Every session that re-derives a known fact pays for it twice: once in tokens, once in the risk of deriving it differently this time. The worst case is a session that contradicts a settled ruling because it never saw it. The conclusions store is a machine-readable file of settled knowledge (`CONCLUSIONS.jsonl`, one JSON object per line, keyed to the file or domain it concerns) that gets read or injected at session start, so future sessions inherit what this one proved. It is distinct from the decisions ledger: decisions are operator rulings; conclusions are anything a session discovered that would take real time to re-derive.

## The line format

```
{"path": "<repo-relative path, or 'domain' | 'operations' | 'process'>", "when": "<ISO date the conclusion was reached>", "what": "<one sentence, the durable fact, specific over general>", "evidence": "<PR #, commit SHA, or doc pointer so a reader can verify>"}
```

Optional fields: `tags` (array of strings) and `obsoleted_by` (pointer to the superseding entry; wrong entries get superseded, the store stays additive).

Three example lines:

```
{"path": "src/sync/orders_sync.py", "when": "2026-02-14", "what": "The orders API DateUpdated field is unreliable for incremental pulls; the watermark must use DateCreated.", "evidence": "PR #23"}
{"path": "domain", "when": "2026-03-01", "what": "A blank plan_type on the membership table means the default plan, not missing data; never count blanks as a coverage gap.", "evidence": "Operator ruling, session 2026-03-01"}
{"path": "dashboards/revenue.sql", "when": "2026-03-19", "what": "The revenue dashboard nets out refunds at query time; reconciling against the raw orders table without netting will always read high.", "evidence": "commit 8f2c1d0"}
```

## When to add a line

Add one when the fact would take real time to re-derive, when it corrects a prior misunderstanding (new line, plus `obsoleted_by` on the old one), when it records a gotcha not obvious from the diff, or when it captures a domain fact only the operator knew. Do not add restatements of code (code is the source of truth), anything already in the rules file, or restated PR bodies (link instead).

## Curation

Promote only verified conclusions, and prune wrong ones by superseding rather than deleting. Keep the curated core small and separate from any bulk-mined archive: when one team merged a history-mined backfill of hundreds of entries into the curated file, it swamped the session-verified entries and wrecked lookup precision. The core file stays small and injection-worthy; an archive is a labeled secondary source, and entries promote only when a session actually relies on one and re-verifies it.

The rules file holds the rules. The state file holds the rolling handoff. This file holds what you now know.
