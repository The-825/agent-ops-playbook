# PARITY.md template: the zero-regression parity contract

One of the four founding docs of a disciplined rebuild. This is the contract that makes
"feature parity, zero regressions" checkable instead of aspirational: every capability of the
old surface is a tracked row, and nothing ships until its row is checked. The enumeration
happens BEFORE the rebuild claims parity, not after; the eight buckets below exist so no
capability class gets forgotten.

How to use this template: copy it, then walk the old system surface by surface and add one row
per capability under the matching bucket. Expect this file to get long; the length is the
point. Keep the rollup table at the bottom current so the parity position is readable at a
glance.

## Row shape

Every row uses the same five columns:

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|

- **Item**: the capability, named concretely (an endpoint path, a panel, a job).
- **Purpose**: one line on what it does for users, so a row can be judged without archaeology.
- **<old-system> source**: where the capability lives in the old repo (file, route, job name).
- **Rebuild phase**: the phase of your build-order doc (BLUEPRINT) that delivers it. Every row
  back-links to a phase; a row with no phase is unscheduled work hiding in plain sight.
- **Status**: see the legend.

## Status legend and the definition of done

| Mark | Meaning |
|---|---|
| ☐ | Not started |
| ◐ | In progress (partially rebuilt, or rebuilt but not yet through the done gate) |
| ☑ | Done |

A row goes ☑ only when ALL of the following hold:

1. The capability is rebuilt and working.
2. Its regression spec passes (the e2e or integration test that covers it).
3. It appears in the API spec (if it is an endpoint).
4. It ships flag-gated, default OFF in production.
5. Your project's continuity checks pass (the rebuilt surface agrees with the canonical data
   and with every other surface that shows the same quantity).

"It works on my machine" does not flip a checkbox. The done definition is the whole contract.

## The eight buckets

Enumerate before claiming parity. Fill every bucket, even if only to record "none."

### 1. API endpoints

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 2. UI panels / views

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 3. Sync / pipeline stages

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 4. Ingestion sources

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 5. Scheduled jobs

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 6. Admin surfaces

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 7. Procedures and views (database layer)

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

### 8. Feature-flag families

| Item | Purpose | <old-system> source | Rebuild phase | Status |
|---|---|---|---|---|
| | | | | |

## Rollup

Keep this table current; it is the one-glance parity position.

| Bucket | Total rows | ☑ Done | ◐ In progress | ☐ Not started |
|---|---|---|---|---|
| API endpoints | | | | |
| UI panels / views | | | | |
| Sync / pipeline stages | | | | |
| Ingestion sources | | | | |
| Scheduled jobs | | | | |
| Admin surfaces | | | | |
| Procedures and views | | | | |
| Feature-flag families | | | | |
| **Total** | | | | |
