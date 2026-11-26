---
name: "cycle-view"
description: "Roll single-name research up into cycle notes (industry, commodity, inventory and capex, credit) and a where-we-stand read per market with a proposed aggressive-to-defensive dial, using fixed indicators and no forecasts. Use for /cycle-view."
---

# Cycle view

The company work says what each business earns. This skill says **where those earnings sit in their cycle, and how hot or cold each market is**, so that a peak is not mistaken for normal and the user knows how demanding to be on price. It produces two things: cycle notes, and one where-we-stand read per market.

The user is an experienced equity analyst running his own and his family's money, with a 15% IRR hurdle over a 3–5 year hold. He does not make macro calls. The standing rule, after Howard Marks: you cannot predict, but you can know where you stand. So this skill describes the present and states what follows from it conditionally. **It never forecasts** rates, growth, prices or the timing of a turn, and it uses no buy, sell or position-size language.

He uses the output for four things, each with a hand-off below: the earnings base for each name, how strict to be on price, where to look for ideas, and a check on concentration.

## Modes

- `/cycle-view cycle NAME` — build or refresh one cycle note.
- `/cycle-view market MARKET` — build or refresh one market read (us, china-hk, japan, korea, taiwan).
- `/cycle-view due` — refresh whatever is due (see Cadence), at most two items a run. Safe to schedule: everything it produces is observation or proposal.
- `/cycle-view stand` — rebuild the one-page view `macro/where-we-stand.md` from the notes and reads.
- `/cycle-view dial MARKET confirm` — record the user's confirmation of a proposed dial. Only he can run this.

## Knowledge base (start)

Run the `research-kb` read step. Read `settings.md` (the confirmed `dials:`), `cycles/index.md`, the note or read being refreshed, and for the names involved their hub, latest earnings file, `MarketRead.md` and `Thesis.md` where they exist.

`cycles/index.md` is the registry: one row per cycle note with its type, depth (full or light), status (active or later), names, and fixed indicator set with the source for each. If it is missing, create it from the list the user has approved and say so. Add or activate a note only when he asks.

## Data

- Public sources through the search and fetch tools; the registry names the source for each indicator. A scheduled run can fetch only addresses written into its prompt or returned by its own searches, so when a fetch is refused, search for the release and use a dated report of it.
- Chinese and Korean official portals are mostly unreadable to the fetch tool. Use dated press that repeats the official release, and name both.
- Every reading carries its period, its release date and its source. A figure with no date inside the period is not used. Never state a reading from memory.
- Company-level readings come from the earnings files already in the vault, not from fresh research.
- Paid sources (cost curves, order books, consensus history) are used only when the user supplies them; otherwise use the free substitute named in the registry and say what it lacks.
- No time series in the vault. A note holds the current reading, the reading three months and a year ago, and where the current one sits in its own 5–10 year range.

## Part 1 — Cycle notes

Four types: **industry demand**, **commodity or price spread**, **inventory and capex**, **credit**. A full note is written for a cycle that touches two or more of his names or sets one name's earnings base. A light note is one page on a cycle he does not own, kept for spotting ideas.

### Rules

1. **Fixed indicators.** Five to eight per note, set in the registry and kept from one refresh to the next. A change to the set is logged with its reason.
2. **Each indicator is scored against its own history**, not against a story: now, three months ago, a year ago, position in its 5–10 year range, direction.
3. **Phase**, on the same scale the earnings updates use: Downturn / Trough / Early recovery / Mid-cycle / Late cycle / Peak / Rolling over. Give the evidence for and against, and the previous phase. If the indicators disagree, say so and give the range ("Late cycle to Peak") instead of forcing one word.
4. **Roll-up from the names.** List each name's own cycle read from its latest earnings file, with the date. Where the names and the outside indicators disagree, the disagreement is a finding.
5. **Earnings against mid-cycle, per name.** Current margin against its 10-year average, and mid-cycle earnings as the 10-year average margin times current revenue. Where the cycle is a spread (a metal against its feedstock, a price against a cost), also give the current spread against its 10-year range. State "over-earning by about x%" or "under-earning by about x%". Where a structural change means the 10-year average no longer applies, say what changed and show both figures.
6. **What the price assumes.** One or two lines from the names' market reads, where they exist.
7. **What would change the phase.** The two or three readings to watch, with their release dates. No prediction of which way they go.

A light note holds items 2, 3 and 7, plus "names worth a first look": at most three, each with one line on why the cycle position makes it interesting. They are candidates for the pre-primer gate, nothing more.

## Part 2 — Market reads

One read per market: United States, China and Hong Kong, Japan, Korea, Taiwan. Each has four blocks, with a fixed set of indicators in each, scored **Hot / Neutral / Cold** against the indicator's own history with the evidence beside it.

| Block | The question (after Marks) | Typical indicators |
|---|---|---|
| Economy | What are conditions, in plain readings? | Growth, inflation, policy rate, currency, profit margins against history |
| Credit cycle | Are lenders eager or reluctant, and terms easy or tight? | Credit growth, lending standards or lending-attitude surveys, spreads, quality of new issuance, bad-loan trends |
| Psychology | Are investors paying up for risk or fleeing it? | Margin debt, retail deposits and flows, new listings, sentiment surveys, who is buying |
| Price of risk | What is an investor paid to take risk today? | Valuation against its own range, earnings yield less the bond yield, dividend yield |

The Economy block is context. The dial is proposed from the other three, because Marks' point is that risk is highest when it looks lowest: easy credit, confident investors and thin compensation.

### The dial

Three settings per market: **Defensive** (conditions hot), **Neutral**, **Aggressive** (conditions cold).

- Propose Defensive when at least two of the three blocks (credit, psychology, price of risk) are Hot and none is Cold. Propose Aggressive when at least two are Cold and none is Hot. Otherwise Neutral.
- **The dial moves slowly.** A new setting is proposed only when two readings in a row point to it. One reading that differs is reported as "leaning" and changes nothing.
- **A proposal is not a setting.** Write it to the market read and to **Waiting on you**. The confirmed dial lives in `settings.md` under `dials:` and changes only through `/cycle-view dial MARKET confirm`.
- Which dial a name uses: the market that drives its earnings and the market where it is listed. Where the two differ, use the more defensive of the two, and record both on the hub.

### Two maps

1. **What the theses depend on.** For each deep-work name, the cycle or macro condition its base case assumes will last: a spread, a rate level, a currency, credit availability, a policy. Take it from the thesis and variant-view files; where they do not say, write "not stated" and do not guess.
2. **Helped and hurt.** The areas helped and the areas hurt by present conditions in that market, side by side, each with whether the price already reflects it (valuation against its own range). Areas that are hurt and priced as if the damage were permanent go under **Where to look next**. Areas that are helped and fully priced are flagged as such. This is a map for research, not a call on any of them.

## Hand-offs (the four uses)

| Use | What this skill provides | Who uses it |
|---|---|---|
| Earnings base | Phase and mid-cycle earnings per name, dated | The value-trap check in `/variant-view` and the normal-earnings step in `/price-alone` take them from the cycle note |
| How strict on price | The confirmed dial. The hurdle stays 15%. Defensive: the conservative case must clear the hurdle or come within three points of it, as well as the base case. Neutral and Aggressive: the base case clearing is enough | `/variant-view` Step 1 |
| Where to look next | Cycles at Downturn or Trough, and hurt-and-priced-as-permanent areas, as suggested screens | The user, and the pre-primer gate |
| Concentration | A table of deep-work names by cycle and by the condition each depends on: position weights from `Decisions.md` for held names, a count for buy-list and watchlist names | The where-we-stand view |

The phase and the confirmed dial at the time are also what `/decision-record` should store with each decision, so that a decision can later be judged against the conditions it was made in.

## Cadence

- A cycle note is due when any name in it has a newer earnings file than the note, or the note is more than 100 days old. A light note is due at 100 days.
- A market read is due when it is more than 85 days old.
- `/cycle-view due` does at most two items a run, missing ones first, then the oldest. When nothing is due it says so in one line.

## Output

- `cycles/<slug>.md` — one per cycle (frontmatter: `type: document`, `doc: cycle-note`, `tickers`, `updated`, `data_through`, `next_checkpoint`, `sources: [skill:cycle-view]`). The vault is append-only: each refresh adds a dated read, newest first, and a dated line in a phase log when the phase changes.
- `macro/<market>.md` — one per market, same frontmatter with `doc: market-read`. Each refresh adds a dated read; a dial log records each proposal and each confirmation.
- `macro/where-we-stand.md` — a view rebuilt from the above, never edited by hand: the dial per market (confirmed, and any proposal), the phase of each cycle, the two maps, where to look next, and the concentration table.
- On each hub in a refreshed note: `cycle`, `cycle_phase`, `mid_cycle_note` (the date of the note) and the two dial markets, adding the fields if the hub lacks them, with a dated `## Log` line.

Commit per `research-kb` (message `cycle-view: <date> — <one line>`).

Reply in a few lines: what was refreshed; any phase that changed and the reading that moved it; any dial proposal, with the two readings behind it; any name now over-earning or under-earning by more than about a quarter; and what is due next.

## Standards

- Plain English. Facts, commentary and inference kept apart; every reading has its period, date and source.
- No forecasts and no timing. Say what the readings are, what has followed such readings before where a base rate is known, and what would change the read.
- A phase or a dial that changes at every refresh is noise. If two successive refreshes disagree, report the disagreement and keep the earlier setting.
- Never state or adjust the user's views. Never change a confirmed dial, a verdict, a zone or a buy price.
- Quotes under 15 words, one per source; paraphrase otherwise.