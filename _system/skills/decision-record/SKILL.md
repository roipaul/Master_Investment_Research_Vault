---
name: "decision-record"
description: "Record the user's own investment decisions (watchlist, buy list with his buy price, initiate, add, trim, exit, pass) in his words with a dated research snapshot, expectations and review date; review and score past decisions. Use for /decision-record."
---

# Decision record

The research skills judge the business and the price. This skill records what the user then decided, so that later he can tell good decisions from good outcomes. It is **record-only**: it logs his decision in his words and never recommends an action, a size or a price. One rule set applies to all his accounts.

## Commands

- `/decision-record TICKER` records a new decision: initiate, add, trim or exit.
- `/decision-record TICKER pass` records a decision not to own, at any stage from triage onward (see Passes).
- `/decision-record TICKER watch` puts a name on the watchlist (see Lists).
- `/decision-record TICKER buy-list PRICE` moves a name to the buy list with his buy price. `buy-price PRICE` changes that price, and `unlist` takes a name off either list (see Lists).
- `/decision-record TICKER review` is the scheduled review. It compares what happened with what the record expected.
- `/decision-record stats` is a read-only summary of `track-record.md` (see Stats).

## Knowledge base (start)

Run the `research-kb` read step. Read `settings.md` for the hurdle and any portfolio rules. Then read the hub, `Thesis.md` or `PriceAlone.md`, `VariantView.md`, the latest file in `earnings/`, `Decisions.md`, `watchlist.md` and `track-record.md`.

**Prerequisite:** a frame must be on file, except for a pass, a watch or an unlist. (A buy-list entry has its own readiness check under Lists.) If the frame is missing, say so. He can override this; log "order overridden by user" with the date.

## Recording a decision

Ask for anything he has not stated in one AskUserQuestion. Never fill in his reasons yourself.

1. **The decision.** Record the action, the date, the price and the currency. Give the size as a percentage of each account he names, using his account labels only. For a trim or exit, record the percentage sold.
2. **Why, in his words.** Quote him verbatim and do not paraphrase.
3. **Snapshot.** Claude fills this from the vault and he confirms it. It holds:
   - the track and zone;
   - the conservative and base returns at today's price, and the harsh case;
   - each variant view with its conviction;
   - the debate verdict;
   - the latest `/earnings-update` call;
   - the conditions at the time, from `/cycle-view` and `/market-read` where they exist: the cycle phase and whether the name is earning above or below its mid-cycle level, the confirmed dial for its markets (or "none confirmed"), and the market's sentiment state for the name;
   - the current commit hash of `Thesis.md`, so a later review reads the thesis as it stood that day.

   Every number carries its date.
4. **Expectations.** Record the one to three observables he expects and by when, what would make him add, and what would make him sell. Offer the thesis falsifiers and the variant-view deadlines as options. He picks or edits them.
5. **Rules check.** Compare the decision with the rules in `settings.md` and report any breach as a fact, for example "position 7% vs limit 5%". This step does not block the decision or advise on it. He may add a reason for overriding a rule.
6. **Review date.** By default this is the next results date or the thesis checkpoint, whichever comes first. He can change it.
7. **Pre-mortem (optional).** One line in his words: "If this loses money, the likeliest reason is…"

**Exits also record:**
- the reason, as one of: falsified / priced in / better use of capital / risk or sizing / mistake found / other;
- the holding period;
- the return including dividends, with the dates used and how it was computed;
- the quality grid: right reason and won, wrong reason and won (luck), right reason and lost (variance), wrong reason and lost (mistake). Claude may propose a box with the evidence, marked **proposed**. He sets the box.

## Passes

A decision not to own is a decision too, and the record of passes is the only way to see what the process misses. Record every Drop at triage, Trap, Pass on price and pass after a write-up. `/research-flow` calls this mode whenever it ends a chain at one of those points. A gate Skip stays a `watchlist.md` line only, unless he asks for a record.

A pass records:
- the stage reached (triage, frame, debate, views or write-up), the date and the price;
- the reason, as one of: quality / no edge / price / value trap / governance / outside his circle or no time / other, plus his words, quoted verbatim;
- the conservative and base returns at that price, if a frame exists;
- what would reopen the name, and a revisit date (default 12 months; he can change it).

Items 3, 5 and 7 of Recording a decision do not apply to a pass.

## Lists: watchlist and buy list

The **watchlist** holds names he has decided to follow towards a buy. The **buy list** holds names that carry his buy price; the price watch (a scheduled task) monitors that list. Each move between lists is a decision and is recorded like one, in his words. Items 3, 5 and 7 of Recording a decision do not apply to list moves.

**Watch.** Record:
- his reason, quoted;
- the work still missing before he would set a buy price. Claude lists what is not on file (frame, debate, views, write-up or price-alone check) and he edits the list;
- what would make him drop the name;
- a revisit date (default: the next results date).

**Buy-list.** First show a readiness check. It reports facts and does not block:
- a frame is on file;
- on the view track, a thesis write-up is on file (at least the debate and the views); on the price-alone track, a check that qualifies;
- the latest fresh-money call is not Don't own, and no falsifier is triggered;
- no work used is stale under `settings.md`.

He can go ahead with gaps; record them as "on the buy list with gaps: …". Then show the reference levels from the work on file, each with its case and date:
- the price at which the conservative case clears the hurdle;
- the price at which the base case clears it;
- the harsh-case loss at his buy price.

The reference levels inform his price; they are not the price. Then record:
- the buy price in local currency, and whether it is to initiate or to add;
- his basis, quoted;
- the conditions that must still hold when the price is reached (offer the falsifiers and the open evidence; he picks);
- a planned size as a percentage, if he gives one;
- a review-by date (default: the next results date, no more than six months out).

**Buy-price.** Record the old price, the new price and his reason, then re-arm the alert.

**Unlist.** Record his reason. If the reason amounts to a decision not to own, record it as a pass instead.

**When the price watch fires.** A `triggered` or `touched` alert puts "buy price reached <date>" in the hub's `awaiting`. When he next records on the name, open by showing:
- the alert;
- what has changed since the buy price was set: results, news, falsifiers, and the reference levels now;
- whether each of his conditions still holds.

He then records one of: initiate or add (recorded as a normal decision), keep the buy price (re-arm), change it, or unlist. An initiate removes the row from the buy list unless he sets an add price.

**Review-by date.** When `buy_review_by` arrives, `/decision-record TICKER review` asks whether his basis still holds in light of the work filed since. He re-confirms the price, changes it, or unlists.

## Review

Read the record, then everything filed since: earnings files, thesis updates and variant-view entries. For each expectation, give the expected reading, the actual reading and a verdict: met, missed or pending. Check his add and sell conditions and report any that have been hit, as facts. Then compare the conditions in the snapshot with conditions now: the cycle phase, the dial and the sentiment state. Say in one line how much of the outcome so far the change in conditions could account for, labelled as inference. A good result made in a rising cycle and a poor one made at a peak are both worth knowing when he judges the decision. Set the next review date. Append the result as a dated section of `Decisions.md`.

**Reviewing a pass** happens at its revisit date, or earlier if a reopen condition is hit. Record:
- the total return including dividends since the pass, with the dates used;
- whether it would have cleared the hurdle at the pass price;
- whether the stated reason held up, with the evidence.

Then place it in the pass grid: reason held and the stock lagged (good pass), reason held but the stock ran anyway (defensible miss, for example a market-wide re-rating), reason wrong and the stock ran (mistake of omission), reason wrong and the stock lagged (lucky pass). Claude may propose a box, marked **proposed**; he sets it. Then he either closes the record or sets a new revisit date.

## Stats

This mode only reads `track-record.md`. It reports:
- hit rate and median return by track, by edge type and by idea source (screen, gate, his own idea);
- the quality grid counts;
- average holding period;
- how often add or sell conditions were hit and then ignored;
- passes: the share that went on to beat the hurdle, by reason and by stage, and the pass-grid counts.

It makes no recommendations.

## Write step

- **`Decisions.md`**: append a dated section and never rewrite. A correction is appended as "Correction <date>".
- **Hub**: set `held` (the account labels, or false) and `next_checkpoint` to the review date, update the **Latest** line, and add a log line.
- **`decisions-log.md`**: add one line: date | ticker | action | size % | track | review date.
- **`track-record.md`**: add a line on exit with the entry and exit dates, return, reason and grid box; and a line when a pass review closes, with the pass date and price, return since, reason and pass-grid box.
- **`watchlist.md`**: for a pass, add a line with the trigger that would reopen the name and the revisit date. Also add the revisit date to the hub's `catalysts:` as type `review`.
- **Lists** (a watch, buy-list, buy-price or unlist, and an initiate or add from the buy list):
  - set the hub's `list` and, for the buy list, `buy_price`, `buy_action`, `buy_basis`, `buy_set`, `buy_review_by` and `alert: armed`; clear the buy fields when the name leaves the buy list;
  - rebuild the **Current watchlist** section of `watchlist.md` from the hubs with `list: watch`, and add a line to its log;
  - add, change or remove the row in `buylist.md`, and append a dated line to its alerts log;
  - add `buy_review_by` to the hub's `catalysts:` as type `review`;
  - rebuild `overview.md` as `/research-flow` describes.
- **Commit**: `<TICKER>: decision-record <date> — <action>`.

## Never

- Recommend an action, size, price target or timing.
- Propose a buy price. Show the reference levels with their case and date, and let him choose.
- Reword his reasons, or record a decision he has not stated.
- Record account numbers or amounts. Sizes are percentages only.
- Edit an earlier record.

## Reply

One line saying what was recorded, plus the review date and any rule breaches. Stop there; the detail is in the vault.