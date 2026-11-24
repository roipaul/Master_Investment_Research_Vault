---
type: view
doc: priorities
updated: 2026-11-24
quality_high: 6           # quality score out of 8 needed for High (returns score at least 1)
upside_base_hurdle: "15%" # base-case return a year at today's price
upside_cons_floor: "8%"   # conservative-case return a year at today's price
---

# Research priorities

Which name to work on next, by business quality and upside at today's price. Built by `/priority-rank`; re-run it after a results day, a new primer or a price move of more than 10%. Quality scores and quick valuations marked *(Claude's)* are proposals until Paul confirms them; nothing here is a buy price.

## How it works

**Quality (out of 8).** Four tests, 0, 1 or 2 each, scored from the primer and earnings work on file:
- **R, returns:** returns above the cost of capital through a cycle (2 = well above, including at the trough).
- **D, durability:** a named reason the returns last (network, cost position, switching costs, licence, structure).
- **G, runway:** room to grow revenue for years (0 = the core is shrinking).
- **E, earnings quality:** free cash flow tracks profit; no persistent add-backs or accounting flags.

**High quality** means 6 or more, with R at least 1. Governance and whether cash reaches minority holders are shown as a separate flag, because the conservative case already prices them.

**Upside.** The scenario values on file, divided by today's price. **High upside** means the base case earns at least 15% a year **and** the conservative case earns at least 8% a year (Paul's choice: rank on the base case, with the conservative case as a floor).

**The grid** gives four boxes, each with its own next step:

| | High upside | Low upside |
|---|---|---|
| **High quality** | **1. Work now**: deep work towards a buy price | **2. Set a price**: no deep work yet; watch for the price that moves it to box 1 |
| **Low quality** | **3. Check for a trap**: run the value-trap check or the price-alone track, not a full thesis | **4. Park**: revisit only on a change in the business or a large price fall |

Within a box, names are ordered by base-case return. A name within one point of a line is flagged as borderline. Ties go to the name with less work left and the nearer catalyst.

## Ranking at 2026-11-24

| # | Ticker | Box | Quality R-D-G-E | Conservative / base a year | Harsh case (total) | Price moving it to box 1 | Price used | Work left before a buy price | Next catalyst |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [[YMM]] | 1 Work now | 8 (2-2-2-2) | 9.1% / 19.2% | -8% | at or below US$8.98 (now inside) | about US$8.7, 2026-11-19 (e) | Triage, model, frame, debate; Q3 update (two uploads) | Q4 results, Mar 2027 (e) |
| 2 | [[0700-HK]] | 2 Set a price (borderline) | 7 (2-2-2-1) | 7.9% / 19.3% | -14% | HK$341 (on the line) | HK$341.6, 2026-11-24 | Triage, model, frame | FY2026 results, about 2027-03-18 |
| 3 | [[NVDA]] | 2 Set a price | 8 (2-2-2-2) | 6.3% / 16.1% | -38% | US$154 (-7%) | US$165.05 close 2026-11-23 | Primer, model, frame | 10-Q, about mid-Dec 2026 |
| 4 | [[PDD]] | 2 Set a price | 7 (2-2-1-2) | 4.5% / 14.6% | -36% | US$75.6 (-10%) | US$83.68 close 2026-11-20 | Frame; merchant, seller and IR calls | Q4 results, late Mar 2027 |
| 5 | [[KSPI]] | 2 Set a price | 6 (2-2-1-1) | 0.1% / 14.2% | -49% | US$67.7 (-21%) | US$85.80 close 2026-11-19 | Import primer; model, frame | Ex-dividend about 2026-12-10; Q4, late Feb 2027 |
| 6 | [[000807-SZ]] | 3 Check for a trap | 3 (1-1-0-1) *(Claude's quick valuation)* | 8.7% / 24.2% | -28% | RMB 24.5 (now inside) | about RMB 24, early-mid Nov (e) | Triage, then the value-trap check (mid-cycle earnings) | FY2026 annual, Mar-Apr 2027 |
| 7 | [[TME]] | 3 Check for a trap | 5 (2-1-0-2) | 9.5% / 18.7% | -9% | US$9.88 (now inside) | US$9.45, 2026-11-17 | Triage, frame (price-alone track candidate) | FY2026 results, about 2027-03-17 |
| 8 | [[FISV]] (held) | 3 Check for a trap (borderline) | 4 (1-2-0-1) | 8.1% / 20.9% | -25% | US$63.0 (on the line) | US$62.79 close 2026-11-17 | Model; decision review | Q4 and 2027 guide, Feb 2027 |
| 9 | [[JD]] | 4 Park (borderline on both lines) | 5 (2-1-1-1) | 7.6% / 26.6% | -44% | US$25.1 (-1%) | US$25.43 close 2026-11-17 | Import primer; model, frame | Q4/FY2026, early Mar 2027 |
| 10 | [[6417-T]] | 4 Park | 5 (2-1-0-2) *(Claude's quick valuation)* | 3.2% / 11.3% | -8% | ¥1,911 (-13%) | about ¥2,200, mid-Nov (e) | Triage | Q3 FY3/2027, early Feb 2027 |
| 11 | [[105560-KS]] | 4 Park | 3 (1-1-0-1) | 3.1% / 10.8% | -36% | KRW 125,000 (-13%) | KRW 144,200 close 2026-11-23 | Sign-off; import earlier work | Q4/FY2026, early Feb 2027 |
| 12 | [[WCC]] | 4 Park | 4 (1-1-1-1) | -4.1% / 7.0% | -50% | US$210 (-31%) | US$303.06 close 2026-11-23 | Sign-off; import earlier work | Q4/FY2026, 2027-02-09 |

Returns run to the end of 2029, about 3.1 years from today (NVDA to its FY31 value point, about 4.2 years). Each uses the scenario table in the name's latest earnings file, or the model (PDD v2.2), with today's price swapped in. A scenario value already includes the dividends paid over the hold.

### Why each quality score

- **YMM 8:** dominant full-truckload matching platform with network effects; asset-light with about 70% of assets in cash; FCF above non-GAAP profit in 2025; penetration still 20-30%. *Flag:* take-rate regulation, VIE structure.
- **Tencent 7:** the core earns high returns, with a social and ad moat and growth in ads, games and cloud. Earnings quality is 1 because the AI loss and capex are open-ended. *Flag:* none on cash return (large buybacks).
- **NVDA 8:** dominant platform, very high returns and cash conversion. *Flag:* governance shock (CEO exit and investigation); the cycle sits in the upside axis, not here.
- **PDD 7:** the lowest-cost marketplace, needing almost no capital. Runway is 1 because domestic growth is mid-single-digit. *Flag:* cash is not returned and disclosure is thin (Paul's pillar 3).
- **Kaspi 6:** about 40% ROE and an ecosystem moat. Runway and earnings quality are 1 because of the slowdown, the credit book and the tenge. *Flag:* country and currency.
- **Yunnan Aluminium 3:** a commodity smelter whose returns are high now but whose capacity is capped; capex has run below depreciation. *Flag:* SOE finance company, related-party flows.
- **TME 5:** strong returns and cash conversion, but organic paid membership is shrinking and competition from Soda is rising. *Flag:* low-return deals such as Ximalaya.
- **Fiserv 4:** sticky banking core, but Merchant and Banking revenue is shrinking, the add-backs recur and leverage is 3x.
- **JD 5:** high returns on its retail capital and the logistics network, but recurring subsidy wars and venture losses absorb the profit.
- **Sankyo 5:** high returns on a cash-heavy balance sheet, but the pachinko market is in structural decline.
- **KB 3 / Wesco 4:** low growth, or returns near the cost of capital; KB's are typical for a bank.

### Quick valuations behind rows 6 and 10 *(Claude's, for ranking only; no model on file)*

- **Yunnan Aluminium** (3,468m shares, net cash about RMB 21bn at Q3, 40-45% payout; cash credited at 50% because part sits with Chinalco Finance):
  - Conservative: the spread normalises and profit steps down from RMB 15bn (2026E) to 9bn by 2029, at 8x. Value about RMB 31 a share.
  - Base: the 45mt capacity cap keeps profit near 15bn, at 8x. Value about RMB 47.
  - Harsh: the spread returns to 2024 levels, profit about 4.5bn. Value about RMB 17.
  - The base case is "the peak holds", which is why the name goes to the trap check, not to box 1.
- **Sankyo** (about 197m shares, net cash about ¥200bn, dividend of ¥100 a year):
  - Conservative: net profit falls 5% a year to ¥34bn, core at 6x plus cash. About ¥2,430 including dividends.
  - Base: profit flat at ¥40bn, core at 8x. About ¥3,070.
  - Harsh: profit falls 12% a year, core at 5x. About ¥2,030.
- **YMM** (1,041m diluted ADS, cash RMB 33.4bn, 6.7 RMB to the dollar, cash credited at 80%, about RMB 2bn a year returned):
  - Conservative: core profit after tax and excluding interest flat at RMB 4.7bn, at 8x excluding cash. About US$11.4.
  - Base: core profit +10% a year, at 10x. About US$15.0.
  - Harsh: take-rate cap, core profit -30%, at 6x. About US$8.0.

## What this says to work on

1. **YMM first.** It is the only name in box 1. The work is the Q3 update (upload the two documents), then triage, the rough model and the frame. Your stated views (take-rate cap later than feared; fulfilment runway) are exactly what the debate would test.
2. **Tencent next.** It sits on the line into box 1. Its conservative case is 7.9% against the 8% floor, with HK$341 as the line. Triage and a model would settle whether the conservative case is too harsh. This is the name where a small price move or a small piece of evidence changes the box.
3. **For NVDA, PDD and Kaspi:** no deep work for now. Their prices for box 1 (about US$154, US$75.6 and US$67.7) are candidates for watchlist revisit triggers. They are not buy prices.
4. **Box 3 (Yunnan Aluminium, TME, Fiserv):** a value-trap check rather than a thesis. TME has the best downside of any name here (-9% harsh case); Yunnan's upside depends on peak spreads holding.

## Not ranked yet

- **Earnings-watch names with no work in the vault:** [[ZTO]], [[3690-HK]] Meituan, [[TCOM]] Trip.com, [[POOL]], [[FDR-MC]] Fluidra, [[UNH]], [[AA]] Alcoa, [[STZ]], [[1590-TW]] Airtac, [[0268-HK]] Kingdee, [[0669-HK]] Techtronic, and [[2454-TW]] MediaTek (Q3 fact pack only). To rank them, put the primers, models and notes from your claude.ai Projects into `inbox/uploads/<TICKER>/` or attach them in a chat. Each is scored once its work is in the vault.
- **No work yet:** SK Square (402340.KS) and Odawara Engineering (6149.T).
- **Price-alone basket:** ranked separately below.

## Price-alone basket (separate, lighter ranking)

Quality here is the basket's own five value-trap tests and the governance check; upside is the conservative return from the 2026-11-15 screen (prices not refreshed).

| Order | Ticker | Conservative return | Five tests / governance | Next step |
|---|---|---|---|---|
| 1 | [[417790-KQ]] TRUEN | 35.1% | Pass / Pass | Refresh the price; ready for a watchlist decision |
| 2 | [[9709-T]] NCS&A | 20.1% | Pass / Pass | Refresh the price; ready for a watchlist decision |
| 3 | [[1161-HK]] Water Oasis | 18.9% | Unclear / Pass | Settle the unclear test (next check 2026-12-15) |
| 4 | [[9919-HK]] Activation Group | 18.2% | Unclear / Pass | Settle the unclear test |
| 5 | Rest of the "Qualifies, provisional" group | 16-27% | Pass or Unclear / Unclear | Governance checks, highest return first: [[6049-HK]], [[036190-KQ]], [[000270-KS]], [[3316-HK]], [[2481-HK]] |

Time-sensitive: [[069510-KQ]] ESTec. The Foster Electric tender offer at KRW 24,000 closes on 2026-12-11, and the tender decision is waiting on Paul.
