---
name: "earnings-update"
description: "After a company reports results: deep read of the financials, presentation and call against all saved work, giving what matters, structural puts and takes, cycle position and a fresh-money Own / Wait / Don't own call, written to the vault. Use for /earnings-update."
---

# Earnings update

Results day is when the thesis meets the facts. This skill reads everything the company published for the period (the release, the full financial statements, the presentation and the call), sets it against all the earlier work in the vault, and answers four questions:

1. What truly matters in this print, and what does it do to the thesis?
2. Which changes are structural, and what are the puts and takes of each?
3. Which changes are cyclical, how is the cycle progressing, and where are we in it?
4. Putting all the earlier work together with today's price: with no position and fresh money, should we own the stock?

It replaces `/thesis-update` on results days and does that skill's bookkeeping (tracking table, falsifiers, re-scored questions, guidance log). `/thesis-update` remains for events other than results.

The user is an experienced equity analyst running his own and his family's money. His hurdle is in `settings.md` (a 15% IRR over a 3-5 year hold unless it says otherwise). This is the one skill that makes an ownership call, and only on the fresh-money question: **Own / Wait / Don't own**. No price target, no fair value, no position size, and nothing on what to do with an existing holding. The call is Claude's read until he confirms it.

## Commands

- `/earnings-update TICKER` - the latest reported period.
- `/earnings-update TICKER FY2026-Q3` - a named period (use the company's own fiscal labels; `H1` for half-year reporters, `FY` for the annual).
- `/earnings-update TICKER confirm` - record his sign-off on the calls (see Sign-off).

One company per run. For several names, run them one at a time.

## Knowledge base (start)

Run the `research-kb` read step: pull the vault, read `settings.md` and the hub `companies/<TICKER>/<TICKER>.md`. Then read all the earlier work on the name, whichever exists:

- `Thesis.md`, including every `## Update` section.
- Earlier files in `companies/<TICKER>/earnings/`: the last two periods and the year-ago period at least.
- `VariantView.md`, `Debate.md`, `DD.md`, `Scuttlebutt.md`, `Triage.md`, `PriceAlone.md`, `Decisions.md`.
- `Primer.md` or `Abridged.md`, for the industry structure and how the business behaved in past cycles.
- The model in `files/`, if there is one, for the driver paths.
- The theme and policy notes the hub links to, and the hubs and latest earnings files of peers already in the vault.

If the vault cannot be reached, use the Project copies or files in the conversation and say so.

**No `Thesis.md`.** Use what exists, in this order: the debate, the variant view, the primer, his old pitch-book line, or his view as he states it. Write the baseline being used in one paragraph (what the return depends on, three to five things to track, what would break it), label it **provisional baseline**, and list what is missing. Invent no probabilities. If nothing at all is on file, ask him for his view in two or three sentences and use that. In an unattended run, write the provisional baseline yourself, label it "Claude's framing, not Paul's view", and add "baseline needs Paul's view or imported work" to the hub's `awaiting`.

## Sources

Collect all of these for the period before analysing. Files he supplies come first; after that, primary sources.

| Document | Where | Used for |
|---|---|---|
| Results release and full financial statements | Company IR site; the exchange or regulator (SEC, HKEX, TWSE MOPS, TDnet/EDINET, DART and so on) | Every line of the income statement, balance sheet and cash flow, segments, share count |
| Quarterly or annual report, with notes | Same | Segment detail, one-offs, accounting changes, related parties |
| Presentation and any data sheet | IR site | KPIs, the slides management chose, what was added or dropped |
| Call transcript: prepared remarks and Q&A | IR site, his upload, a connected data tool, or Capital IQ via `research-portals` | Management's claims, what analysts pressed on, changes in language |
| The same documents for the prior period and the year-ago period | Vault first, then the sources above | Comparison of numbers, guidance and language |
| Latest results of 2-4 peers, customers or suppliers | Their IR sites; their vault files | The cycle read |
| Sell-side reaction: Bernstein and CLSA notes after the print | `research-portals` | How brokers' estimates of undisclosed KPIs moved, their channel checks, and accounting changes they flag. These are estimates, labelled as such |
| Consensus before the print | An export under `data/`, figures he supplies, or Capital IQ via `research-portals` | Context only |

- If Daloopa or another data tool is connected, use it for the numbers and the KPI history, and cite it. A `daloopa:earnings-review` already on file is an input, not a substitute for this read.
- **Documents that cannot be reached.** If the results release, the financial statements, the presentation or a full transcript of the call cannot be fetched, pause: do not write the update. Name each missing document and ask him to upload it, either in a chat with `/earnings-update TICKER` or into `inbox/uploads/<TICKER>/` in the vault; look in that folder before asking. In an unattended run, put "upload <documents> for <PERIOD>" in the hub's `awaiting` field and in the ticker's row in `monitoring.md`, report it, and stop work on that name. A complete third-party transcript counts and is named as such under Gaps; a summary of the call does not. A company that holds no call is not a gap: say so and use its briefing materials.
- **Timing.** Run after the call, once the release, statements, presentation and transcript are all in hand. Do not run on the release alone unless he asks for an early read, in which case mark the file **Preliminary**. If only the full quarterly or annual report is still to be filed, write the update, list the report under Gaps, and append a dated `## Addendum` when it arrives; never rewrite the file.
- **Other languages.** Translate non-English sources into English and cite the original document. He does not read Japanese.
- If no consensus is available, leave that column out. What the thesis expected is the benchmark that counts.

## Workflow

### 1. Facts first

Work from the full statements, not the highlights page.

- **Results table.** For every tracked metric and each main line and segment: actual | year on year | quarter on quarter | what the thesis expected | what management guided last time | consensus if available.
- **Cash and balance sheet.** Operating cash flow and free cash flow against net income; working capital, capex, net cash or debt, buybacks and dividends, share count.
- **Earnings quality.** One-offs, gains and charges; capitalised costs; stock compensation; tax rate; reserve releases; any change of accounting policy or segment definition.
- **Guidance.** New against old, and what the change implies for the remaining periods of the year. Keep the cumulative guidance log: what was guided, what was delivered, the beat-or-miss pattern.
- **Disclosure changes.** A metric dropped, added or redefined is a finding in itself.

### 2. The call and the deck

- What management chose to stress, and what it left out compared with last time.
- Slides added, dropped or reworded against the previous deck.
- What analysts pressed on in the Q&A, which questions were answered with numbers, and which were not answered.
- Where the wording changed from the previous call on the points the thesis depends on (demand, pricing, competition, capital return).
- Where the brokers' post-results notes read the print differently from management. Also note which estimates of undisclosed KPIs they changed. Get the notes through `research-portals`, in the main thread, because the portals need his browser.

Management's explanation is a claim until a number supports it. Keep fact, claim and inference apart throughout.

### 3. Sort every notable change

| Type | Test |
|---|---|
| Structural | Would still be there after a full cycle: market share, pricing power, cost base, mix, industry structure, regulation, capital allocation, management |
| Cyclical | Moves with the demand, inventory, price or credit cycle and should reverse |
| One-off | Will not repeat: a gain, a charge, timing, currency translation, calendar effects |
| Noise | Inside normal quarterly variation |

When the type is unclear, say so, carry the item under both headings as "unresolved: structural or cyclical", and name the reading that would settle it. Management calling a share loss or a price cut temporary is a claim, not a classification.

### 4. Structural changes: puts and takes

One block per structural change:

- **What changed**, with the number and its source.
- **Puts**: what it adds to earnings power or value.
- **Takes**: what it costs or puts at risk.
- **Net effect**: a sized effect on base-case earnings or value, with the arithmetic shown and estimates marked (e), and the period over which it plays out.
- **Which debate question or variant view it updates.**
- **Confidence**, and what would confirm or reverse it.

Also list any structural change the thesis expected by now that did not show up.

### 5. The cycle

1. **Cycle indicators.** A fixed set of five to eight per company. On the first run, choose them from the primer's industry section and the theme note; on later runs, carry the set from the last earnings file so that quarters can be compared, and note any change to the set with the reason. Typical indicators: orders, backlog or book-to-bill; volumes; pricing; inventory at the company and in the channel or at customers; utilisation; lead times; customers' capex or end demand; credit costs for lenders; margin against its mid-cycle level. Table: indicator | now | last period | a year ago | direction.
2. **Peers.** Read the latest results of two to four peers: the closest competitor, a key customer or supplier, and one bellwether for the end market. Keep the same set each quarter and state which period of each was used. Say where they agree with the company and where they do not.
3. **Phase.** One of: Downturn / Trough / Early recovery / Mid-cycle / Late cycle / Peak / Rolling over. Give last period's phase and this period's, the pace against what the last update expected, and the evidence for and against. If segments or end markets sit at different points, give each its own line.
4. **Earnings against mid-cycle.** Is the company over-earning or under-earning, and by roughly how much?
5. **What the price assumes** about the cycle.
6. **Next period.** The readings that would confirm the cycle is progressing as read, and the readings that would mean the phase is wrong.

If the business is not cyclical in a way that matters to the thesis, say so in two lines, cover the one or two outside factors that do touch it (consumer spending, credit, rates, currency), and do not force a phase.

### 6. Thesis scorecard

- **Tracking table.** For each signal in "What to track": expected | actual | verdict (ahead / in line / behind / not disclosed) | the question it updates. Add any signal this print made relevant.
- **Falsifiers.** Line by line: triggered / not triggered / partially, with the number.
- **Re-score.** For each debate question the print touches: old probability, new probability, and the evidence. Move a probability only on evidence from this print or from the peers read. Keep the debate's calibration (50-55 toss-up, 55-65 lean, 65-80 clear, above 80 strong). List the untouched questions as unchanged.
- **Driver assumptions.** If a reported trend breaks a base-case assumption, restate it.
- **What the thesis rests on.** Where a variant-view frame exists, restate its label (near-term, duration or discount) and say whether this print bore on it. A duration thesis is tested by share, retention and pricing readings, and a discount thesis by the risk it names (cycle position, payout, governance events). A beat or a miss on the quarter tests neither.

### 7. What truly matters

Rank every finding by its effect on value: does it change terminal-year earnings in a scenario, the probability of a critical question, or a falsifier? Keep the three to five that do. For each: finding | structural, cyclical or one-off | effect on the thesis | size.

Then list, one line each, the things that drew attention but do not matter, with the reason. A beat or a miss against consensus is not a finding by itself.

**Thesis call**: Intact / Strengthened / Weakened / Falsified (a falsifier triggered), with the two or three readings that decided it.

### 8. Valuation refresh

- Price, diluted share count and net cash, each dated and sourced.
- Recompute the thesis scenario table for every assumption that changed, showing the arithmetic. Leave unchanged cells alone and say they are unchanged.
- Returns at today's price for the conservative, base and harsh cases, as `/variant-view` defines them, and which scenario the price now implies.
- The share-price move since the print, and what the market seems to have taken from it.
- **Consensus against his numbers.** Where a variant-view frame exists and consensus is available, for each key variable give consensus before and after the print beside the user's number and the number the price implied. Say whether consensus moved toward him, and how the price reacted to that move. Cuts toward his number with a flat or rising price support the reading that the cuts were already in the price. A falling price says they were not, and that the gap was smaller than the frame showed. Name this reading as an evidence item for `/variant-view` to log.
- **Model.** Do not rebuild the Excel model. Flag **Model rebase due**, with the reason, when reported operating profit runs more than about 10% away from the model's path for the year, when segments are redefined, when the share count moves by more than about 3%, after a deal, or when the model is more than two results periods old.

### 9. Fresh-money view

Assume no position and no history with the stock. Write the case as someone meeting it today would: what you get at this price, what has to be true, and what the evidence from all the work on file says about each of those things. Only then compare it with the earlier verdict; where they differ, say which is right and why. Research already done is not a reason to own.

| Call | Conditions |
|---|---|
| **Own** | Thesis Intact or Strengthened; no falsifier triggered; the base-case return at today's price meets the hurdle; the harsh-case loss is stated and bearable; the value-trap check has not failed; and, where the name needs a variant view, at least one view is still not in the price and is supported by evidence |
| **Wait** | The business case stands but one thing is missing. Price: give the price at which the base case meets the hurdle, as an entry level worked from the scenario table and not as a target. Evidence: name the reading and the date that would settle the open High-materiality question. Cycle: earnings sit above mid-cycle and the price capitalises them; say what would have to reset |
| **Don't own** | Thesis Falsified; or Weakened to the point where the base case misses the hurdle at any price near today's; or a quality or governance failure |

Between two calls, take the more cautious one and say what would move it. State the call in one sentence and the reasoning in a short paragraph that draws on the business verdict, the structural changes, the cycle position and the price. If he holds the name and the call is Wait or Don't own, say only that a decision review is due under `/decision-record`; the decision is his.

### 10. Check before writing

Every number carries its period and source; computed numbers say what they are computed from; the bottom line agrees with the sections under it; the scenario figures in the bottom line match the valuation section; dates and the price are right; no price target or position size anywhere.

## Output and knowledge base (end)

**1. The period file.** Write `companies/<TICKER>/earnings/<PERIOD>.md` (for example `earnings/FY2026-Q3.md`) with document frontmatter: `type: document`, `doc: earnings-update`, `tickers`, `period`, `updated`, `data_through`, `next_checkpoint`, `price_check`, `status: proposed`, `sources: [skill:earnings-update]`. Use the same shape every period so files can be read side by side:

```
# <Company> - <period> earnings update (reported <date>)
Gaps: documents missing, or "Preliminary", if any.

## 1. Bottom line
Thesis: Intact / Strengthened / Weakened / Falsified - one sentence. (Claude's read)
Fresh money at <price> on <date>: Own / Wait / Don't own - one sentence with its condition. (Claude's read)
What truly matters: 3-5 ranked lines (finding | type | effect on thesis | size).
What does not matter: one line each.

## 2. What was reported
Results table; cash, balance sheet and earnings quality; guidance and the guidance log;
disclosure changes; the call and the deck.

## 3. Structural changes: puts and takes

## 4. The cycle
Indicator table; peers; phase last period and now; earnings against mid-cycle;
what the price assumes; what to see next period.

## 5. Thesis scorecard
Tracking table; falsifiers; questions re-scored; assumption changes.

## 6. Valuation and the fresh-money view
Price, shares and net cash; scenario table; returns at today's price; what the price implies;
the call and its reasoning; model rebase flag.

## 7. Next checkpoint and follow-ups
Date, what to look for, IR questions, desk checks.

## Sources
```

The bottom line must fit on one screen. The whole file runs three to six pages; put depth in sections 3, 4 and 6 and keep section 2 to tables.

**2. `Thesis.md`.** Append a short dated section and never rewrite earlier ones:

```
## Update - <date>: <period> results
Thesis call (proposed): ...
Fresh money at <price> (proposed): ...
What mattered: three lines.
Assumption changes with the recomputed scenario figures, if any.
Cycle: phase, direction.
Next checkpoint.
Full write-up: [[earnings/<PERIOD>]]
```

Update the thesis header (data-through period, next results date, price) and, if an assumption changed, the affected cell in Section 5 with a footnote pointing to this update. Where there is no `Thesis.md`, skip this step and say so.

**3. Hub.** Set `updated`, `data_through`, `next_checkpoint`, `next_results`, `price_check`, the **Latest** line, the Documents list, the date under `steps:`, the critical-questions table probabilities, `cycle` (phase and date; add the field if it is missing) and a dated `## Log` line. Do **not** change `verdict`, `zone` or `conviction`, and do not write `fresh_money`: put "confirm earnings-update <PERIOD>: thesis <call>, fresh money <call>" in `awaiting`.

**4. Read-across.** Append the cycle reading and any structural finding to the theme and policy notes they bear on (`## Evidence log`, dated, `[[TICKER]]`), and to the notes of peers that were read.

**5. Watch list.** If `monitoring.md` lists the ticker, update its row (last period done, next results, status) and the "Waiting on Paul" section before committing.

**6. Commit and push** per `research-kb`, with the message `<TICKER>: earnings-update <PERIOD> - thesis <call>, fresh money <call> (proposed)`. If the vault could not be reached, send the files that would have been written and say plainly that nothing was saved to the vault.

The ledger in `VariantView.md` belongs to `/variant-view`; after this run, name `/variant-view TICKER` (or `/price-alone review`) as the next step and do not edit that file here.

## Sign-off

When he replies, or runs `/earnings-update TICKER confirm`:

- Append `## Sign-off - <date>` to the period file with his decision on each call, in his words if he overrides, and set `status: confirmed`.
- Update the hub: `verdict` if the thesis call changes it, `fresh_money` (call, price, date; add the field if it is missing), clear `awaiting`, and add a `## Log` line.
- `watchlist.md`: add a line if a call changed, with the entry level or the evidence a Wait depends on. `track-record.md`: add a line if Falsified.
- Commit and push.

Never record a sign-off he has not given.

## Reply

A few lines: the thesis call; the fresh-money call with its condition; the three things that mattered; the cycle phase and direction; what is waiting on him (sign-off, a missing document, a model rebase). The detail is in the vault.

## Standards

- Plain English; tables for numbers, prose for argument.
- Reported numbers carry the source and the period; estimates are marked (e).
- Fact, management claim and inference are kept apart.
- The same structure, the same cycle indicators and the same peers every period, so periods can be read side by side.
- Notes hold judgments, not data: no long time series in the file. The indicator table holds three points only (now, last period, a year ago).
- Avoid "genuinely", "honestly" and "straightforward"; no hedging boilerplate. Uncertainty lives in the scenarios, the probabilities and the open questions.