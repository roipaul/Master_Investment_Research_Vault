---
type: company
ticker:
name:
exchange:
sector:
stage: gate            # gate | primer | triage | frame | debate | evidence | views | writeup | decision | monitoring | deferred | dropped
track: undecided       # undecided | view | price-alone
verdict:               # latest triage or thesis verdict
zone:                  # price-alone | needs-a-view | pass-on-price
conviction:            # open variant views and levels, e.g. "V1:2, V2:1"
price_check:           # price and date of the last check
conservative_return:   # at the price above
base_return:           # at the price above
harsh_case:            # return or loss in the harsh case
held: no               # yes once a buy is recorded in Decisions.md
list: none             # none | watch | buy (set only by /decision-record)
buy_price:             # Paul's buy price, local currency, e.g. "US$70.00" (list: buy only)
buy_action:            # initiate | add
buy_basis:             # Paul's words on what the buy price earns
buy_set:               # date the buy price was set or last changed
buy_review_by:         # date the buy price must be re-confirmed
entry_level:           # Claude's reference price where the case clears the hurdle, with case and date
alert:                 # armed | near | triggered <date> | paused (written by the price watch)
catalysts: []
awaiting:              # what is waiting on Paul, if anything
updated:
data_through:          # latest reported period the notes reflect
next_checkpoint:
next_results:
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
  update:
---

# <Company> (<TICKER>)

**Latest:** <date> — <one line on where this stands>

## Thesis in one paragraph

## Critical questions

| # | Question | Verdict | Probability | As of |
|---|---|---|---|---|

## Variant views

| V# | Claim | Type | Conviction | Last changed | Resolves by | Evidence deadline |
|---|---|---|---|---|---|---|

## Documents

## Links

Themes, policies, peers, entities and people this company connects to.

## Log

- <date> — <what was done, by which skill>
