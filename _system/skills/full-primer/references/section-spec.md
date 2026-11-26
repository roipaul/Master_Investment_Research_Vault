# Full Primer — Section Specification

This is the section-by-section contract. Each entry says what the section must answer, what table(s) it typically carries, and what a weak version looks like. Sub-section names in **bold** are the run-in headings to use inside each numbered section.

Write each Part to its own markdown file. Use `#` for the Part title (e.g. `# Company Overview`), `##` for the numbered sub-sections (`## Customers and Distribution`), and `###` or bold run-ins for the sub-sub-sections. The build script numbers `#` and `##` headings.

---

## Part 1 — Company Overview (file: part1_company.md)

Single `##` section titled `<Company Name> (<TICKER>) — Company Primer`. Then these run-in sub-sections in this order:

### Company Overview (2–3 paragraphs)
- What the company is in one sentence a layperson understands, then the listing (exchange, ticker), HQ, CEO, and any announced succession.
- Scale facts: revenue, employees, countries, customers/members/stores — whichever 3–4 numbers define the business.
- The core model in one paragraph (e.g. "asset-light franchisor", "wholesale distributor between manufacturers and 125,000 trade pros", "per-seat SaaS with product-led growth").
- Current strategic framing in the company's own words if it has one ("Hungry for MORE", "Focus40", "Design and Make Platform").

### Segments
- Reportable segments as the company reports them, each with: what it sells, to whom, revenue and share of total for the latest FY, and one distinguishing economic feature (margin profile, cyclicality, growth).
- A summary table: Segment | FY revenue | % of total | (margin if disclosed).
- If one reportable segment: say so, then describe the internal cuts management discusses (product families, customer groups, geographies).
- Flag any segment realignments in the last two years and their effective dates — these break historical comparisons in Part 4.

### How the Business Model Works (3–5 pages — the most important sub-section)
Answer, in prose with sub-headings:
1. **Where revenue comes from, mechanically.** Pricing unit (per seat, per unit case, royalty %, take rate, premium PMPM, final value fee), who pays, when revenue is recognised. Distinguish gross vs. net presentation where it matters (PBM pass-through, 1P vs 3P, agency vs principal).
2. **Cost structure and unit economics.** What the margin is made of; which costs are variable; what scale does to margin; rebates, pass-throughs, mix effects.
3. **The demand engine.** What drives volume across a cycle — installed base, replacement cycles, enrolment, capex cycles, consumption. Separate recurring/non-discretionary from cyclical/discretionary and quantify the split if the company does.
4. **The flywheel or reinforcing structure**, if one exists — how services, data, logistics, distribution or product breadth feed each other. Explain the mechanism, not the marketing.
5. **Go-to-market / transaction model** — direct, channel, franchise, agency; any model transition under way and its accounting effects.
6. **Key operating metrics** management uses (ARR, unit cases, MEUs, NIMAL, same-store sales) with definitions.
7. **Funding or capital model** if non-standard (credit book funding, securitisations, franchisee profit share, bottler equity stakes).
Weak version: a list of products with adjectives. Strong version: a reader could sketch the P&L drivers from memory.

### Products and Services
- Product families with a short explanation of what each does and who uses it. A table (Product family | Key products | Function / demand driver | Margin profile if known) is standard.
- Product-mix percentages where disclosed.
- New products and their traction numbers (adoption %, revenue, users) — dated.
- Digital/AI/platform offerings and how they are monetised.

### Brand Portfolio
- Brand → category/target-market table. For B2B single-brand companies, say so in a paragraph and note series/model naming conventions instead.
- Acquired brands and what they became.

### Corporate History
- Founding, IPO, and 3–6 **structurally consequential** events: acquisitions that created a segment, divestitures, model transitions (perpetual→subscription, refranchising), failed deals, leadership transitions. Dates and deal sizes.
- Do not write a year-by-year chronology. If the sources are thin on history, say so.

---

## Part 2 — Company Logistics (file: part2_logistics.md)

### 2.1 Customers and Distribution
**Who Are the Customers**
- Customer types, concentration (any >10% customer; largest named customers), customer counts, spend tiers, end-market mix table (End market | % of revenue | YoY growth), member/user counts, retention or NDR.
- Named customers or marquee wins where disclosed.
**Distribution Channels**
- Every channel with its share if known: direct sales, branches/stores, distributors/resellers (count, largest distributor's share), digital/e-commerce % of sales, aggregators, franchise, brokers.
- Channel shifts under way and incentives changing behaviour (partner compensation, new transaction model).
- Table of channel KPIs where available.

### 2.2 Suppliers and Procurement
- Named key suppliers with share of COGS or purchases; supplier concentration risk.
- Key commodity/input exposures (metals, resin, sweeteners, cloud hosting, drug costs, provider networks) with any disclosed cost shares or sensitivities.
- Procurement model: centralised purchasing, rebates, vertical integration, private label, long-term contracts (with expiry dates), hedging.
- Tariff / trade exposure and pass-through behaviour.
- For software: hosting provider and purchase commitments; royalty/third-party model costs.
- For insurers: provider contracting, PBM delegation, value-based arrangements.
- If not disclosed: say "No commodity-level procurement detail is disclosed" and stop.

### 2.3 Geographic Distribution
- Revenue by geography table (Region | FY revenue | % | YoY) for 2–3 years; profit or margin by geography if disclosed, otherwise the best proxy (FX sensitivity, capex by region, location count) with the caveat that it is a proxy.
- Concentration (e.g. four Sunbelt states = 54%; mainland China = 94%).
- Regional dynamics: which regions are growing/shrinking and why; FX exposures by currency.
- Refranchising, exits, or new-market entries that change the map.

---

## Part 3 — Industry Overview (file: part3_industry.md)

Write this so it would make sense to a reader who has never heard of the company. Use the company only as an example.

### 3.1 Industry Overview
**Introduction** — what the industry is, what it sells, to whom, and why it exists economically (2–3 paragraphs).
**Industry Size** — a table of 2–4 third-party estimates (Estimate | Year | Source | Scope/definition). When they disagree, explain the scope difference. Include the company's own TAM framing separately and label it as vendor-sourced. Give growth rate (CAGR) with source.
**How the Industry Works** — value chain, business models in use (and their margin implications), channels, pricing models, platform/ecosystem effects, contract structures.
**Demand Drivers and Cyclicality** — what demand correlates with (industrial production, housing, enrolment, consumer confidence, capex cycles), seasonality, the recent cycle in a short table or paragraph (last 3–4 years), regulatory environment (a table if there are many regimes).
**Key Industry Trends and Developments** — 4–7 trends, each a titled paragraph: technology shifts (AI, cloud, electrification), consolidation, localisation/tariffs, regulation, pricing-model change, new entrants. Each with a sourced fact.

### 3.2 Industry Competitive Dynamics
**Competitive Landscape** — the players by tier, a competitor table (Company | Positioning / revenue / notes), market shares with source and year for each (national, regional, segment-level as available). State plainly when no reliable comparable share data exists and what the figures shown actually measure.
**Level of Competitive Intensity** — high/moderate/low and *why*, by segment; how it varies with the cycle; where price competition bites and where it doesn't; barriers to entry vs. barriers to scale; recent evidence (closures, price wars, new entrants).
**Basis of Competition** — a table or titled bullets: Dimension | What it means in this industry | Who it favours. Typical dimensions: price, breadth/assortment, service/lead time, technology/platform, brand, scale/purchasing, quality/reliability, regulatory execution, integration.
**Structural Dynamics and Outlook** — consolidation, scale advantages compounding, disruption risks (AI, cross-border entrants, regulation), and the "last territory" or contested segments. End with a 2–3 sentence summary.

---

## Part 4 — Financial Overview (file: part4_financial.md)

Most table-dense part. Every table header states the unit and currency. Every number carries a citation. Define company-specific terms (adjusted EPS, FCF, ARR, MEU, NIMAL, DSR, MCR) before using them — a short definitions list at the top is fine.

### 4.1 KPI Trends
**Top-line KPIs** — revenue by FY (3 years) and by quarter (last 4–8), YoY growth reported and organic/FX-neutral/constant-currency; decomposition into price / volume / mix / FX / M&A where management gives it.
**Segment and product KPIs** — segment revenue and growth table; product-category growth; geography growth by quarter; operating metrics specific to the business (membership, unit cases, scripts, GMV/TPV, items sold, subscriptions, RPO/billings, same-store sales, store counts, digital penetration, utilisation, backlog, order index).
**Profitability KPIs** — gross margin, operating margin, adjusted margin by quarter and FY in tables; drivers of each move named; segment margins; the metric that matters most for the model (MLR for insurers, NIMAL for lenders, incremental margin for distributors, non-GAAP operating margin for software).
**Working capital / balance-sheet KPIs** — inventory days, DSO, DCP, leverage ratio, ROIC as relevant.
For each KPI table, a paragraph of drivers follows: what moved, why, and whether it is structural or timing (rebate true-ups, selling days, hurricanes, deferred tax payments, one-time gains).

### 4.2 Financial Highlights
- Income statement summary table (3 FYs + latest quarter): revenue, gross profit, opex lines, operating income, net income, EPS, adjusted figures.
- GAAP vs. non-GAAP reconciliation items, explicitly enumerated (SBC, impairments, termination fees, restructuring, remeasurements, cyber costs).
- Balance sheet table (cash, debt, net debt, equity, leverage) and cash-flow table (CFO, capex, FCF, FCF conversion).
- A paragraph each on the two or three biggest things the reader must understand about the financials (e.g. "SBC is 129% of revenue", "revenue will decline in 2026 by design", "operating cash flow was depressed by a $6bn IRS deposit").

### 4.3 Capital Allocation
- Tables for buybacks (by year: shares, $ amount, average price, authorisation remaining), dividends (per share, total, growth, payout), capex (by year, % of sales, major projects), acquisitions/divestitures (deal, date, size, what it added).
- Debt activity: issuances, repayments, refinancings, facilities, maturities, ratings.
- Management's stated allocation framework (priorities, leverage target, payout target) and whether actual behaviour matches it.

### 4.4 Long-Term Guidance & Outlook
- Current-year guidance table (Metric | Guidance | Prior guidance | Date given/revised | Latest actual) — include underlying assumptions management states (volume, pricing, tax rate, share count, FX, M&A).
- Segment-level guidance and margin trajectories.
- Long-term algorithm table (revenue growth, margin, EPS growth, FCF conversion, leverage target, capital-return policy) with the date it was set/reaffirmed.
- Strategic investment programs and transformation plans with dollar sizes and timelines.
- Leadership transitions.
- **Key risks to the outlook** — 4–6 titled paragraphs drawn from what the sources actually say (rate notices, subsidy expiry, cycle duration, model transition headwinds), each with the sourced fact behind it. Not a generic risk list.

---

## Sources (file: sources.md)

One numbered line per source, in first-use order, with the document type and date:
```
1. Company X, Q1 2026 Earnings Call, Apr 23, 2026 — conference call transcript
2. X 8-K EX-99.1 — earnings release, 2026-04-23
3. X 10-K FY2025 — annual report, filed 2026-02-19
4. Grand View Research (2024) — web research, global market sizing
```
Group nothing; the order is citation order. Web research entries name the publisher and year.

---

## Table conventions

- Markdown pipe tables. First column is the label; numeric columns right-aligned by content convention (the build script does not align, so keep columns consistent).
- Units in the header: `Revenue ($M)`, `Net Sales (¥B)`, `Share of Sales (%)`.
- Use `—` for not available, never a blank.
- Put the citation list for a table either in the header row labels or as an italic *Sources: [1][4]* line immediately below the table, as the samples do.
- Keep tables ≤ 7 columns so they render in portrait.
