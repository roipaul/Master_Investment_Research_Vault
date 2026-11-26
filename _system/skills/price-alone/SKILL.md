---
name: "price-alone"
description: "For cheap stocks that need no variant view: screen a supplied list for high-yield, low-debt, cash-returning names, run the value-trap and governance checks on each, and keep the basket table. Use for /price-alone."
---

# Price-alone track

Some stocks are cheap enough that a deliberately conservative case still earns the hurdle. They need no variant view; the price does the work. The whole job on this track is different from the view track: **make sure it is not a value trap, make sure the cash can reach a minority shareholder, and keep the work light enough to cover a basket of names.** Without a view, the result rests on the group behaving as cheap, sound businesses usually do, so no single name deserves the depth of a full primer and debate.

The user is an experienced equity analyst running his own and his family's money, best placed to research Hong Kong, China, Japan, Korea and Taiwan. His hurdle is a **15% IRR over a 3–5 year hold**. No price target, fair value, buy/sell or position-size language; he sets sizes himself.

## Modes

- **Screen** — `/price-alone screen` with a data file or a list of tickers. Filters and ranks.
- **Check** — `/price-alone TICKER check`. The full check on one name. Also the hand-off from `/variant-view TICKER frame` when the zone is "Price alone".
- **Review** — `/price-alone review`. Re-checks every name in the basket table after results or on a set date.

## Knowledge base (start)

If the `research-kb` skill is available, run its read step and read the hub, `VariantView.md`, any primer and `price-alone-basket.md`. Otherwise use the Project copies or files in the conversation and say so.

## Screen

Use the data source the user has set up. If there is none, ask for an export (CSV or Excel) with, per company: ticker, name, exchange, sector, market cap, average daily value traded, net cash or net debt, and 5–10 years of revenue, EBIT, net income, free cash flow, dividends paid, buybacks and share count, plus the largest shareholder's stake and type (state, family, parent company, holding company, none). Ask for two currency fields per company: the currency of the market cap and the currency of the financials. Where the data source can supply them, also ask for related-party sales as a share of revenue, and the dividend paid in the last downturn year. For a short list of tickers, the figures can be pulled from filings instead. Never fill a missing field with a guess or a zero; mark it missing.

### Data checks (before any filter runs)

Cheap-looking results are often data errors, so run these checks first and report what they found:

- **Currency.** Confirm the market cap and the financials are in the same currency. Snap each implied exchange rate to the nearest standard rate (for example USD 1, CNY ~6.7–7.2, HKD ~7.8, JPY ~150–160, KRW ~1,400, TWD ~31–33, using current rates) and flag any mismatch. Hong Kong-listed companies reporting in RMB, and US-listed Chinese companies, are the usual cases.
- **Missing versus zero.** Treat a blank or zero dividend, buyback or cash figure as missing unless the filing confirms zero. Korean dividends are often missing in Capital IQ exports.
- **Outliers.** Re-check any name whose conservative yield exceeds twice the screen median before ranking it.

Default filters (the user can change any of them; say which were used):

| Filter | Default |
|---|---|
| Conservative yield | Five-year average free cash flow over market cap of 12% or more, or EV/EBIT of 7 or less. Banks and insurers: P/E of 7 or less with return on equity of 10% or more |
| Not shrinking | Revenue no lower than five years ago |
| Leverage | Net debt under 1.5x EBITDA (not applied to financials) |
| Cash return | Dividends plus net buybacks at least 30% of free cash flow over five years, and share count not rising |
| Earnings quality | Free cash flow at least 70% of net income over five years |
| Returns | Average return on capital above roughly 8–10% through the cycle |
| Tradable | Daily value traded above the floor the user sets |

**Normal earnings.** Use the lower of the last 12 months and the five-year average. For names flagged cyclical (commodities, materials, shipping, semiconductors' memory makers, and any name whose current margin is more than 1.3x its 10-year average), cap normal earnings at the 10-year average margin times current revenue, and show the trailing figure beside it for reference only. A peak margin is a cap, not just a flag. Where a cycle note covers the name (`cycles/`, from `/cycle-view`), use its phase and mid-cycle earnings and cite its date. A name whose cycle note reads Late cycle, Peak or Rolling over is treated as cyclical here whatever its sector.

**Governance pre-screen.** Run these before ranking, because governance kills more cheap Asian names than business quality does. Mark each Pass or Flag; a Flag ranks the name lower but does not drop it:

- controlling holder type and stake;
- dividend paid through the last downturn (cut to zero is a Flag);
- share count rising over five years;
- related-party sales above 20% of revenue, where available;
- cash above half of market cap with a low payout (cash that may not reach minority holders).

Flag, do not drop: a listing younger than three years and a controlling holder above 50%.

Output a ranked table with pass or fail per filter, the governance pre-screen, the data-check flags, the missing fields, and the top names proposed for a check. The user picks which go forward.

**Carry structured fields between batches.** When screening runs in batches, keep one row per name with fixed fields: five-test results, governance result, failed test (if any), key question, data gaps, verdict and source. When batches are combined, or names are chosen for the next stage, work from these fields and re-read the notes for any name near a cut-off. Never select from one-line verdicts alone.

## Check (one name)

1. **One-page read.** What it sells, to whom, why it earns what it earns, and what happened in the last downturn. Use the abridged primer if one exists; otherwise write the page from the latest annual report. No full primer.
2. **Zone and value-trap check.** Reuse `/variant-view TICKER frame` if it has been run; otherwise apply its Step 1. The five tests are earnings base, structural decline, balance sheet, cash reaching shareholders and earnings quality, each marked Pass / Fail / Unclear with numbers. The zone is set by the rebuilt conservative case.
3. **Governance and cash.** This is where cheap Asian companies most often disappoint, so it is required:
   - Who controls the company, and their record with minority holders: past buyout offers and at what price, related-party deals, asset injections, share pledges.
   - Where the cash sits: onshore or offshore, restricted, pledged, lent to related parties, or deposited with a group finance company (and the deposit cap); cross-holdings and treasury shares.
   - Related-party trading: sales to and purchases from the controlling holder as a share of the total, the annual caps approved, and how pricing is set.
   - The dividend record through the last downturn, and what the company has said about payout policy (including Korea Value-up or Tokyo Stock Exchange disclosures where relevant).
   - The record on acquisitions and other uses of retained cash.
   - Auditor, audit qualifications and board independence.
   Hand registry, insider and related-party lookups to `/desk-dd`. Mark the section Pass / Fail / Unclear.
4. **Why is it cheap, and who is selling?** One or two sentences.
5. **What pays while waiting.** The dividend and buyback yield actually paid, as carry. Then any trigger that could close the gap (a payout change, a buyout, an activist, index inclusion). Carry must be able to earn most of the hurdle; triggers are upside, never the base case.
6. **Harsh case.** Earnings at the last trough level and the payout at its trough level: the return at today's price, and the loss if the multiple also falls to its 10-year low.
7. **Verdict:**
   - **Qualifies** — the rebuilt conservative case clears the hurdle, all five tests pass and governance passes.
   - **Qualifies, provisional** — Unclear items remain; list each with a route (Desk / People / Wait) and a date.
   - **Needs a view** — one test fails. Send it to `/thesis-debate` and `/variant-view` with the failed test as the key question.
   - **Trap** — two or more tests fail, or governance fails because cash cannot reach minority holders. Drop, with the reason and what would reopen it.

Set the exit conditions now, so they are not decided under pressure later: (a) the conservative return at the then-current price falls below the hurdle (the price has done its work); (b) any test or governance turns to Fail; (c) after two to three years, carry received is well short of what was expected.

## Review

For each name in the basket: refresh the price and the conservative return; re-run the five tests on the new numbers in two lines each; compare payout actually paid with what was expected; check the three exit conditions. Report only what changed, then the full table.

## Output

Write `companies/<TICKER>/PriceAlone.md` in the vault (frontmatter: `type: document`, `doc: price-alone`, `tickers`, `updated`, `data_through`, `next_checkpoint`, `sources: [skill:price-alone]`), following the seven steps above, with sources.

Keep one table at `price-alone-basket.md`: `Ticker | Date checked | Conservative return | Five tests | Governance | Carry yield | Why cheap | Group | Status | Next check`. **Group** records country, sector and type of controlling holder, so that several names sharing one kind of trap are visible at a glance.

Then update the hub (track, verdict, `updated`, `next_checkpoint`, a dated `## Log` line) and commit per `research-kb` (message `<TICKER>: price-alone <date> — <verdict>`). If the vault is unreachable, send the files.

Reply in a few lines: the verdict, the conservative return, any test that is not a Pass, the governance result and the next check date.

## Standards

- Facts, management claims and inferences labelled as such; every number carries its source and period.
- Quotes under 15 words, one per source; paraphrase otherwise.
- A cheap multiple is a question, not an answer. If every name screened comes back "Qualifies", re-check the earnings-base and governance sections before delivering.
- No price target, fair value, buy/sell or sizing language.