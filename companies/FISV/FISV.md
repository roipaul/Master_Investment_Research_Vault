---
type: company
ticker: FISV
name: Fiserv, Inc.
exchange: NASDAQ
sector: US payments and bank technology (merchant acquiring incl. Clover, card issuing, core banking, digital payments)
stage: monitoring      # gate | primer | triage | frame | debate | evidence | views | writeup | decision | monitoring | deferred | dropped
track: undecided       # undecided | view | price-alone
verdict: "Thesis Intact (provisional baseline), confirmed 2026-11-18"
zone:                  # price-alone | needs-a-view | pass-on-price
conviction:            # open variant views and levels, e.g. "V1:2, V2:1"
price_check: "US$62.79, close 2026-11-17 (Yahoo Finance)"
conservative_return:   # at the price above
base_return:           # at the price above
harsh_case:            # return or loss in the harsh case
held: yes              # own money, under 3%; see Decisions.md
awaiting:
fresh_money: "Wait at US$62.79, 2026-11-17 (confirmed 2026-11-18); evidence: Q4 2026 results and 2027 guide, Feb 2027; price alternative about US$52"
cycle: "Not cyclical in a way that matters; company-specific under-earning (2026-11-18)"
market_focus: "Whether the annual guide holds; revenue growth over EPS. Mostly an earnings argument, with a trust discount (2026-11-28)"
sentiment: "Sceptical (2026-11-28); the event log reads as Washed out from Aug to 3 Nov 2026"
market_read: 2026-11-28
updated: 2026-11-28
data_through: FY2026-Q3
next_checkpoint: Q4 2026 results and 2027 guide, around Feb 2027
next_results: around 2027-02-10 (not yet announced)
steps:                 # date each step last ran
  gate:
  primer:
  abridged:
  triage:
  model: 2026-11-18
  frame:
  debate:
  dd:
  scuttlebutt:
  views:
  writeup:
  decision: 2026-11-18
  update: 2026-11-18
---

# Fiserv (FISV)

**Latest:** 2026-11-18 — Q3 2026 earnings update confirmed. Value DCF model v2 (US$62.79 price): base US$164; conservative US$96 at an 8.5% WACC; conservative with a 15% cost of equity US$61.
- Thesis call: Intact, on a provisional baseline.
- Fresh-money call: Wait, at US$62.79, pending Q4 2026 results and the 2027 guide (Feb 2027).
- Merchant and Clover revenue are weak while peers grow. Banking attrition is down. Elevate savings target is US$1bn. Buybacks resume at 3.1x leverage.

## Thesis in one paragraph

No thesis written yet. Provisional baseline (Claude's framing, 2026-11-18): the 2026 trough holds, and organic growth returns to mid-single digits. Margins recover from about 31% toward the 37% target through Project Elevate. Cash flow funds buybacks at a low multiple, with leverage near 3x. See [[earnings/FY2026-Q3]].

## Critical questions

No debate on file; there are no probabilities. Open questions from the Q3 2026 update:

| # | Question | Verdict | Probability | As of |
|---|---|---|---|---|
| 1 | Is Clover's revenue-volume gap a one-off reset or share and pricing loss? | Open | - | 2026-11-18 |
| 2 | Has banking attrition troughed, and when does it show in revenue? | Open | - | 2026-11-18 |
| 3 | How much of Elevate's US$1bn reaches profit by 2029? | Open | - | 2026-11-18 |
| 4 | Will capital allocation stay disciplined at about 3x leverage? | Open | - | 2026-11-18 |

## Variant views

| V# | Claim | Type | Conviction | Last changed | Resolves by | Evidence deadline |
|---|---|---|---|---|---|---|

## Documents

- [[earnings/FY2026-Q3]] — Q3 2026 earnings update, 2026-11-18 (confirmed)
- [[Decisions]] — decision record; Hold, 2026-11-18
- [[MarketRead]] — market read, first build 2026-11-28 (29 event rows, April 2025 to November 2026)
- `files/FISV_Financial_Model_2026-11-18_v1.xlsx` — value DCF model v1 (modified DCF on core EBITA, restructuring as operating cost; data through Q3 2026)
- `files/FISV_Financial_Model_2026-11-18_v2.xlsx` — v2: adds a base/conservative scenario switch (saved on Conservative)

## Links

Peers: FIS, Jack Henry (JKHY), Global Payments (GPN), Toast (TOST). No vault notes yet. Related chat coverage: FIS and Jack Henry as banking comps.

## Log

- 2026-11-18 — Hub created; FY2026-Q3 earnings update (earnings-update). Proposed: thesis Intact (provisional baseline), fresh money Wait at US$62.79. No primer, debate, thesis or model on file.
- 2026-11-18 — Sign-off: Paul confirmed thesis Intact (provisional) and fresh money Wait at US$62.79. Decision review requested.
- 2026-11-18 — Decision recorded: Hold, own money, under 3%; review 2027-02-15 (decision record written by hand; the /decision-record skill is not installed).
- 2026-11-18 — Value DCF model v1 (value-dcf-model): modified DCF on core EBITA, 5y history / 2026-30 explicit / 2031-35 fade. US$164 a share at a 7.5% WACC (cross-check US$156); US$85 with a 15% cost of equity; price US$62.79. Base case is Claude's (revenue CAGR 2.7% 2025-30, core margin 35.5% by 2030, restructuring costs in core EBITA through 2027).
- 2026-11-18 — Value DCF model v2 (value-dcf-model): conservative scenario on Paul's direction (turnaround, margin reset, competitive acquiring market, leverage). Merchant growth 3-3.5% from 2027, adjusted margin 32.5% by 2029, 2035 core margin 32%, incremental ROIC 15%, beta relevered to 1.26 (cost of equity 11.4%, WACC 8.5%). Conservative US$96 a share (cross-check US$92); US$61 with a 15% cost of equity. Steps from base US$164: Merchant growth −9, margin reset −16, ROIC −15, beta −28.
- 2026-11-28 — Market read, first build (market-read, unattended). Focus: whether the annual guide holds, and revenue growth over EPS. The argument is mostly about earnings, with a trust discount. Sentiment: Sceptical at US$61.49 (2026-11-27 early close, StockAnalysis); the log reads as Washed out from August to the Q3 print. Not resolved: the 2 Nov close in the Q3 earnings file (US$50.02) against about US$52 implied by three press sources; see MarketRead, open puzzle 4. No flag raised.
