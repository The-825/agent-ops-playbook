# DECISIONS.md template: what we do differently, and why

One of the four founding docs of a disciplined rebuild (alongside your operating rules doc,
your phased build order, and your parity checklist). Each row is a day-one decision paired
with the specific debt or incident in the old system it prevents. That pairing is the point:
abstract rules are easy to ignore; a rule traced to a named failure earns its place. Filling
in the right column doubles as a retrospective of the system you are replacing.

How to use this template: copy it, keep the left column (neutralize or delete any decision
that does not apply to your stack), and replace every right-column prompt with your own
evidence. Be specific: name the file, the number, the outage, the week lost. If you cannot
name a failure a decision prevents, question whether the decision belongs in your list.

> **Example of a filled row (anonymized, from a real production system):**
>
> | Decision | What it avoids in the old system |
> |---|---|
> | Modular frontend, one module per view, from day 1 | The old frontend grew into a ~19,000-line single-file classic script; the decomposition plan kept outrunning itself because extraction started years too late. |

## Architecture (structure from commit 1, not retrofitted)

| Decision | What it avoids in <old-system> |
|---|---|
| Modular frontend, one module per view, from day 1 | *What monolith did the old frontend become, and when did extraction start?* |
| App factory + per-area route modules + shared helpers from day 1 | *Did the old backend start as a single file? When was it decomposed, and what did the delay cost?* |
| One version-controlled database view layer | *Did views exist only in a console? Did any drift from their checked-in DDL?* |
| Data-quality assertions wired into a real run gate | *Were assertions compile-only? Did any ever run against production?* |
| Feature flags on one store, fail-closed uniformly, from day 1 | *Did flags live in two stores? Did any flag fail open on exception?* |
| Central config registry from day 1 (one frozen dataclass, every env var and threshold in it) | *Where were the magic numbers scattered? What inline literals survived the retrofit?* |
| CI-stamped version strings, never hand-bumped | *What drifted when versions were hand-edited in two places?* |
| Migration runner (tracks applied-per-tenant, refuses duplicate numbers and out-of-order apply) | *What numbering collision or out-of-order apply reached your database from a loose folder?* |
| ADR directory from day 1 | *Which architectural decision can nobody explain anymore?* |

## Testing and CI (floor before features)

| Decision | What it avoids in <old-system> |
|---|---|
| CI lint guards from the first PR | *What convention decayed for months before a guard stopped the re-creep?* |
| Test-gated deploys from the first deploy | *Did a red test ever fail to block a rollout? What shipped broken?* |
| Route-integration harness + render-the-view smoke from day 1 | *What bug returned 200 from the route but rendered an empty page?* |
| Browser e2e suite from day 1 | *What runtime regression class forced the retrofit?* |
| API spec discipline, prefer generated over hand-curated | *Did the hand-curated spec drift as routes evolved?* |

## Data model (design-in, not patch-in)

| Decision | What it avoids in <old-system> |
|---|---|
| Typed ingestion, no schema autodetect, plus a null-rate quarantine that refuses a degraded write | *Did an autodetect load ever silently null out or re-type columns at scale?* |
| Never rebuild a canonical store from a side snapshot or spreadsheet | *Did a rebuild-from-snapshot ever resurrect deleted state?* |
| Soft-delete recoverability as the load-bearing wall | *What longitudinal analysis is only possible because records never disappear?* |
| Stamp the real domain event, not the sweep date | *Did a batch-sweep timestamp masquerade as the event date and break an analysis?* |
| Blank-is-not-missing encoded in the data dictionary at schema time | *Which presence-flag or categorical fields were misread as "mostly missing"?* |
| Reconcile stated intent against observed behavior as first-class | *Where did a silent "no" (a form nobody was required to submit) distort a denominator?* |
| One writer per field; resolver-owned columns excluded from bulk upserts | *Did a re-pull ever wipe hand-resolved values? What did resolution coverage do once you excluded them?* |
| Incremental watermark on a reliable field | *Which timestamp field turned out to be unreliable, and what did syncing on it miss?* |
| Stable-key table naming, never a mutable slug | *Did renames ever spawn duplicate tables via slug drift?* |
| Operator-set current-period singleton, never derived from the clock | *Did calendar logic baked into code go stale until a redeploy?* |
| Resolve identity to a canonical key before comparing aliases | *How many "changes" were the same person under different aliases or typos?* |

## Process

| Decision | What it avoids in <old-system> |
|---|---|
| Source-inventory gate before any multi-source aggregation | *What surface got built on the first source reached and missed the rest?* |
| Batch-push cadence + feature-slug branches | *Did work ever land on a session-named or auto-generated branch?* |
| Capture a semantic ruling the same turn it lands | *Which ruling lived only in a transcript and got re-litigated or silently violated?* |

## Build order (the meta-lesson)

Fill this section in prose. The pattern to look for: the old system built features first and
the force-multiplier floor second, so config registries, flags, the view layer, e2e tests,
the API spec, the test harness, and module decomposition all arrived as retrofits. The
rebuild inverts that order: lay the floor first (Phase 0 infrastructure, then the data
spine), then compose features on the patterns. State your own version of that verdict here,
with whatever evidence your retrospective produced, and link your build-order doc.
