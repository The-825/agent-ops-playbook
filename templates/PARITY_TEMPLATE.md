# Parity inventory template

*From the book: Chapter 1, The Data Debt Audit.*

Rebuilds fail by silently dropping the feature nobody remembered. Not the big pages, the small stuff: the endpoint one report depends on, the Sunday job that renews a webhook, the permission rule that hides admin tools from regular users. The parity inventory is the zero-regression contract for any rebuild or migration: every capability of the old system appears here as a row, and parity is declared only when every row is checked with evidence. No row, no capability; unchecked row, not done.

## How to use this inventory

1. **Inventory first, build second.** Before writing any new code, walk the old system and fill every bucket below. Crawl the route table, the scheduler config, the cron entries, the permission checks, the report list. The rows you fail to write are the regressions you will ship.
2. **One row per capability.** Purpose in a few words, where it lives in the old system, which build phase it lands in, and a status.
3. **Status legend:** `☐ not started` / `◐ in progress` / `☑ done`. A row moves to `☑ done` only when the capability is rebuilt AND its named evidence exists (a passing test, a verified output, a recorded operator sign-off). Note the evidence in the Status cell.
4. **Deferred and dropped are statuses, not deletions.** If a capability is intentionally not being rebuilt, mark it `DROPPED` with the reason and who approved it. A silent omission and a recorded drop are entirely different things.
5. **The rollup at the bottom is the honesty check.** Totals per bucket, so "we're basically done" has to survive arithmetic.

## The inventory

```markdown
# PARITY.md · zero-regression inventory for <rebuild name>

Every capability of <old system> appears here as a row. No capability is done
until its row is checked with the evidence named on it. This rebuild does not
invent new scope: parity first, then improvements.

Legend: ☐ not started / ◐ in progress / ☑ done (rebuilt + evidence recorded).

---

## 1. Pages and user-visible surfaces

| Item | Purpose | Old-system source | Phase | Status |
|---|---|---|---|---|
| Orders list page | Browse and filter orders | /orders | 2 | ☐ not started |
| Order detail page | Single order with line items | /orders/:id | 2 | ☐ not started |
| Revenue dashboard | Executive rollup, monthly trend | /dashboard | 3 | ☐ not started |
| Member signup form | Public signup, writes membership record | /signup | 2 | ☐ not started |
| <every page, panel, modal, and export button> | | | | ☐ not started |

## 2. API endpoints

| Item | Purpose | Old-system source | Phase | Status |
|---|---|---|---|---|
| GET /api/orders | Orders list (paginated, filterable) | orders module | 2 | ☐ not started |
| PATCH /api/orders/<id> | Edit one order | orders module | 3 | ☐ not started |
| GET /api/members/summary | Membership rollup counts | members module | 3 | ☐ not started |
| <every route, including the internal and diagnostic ones> | | | | ☐ not started |

## 3. Scheduled jobs and pipelines

| Item | Cadence | Action | Phase | Status |
|---|---|---|---|---|
| daily-orders-sync | 6 AM daily | Pull new orders from the source API | 1 | ☐ not started |
| weekly-digest | Mon 8 AM | Email the revenue digest to leadership | 3 | ☐ not started |
| monthly-full-refresh | 1st @ 5 AM | Full re-merge to catch late edits | 1 | ☐ not started |
| <every cron entry, scheduler job, and retry/renewal job> | | | | ☐ not started |

Decommissioned, do NOT recreate: <jobs and services retired on purpose>.

## 4. Reports and views

| Item | Purpose | Old-system source | Phase | Status |
|---|---|---|---|---|
| Active-members view | Canonical active-member filter | warehouse view | 1 | ☐ not started |
| Monthly-revenue view | Netted monthly revenue (refunds excluded) | warehouse view | 2 | ☐ not started |
| Churn report | Monthly churn by plan | reporting suite | 3 | ☐ not started |
| <every view, saved report, and export the business actually opens> | | | | ☐ not started |

## 5. Integrations and webhooks

| Item | Purpose | Old-system source | Phase | Status |
|---|---|---|---|---|
| Signup-form webhook | Receives form submissions in real time | webhook receiver | 1 | ☐ not started |
| Payment-provider sync | Reconciles charges and refunds | billing module | 2 | ☐ not started |
| <every third-party connection, inbound and outbound> | | | | ☐ not started |

## 6. Roles and permissions

| Item | Rule | Old-system source | Phase | Status |
|---|---|---|---|---|
| Admin-only settings | Settings surface hidden from non-admins | auth module | 2 | ☐ not started |
| Member-data gate | Every member-data endpoint resolves the caller first | auth module | 1 | ☐ not started |
| <every role, gate, and visibility rule> | | | | ☐ not started |

## 7. Tests and quality gates

| Item | Covers | Old-system source | Phase | Status |
|---|---|---|---|---|
| Orders e2e smoke | Orders page renders with live data | e2e suite | 2 | ☐ not started |
| Data-quality assertions | Views return zero bad rows | warehouse tests | 1 | ☐ not started |
| <every CI gate, lint guard, and assertion the old system ran> | | | | ☐ not started |

## 8. Operational docs and runbooks

| Item | Purpose | Old-system source | Phase | Status |
|---|---|---|---|---|
| Deploy runbook | How a change reaches production | ops docs | 1 | ☐ not started |
| Incident rollback steps | Cheapest reversal per failure class | ops docs | 2 | ☐ not started |
| <every doc an operator would miss at 2 AM> | | | | ☐ not started |

---

## Rollup

| Section | Rows | ☑ done |
|---|---|---|
| 1. Pages and surfaces | <n> | 0 |
| 2. API endpoints | <n> | 0 |
| 3. Scheduled jobs | <n> | 0 |
| 4. Reports and views | <n> | 0 |
| 5. Integrations | <n> | 0 |
| 6. Roles and permissions | <n> | 0 |
| 7. Tests and gates | <n> | 0 |
| 8. Operational docs | <n> | 0 |

Zero rows checked at day one. Parity is declared when every row is ☑ done or
recorded DROPPED with an approval. Nothing in between counts.
```

The old system's forgotten corners are the whole reason this file exists. Inventory them before you rebuild, or meet them again in production.
