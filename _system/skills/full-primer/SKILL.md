---
name: "full-primer"
description: "Generate a full, cited company primer (Company Overview → Company Logistics → Industry Overview → Financial Overview) for a stock ticker, delivered as a numbered .docx and PDF of roughly 35–50 pages. Use this whenever the user runs /full-primer on a ticker or company name, asks for a \"primer\", \"full primer\", \"company primer\", \"top-of-funnel read\", \"initial read\", or wants a thorough description of a business, its customers/suppliers/geographies, its industry structure and competitive dynamics, and its financials and guidance — even if they only name the ticker. Not for pitch write-ups with a thesis and return drivers (those are a separate format), earnings flashes, models, or valuation work."
---

# Full Primer

A full primer is a **descriptive, pre-judgment research document**: it explains what the company is, how it makes money, who it sells to and buys from, how the industry works and competes, and what the numbers and guidance say. It deliberately contains **no investment thesis, no valuation, no recommendation** — it is the fact base an analyst reads before forming a view. Length is a feature: the target is ~35–50 pages, written in full prose paragraphs with tables where numbers are compared.

The user is an experienced equity analyst. Write for that reader: plain English, no filler, no hedging boilerplate, no "it is worth noting" padding, and every specific figure or claim carries a bracketed citation to a numbered source.

## Primary filings come first (standing rule)

Every company fact in the primer — revenue, segment and regional splits, customers, orders and backlog, margins, balance sheet, cash flow, capex, dividends, buybacks, share count, ownership, guidance, management — must come from the company's **primary filings and official disclosures**, not from press articles, broker reports, data aggregators or AI summaries. Secondary sources are allowed only for things the company does not itself say: industry size and structure, competitor figures (from the competitors' own filings where possible), market shares, and analyst consensus. Label every such figure as secondary in the text or the citation.

Where to find the primary documents, by market:

- **Korea:** DART (dart.fss.or.kr) business reports (사업보고서), half-year and quarterly reports, and the earnings-release and IR filings. The OpenDART API (opendart.fss.or.kr) needs the user's key, which the user supplies in the session; never write the key into any file, document or source list. Use the corpCode list to find the company code, then the list, document and financial-statement endpoints.
- **US:** SEC EDGAR 10-K, 10-Q, 8-K, proxy statement.
- **Japan:** EDINET securities reports and TDnet releases.
- **Hong Kong:** HKEXnews annual and interim reports and announcements.
- **Taiwan:** MOPS annual reports and material information.
- **China (A-shares):** CNINFO (static.cninfo.com.cn) full annual, half-year and quarterly reports; report summaries (摘要) are also printed in China Securities Journal (epaper.cs.com.cn). Read the full report, not only the summary: product margins, top customers and suppliers, related-party trades and subsidiaries are only in the full text.
- **Elsewhere:** the exchange or regulator filing system, then the company's IR site.

Access rules. The shell often cannot reach regulator sites because of the network allowlist, while the web-fetch tool often can, so try the fetch tool and then the shell before concluding a source is unreachable. Never write that a filing was "not accessible" unless you actually tried both. Before searching, check whether the user has staged filings for this name (uploads, or his dated Screens folder via the device bridge) and use those first. Long filings come back in parts from the fetch tool: keep reading with the offset it reports until the sections needed (business, customers and suppliers, segments, related parties, notes) are covered, rather than stopping at the first part. If the latest quarterly reports cannot be retrieved, ask the user for them before drafting the Financial Overview from broker notes. If a primary filing cannot be retrieved, say so in the reply and in a short "Source limitations" note at the top of the document, state what was tried and what failed, name the figures that therefore rest on secondary sources, and ask the user to supply the file or the key. Do not silently fall back to press summaries.

## Workflow

1. **Resolve the ticker.** Confirm company name, listing exchange, fiscal-year end, reporting currency, and whether it's a US filer (10-K/10-Q/8-K) or foreign (annual report, interim reports, 20-F, TSE/HKEX/TWSE/DART filings). Non-US names get the same report; just note FY conventions (e.g. "FY2025 = year ended March 2025") the first time they appear.

2. **Collect sources before writing anything.** First, if the `read-across` skill and the research vault are available, run `/read-across TICKER`: it writes `Prior.md`, the pack of what earlier research on adjacent companies already established (see "Using earlier research" below). Then follow the primary-filings rule above. Gather, in this priority order:
   - Latest annual report / 10-K / business report (business, risk factors, segments, customers, suppliers, geography, MD&A, notes).
   - Last 4–6 quarterly or half-year reports, earnings releases, presentations and call transcripts (KPI trends, guidance, management colour).
   - Investor day / analyst day materials and sell-side conference transcripts if available (long-term targets, strategy).
   - Company IR site: product pages, history, segment descriptions.
   - Industry sources: 2–4 third-party market-size estimates (name the research firm and year), trade press, regulator or association data, competitor filings for market share.
   
   Use WebSearch/WebFetch for all of this; regulator filing systems and IR sites are the primary feeds. If a Daloopa connector or similar fundamentals MCP is available in the session, use it for the KPI time series in Part 4 — it is cleaner than scraping tables from releases, but reconcile it to the filing. Keep a running numbered source list as you go (see Citations below). Expect 15–30 sources. Do not start drafting until the annual report and at least the last four quarters are in hand; the Financial Overview depends on quarterly granularity.

3. **Write the four parts in order**, each to its own markdown file in the working directory (`part1_company.md` … `part4_financial.md`). Read `references/section-spec.md` before writing — it specifies every section and sub-section, what each must answer, and the table patterns the samples use. Write part by part rather than in one pass: each part is 8–15 pages and benefits from a fresh look at the sources.

4. **Assemble** with `python3 scripts/build_primer.py --ticker TICKER --company "Company Name" --out primer_dir/`. It concatenates the parts, numbers sections (1, 1.1, 2.1 …), prepends a table of contents, appends the source list, and produces `<Company>_<TICKER>_Primer_Full.docx` and `.pdf`. Open the PDF (Read a few pages) to confirm tables rendered and the TOC resolved before sending.

5. **Check the work** before delivery: (a) every number in a table has a citation; (b) segment revenue sums roughly to consolidated revenue; (c) the most recent quarter referenced is actually the latest reported (search "TICKER earnings" for the current date to confirm); (d) no sentence recommends, values, or opines on the stock; (e) every company figure traces to a primary filing, and any figure that rests on a secondary source is labelled as such and listed in the source-limitations note; (f) every KPI carries its scope, and every comparison is like-for-like in product, geography and definition, with the accounting policies that move credit or impairment metrics (write-off thresholds, staging rules, restrictions on selling bad loans) noted where they apply. Then send both files with `SendUserFile`.

## Report structure

Always this exact skeleton. Headings are the numbered sections; sub-headings inside each are bold run-ins or H3s as `references/section-spec.md` describes.

```
1. Company Overview
   1.1 <Company> (<TICKER>) — Company Primer
       Company Overview · Segments · How the Business Model Works ·
       Products and Services · Brand Portfolio · Corporate History
2. Company Logistics
   2.1 Customers and Distribution
   2.2 Suppliers and Procurement
   2.3 Geographic Distribution
3. Industry Overview
   3.1 Industry Overview
   3.2 Industry Competitive Dynamics
4. Financial Overview
   4.1 KPI Trends
   4.2 Financial Highlights
   4.3 Capital Allocation
   4.4 Long-Term Guidance & Outlook
   4.5 Read-across from Earlier Research   (only when a pack exists)
Sources
```

## Using earlier research (the read-across pack)

When `Prior.md` exists, the primer builds on it. When it does not, or it says nothing adjacent is on file, write the primer as before and leave out section 4.5.

- **Use sections 2 to 5 of the pack only**: facts to reuse, benchmarks, inherited open questions and items to test. Never use section 6, the hypotheses from earlier judgments. The primer stays descriptive.
- **Weave the learnings into Part 3** (industry structure, competitor table, basis of competition) and into the customers and suppliers sections of Part 2 where an adjacent company is the customer or supplier. Cite each as our own earlier work with its date, for example "[n] Pool Corp primer, vault, data through Q3 2026", and keep its original source in the source list.
- **The primary-filings rule is unchanged.** A learning from another company's primer may describe that company or the industry. Every fact about this company still comes from its own filings.
- **Respect the dates.** A learning the pack marks "as of" is written with that date and is not stated as current unless a current source confirms it.
- **Close with section 4.5**, written at the end of `part4_financial.md` so the build script numbers it. Three short lists: what this company's filings **confirmed** from earlier work, what they **contradicted** (with both figures and both sources), and what remains **open**. Add the benchmark table from the pack with this company's own figures beside it.
- **After delivery**, run `/read-across TICKER file` so that what this primer established is filed for the next company.

## What makes these primers good (the standard to hit)

- **Mechanism over description.** "How the Business Model Works" is the heart of Part 1: walk through where a dollar of revenue comes from, what the unit economics are, what the recurring vs. cyclical pieces are, and how the pieces reinforce each other (e.g. POOL's installed-base → maintenance demand → private label → POOL360 loop; MELI's marketplace → payments → credit → ads flywheel). Explain *why* the structure matters, not just that it exists.
- **A money map before anything else.** In "How the Business Model Works", include a table with one row per product (not per segment): who pays, what the fee or price is and what it depends on (category, payment method, tenor), which reported segment books the revenue, and which segment carries the matching costs, funding, credit losses and capital. Build it from the company's own tariff or pricing pages and the segment note, not from summaries. Where revenue and the capital or risk behind it sit in different segments (a marketplace fee that exists only because a bank subsidiary funds the instalment), say so: segment margins will flatter one side and depress the other.
- **Economic profile per business.** One short table: asset-light or asset-heavy, what it consumes (capital, inventory, deposits, capex), which risk it carries (price, volume, credit, rates, regulation), and which way it is moving (an asset-light marketplace adding own retail and stores is becoming heavier).
- **Scope on every number.** Every KPI states its scope in the table header or a column: geography (home market vs consolidated incl. acquisitions), currency basis (reported vs constant currency), level (segment vs group) and period. When the company changes how a metric is calculated or what it covers, show both versions. Never compare a figure to a benchmark of a different scope (unsecured consumer NPLs vs a whole banking sector incl. corporate loans).
- **Numbers in tables, drivers in prose.** Every part uses tables for comparisons (segment mix, geography, KPI by quarter, guidance vs. actual) and prose to explain what moved them. A table never stands alone — the paragraph after it says what the reader should take from it.
- **Quarterly granularity in Part 4.** KPI tables run the last 4–8 quarters plus 2–3 fiscal years, so the reader can see inflections. Include price/volume/mix decomposition, segment margins, the one-off items that distort GAAP, and the reconciliation points management uses (adjusted EPS, FCF definitions).
- **Guidance stated as management stated it**, with the date and the prior guidance it replaced, and the long-term algorithm (growth targets, margin targets, capital-return policy) as a table.
- **Calibrated scepticism.** Where management framing is self-serving (e.g. "competitors' closures prove our model"), say so in a sentence. Where market-size estimates from different research firms diverge, show them side by side and explain the scope difference rather than picking one. Where data is not disclosed, say "not disclosed" rather than estimating.
- **Industry section stands on its own.** A reader who knows nothing about the sector should finish Part 3 understanding how the industry works, who the players are with market shares (sourced, dated), what the basis of competition is, where competitive intensity is high vs. low, and what the structural trends are. Use the company as the example, not the subject.

## Citations

Inline numeric citations in square brackets after the claim: `[3]`, or `[3][7]` for several. Number sources in order of first use and list them at the end in this form (the build script renders the list):

```
3. Pool Corporation, Q1 2026 Earnings Call, Apr 23, 2026 — conference call transcript
7. POOL 10-K FY2025 — annual report (filed 2026-02-19)
12. Grand View Research (2024) — web research, global pneumatic actuators market
```

For regulator filings cite the document name, period and filing identifier (e.g. DART receipt number rcept_no, EDGAR accession number). Keep a `sources.md` file alongside the part files with one numbered line per source; the build script appends it. Third-party market data gets the firm and year in the citation text itself (e.g. "[Source: Circana, 2025]") when the number is contested, as the samples do.

## Length and tone calibration

| Part | Target pages | Notes |
|---|---|---|
| 1 Company Overview | 12–18 | Business model sub-section alone is 3–5 pages |
| 2 Company Logistics | 5–8 | Tables for customer tiers, end-market mix, geography |
| 3 Industry Overview | 8–12 | Market-size table with sources; competitor table |
| 4 Financial Overview | 12–20 | Most table-dense; quarterly KPI tables |

Prose is formal but direct. No bullet-point-only sections — bullets appear inside prose sections for lists of products or drivers, never as the whole section. Avoid "genuinely", "honestly", "straightforward". Do not hedge every sentence; one well-placed caveat beats five.

## Edge cases

- **Single-segment companies** (SMC, Fastenal, Figma): still write the Segments section — explain that it is one reportable segment and what internal breakdowns (product mix, geography, channel) the company gives instead.
- **Pre-IPO or recently listed** (Figma): corporate history covers the IPO mechanics; SBC and dual-trigger RSU distortions get their own paragraph in Part 4.
- **Franchise / asset-light models** (DPZ, KO): make the distinction between system-wide sales and reported revenue explicit early and carry it through Part 4.
- **Insurers / financials** (ELV, UNH): the "unit economics" are MLR/benefit ratios, days claims payable, reserve development, risk adjustment; Part 2 "suppliers" are providers and PBMs.
- **Foreign filers**: cite the annual securities report / interim report / DART business report; translate figures into the reporting currency with units stated in every table header (¥B, NT$ thousands, R$M, KRW bn).
- **Thin disclosure** (e.g. no customer names, no segment profit): say so explicitly in the relevant sub-section, and use the nearest proxy the company does disclose (FX sensitivity as a proxy for regional profit, capex by region, etc.).