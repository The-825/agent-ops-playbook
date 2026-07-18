# Feature flag lifecycle

*From the book: Chapter 7, The Culture Shift.*

Shipping a feature to everyone at once leaves you one bad deploy away from a pressure revert: a rollback commit written at speed, entangled with unrelated changes that landed since, pushed while users are already seeing the breakage. The alternative is a graduation ladder. Every user-visible feature merges dark behind a flag, and rollout becomes a config change instead of a deploy. Paste the rules below into your agent rules file or engineering handbook.

```markdown
## Feature flag rules

1. Every user-visible feature ships behind a feature flag, default OFF
   in production. The code merges and deploys dark.
2. Graduation ladder, in order:
   a. OFF: merged, live in production code, invisible to everyone.
   b. Owner-only preview: enabled for the builder's own account, who
      exercises the feature against real production data while nobody
      else sees it.
   c. Role or team pilot: enabled for one role or team.
   d. Graduated: default ON for everyone.
3. Rollback at any rung is a config change: reset the flag to OFF and
   clear the per-identity and per-role enables. No deploy, no revert.
   Reversible by config, not by revert.
4. Flags fail closed. If the flag store is unreachable or the flag is
   unknown, the feature is OFF.
5. The flag store lives on the transactional database, not the
   analytics warehouse. A warehouse-backed flag table becomes a stale
   second source of truth.
6. Retire the flag once the feature has been graduated and stable for a
   full release cycle. Remove the flag check and the flag row; a dead
   flag is a trap for the next reader.
```

## Adoption notes

The binding rule is only the first hop: ship OFF. Every later hop is a judgment call the owner makes when ready, which is exactly the point. The ladder separates "is the code deployed" from "who can see it", and once those are separate questions, launches stop being events.

The owner-only rung earns its keep fast. It is the only way to test a feature against real production data with zero user exposure, which matters most for anything that writes: a staging box that shares the production database cannot give you that safety, because a staging write is a production write.

On storage, the failure mode is subtle. A flag table in the analytics warehouse looks convenient right up until runtime toggles and the warehouse copy drift apart, and then two systems disagree about what is live. Keep flags where your app already does transactional reads, and treat the runtime store as the single source of truth.

When in doubt: flag it.
