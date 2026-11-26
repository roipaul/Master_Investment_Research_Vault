---
name: "variant-view"
description: "Find where the user's view differs from what a stock's price implies, state each variant view as a testable claim, and keep a dated ledger of evidence and conviction per key question. Use for /variant-view."
---

# Variant view

The debate judges whether the business thesis is true. This skill asks a different question: **is any of it not already in the price, and how well is that supported?** A view can be correct and still earn nothing if the market already holds it. The skill finds what the price implies, sorts the user's views into variant, consensus and no-disagreement, states each variant view as a claim that can be checked, and keeps a ledger of the evidence and the conviction it supports. Run again later, it logs new evidence and moves conviction. It is used in two passes: a frame early in the research, before the debate, and the views after the debate and the evidence work.

The user is an experienced equity analyst running his own and his family's money. His hurdle is a **15% IRR over a 3–5 year hold**. No price target, no fair value, no buy/sell or position-size language. "There is no variant view here" is an allowed and useful result; say it plainly when it is true.

## Modes

- **Frame** — `/variant-view TICKER frame`. Steps 1–2 only: the zone, the value-trap check and what is priced in. Run it early, right after triage and the rough model and **before** the debate, because it decides which track the name takes and tells the debate which questions the price disagrees with.
- **Views** — `/variant-view TICKER views`. Steps 3–6, run after the debate and the evidence work. Refresh the price and the frame first.
- **Workshop** — `/variant-view TICKER workshop`. A guided session that helps the user develop his own views (see Workshop mode). It needs the frame; run the frame first if it is missing.
- **Build** — `/variant-view TICKER` with no ledger and a thesis already in place. Frame then views in one run, Steps 1–6.
- **Update** — `/variant-view TICKER` when a ledger exists, or `/variant-view TICKER log ...` with new evidence (results, a DD finding, scuttlebutt, a policy event, the user's own note). Step 7 only.

## Knowledge base (start)

If the `research-kb` skill is available, run its read step: pull the vault and read the hub `companies/<TICKER>/<TICKER>.md`, then `VariantView.md`, `MarketRead.md`, `Thesis.md`, `Debate.md`, `DD.md`, `Scuttlebutt.md` and the linked policy and theme notes, whichever exist. Otherwise use the Project copies or files in the conversation and say so. The skill works without a primer or debate, from the user's stated views plus filings, but say that the fact base is thinner.

## Step 1 — Which zone is the stock in?

This decides whether a variant view is needed at all. Get the price, diluted share count and net cash, dated and sourced. Then compute two returns **at today's price** (returns, not target prices):

- **Conservative case**: demonstrated earnings power (not forecasts), growth of 0–2% unless a higher rate is close to certain, no change in the multiple. Return is roughly free-cash-flow yield plus growth.
- **Base case**: the user's own expected path, no change in the multiple.

| Zone | Test | What the idea needs |
|---|---|---|
| Price alone | Conservative case earns 15% or more **and** the value-trap check passes | No variant view required |
| Needs a view | Only the base case earns 15% | A view that differs from the price and is right |
| Pass on price | Even the base case falls short | Nothing here fixes it |

**The dial.** Read the confirmed dial for the name's markets from `settings.md` (`dials:`): the market that drives its earnings and the market where it is listed, using the more defensive of the two. The hurdle stays 15% at every setting. When the dial is Defensive, a name on the view track must also have its conservative case clear the hurdle or come within three points of it; if it does not, say so beside the zone and treat the price as not yet paying for present conditions. At Neutral or Aggressive, or where no dial is confirmed, the table above applies as written. State the dial and its confirmation date beside the zone. Never act on a proposed dial.

Cash counts only to the extent it reaches shareholders or is reinvested at a decent return; state how much is credited and why. Show the arithmetic in a small table. 

### Value-trap check (required when the stock is cheap)

Run this whenever the conservative-case return is **10% or more**, which is within about five points of the hurdle, and not only when it clears 15%. A low multiple means the market doubts the earnings; this check asks whether the doubt is justified. Answer each test with numbers and a source, and mark it **Pass / Fail / Unclear**.

| Test | What to compute | Fails when |
|---|---|---|
| Earnings base | Current earnings against the 5–10 year average and the last trough; margin against its own history and peers; one-offs, subsidies and gains stripped out | Current earnings sit well above the through-cycle level with no structural reason |
| Structural decline | Five-year trends in volume, market share and real pricing; the industry's volume trend; substitution or regulation under way | Volume or share is falling for reasons that are not cyclical |
| Balance sheet | Net debt to EBITDA, interest cover, maturities inside the hold period; the return recomputed on enterprise value (the unlevered yield) | The yield clears only because of leverage, or debt must be refinanced inside the hold period on weak cover |
| Cash reaching shareholders | Five-year record of dividends plus net buybacks as a share of free cash flow; what retained cash was spent on and what it earned; where cash sits and what restricts it (onshore, VIE, regulatory capital); related-party flows | Little cash has come out, or retained cash was spent at low returns |
| Earnings quality | Free cash flow against net income over five years; working-capital and capitalised-cost trends; stock compensation; auditor or accounting changes | Cash conversion is persistently low or falling without an investment reason |

Then answer in one sentence: **why is it cheap?** Name the market's most likely reason (from Step 2 when it has been run) and say whether any of the five tests confirms it.

What the result does:

- **Rebuild the conservative case** on what the tests show: through-cycle earnings, the unlevered yield where leverage is high, and cash credited only at the historical payout rate. Recompute the return. The zone is set by the rebuilt figure, not the headline multiple.
- **Any Fail** means the stock is not "Price alone". It moves to "Needs a view", and the failed test becomes a key question in Step 5: the view the user then needs is that the problem is temporary or over-discounted.
- **Any Unclear** goes into the gaps table with a route and a date; until it is settled the zone reads "Price alone (provisional)".

Adjust by sector. For banks and insurers, use return on equity and payout instead of free-cash-flow yield, and replace the balance-sheet test with capital ratios, through-cycle credit costs and reserve coverage. For cyclicals, build the earnings base on mid-cycle prices and margins; a low multiple on peak earnings is a Fail until shown otherwise. Where a cycle note covers the name (`cycles/`, from `/cycle-view`), take the phase and the mid-cycle earnings from it and cite its date. If the note is more than 100 days old, say so and use it as a first estimate only.

## Step 2 — What is priced in

Build one table: `Variable | Implied by price | Sell-side consensus | User's view | Position | Gap | Effect on value`.

The **Gap** is always measured against the implied number, never against consensus. **Position** places the user's number against both benchmarks:

| Position | What it means |
|---|---|
| Above both | He disagrees with everyone on size. The evidence bar is highest here |
| Below consensus, above the price | **Cuts ahead.** The price already doubts consensus, and estimate cuts are still to come. Use the reactions log (item 2 below) to check how the stock moved on past misses and cuts. If it still fell, the cuts are not fully in the price and the gap is smaller than it looks. Write this flag into the frame |
| Above consensus, below the price | The price asks for more than he expects. No gap on this variable |
| Below both | No gap on this variable; another variable must carry the idea |

Fill the user's column only with numbers he has stated. In Frame mode, before a workshop, leave it and the Position blank where he has given none.

1. **Reverse the valuation.** Solve for the growth, margin and duration that justify the price (reuse the debate's price check if it exists). State three or four implied assumptions.
2. **Read the reactions.** Take them from `MarketRead.md` when it exists: its focus, what the market ignores, its earnings-or-discount reading and its sentiment position, citing the event rows. If it is missing or more than 30 days old, run `/market-read TICKER` first. If that cannot be done in this session, do the short version here: for the last four to six results days and material events, what was reported, which metric the commentary fixed on, and the stock's move against peers and its index. Beats that do not lift the stock mean the discount is not about near-term numbers.
3. **Peer test.** If listed peers and the country or sector trade at the same discount, part of the gap is not company-specific; say how much.
4. **Who is on the other side.** Short interest, holder changes, downgrades, the bear notes' stated reasons. Where the user has access, use `research-portals`:
   - Bernstein and CLSA notes for the brokers' stated reasons and rating changes;
   - Capital IQ for ownership changes, insider transactions and the transcript passages analysts pressed on;
   - Xueqiu for Chinese names.

   Summarise the reasons; never copy the notes.

The consensus that matters is the price, not sell-side estimates. For a KPI the company does not disclose, fill the sell-side column with the range of broker estimates from `research-portals` rather than a single number, because the spread shows how uncertain the market's inputs are. Sell-side numbers go in the table only to show where they sit relative to it. Label which implied assumptions are computed and which are inferred from reactions.

### What the thesis rests on

Two short pieces of arithmetic and one label. They tell the user what kind of claim he would be making before he spends time on it.

1. **Covered share.** Add five years of conservative-case free cash flow (undiscounted) to the cash credited in Step 1, and divide by the market cap. This is the share of today's price that the next five years repay on cautious numbers. The rest has to come from year six onward.
2. **How the return arrives.** Split the base-case return into what the business pays with no change in the multiple (cash yield plus growth) and what needs the multiple to rise. If the first part alone meets the hurdle, the user does not need the market to agree with him. If it does not, name the event that would change the multiple and its likely date. "The market will come round" is not an event.
3. **Label.** One label, or two with the main one first:

| Label | When | What the view must then show |
|---|---|---|
| Near-term | Covered share of roughly two-thirds or more | Nothing about durability. The value-trap check carries the weight; this is a price-alone candidate |
| Duration | Covered share below about half, and the stated reasons for the low price (reactions, bear notes) are that earnings fade or the business declines | The advantage lasts longer than priced, with markers that can be checked inside the hold period |
| Discount | Covered share below about half, the earnings path is not much disputed, and the low price is a markdown for cycle, governance, country or cash that may not reach holders (the peer test usually shows it) | The risk is smaller than priced, or clears by a date, and the harsh case is bearable |

Between one half and two-thirds, give both labels. A user whose numbers are below consensus and who still sees value above the price is making a Duration or Discount claim, or relying on the price already assuming less than he does. Say which.

### Hand-off from the frame

In Frame mode, stop after Step 2 and report five things:

- **Track.** Price alone → `/price-alone TICKER check`. Needs a view → `/thesis-debate`, then the evidence skills (`/desk-dd`, `/scuttlebutt`, `/policy-timeline`), then Views mode. Pass on price → say so, and record the return the base case earns at today's price so the name can be revisited when that changes.
- **Questions for the debate.** Turn each implied assumption into a question ("the price implies order growth of about x% a year for five years; is that too low?") and say which of the primer's High-materiality questions it maps to. The debate should spend its effort where the price and the facts might disagree, not on questions the price already answers the user's way.
- **Why it is cheap or dear**, in one sentence.
- **What the thesis rests on**: the label, the covered share, and any "cuts ahead" flag from the Position column.
- **How the return arrives**: the part the business pays with no change in the multiple, the part that needs a re-rating, and the event and date for the second part.

Write these to the ledger as a dated frame section. Views mode re-reads it and refreshes the price before continuing.

## Workshop mode — helping the user develop views

The views in the ledger must be the user's own. This mode helps him form them: you ask, he answers. You may supply facts, base rates, analogues and the strongest bear reply. You may not supply the view or the number. If he asks what you think, give candidates marked as candidates, each with the evidence it would need.

Ask **one question at a time**, in plain text, and wait for the answer. Keep a session to about eight questions.

1. **Open with the frame.** State the label (near-term, duration or discount) and the covered share first, so he knows what kind of claim is on the table. Then show the implied-assumptions table and ask which line he would bet against, and what his number is.
2. **If nothing comes, try the other four starting points in turn:**
   - *Disputed facts* — list the facts on which the bull and bear cases disagree (from the debate, if it exists) and ask which way he thinks each falls, and why.
   - *Comparison* — ask where this situation has played out before, in another country, industry or company, and how it resolved. Offer two or three analogues as facts if he wants them.
   - *Anomaly* — put two or three numbers from the filings that do not fit the prevailing story in front of him, without interpreting them, and ask what he makes of them.
   - *Year five* — ask what the business looks like in five years that a two-year view would miss.
3. **For each view that emerges, ask:** his number and by when; which mechanism from the Step 4 list explains why the market is wrong, what evidence shows it is at work, and what would end it; what would change his mind.
4. **Give the strongest bear reply** in two or three sentences, with its evidence, and ask whether the view survives, changes or is dropped.
5. **Stop** when he has one to three views in four-part form, or says there is none. "No view" is a result: record it, and point to the zone (the name may still qualify on price alone) or to a Defer.

Write each surviving view in the Step 4 form, in his words, and mark the five tests. Append a dated session log to the ledger: which starting points were used, which views emerged, which were dropped and why. Then continue to Step 5, or stop if he wants to gather evidence first.

## Step 3 — Sort the user's views

Take the views from the user, the thesis, the debate or a workshop session. **Never assign him a view he has not stated.** You may propose candidates; mark them "candidate" until he adopts one. Classify each:

- **Variant** — differs from an implied assumption on a variable that moves value.
- **Consensus** — true, but the price or the bulls already hold it.
- **No disagreement** — a real risk he accepts and is paid for.

Give each variant view a type, because the type sets what evidence decides it:

| Type | The claim | Evidence that decides it |
|---|---|---|
| Duration | Growth or returns last longer than priced | Cohort and retention data, entrant economics, how similar advantages faded elsewhere |
| Magnitude | Same direction, different size | Unit-level data, penetration curves in comparable markets, capacity |
| Probability | A tail risk is over- or under-weighted | Base rate of the event, a modelled harsh case, the trigger variable |
| Framing | The market uses the wrong lens | Segment disclosure, what the right comparables are valued at, proof of which lens the market uses |
| Mechanism | What the advantage really is | Customer and channel evidence on why they buy, win/loss data, cost curves |

### The bridge: earnings and discount

Once the views are sorted, show where the gap between the user's case and the price comes from. Every variant view sits on one of two legs, and the thesis is built on the leg that is both large and well supported.

- **Earnings leg**: he expects a different earnings path from the one the price implies. Magnitude views sit here, and so do Duration views about how long growth or margins last.
- **Discount leg**: on the same earnings, he thinks the price marks them down too far. Probability and Framing views sit here, along with discounts for cycle, governance, country and access to cash.

A Mechanism view goes on whichever leg it changes. Build one table for a named year three to five years out, using only numbers he has stated:

| Leg | Implied by price | Consensus | User | Difference | Views | Conviction | His probability |
|---|---|---|---|---|---|---|---|
| Earnings | Year-N earnings the price needs | Consensus for year N | His year-N earnings | His against implied, in % | V# | Lowest level among them | His figure, if he gives one |
| Discount, as a multiple | The multiple the price pays on normal earnings | n/a | The multiple he argues for, with the comparison behind it (own history, peers of like quality) | In % | V# | As above | As above |
| Discount, as a return | The return the price offers on his earnings path with no change in the multiple | n/a | The hurdle | In points | | | |
| Discount, in years | The years of earnings or growth the price assumes | n/a | His | In years | | | |

The three discount rows say one thing in three ways; show all three. Fill the conviction column after Step 6. Then state:

1. **Split.** Roughly what share of the whole gap comes from each leg, from the earnings ratio and the multiple ratio. Say "about two-thirds earnings, one-third discount"; do not give false precision.
2. **Certainty per leg.** Two measures, kept apart: the conviction level from Step 6, which moves only on evidence, and his own probability that he is right on that leg, in his words. Never fill in his probability for him.
3. **What the thesis is built on.** The leg, or legs, with both real size and conviction at level 2 or above. A leg that is large but sits at level 0 or 1 is a hope until the evidence arrives. List what would lift it, and treat it as a show-me view if it depends on uncertainty clearing.
4. **The discount leg needs a path.** A low multiple can last for years. If the thesis leans on the discount leg, the frame's "how the return arrives" must show either that the business pays the hurdle with no re-rating, or a dated event that narrows the discount.

If he differs on neither leg, there is no variant view; say so. The table uses earnings, multiples, returns and years, never a value per share.

## Step 4 — State each variant view

Four parts, two or three sentences in total, with a number and a date:

1. **Variable** — the one thing the claim is about.
2. **Gap** — the user's number against the implied number.
3. **Reason** — the evidence for the claim. Why the market is wrong goes in its own block below.
4. **Resolution** — what observable result shows who was right, and by when.

**Why the market is wrong (required for every variant view).** A view with no account of the other side is only a disagreement. Write four lines, in the user's words where he has given them:

- **Mechanism** — one from this list, or say that none fits:
  - *Horizon*: holders judged on the next year cannot own it through estimate cuts or a slow payoff.
  - *Extrapolation*: recent trouble is priced as permanent.
  - *Constrained sellers*: index changes, mandate, country or sector exclusions, redemptions, a spin-off.
  - *Uncertainty*: a wide range of outcomes is priced like a bad one until it resolves.
  - *Complexity or neglect*: structure, disclosure, language or thin coverage keep buyers away.
- **Evidence the mechanism is at work** — holder changes, exclusion lists, the path of estimate revisions against the price, coverage counts, the reactions log from Step 2. A mechanism asserted without evidence counts as not named.
- **What ends it** — the event or condition that removes the mechanism, and whether the return needs it to end (from "how the return arrives" in the frame).
- **The case that the market is right** — the strongest version in two or three sentences, and the observable that would show it.

**Show-me views.** A view is a show-me view when it depends on uncertainty going away rather than on evidence the user can gather now: a competitive fight still in progress, a regulatory outcome pending, a turnaround not yet visible in the numbers. Buying one is a bet that the uncertainty clears, and the usual cost of being wrong is years of dead money. So each show-me view carries an **evidence deadline**: a date, no more than 12–18 months out, and the specific observable that must appear by then (for example, "market share stable above x% for two consecutive quarters by Q2 2027"). Set it at build and write it in the summary table.

Then mark five tests pass or fail: stated with a number; a smart bear would disagree; the price disagrees; the mechanism that makes the market wrong is named with evidence; it can be proven wrong by a date. A view that fails two or more goes back to Consensus or is rewritten. If the facts show the view is framed wrongly (for example, the feared event has already happened in mild form), restate it and say why.

## Step 5 — Key questions and evidence

For each variant view, list the two to four questions that decide it (use the debate's Q numbers where they match). Before researching, write what each side needs to be true. **Search for the disconfirming evidence first.**

Evidence table per view: `E# | Date | Evidence | Source | Independent of company? | For / Against / Neutral | Question`.

Then a gaps table: `Missing evidence | Why it matters | Route | By when`, with route as **Desk** (hand to `/desk-dd` or `/policy-timeline`), **People** (hand to `/scuttlebutt`, or say who to find and what to ask) or **Wait** (a dated event).

For any view that depends on a policy, regulatory or political outcome, three items are required: the **base rate** (every past intervention, what was demanded, what changed afterwards), the **bounded-downside test** (model a specific harsh outcome and compute the return at today's price) and the **trigger variable** (what has set off action before, and its current reading). Proving such an event will not happen is not possible; showing the thesis survives it is.

## Step 6 — Conviction

Conviction measures how well the view is supported. It is separate from the debate's probability, and it moves **only on logged evidence**.

| Level | Name | Required |
|---|---|---|
| 0 | Hypothesis | Stated; evidence is the user's reasoning or company sources only |
| 1 | Supported | Gap quantified; a base rate or analogue; at least one source independent of the company |
| 2 | Tested | The deciding evidence for its type is in hand; the bear case is answered with numbers; a harsh case is modelled |
| 3 | Strong | Tested, plus the harsh case still earns an acceptable return at today's price, the trigger variable is not deteriorating, and some of the evidence is primary work others do not weight |

Caps: a view on a policy or political outcome cannot pass level 1 until the bounded-downside test is done, and cannot reach level 3 if the harsh case loses real money. A view that fails any of the five tests cannot pass level 1. A view with no mechanism named and evidenced in its why-the-market-is-wrong block stays at level 0. A show-me view cannot pass level 1 until its named observable first appears. State next to each level what single piece of evidence would move it up, and what would move it down.

## Step 7 — Update

1. Add each new item to the evidence table with its date and source. Results and filings come from primary sources. Rows passed on from `MarketRead.md` are evidence about what the market believes, not about the business. They can change the Gap, the Position, the why-the-market-is-wrong block and the bridge, and they can mark a view Priced in. On their own they never raise a conviction level. A persistent reaction against a view (three or more rows) goes into the gaps table as a question: what might the market know that the user does not?
2. Re-score conviction for the views it touches: old level → new, citing the E# that caused it. Unchanged views are listed as unchanged.
3. Refresh the price and Step 1, re-running any value-trap test the new evidence touches. If the price has moved so the gap has closed, mark the view **Priced in** and run the priced-in review below. If the zone changed, say so.
4. Check resolution dates and evidence deadlines. A show-me view whose deadline has passed without its observable is marked **Expired**: conviction returns to 0, it moves to resolved views as "Expired, unproven", and the status line says the evidence did not arrive and the view no longer supports the idea. A deadline is extended only on an evidence item logged after the deadline was set, with the reason written down; waiting longer is never the default. A view whose date has passed is scored **Right / Wrong / Unresolved** with the number, and a line goes to `track-record.md` with the lesson, what the view rested on (near-term, duration or discount), its type and the mechanism named. Keeping these fields lets results be compared by kind of edge. This scored record is the only real test of whether the views carry an edge, so never skip it.
5. Move closed gaps out of the gaps table; add new ones.

Append; never rewrite earlier entries.

### Priced-in review

When a view is marked Priced in, the reason to own has changed. The return no longer comes from the market being wrong; it has to come from the business alone, and that needs its own check against the hurdle.

1. **Confirm it is priced in.** The implied assumption has moved most of the way to the user's number (roughly four-fifths of the original gap has closed), or the price now requires more than the user's number.
2. **Recompute both returns at today's price**, with no change in the multiple: the conservative case and the user's base case.
3. **State one status:**
   - **Still clears** — the base case earns 15% or more. The idea now rests on compounding; list what must stay true (the debate's critical questions).
   - **Falls short** — the base case earns less than 15%. The view has done its work and nothing in the ledger now supports the hurdle. Say so plainly.
   - **Other views remain** — another open variant view still carries a gap; name it and its conviction.
4. **Score the view** in resolved views: **Right** if the gap closed on the evidence the view named, **Right for another reason** if the price moved for something else (a market-wide re-rating, a different catalyst). The difference matters for the track record, because only the first shows an edge.
5. **Log a dated line:** `V# priced in on <date> at <price>; base-case return now x%; status`.

The output is the status and the arithmetic, never buy or sell language.

## Output

Write `companies/<TICKER>/VariantView.md` in the vault (frontmatter: `type: document`, `doc: variant-view`, `tickers`, `updated`, `data_through`, `next_checkpoint`, `sources: [skill:variant-view]`). If the vault is unreachable, write `VariantView_<TICKER>.md` and send it.

```
Header: company, ticker, date, price and net cash with date, zone, track, and which modes have been run with their dates.
1. Summary table: V# | Claim (one line) | Type | Leg | Class | Gap | Conviction | Last changed | Resolves by | Evidence deadline (show-me)
2. Zone arithmetic and value-trap check (Step 1)
3. What is priced in (Step 2 table with positions, reactions log), then what the
   thesis rests on (covered share, how the return arrives, label)
4. Views sorted (variant / consensus / no disagreement, one line each), then the
   bridge (earnings and discount legs, split, certainty per leg, what the thesis
   is built on)
5. One section per variant view: statement, why the market is wrong, five tests, key questions,
   evidence table, gaps table, conviction with what would move it
6. Conviction log: dated lines, old → new, evidence ID
7. Resolved views: outcome and lesson
Sources
```

Then update the hub (a variant-views table with conviction, the **Latest** line, `updated`, `next_checkpoint`, a dated `## Log` line), pass new tracking signals to the thesis's "What to track", and commit per `research-kb` (message `<TICKER>: variant-view <date> — <one line>`).

Reply in a few lines: the zone, the value-trap result when the check ran, each variant view with its conviction level, the one piece of evidence that would move each, any view newly Priced in or Expired with its status, and the next checkpoint.

## Standards

- Plain English. Facts, management claims and inferences labelled as such; every evidence row carries a URL or filing reference.
- Numbers computed, not asserted; implied assumptions show their arithmetic.
- Quotes under 15 words, one per source; paraphrase otherwise.
- No price target, fair value, buy/sell or sizing language. Zones and conviction levels describe the idea, not the trade.
- Most variant views turn out wrong because the market is usually roughly right. Keep both sides to the same standard, and if every view in a ledger sits at level 2 or 3, re-check the counter-evidence before delivering.