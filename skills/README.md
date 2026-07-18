# Skills

Reusable rule sets from From Archivist to Architect, keyed to the book's chapters. A skill here is a paste-able rule set: a numbered list you can drop into your own agent rules file (CLAUDE.md or equivalent) or a team handbook and enforce as-is. Each file opens by naming the concrete failure the rules prevent, then gives you the block to copy. Take the whole set or cherry-pick single rules; they are written to stand alone.

| File | What it covers | From the book |
|---|---|---|
| [agent-session-efficiency.md](agent-session-efficiency.md) | Token-budget habits that stop an agent session from costing twice what it should, plus the operator-side counterpart. | Chapter 10 |
| [data-truth-rules.md](data-truth-rules.md) | Four rules against confidently wrong numbers: blank is not missing, signup is not activation, mirror the canonical query, sweep every source first. | The data-truth thread in Chapters 1, 3, and 5 |
| [feature-flag-lifecycle.md](feature-flag-lifecycle.md) | The graduation ladder for user-visible features: OFF, owner-only, pilot, graduated, retired. Reversible by config, not by revert. | Chapter 7, The Culture Shift |
| [regression-layering.md](regression-layering.md) | Catch each class of regression at the lowest layer that can catch it, from parse checks up to data-quality assertions. | Chapter 10 |
| [forward-only-migrations.md](forward-only-migrations.md) | Schema changes that only move forward: immutable numbered files, a runner that tracks applied-state, deprecation notes instead of drops. | Chapter 3, The SQL Library |
