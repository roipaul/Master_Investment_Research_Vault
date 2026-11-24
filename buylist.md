---
type: list
doc: buylist
updated: 2026-11-24
near_band: "5%"            # a name within this distance of its buy price is marked near
remind_days: 7             # how often a triggered name with no decision is re-sent
---

# Buy list

Names Paul has moved from the watchlist to the buy list, each with **his** buy price. A scheduled task ("Buy list price watch") checks every armed row on weekdays after the Asia close and after the US close, and notifies Paul when a price reaches its buy price. A hit is a prompt to decide, not a decision: Paul records what he does with `/decision-record`.

**Who writes what.** Rows are added, changed and removed only by `/decision-record` (`buy-list`, `buy-price`, `unlist`, or an initiate). The price watch writes only the **Last price**, **Gap** and **Alert** columns and the alerts log.

**Alert values:** `armed` · `near` (within `near_band`) · `triggered <date>` (closed at or below the buy price) · `touched <date>` (traded through it intraday, closed above) · `no verified price` · `paused`.

## Buy list

| Ticker | Company | Action | Buy price | Basis (Paul's words) | Set | Review by | Last price (date, sources) | Gap | Alert |
|---|---|---|---|---|---|---|---|---|---|

## Alerts log

Dated lines, newest at the bottom. Never rewritten.

- 2026-11-24 — Buy list created; no names yet.
