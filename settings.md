---
type: settings
hurdle: "15% IRR over a 3-5 year hold"
flow_mode: ask-every-step     # ask-every-step | gates-only
max_active: 3                 # names in deep research at once
frame_stale_days: 90
frame_stale_price_move: "15%"
primer_stale_months: 12
max_awaiting: 10              # open items waiting on Paul (ranks 2 to 5) before new work stops
cycle_items_per_run: 2        # cycle notes or market reads one scheduled cycle-view run may build or refresh
market_read_builds_per_run: 3 # first builds one scheduled market-read run may do
liquidity_floor:              # minimum average daily value traded, set by Paul
dials:                        # set only by Paul, via /cycle-view dial MARKET confirm
  us:
  china-hk:
  japan:
  korea:
  taiwan:
skill_freeze: "on since 2026-11-27 — edits to existing skills only; see _system/skill-tests.md"
updated: 2026-11-27
---

# Settings

The skills read this file. Change a value here and it applies from the next run.

- **flow_mode** — `ask-every-step` asks before each skill runs. `gates-only` chains the mechanical steps and stops at the four judgment points: after the gate, after triage, after the frame, and for views and decisions.
- **max_active** — the most names that can sit between triage and decision at one time.
- **frame_stale_days / frame_stale_price_move** — when the zone and priced-in work is re-run.
- **dials** — the confirmed aggressive-to-defensive setting for each market (Defensive, Neutral or Aggressive). Blank means none is confirmed, and the skills apply their usual tests. The hurdle does not change with the dial.
- **skill_freeze** — while on, no new research skill is built. It lifts when each new skill has run on two or three names; the count is kept in `_system/skill-tests.md`.
- **max_awaiting, cycle_items_per_run, market_read_builds_per_run** — hard limits for the waiting list and the scheduled runs. The number here wins over any number written in a skill or a task prompt. The earnings watch keeps its own limit in `monitoring.md` (`max_updates_per_run`).
