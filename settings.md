---
type: settings
hurdle: "15% IRR over a 3-5 year hold"
flow_mode: ask-every-step     # ask-every-step | gates-only
max_active: 3                 # names in deep research at once
frame_stale_days: 90
frame_stale_price_move: "15%"
primer_stale_months: 12
liquidity_floor:              # minimum average daily value traded, set by Paul
updated:
---

# Settings

The skills read this file. Change a value here and it applies from the next run.

- **flow_mode** — `ask-every-step` asks before each skill runs. `gates-only` chains the mechanical steps and stops at the four judgment points: after the gate, after triage, after the frame, and for views and decisions.
- **max_active** — the most names that can sit between triage and decision at one time.
- **frame_stale_days / frame_stale_price_move** — when the zone and priced-in work is re-run.
