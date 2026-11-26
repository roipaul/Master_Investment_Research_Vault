---
name: "market-read"
description: "Read what the market is focused on for a stock: log news and events against the stock's move versus peers and its index, infer the market's logic and sentiment, and flag where it meets the user's views. Use for /market-read."
---

# Market read

The primer and the debate describe the business. This skill describes the other side of the trade: **what the market is paying attention to, what it has stopped reacting to, and what story the price seems to rest on.** It does this by logging news and events against the stock's move, measured against peers and its index, and inferring the market's logic from the pattern. It holds none of the user's views. `/variant-view` is where his views meet this read.

The user is an experienced equity analyst running his own and his family's money, with a 15% IRR hurdle over a 3–5 year hold. He uses the read for four things, and each has a hand-off below: to frame his view against what is priced, to time entries, to notice when a view has been priced in, and as evidence on his thesis. No price target, fair value, buy/sell or position-size language.

Two cautions run through the whole skill. Most price moves have no single cause, so "no clear read" is a normal and useful answer. And a market reaction shows what other investors believe, not what is true about the business.

## Modes

- **Build** — `/market-read TICKER`. First run for a name: 12–24 months of history, 15–30 event rows, and the first read.
- **Update** — `/market-read TICKER update`. Adds rows since the last run and restates the read only if it changed. Run after each `/earnings-update` and after any large move.
- **Digest** — `/market-read digest`. Update mode across every deep-work name (held, buy list, watchlist, in research; taken from the hubs). Reports only what changed. Safe to run on a schedule, because nothing in it decides for him.

## Knowledge base (start)

Run the `research-kb` read step. Read the hub, `MarketRead.md` if it exists, and `VariantView.md`, `Thesis.md` and the latest earnings file for the questions, views and peer set already on file. If the vault is unreachable, say so and send the file at the end.

## Data

Public web sources, so that the skill can run unattended.

- **Prices.** Daily closes for the stock, two to four peers and the local or sector index, from exchange sites and public quote pages through the search and fetch tools. Use the peer set the earnings file already keeps; otherwise pick it from the primer's industry section, record it in the header and keep it fixed. If a price export for the name sits under `data/`, prefer it.
- **News and events.** Company announcements on the exchange filing system first, then news coverage, rating and target changes as reported publicly, index and placement notices, policy announcements. When the user is present and a browser is connected, `research-portals` can add broker reasons and Xueqiu discussion; skip it in unattended runs.
- **Consensus.** Public consensus figures where available, with the source named. Mark "not available" otherwise.

Every move carries its dates and source. If a move cannot be found, or two sources disagree by more than half a point, mark the row "price unverified" and infer nothing from it. Never state a move from memory. Price histories stay out of the vault; the log holds one row per event.

## Step 1 — Choose the events

An event enters the log when any of these is true:

1. It is a results day or a guidance change.
2. The stock moved 5% or more against its index in a day, or 10% or more over five trading days. Halve both thresholds for companies above roughly US$20bn of market value.
3. It is news of real size for the business that produced **no** move: a large buyback, a deal, a regulatory ruling, a strong or weak print. Non-reactions are data.
4. A peer's results or a sector or policy event that moved the peer group.

## Step 2 — Log each event

One table, appended to on every run:

`E# | Date | Event | Type | Stock move (1 day / 5 day) | Against peers | Against index | What commentary fixed on | Read | Confidence | Source`

**Type** is one of: results, guidance, company news, peer or industry read-across, policy or regulatory, macro or market-wide, flow (index change, placement, lockup, block sale), broker (rating or estimate change), no news.

Rules for the **Read** column:

- **Separate market, sector and stock first.** Subtract the index and the peer median. A move shared with peers says something about the sector, not the company.
- **Read the sign against the news.** Good news with a fall, bad news with a rise, or a beat with no move shows what was already expected. Where consensus is available, give the surprise against it.
- **Name the metric.** Record what the headlines and the analysts' questions fixed on: revenue, margin, guidance, capital return, a regulatory point.
- **Grade the cause.** High: a dated company event, a stock-specific move and commentary that agrees. Medium: a plausible event, but the move is shared or several things happened at once. Low: no identifiable cause; write "no clear read" and do not invent one.
- **Flow events are not opinions.** An index deletion or a placement moves the price without changing anyone's view of the business. Log them, and leave them out of the inferred logic.

## Step 3 — Infer the market's logic

A pattern needs at least three consistent rows. State each item with the E# rows that support it, and label all of it inference.

1. **Focus.** The one or two variables the price responds to now.
2. **What it ignores.** News of real size that produced no move.
3. **Earnings or discount.** Is the market arguing about the earnings path or about what the earnings are worth?
   - *Earnings*: the stock moves on estimate-relevant news, and estimate revisions track the price.
   - *Discount*: the stock moves on governance, policy, capital return, rates or risk events while estimates barely change.
   - Where a public source gives forward estimates now and a year ago, split the 12-month price change into the change in estimates and the change in the multiple. If only trailing earnings are available, use those and say so.
4. **The story.** One paragraph: "The market's working story appears to be …", with a confidence level and the two readings that would show the story has changed.
5. **Open puzzles.** Moves with no cause found, and reactions that contradict the story.

If more than half the rows carry High confidence, re-check them; real attribution is rarely that clean.

## Step 4 — Sentiment position

Where sentiment stands against the stock's own history. Give each reading with its date and source:

- the multiple against its 5–10 year range;
- the price within its 52-week range, and against peers over one and three years;
- the mix and direction of analyst ratings, and short interest where it is published;
- **reaction asymmetry**: a stock that falls more on bad news than it rises on good is fragile or crowded; one that stops falling on bad news is washed out.

State one of: **Washed out / Sceptical / Neutral / Warm / Crowded**, with the evidence and the previous state. This describes sentiment. It is not a call on the stock.

## Step 5 — Against the user's views

Only when `VariantView.md` exists. For each open variant view, one line: the market's apparent stance on that variable, whether commentary has started to cite his reason, and whether the stock now responds to his variable. Never restate, adjust or add to his views here.

## Hand-offs (the four uses)

| Use | What this skill passes on | Where it goes |
|---|---|---|
| Frame his view | Focus, what is ignored, the earnings-or-discount reading and the event log | `/variant-view` Step 2 reads `MarketRead.md` in place of its own reactions log |
| Time entries | The sentiment state. When it reaches Washed out or Crowded on a buy-list or watchlist name, add "market read: sentiment <state>; buy price review?" to the hub's `awaiting` | His decision under `/decision-record`. Never change `buy_price` |
| Detect priced-in | "V# may be priced in" when the market's story has moved to his claim or the multiple has re-rated on his variable | `/variant-view TICKER` update runs its priced-in review. Proposed only |
| Test his thesis | Each new row that bears on a view or debate question, named as a candidate evidence item | `/variant-view` logs it. Reaction evidence shows what is priced, so it cannot raise conviction by itself |

A persistent reaction against one of his views (three or more rows) is passed on as a question: what might the market know that he does not?

## Output

Write `companies/<TICKER>/MarketRead.md` in the vault (frontmatter: `type: document`, `doc: market-read`, `tickers`, `updated`, `data_through`, `next_checkpoint`, `sources: [skill:market-read]`). The vault is append-only, so each run adds a dated read and leaves earlier ones as written:

```
Header: company, ticker, peers and index used, window covered, price sources.
1. Reads (newest first). Each dated read: focus, what is ignored, earnings or
   discount, the story with confidence, sentiment position, and the view-by-view
   lines from Step 5. An unchanged read is one dated line saying "unchanged".
2. Shift log: one dated line whenever the focus, the story or the sentiment
   state changes, with the rows that caused it.
3. Event log (the Step 2 table; rows are appended, never edited).
4. Open puzzles.
Sources
```

Update the hub: `market_focus`, `sentiment` and `market_read` (the date), adding the fields if the hub lacks them; the **Latest** line only when the read changed; any `awaiting` flag from the hand-offs; a dated `## Log` line. Commit per `research-kb` (message `<TICKER>: market-read <date> — <one line>`). The digest makes one commit for all names.

Reply in a few lines per name: the focus, whether the market is arguing about earnings or the discount, the sentiment state, what changed since the last read, and any flag passed on. For the digest, list only the names where something changed, then one line naming the rest as unchanged.

## Standards

- Plain English. Facts, commentary and inference kept apart; every row has a source.
- Quotes under 15 words, one per source; paraphrase otherwise. Summarise broker reasons and never copy notes.
- A move is not an argument. Report what the market appears to believe, and leave whether it is right to `/variant-view` and the debate.
- No price target, fair value, buy/sell or sizing language. Sentiment states describe the market, not what to do.