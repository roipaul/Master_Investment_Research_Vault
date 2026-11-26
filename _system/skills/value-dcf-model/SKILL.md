---
name: "value-dcf-model"
description: "Build or rebase a value-oriented three-statement + DCF Excel model for a listed company from annual reports and/or a data file; use for 'build a model / DCF / valuation of X' and for follow-up edits to one."
---

# Value-oriented DCF model

Deliverable: an Excel workbook (three statements, assumptions, DCF, multiples, one-page summary) that ties to the reports, recalculates with zero errors, and can be defended line by line. Questions for IR only when asked. Responses to the user stay concise; explanations go in the workbook's notes columns, not in long chat replies.

## 1. Before building: ask once, then go

One AskUserQuestion covering everything the brief leaves open. Do not build with guesses on these:

- **Valuation style** (always ask): (a) modified DCF — adjusted/core EBITA as the cash-flow proxy, PPA amortisation added back with no tax shield, lease payments treated as capex and leases excluded from net debt, explicit deductions for debt-like items, optionally blended with a normalised-earnings × warranted-multiple cross-check; (b) classic unlevered FCF — EBIT-based, tax shields, leases in net debt; (c) owner-earnings / earnings-power. The style changes calculation definitions only; every tab uses the same layout (section 3a) whatever the style.
- **Horizon** (always ask): years of history, explicit forecast years, and whether the DCF extends beyond the explicit years (organic growth, margin drift, reinvestment at an incremental ROIC) before the terminal value.
- **Security valued** (share class, fixed discounts between classes), valuation date, currency/units.
- Anything the brief imposes (assumptions, deductions, treatments) — read it twice and list each item with how it will be modelled before starting.

If the user is away, take the most defensible reading, state it at the top of the reply, and proceed.

## 2. Inputs

- Use what is attached. If nothing is attached, fetch: the last N annual reports (N = history years), the latest interim report, and current prices/yields (web). Say which documents were used.
- A data file (Daloopa-style xlsx/csv) is the history source when present; annual reports are still read for the notes.
- Read the notes, not just the primary statements. Minimum list: business combinations (purchase-price allocation, contingent consideration), intangibles and D&A by class (split acquisition-related amortisation from the rest), PP&E and rental/lease assets, leases (IFRS 16 roll-forwards), provisions and items affecting comparability, financial instruments and borrowings (maturities, supply-chain financing in payables), post-employment benefits, tax (effective rate drivers), equity and share counts (treasury shares, dividend record/payment dates), associates/JVs and minorities, contingent liabilities and commitments.
- Work on a copy; never edit the user's upload in place.

## 3. Workbook structure and conventions

Tabs in this order: Summary · DCF · Multiples · Performance Analysis · Assumptions · Income Statement · Balance Sheet · Fixed Assets & D&A · Cash Flow. When scenarios or 'what the price implies' are asked for, add Range of outcomes and Price slider straight after Summary (section 6b). Years run left to right in the same columns on every tab (history then forecast); one label column A; a notes/source column to the right of inputs.

- Colours: blue = hard-coded input, black = formula, green = link to another sheet; grey italic small = notes and source citations (report, note number, page/table).
- Every input lives on Assumptions; statements contain only formulas and links. No hard-codes inside the statements except reported history.
- Checks rows on every statement (balance sheet balances; cash-flow closing cash = balance sheet; D&A and operating profit tie to the income statement; fixed-asset roll-forwards close; equity and borrowings roll). All must be exactly zero.
- Switches for any treatment the user may want to flip (e.g. convertible as debt vs if-converted; whether given margins include a specified loss). Document the switch on the same row.
- Build with openpyxl from a script that locates rows by their labels, not hard-coded row numbers (assert the label before writing). Keep a reusable helper for formats/colours and a row-restructure tool that remaps every formula and text citation across the workbook when rows move.
- Recalculate every version with LibreOffice (`recalc.py`) and refuse to deliver with any #REF!/#NAME?/#VALUE! or a non-zero check.
- File naming: `<TICKER>_Financial_Model_<date>_v<N>.xlsx`, N incrementing from the user's latest version.

## 3a. Layout standard (identical for every valuation style)

The reference is the modified-DCF workbook layout. A classic or owner-earnings model reuses the same tabs, block order, row order and formatting; only the definitions inside a few rows change, and those rows state their basis in the label.

**Every tab**
- Gridlines off; Arial 10; zoom 85–100.
- Rows 1–3: company name and ticker (bold 12) · tab title (bold italic 11) · one grey italic 8pt line with units, fiscal-year definition and the colour legend.
- Year header: row 7 grey italic 8pt 'Actual'/'Forecast' above each column; row 8 the currency unit ('SEK m') in A, years formatted `0"A"` / `0"E"`, bold, right-aligned, medium bottom border. History then forecast in the same columns (B onward) on every statement tab, so a given column is the same year everywhere.
- Column A labels wide enough to show the full label (~70–100), year columns ~12.5; notes and source citations in one grey italic 8pt column to the right of the last year (Assumptions: column E).
- Section headers: white bold text on navy fill (1F3864). Sub-headers bold, no fill. Detail rows indented one level; 'of which' rows two.
- Totals and subtotals bold with a thin top border; balance-sheet grand totals thin top + double bottom. Growth and margin rows directly under their line, grey, labelled '% change' / '% of revenue'.
- Number formats: `#,##0_);(#,##0);"-"_)` for amounts, two decimals for per-share, `0.0%` for ratios, `0.0"x"` for multiples. Costs and outflows negative; signs consistent between statements and cash flow.
- Check rows at the bottom of the block they test, indented, labelled 'check', showing zero.
- Freeze panes below the year header and right of column A; landscape, fit to one page wide.

**Tab skeletons (same block order in every style)**
- *Assumptions*: Market data → revenue and margins by forecast year → acquisitions and acquisition accounting → working capital → capex, fixed assets and leases → maintenance capex → tax, financing and shareholders → investments, minorities and special items → long-term and discount-rate assumptions. Inputs in column B (by year in B–D where they vary), notes in E.
- *Income Statement*: revenue → cost of sales → gross profit → opex lines → items affecting comparability → adjusted EBITA (and core EBITA if anything is excluded) → acquisition amortisation → operating profit → financial items → profit before tax → tax → net profit → minorities → owners → shares, EPS, DPS → Returns block.
- *Balance Sheet*: ASSETS (current, non-current, total) → EQUITY AND LIABILITIES (current, non-current, equity, total) → balance check → Key balances and ratios (net debt on the style's basis, NWC, invested capital incl./excl. goodwill) → acquisition landing block → memo roll-forwards.
- *Fixed Assets & D&A*: D&A summary (by class, reconciled to the cash-flow add-back) → lettered roll-forward sections A, B, C… per asset class, each Opening → additions → acquired → depreciation/amortisation → other → Closing (= Balance Sheet row) → lease liabilities last.
- *Cash Flow*: operating (profit, D&A, non-cash items, operating cash surplus, financial items, tax, working-capital lines) → investing → financing → net cash flow, opening/FX/closing cash → checks → Free cash flow block (capex by type, total capex, FCF before acquisitions and dividends, FCF after acquisitions).
- *Performance Analysis*: the sections in 6a, in that order, same year columns.
- *DCF*: one column per year (explicit then extension) and a Terminal column. Blocks: cash-flow build → discounting (period, factor, PV) → terminal value → Enterprise value to per-share value (bridge) → Discount rate (WACC build) → cross-check block. Method columns B/C/D in the bridge when there is more than one method (e.g. DCF / cross-check / blended).
- *Multiples*: market data rows → market cap → EV rows (each labelled with its basis) → 'Multiples at the prices above', one row per multiple, basis in the label.
- *Summary*: left half market snapshot then financial summary (years across); right half valuation per share (headline first), price, upside, implied multiple, then key assumptions and bridge items as label / value pairs; IR questions (when asked) across the bottom. One landscape page.

**DCF rows whose definition changes by style (position and label pattern fixed)**

| Row | Modified | Classic UFCF |
|---|---|---|
| Profit base | Core EBITA (PPA added back) | EBIT (after PPA amortisation) |
| Tax | Profit base × rate, no PPA or interest shield | EBIT × rate (shield only on deductible PPA) |
| NOPAT | After-tax core EBITA | After-tax EBIT |
| + D&A | Excl. PPA and right-of-use depreciation | All D&A incl. PPA and right-of-use |
| − Capex | PP&E + intangibles + rental + lease payments | PP&E + intangibles + rental + new leases (ROU additions) |
| Bridge: net debt | Excl. leases | Incl. leases |

All other rows are identical across styles. An owner-earnings model uses the same skeleton with the cross-check block as the primary method. The style is fixed at build time (no style switch cell).

## 4. Modelling choices (defaults; override from the brief)

- **Revenue**: organic growth × FX translation + acquired revenue consolidated. Keep history growth decomposed the same way where the reports allow.
- **Margins**: forecast EBITA margin; derive opex as the plug. Show adjusted EBITA (ex items affecting comparability) and, if something is excluded from the valuation base, a separate 'core' line with the exclusion explicit.
- **Acquisitions**: EV spent per year at an EV/sales multiple; allocate EV to goodwill / amortisable intangibles / acquired working capital / net tangible assets using the company's own recent allocation; amortise new intangibles over a stated life (half-year in year one); run the existing intangible pool off over its remaining life, calibrated so the first forecast year reproduces the latest actual amortisation.
- **Fixed assets**: roll-forwards per class (acquired intangibles, internally generated intangibles, rental fleet, other PP&E, right-of-use assets, lease liabilities) with capex as % of revenue and depreciation as % of opening balance; D&A summary reconciled to both the notes and the cash-flow add-back (state any residual).
- **Working capital**: DIO/DSO/DPO days plus % of revenue for other items; cash-flow working-capital lines exclude acquired balances and FX translation (those go through acquisitions and reserves respectively).
- **Financing**: interest on opening net debt; dividends = prior fiscal year's declared DPS × basic shares at the payment dates (verify record dates — the dividend paid this year belongs to last year's earnings); minority dividends; no plug on cash — cash is the output.
- **Share counts**: basic vs diluted kept as separate inputs; any convertible instrument is either if-converted (shares in count and market cap, nothing in net debt) or debt at face — never both.
- **Net debt for the bridge**: latest reported balance sheet, adjusted for cash events between balance-sheet date and valuation date (dividend instalments paid), with the lease treatment matching the style chosen.
- **DCF**: mid-year discounting; stub for the remaining share of the current year; explicit years then an extension block (organic growth, margin drift to a cap, D&A at constant intensity, maintenance capex at a stated intensity of revenue, growth reinvestment = ΔNOPAT ÷ incremental ROIC, working capital at the modelled intensity); Gordon terminal; show terminal value as a share of EV and the implied exit multiple.
- **Maintenance capex**: express as an intensity (% of revenue) anchored to a base year and apply to revenue. Never chain it off the prior year's total capex — that compounds.
- **Taxes in the DCF**: one rule for all years. Under the modified style, tax = core EBITA × rate in every year (no shield on PPA or interest); do not link early years to the reported tax line.
- **WACC**: show the bottom-up build (cost of equity with its CAPM inputs and any company hurdle rate, after-tax cost of debt from traded bond yields, weights from market cap and net debt) and a single 'rate used' cell that everything references. Weights use the same share-count basis as the market cap.
- **Cross-check**: normalised final-year owner earnings (NOPAT + D&A ex PPA − maintenance capex) × warranted multiple (1 − g/ROIC)/(WACC − g), discounted to the valuation date; blend only if the user wants a blend.
- **Bridge**: core EV → add investments valued outside the core (associates at value, stakes carried at valuation) → less net debt → less debt-like future cash outflows (specific provisions, contingent consideration, restructuring, environmental) → add non-operating assets → less minorities → equity → per share → apply any class discount → upside.

## 5. Enterprise-value consistency (check every version)

Three EVs, each with its own purpose; never mix bases:

- *Market EV* (consolidated): market cap + net debt + minorities (+ convertible at face if treated as debt). Use for leverage and WACC weights. No associate deduction.
- *Multiple EV*: market EV less investments whose income is not in the denominator (associates at value); if the denominator excludes a consolidated unit's result, exclude 100% of that unit from EV (the group's stake and the partner's NCI). Label the basis on the row.
- *DCF EV*: core EV from the cash flows plus the same investments added back at value; the bridge must mirror the multiple basis so the implied multiple and the market multiple are comparable on the Summary.

## 6. Summary page (always built)

One landscape page: market snapshot; valuation per share by method with the headline first; current price and upside; implied vs market multiple on the same basis; financial summary (revenue, EBITA and margins, EPS, DPS, FCF, net debt, ROIC incl. and excl. goodwill, multiples, yields); key assumptions and bridge items with the numbers that drive them; one line each on any treatment a reader could question (lease treatment, convertible basis, what is excluded from core, maintenance-capex basis, terminal-value share). Print area set; check the rendered page fits.

## 6a. Performance Analysis tab (always built)

A ratio sheet so the user can sanity-check the forward assumptions against history. All formulas, nothing feeds the valuation; same year columns as the statements (history and forecast), averages on opening and closing balances. Sections:

- **Growth**: revenue and each segment/revenue line, key volume and price KPIs, gross profit, operating profit, core EBITA, net income, EPS, each opex line.
- **Unit economics / KPIs** specific to the business (price, volume, mix, penetration, revenue per user or unit).
- **Margins**: gross (and gross excluding any pass-through or low-margin line that distorts the headline), each opex line as % of revenue, opex ÷ the relevant revenue base (operating leverage), operating, core EBITA, SBC, net, effective tax rate, share of pre-tax profit from interest income.
- **Turnover and capital intensity**: revenue ÷ average invested capital (incl. and excl. goodwill), ÷ total assets, ÷ net PP&E; capex ÷ revenue; capex ÷ depreciation; D&A ÷ revenue; NWC ÷ revenue; receivable, inventory, payable days and other working-capital ratios.
- **Returns**: ROIC incl. and excl. goodwill (one tax basis for history and forecast), ROE, ROE excluding net cash, ROA.
- **Cash flow**: FCF, FCF margin, FCF ÷ net income, CFO ÷ EBITDA, unlevered FCF ÷ NOPAT.
- **Capital returns and balance sheet**: payout, DPS, net cash (per share, ÷ assets), equity ÷ assets, goodwill ÷ equity, leverage where relevant.
- **At the current price**: P/E, P/E ex cash, EV ÷ EBITA, FCF yield, shareholder yield by forecast year.
- **DCF period block**: revenue growth, margin, NOPAT growth, reinvestment rate, capex and depreciation intensity, FCF ÷ revenue across explicit and fade years.

When delivering, flag any forward ratio that breaks sharply from history (e.g. capex persistently far above depreciation, opex growing faster than revenue on a high-gross-margin business, returns rising because invested capital shrinks).

## 6b. Range of outcomes and Price slider (when asked for scenarios, what the price implies, or a range or slider chart)

In a model context, "slide" or "slider" means a chart inside the workbook. Ask before making a deck.

Both tabs are all formulas, linked to Assumptions, Income Statement, Balance Sheet and DCF. Their own inputs are blue cells on the tab.

**Basis**
- Operating earnings = core EBITA × (1 − tax). Interest is excluded, because surplus cash is valued separately.
- Surplus cash comes from the bridge.
- Annual return runs to the end of the last explicit year and is compared with the hurdle.
- Central-view inputs are proposals until the user signs them off. Say so on the tab.

**Range of outcomes tab**
- **(A) Inputs and links.**
- **(B) What the price implies,** at cash credits of 0%, 30%, 50% and 100%:
  - implied value of the operations;
  - P/E on operating earnings;
  - implied perpetual growth = cost of equity − 1 ÷ P/E;
  - the cash credit at which the operations trade at the central exit P/E.
- **(C) Scenarios, bear to bull.** Define each by how the debate's critical questions resolve: growth, exit P/E excluding cash, and cash credit. For each, show:
  - terminal-year earnings;
  - cash rolled forward (today's cash plus earnings × conversion, compounding at the after-tax yield);
  - equity value and value per share;
  - annual return, and whether it clears the hurdle;
  - "what has to be true".

  Include a market-implied row (flat earnings, today's multiple) and a probability-weighted row (probability of capital return × the returned and not-returned cases).
- **(D) Conviction the price requires:**
  - the probability of capital return needed for the hurdle;
  - the growth needed at the central P/E;
  - the exit P/E needed;
  - a row showing the return at each probability of capital return.
- **(E) Return grids:** growth × exit P/E, one grid per cash credit. Shade green where a cell clears the hurdle and red where it loses money.

**Price slider tab**
- **Bars.** One bar per critical question, plus overall return. Each bar runs from a bear end to a bull end, both blue inputs.
- **Markers:**
  - ▼ priced in = the setting at which today's price earns exactly the cost of equity, with the other questions held at the central view;
  - ■ needed = the setting that earns the hurdle;
  - ▲ the central view.
- **Table.** Above the bars, the same three values per question, plus "central view less priced in".
- **How to build it.** Make the bars from cells so they recalculate live and render in LibreOffice:
  - 41 narrow columns;
  - the track row holds index numbers hidden with format `;;;@`, coloured with an orange → grey → blue colour scale;
  - marker characters come from formulas comparing the column index with ROUND(position × 40);
  - the ■ marker is text in the track row (a conditional fill there loses to the colour scale);
  - value readouts sit to the right of each bar.
- **Overflow.** Formula cells block text overflow, so values never go inside the bar.
- **Check.** Render the tab to PDF and look at it before delivery.

## 7. Review pass before every delivery

Tie-out: history equals the reports (income statement, balance sheet, cash flow, D&A by class, equity roll, borrowings roll, NWC, share counts, dividends). Then the pitfall list:

1. EV bases mixed (associate or NCI in EV against an EBITA that excludes them, or vice versa).
2. Convertible counted in both share count and debt (bridge, WACC weights, EPS).
3. Maintenance capex chained off prior-year capex (compounds) instead of intensity × revenue.
4. Tax rule differs between explicit and extension years (shield on PPA/interest sneaking in via the reported tax line).
5. Dividend timing: this year's cash dividend is last year's DPS; record dates vs valuation date.
6. Basic vs diluted shares mixed (dividends and class splits on basic; valuation on diluted).
7. Cost of equity or WACC defined in two places; terminal growth not linked to the long-term growth input.
8. Working-capital cash lines double counting acquired balances or FX.
9. D&A summary vs cash-flow add-back residual unexplained.
10. Stale row references after inserting/deleting rows (text citations included) — rebuild from labels.
11. Summary labels describing a prior version's method or numbers; wrong number formats on the page.
12. Terminal value share and 'last explicit year' FCF: the base year must be settled (no one-off step in the final year).

Report each delivery as: what changed, value before/after and why, checks status. Do not recap the steps.

## 8. Working with the user's edits

The user reworks the file and uploads it. Each round: recalc the upload, diff it against the last delivered version (formulas and labels, sheet by sheet), rebase onto the upload, make only the requested changes plus any genuine errors found (say which), re-run checks and the pitfall list, deliver the next version number. Push back with reasons when a requested change breaks consistency, and offer the alternative. If the user asks a conceptual question, answer from the actual formulas in the file (inspect first), not from memory of an earlier version.

## 9. IR questions (on request)

Five, one topic each, about the financial statements and their presentation, each carrying the specific figure and note it refers to, ending in a question the company can actually answer. Good territory: items affecting comparability that recur, PPA deductibility and lives, cash-flow classification choices, debt-like items outside the company's net-debt definition, capitalised development costs, impairment-test inputs, effective tax rate drivers, pension cash vs charge. Drop anything already answered in the reports and anything that is a business question rather than a statements question.