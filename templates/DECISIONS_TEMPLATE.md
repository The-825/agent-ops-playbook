# Decisions ledger template

*From the book: Chapter 6, How We Rebuilt the Honors Stack.*

A ruling that lives only in a transcript gets re-litigated. Worse, a session that never saw it ships work that quietly contradicts it. The decisions ledger is the counter: an append-only file where every durable ruling (a price, a name, a threshold, a policy call) lands the same turn it is made. Same turn, not end of session, because a session can end or compact before any summary gets written. Capture on the event beats capture on a schedule.

## The format

```markdown
# DECISIONS.md · decisions ledger

One entry per durable ruling, newest last. Append the entry the SAME turn the
ruling lands, before moving on to the work it unblocks. Superseded entries stay
in the ledger with a "Superseded by D-<n>" line added. Never silently rewrite
an entry.

## D-<n> · <date> · <topic>
Ruling: <the decision, one or two sentences>
Why: <one line of rationale>
Source: <where it landed: session, PR #, email>
```

Two example entries, the shape to copy:

```markdown
## D-4 · 2026-03-02 · Membership pricing
Ruling: Annual membership launches at $79, monthly at $9. No founding-member
discount tier.
Why: Annual under $80 tested better than a discount ladder, and one price is
easier to defend in copy.
Source: Pricing session, 2026-03-02.
Superseded by D-9.

## D-5 · 2026-03-11 · Revenue dashboard naming
Ruling: The executive dashboard is titled "Revenue Overview", not "Sales
Dashboard". "Revenue" everywhere it appears: nav, page title, exports.
Why: Finance and sales argued over "sales"; "revenue" matches the ledger the
numbers come from.
Source: PR #41 review thread.
```

## Adoption notes

The bar for an entry is durability, not importance. If a future session could plausibly redo the debate, it goes in. The Superseded line is what keeps the ledger honest: the old ruling stays visible with its reasoning, so you can always see what changed and why, and nobody wonders whether an entry was quietly edited.

An entry costs thirty seconds. Re-litigating the same decision costs an afternoon, and sometimes it costs the decision.
