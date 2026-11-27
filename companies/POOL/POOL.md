---
type: company
ticker: POOL
name: Pool Corporation
exchange: NASDAQ
sector: US pool supplies distribution
stage: monitoring            # gate | primer | triage | frame | debate | evidence | views | writeup | decision | monitoring | deferred | dropped
track: undecided       # undecided | view | price-alone
verdict: "Thesis Intact (provisional baseline; margin and cost legs behind) - earnings-update FY2026-Q3, confirmed 2026-11-27"
zone:                  # price-alone | needs-a-view | pass-on-price
conviction:            # open variant views and levels, e.g. "V1:2, V2:1"
price_check: "US$213.85, close 2026-11-24 (Investing.com; Yahoo Finance and stockscan.io agree)"
conservative_return:   # at the price above
base_return:           # at the price above
harsh_case:            # return or loss in the harsh case
held:                  # not recorded; yes once a buy is recorded in Decisions.md
entry_level: "about US$173 — base case (18 times 2029 EPS of about US$13.7) meets the 15% hurdle; about US$191 at 20 times; 2026-11-25 (Claude's read, proposed)"
fresh_money: "Wait at US$213.85, 2026-11-24 (confirmed 2026-11-27); Price: the base case returns about 7% a year and meets the 15% hurdle at about US$173 (about US$191 at 20 times). Evidence: the 2027 framework on 2027-02-18, and whether it shows the operating leverage the rise since the print pays for"
awaiting: "baseline needs Paul's view or imported work; import primer and earlier outputs into the vault"
updated: 2026-11-27
data_through: FY2026-Q3
next_checkpoint: "Q4/FY2026 results, 2027-02-18: the 2027 framework — gross margin after season-start price increases, expense growth against gross profit, inventory and vendor programmes, Team Horner's price and the plan for its manufacturing, interest after the swaps expire"
next_results: "Q4/FY2026: 2027-02-18 (stated by the CEO on the Q3 call, 2026-10-22; no scheduling release yet)"
cycle: "Trough, extended: new construction at the bottom with housing data worsening; maintenance steady and price-led; remodel stable; channel inventory destocked — 2026-11-25 (Claude's read, proposed)"
cycle_phase: "us-housing-channel: Downturn to Trough — cycle note [[us-housing-channel]], 2026-11-26 (Claude's read, proposed); the Q3 earnings update's own read above is Trough, extended"
mid_cycle_note: 2026-11-26   # not sized: under-earning on volume in the discretionary part; ten-year margins and the sales split are not on file
dial_markets: "earnings: us; listing: us"
catalysts:
  - date: "Q1 2027"
    event: "Team Horner acquisition expected to close (18 HornerXpress centres, AquaCal AutoPilot, French fiberglass plants); subject to regulatory approval"
    type: corporate
    tests: "baseline leg 5 (competitive position, supplier relations)"
    status: expected
    source: "Pool Corp release and 8-K, 2026-11-16"
  - date: "February 2027"
    event: "Interest-rate swaps on US$300m of debt expire; that debt reprices from under 1% to about 5.2%"
    type: corporate
    tests: "baseline leg 4 (capital return and EPS quality)"
    status: confirmed
    source: "CFO on the Q3 2026 call, 2026-10-22"
  - date: "H1 2027"
    event: "Investor Day (postponed from 2026-05-12)"
    type: corporate
    tests: "baseline legs 2 and 3 (margin and operating leverage)"
    status: expected
    source: "CEO on the Q3 2026 call, 2026-10-22"
  - date: "January 2027"
    event: "Leslie's Chapter 11 plan confirmation (outside date about 2027-01-08) and emergence"
    type: industry data
    tests: "baseline leg 5"
    status: expected
    source: "Leslie's 8-K, 2026-09-30; Debtwire, 2026-10-21 (press)"
steps:                 # date each step last ran
  gate:
  primer:
  abridged:
  triage:
  model:
  frame:
  debate:
  dd:
  scuttlebutt:
  views:
  writeup:
  decision:
  update: 2026-11-25
---

# Pool Corporation (POOL)

**Latest:** 2026-11-25 — FY2026 Q3 earnings update written as a backfill (results of 2026-10-22). Proposed, Claude's read against a provisional baseline: thesis Intact with the margin and cost legs behind; fresh money Wait at US$213.85 (2026-11-24), on price: the shares are up 24% since the day before the results, the base case returns about 7% a year and meets the 15% hurdle at about US$173. Awaiting Paul's sign-off and his own baseline. See [[earnings/FY2026-Q3]].

## Thesis in one paragraph

Not written in the vault yet. Until Paul's earlier work is imported, an earnings update uses a provisional baseline and says so.

## Critical questions

| # | Question | Verdict | Probability | As of |
|---|---|---|---|---|

## Variant views

| V# | Claim | Type | Conviction | Last changed | Resolves by | Evidence deadline |
|---|---|---|---|---|---|---|

## Documents

- [[earnings/FY2026-Q3]] — earnings update, Q3 2026 (reported 2026-10-22; written 2026-11-25; status confirmed 2026-11-27)

## Links

Peers read: Pentair (PNR), Hayward (HAYW), Leslie's (LESL), Home Depot (HD). In the watch list: [[FDR-MC]] (Fluidra). Bellwethers read with them: SiteOne, Latham, US existing-home sales and mortgage rates. Themes: [[pool-industry-cycle]]. Cycle note: [[us-housing-channel]] (`cycles/us-housing-channel.md`).

## Log

- 2026-11-19 — Hub created and added to `monitoring.md` (earnings watch set-up). No primer, thesis or model on file.
- 2026-11-25 — earnings-update FY2026-Q3 (backfill; results of 2026-10-22). Proposed: thesis Intact against a provisional baseline (Claude's framing, not Paul's view), margin and cost legs behind; fresh money Wait at US$213.85, on price (base case about 7% a year; hurdle met at about US$173). Cycle: Trough, extended. Sales +3.7% (price 3, volume 1), gross margin 29.0% (-60bp against a July guide of -30bp), expenses +5.1%, operating income -3.3%, EPS flat at US$3.40 on 3.5% fewer shares; adjusted EPS guide US$10.87-11.17 held, sales guide raised to +3-4%, gross-margin guide widened to 30-50bp lower; nine-month operating cash flow 115% of net income; inventory -3%. New CEO since May; Team Horner agreed 2026-11-16, price undisclosed. Next results 2027-02-18. No verdict, zone or conviction changed. Read-across appended to [[pool-industry-cycle]].
- 2026-11-26 — `/cycle-view` (weekly check): cycle note [[us-housing-channel]] built (`cycles/us-housing-channel.md`). Phase Downturn to Trough: the housing data that lead discretionary pool work were still falling in October (existing-home sales 3.75m, the lowest since August 2010; single-family permits 772 thousand, the lowest since January 2023; 30-year mortgage rate 7.21% on 25 November against 6.23% a year ago), while repair and remodel spending and big-box comparable sales are flat to slightly up. This differs in weight from the Q3 update's "Trough, extended", which is left as written. Earnings against mid-cycle not sized. Hub fields added: `cycle_phase`, `mid_cycle_note`, `dial_markets`. No verdict, entry level or view changed.
- 2026-11-27 — Sign-off: Paul confirmed thesis Intact (provisional baseline; margin and cost legs behind) and fresh money Wait for FY2026-Q3. `verdict` and `fresh_money` set; `list` and `held` not changed.
