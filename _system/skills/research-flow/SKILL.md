---
name: "research-flow"
description: "Orchestrate the research pipeline across companies: read each company's stage from the vault, say what is next, stale or waiting on the user, run the next skill up to the next judgment point, and keep the pipeline table. Use for /research-flow."
---

# Research flow

The user's research runs through a dozen skills in a set order. This skill keeps track of where each company stands, runs the next step, and stops wherever the judgment is his. It adds no analysis of its own: to run a stage, load that skill with the Skill tool and follow it in full, never a shortened version from memory.

The state lives in each company's hub note in the vault (`stage`, `track`, the dates under `steps:`, `awaiting`). `pipeline.md` is only a view rebuilt from those hubs. If the vault cannot be reached, say that the flow cannot be tracked, and offer to run a single skill from the Project documents instead.

## The pipeline

| # | Stage | Skill | Needs first | Stops for the user |
|---|---|---|---|---|
| 1 | Gate | `/primer-triage TICKER gate` | nothing | **Yes**: Primer / Watch / Skip |
| 2 | Primer | `/full-primer`, then `/abridged-primer` | gate confirmed Primer | no |
| 3 | Triage | `/primer-triage` | primer | **Yes**: Dig / Defer / Drop |
| 4 | Model | `/value-dcf-model`, a rough version for drivers and sensitivity | Dig | no |
| 4b | Market read | `/market-read TICKER` (first build) | Dig | no |
| 5 | Frame | `/variant-view TICKER frame` | model, or filings if no model; the market read | **Yes**: the track, and pruning the debate questions |
| 6a | Debate | `/thesis-debate` | frame, view track | no |
| 7a | Evidence | `/desk-dd`; `/scuttlebutt` and `/policy-timeline` when the plan calls for them | debate | no (the people plan is his to act on) |
| 8a | Views | `/variant-view TICKER workshop`, then `views` | evidence | **Yes**: always done with him |
| 6b | Price-alone check | `/price-alone TICKER check` | frame, price-alone track | **Yes**: the verdict |
| 9 | Write-up | `/thesis-writeup` | views, or a price-alone verdict | no |
| 10 | Decision | `/decision-record` | write-up or price-alone verdict | **Yes**: his decision, his words |
| 11 | Monitoring | `daloopa:earnings-prep` → `daloopa:earnings-review` → `/earnings-update` (`/thesis-update` for events other than results) → `/variant-view` update or `/price-alone review` | a decision on file, or the name kept on watch | flags only |

Skip, Watch, Defer, Drop, Trap and "Pass on price" end the chain: set the stage, add the watchlist line with its trigger and revisit date, and log it. A Drop, Trap or Pass on price, or a pass after the write-up, also runs `/decision-record TICKER pass`, which stops for his reason. Ending a name early is a good outcome, not wasted work.

## Commands

- `/research-flow status` — every name: what is waiting on him, what is next, what is stale. Rebuilds `pipeline.md`.
- `/research-flow TICKER` — where one name stands and its next step; runs it according to the mode.
- `/research-flow new TICKER` — create the hub and run the gate.
- `/research-flow due` — the monitoring pass (below).
- `/research-flow calendar` — dated events across every name for the next 90 days. Rebuilds `calendar.md` (see Calendar).
- `/research-flow overview` — every researched name by list, with buy prices and reference entry levels. Rebuilds `overview.md` (see Overview). `status` rebuilds it too.

## How a run works

1. Run the `research-kb` read step. Read `settings.md`, then the frontmatter and **Latest** line of each hub (not the full documents).
2. Take the stage from the hub and check it against the files: if the hub says the debate ran but `Debate.md` is missing, flag it and do not proceed on that name.
3. Apply the staleness checks: a frame older than `frame_stale_days` or a price move beyond `frame_stale_price_move` since `price_check`; a primer older than `primer_stale_months`; a thesis with no `/earnings-update` file for the latest results; an `/earnings-update` call still awaiting his sign-off; a show-me evidence deadline within 30 days or passed; a decision review or Defer revisit date due; a view marked Priced in with no review; a market read more than 14 days old on a deep-work name (held, buy list, watchlist or in research).
4. Name the next action for each name and whether it needs him.
5. Run according to `flow_mode`.

## How much runs without asking

- **`ask-every-step`** (the setting to start with): name the next skill, what it will produce and roughly how long it takes, then wait for his go-ahead.
- **`gates-only`**: run each step in turn and stop at the next stage marked **Yes** above.

In either mode, run **at most one heavy stage per session** (`/full-primer`, `/value-dcf-model`, `/thesis-debate`). After it, write the state, commit, and stop with the command for the next step. Long chained sessions produce worse work, and the vault makes stopping free.

## Order rules

- No debate before a frame.
- No views before the debate and at least the desk part of the due diligence.
- No write-up before the views, or before a price-alone verdict on that track.
- No decision record without a frame.
- No more than `max_active` names between triage and decision. If a new Dig would exceed it, list the active names and ask which to pause.

He can override any of these. Do as he says and log "order overridden by user" with the date.

## Monitoring pass

For each name that is held or in monitoring:

- Results due within seven days and no prep on file → run `daloopa:earnings-prep`.
- Results published and not yet reviewed → `daloopa:earnings-review`, then `/earnings-update`, then `/variant-view` update (or `/price-alone review`).
- Find the next results date from the company's own announcements and write `next_results` to the hub.
- A catalyst within seven days that tests a question or view: name the question and the reading that would move it. This goes in the reply only; it does not get its own document.
- A non-results catalyst that has passed with no reading logged: run `/thesis-update` with that event (or `/price-alone review` on that track), then clear it from `catalysts:` per `research-kb`.
- A pass or decision review date that has arrived: run `/decision-record TICKER review`.
- Market read: run `/market-read digest` when the last read on any deep-work name is more than seven days old, and `/market-read TICKER update` after each `/earnings-update`. Pass its flags on. "May be priced in" leads to a `/variant-view` update. A sentiment extreme on a buy-list or watchlist name goes under **Waiting on you**.
- Cycle view: run `/cycle-view due` when a cycle note has a name with a newer earnings file than the note, a cycle note is more than 100 days old, or a market read is more than 85 days old. The "Cycle view — weekly check" scheduled task normally does this. A dial proposal goes under **Waiting on you** with the command `/cycle-view dial MARKET confirm`; it changes nothing until he confirms it. A name whose cycle note now shows it earning well above or below mid-cycle is flagged for a re-run of its frame.
- Buy list: a `buy_review_by` date that has arrived, or "buy price review" in `awaiting`, means run `/decision-record TICKER review`. An alert `triggered` more than seven days ago with no decision recorded goes under **Waiting on you**.

A change in verdict, conviction level or zone that comes out of this pass is written as **proposed** and put in the hub's `awaiting` field. It becomes final only when he confirms it. This pass is safe to run on a schedule because nothing in it decides for him.

## Calendar

`calendar.md` is a view, like `pipeline.md`: rebuild it from the hubs and never edit it by hand. Gather the following from every hub, then add the resolution dates and evidence deadlines from each `VariantView.md` summary table:
- `catalysts:`;
- `next_results`;
- `next_checkpoint`;
- Defer and pass revisit dates;
- decision review dates.

Write one table sorted by date: `Date | Ticker | Event | Type | Tests | Held | Status`. Mark with ★ any event that tests a High-materiality question, a variant view or a falsifier on a held name. Put events that have only an expected month or quarter in a separate block below the table. Flag clusters, meaning one event that bears on several names (a policy ruling, an index rebalance, a peer's results that the cycle reads depend on). Use no positioning language.

## Overview

`overview.md` is a view: rebuild it from the hubs, `watchlist.md`, `buylist.md` and `price-alone-basket.md`, and never edit it by hand. It has these groups, in order, with a table in each:
1. **Buy list**: buy price, action, last price and gap, alert, review-by date.
2. **Held**: last decision, fresh-money call, reference entry level, next checkpoint.
3. **Watchlist**: basis, work still missing before a buy price, reference entry level, revisit date.
4. **In research**, not yet on a list: stage and next step.
5. **On the earnings watch** with no list decision yet.
6. **Price-alone basket**: status, conservative return, next check.
7. **Passed or dropped**: reason and revisit date.

Every price carries its date and source. Keep **buy price** (his, buy list only) and **reference entry level** (Claude's arithmetic, labelled as such) in separate columns, and never merge the two. Close the file with a note on research that sits only in claude.ai Projects and is not yet in the vault.

## Never

- Invent or alter his views, or record a decision on his behalf.
- Skip a stage marked **Yes** in `gates-only` mode.
- Use buy, sell or position-size language of its own. "Buy list" and "buy price" name his own lists and prices, and are reported as facts.
- Recompute an old return silently: a number older than its staleness limit is shown as stale until the frame is re-run.
- Delete notes.

## Reply

For `status` and `due`, three short blocks, one line per item: **Waiting on you** (buy prices reached come first), **Ran since last time**, **Due soon**. For `overview`, give one line per group with its count and any buy-list name within 5% of its buy price; the rest is in `overview.md`. For `calendar`, give the next 14 days one line each with the ★ items first, then any clusters; the rest is in `calendar.md`. For a single ticker: its stage, what has been done with dates, the next step, and whether that step needs him. Then stop; the detail is in the vault.