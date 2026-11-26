---
type: theme
name: ai-ad-monetization
tickers: [GOOGL, META, 0700-HK, APP, BABA, AMZN]
updated: 2026-10-07
data_through: Q2 2026 (quarter ended 2026-06-30)
status: imported
sources: [chat:https://claude.ai/chat/73788ad7-9fb0-4303-b6f0-41887b7e5e3e]
---

# How AI improves ad-ecosystem monetization (2026-10-07)

Companies covered: [[GOOGL]], Meta (META, no hub yet), [[0700-HK]] (Tencent), AppLovin (APP), Alibaba (BABA), [[AMZN]]. Related: [[ai-infrastructure-cycle]]; the Q3 2026 Search follow-up is in [[companies/GOOGL/earnings/FY2026-Q3|GOOGL FY2026-Q3]].

> **Imported** on 2026-11-26 from the Global Tech Project chat "AI in ad ecosystem monetization" (2026-10-07). Claude's replies are copied as written, with tool calls and closing offers of further work removed; Paul's requests are kept as the section headings. **Claude's framing, not Paul's view.**

## 1. "I am researching how AI helps better ad ecosystem monetization. Can you help me understand it end to end? And use Google, Meta, Tencent, and others as examples."

Here's the end-to-end picture. The short version: AI doesn't change the arithmetic of an ad business, it changes every coefficient in it, and the gains show up in the P&L as price-per-ad growth that outruns engagement growth.

### 1. The arithmetic AI is acting on

Ad revenue = impressions × ad load × price per impression. Price is set in an auction where each advertiser's effective bid ≈ their bid × the platform's predicted probability that *this* person converts. So the platform's prediction quality is the hidden variable in the price. Better prediction → the impression goes to the advertiser who values it most → higher clearing price *and* lower cost-per-result for that advertiser at the same time. That's why this is positive-sum: the gain comes from eliminating wasted impressions, not from charging more for the same thing.

AI pulls on six levers:

1. **More engagement (supply)** — recommendation models grow time spent, i.e. the impression base.
2. **Higher ad load without hurting engagement** — relevance is what lets you add ads.
3. **Higher value per impression** — retrieval + ranking models (the core).
4. **More advertisers and bigger budgets** — automation and generated creative collapse the cost of advertising, pulling in the long tail; higher ROAS makes existing advertisers spend more.
5. **Signal recovery** — modelling around iOS/privacy signal loss.
6. **New inventory** — ads inside AI answers and chat.

### 2. The pipeline, stage by stage

**Supply: organic recommendation.** Meta's feed/Reels ranking, YouTube Shorts, and Tencent's Video Accounts are the same model family as ad ranking. Video Accounts' time spent grew over 20% y/y in Q2 2026, helped by a new multi-variable content ranking system. Tencent is the clearest case of lever 2: management has said its ad load of 3–4% is dramatically below peers' mid-teens, and that it can keep outgrowing the industry by taking it higher — AI relevance is what makes that safe.

**Advertiser setup: automation.** The direction everywhere is "give us an objective and a credit card." Meta's Advantage+ campaigns hit a $75B annual revenue run rate in Q2 2026. Google's AI Max left beta in April 2026, with Dynamic Search Ads, auto-created assets and campaign-level broad match all auto-upgrading into it from September; Google says advertisers adopting AI Max or PMax see ~15% more conversions or value on Search at similar ROAS. Tencent's equivalent is AIM+, its automated campaign management solution that helps advertisers buy performant impressions. Alibaba's Quanzhantui plays the same role on Taobao, and management has tied customer-management revenue growth to rising take rates and increased penetration of full-site promotional tools.

**Creative: generative AI.** This is lever 4 — it removes the production bottleneck for small advertisers and gives the ranking model more variants to learn from. Zuckerberg said 9 million small businesses now use at least one Meta AI ad-creative tool, and the company is rolling out systems that connect campaign performance data to new ad variations. Google's AI Max combines search-term matching, text customization and final-URL expansion, with AI Brief letting advertisers give a plain-language briefing to guide generation.

**Retrieval → ranking → auction: the core.** Meta's stack is the most documented. Andromeda is the retrieval engine, built on NVIDIA Grace Hopper, with 10,000x the model complexity of what it replaced; Lattice consolidates what used to be separate prediction models into one large model predicting multiple outcomes at once, from click through to purchase probability; GEM is an LLM-scale foundation model that unifies ranking, so a conversion signal on Instagram Reels immediately improves predictions on Facebook Feed. Disclosed lift: more than 8% more ad clicks and 15.7% more Facebook conversions, driven by expanding the context from a person's organic and ads activity used to judge relevance. Tencent frames its growth the same way: enhancements to the AI-driven ad recommendation model that picks the ad for each user for each impression. At Google the win is query understanding: Gemini's reasoning decodes longer, more detailed queries that previously resisted monetization.

**Measurement and closed loop.** Prediction only works with conversion signal. With iOS 26 cutting browser-side pixel signal, server-side Conversions API has gone from nice-to-have to required at Meta. Tencent's structural edge is that the loop closes inside WeChat: Mini Games and Mini Shops advertise on Tencent-managed properties with integrated closed-loop marketing. Amazon's retail media is the same idea — purchase data is the conversion signal.

**New inventory: ads in AI answers.** Google's path is AI Max → AI Overviews/AI Mode; Gemini looks at the full AI Mode response plus the query to decide which ads are relevant, and AI Mode has crossed 1 billion monthly users with queries averaging three times the length of traditional ones. OpenAI began showing ads to US Free and Go users on 9 February 2026 and opened a self-serve Ads Manager on 5 May 2026, with retail advertisers able to upload a catalog and have ChatGPT generate ads per item. Google is already pushing past ads into transactions: Direct Offers in AI Mode, where Google's system picks the moment to serve an offer, and checkout inside AI Mode.

### 3. How it reads in the numbers

| | Q2 2026 datapoint | What it tells you |
|---|---|---|
| Meta | Ad revenue +27% to $59.4B; impressions +14%, price per ad +12% | Price growth ≈ value-per-impression gains; impressions ≈ engagement + load |
| Google | Search +17% to $63.3B, first easing after four quarters of acceleration (10%→12%→15%→17%→19%) | AI surfaces additive so far; the open question is monetization density per query |
| Tencent | Marketing services +22% to RMB43.6B as AI upgrades lifted advertising and pricing in Weixin | Fastest segment, off a low ad load — most runway |
| AppLovin | Revenue +52.8% to $1.92B but a narrow miss; AXON model improvement slowed in Q2 due to architecture upgrades | The pure-play: growth cadence = model-improvement cadence |

The cost side is the other half. Meta's capex was $31.1B in the quarter and operating margin fell to 31% from 43% (partly one-offs). Tencent said operating profit could have grown 19% without new-AI-product costs, and capex jumped 176%. AppLovin is spending roughly $0.10 of compute per incremental revenue dollar. So the right metric is incremental ad revenue per incremental inference dollar, not revenue growth alone.

### 4. Structural implications

- **Flywheel concentrates share.** Prediction quality scales with conversion data × compute × engagement. Walled gardens with first-party conversion loops (Meta, Google, Tencent, Amazon, Alibaba) widen the gap over open-web ad tech; even AppLovin, a strong engine, is dependent on others' signal.
- **Disintermediation.** Automation plus generated creative shrinks what agencies and tooling vendors do; Meta's Ads MCP connector has already prompted talk of disintermediation of parts of the journey.
- **Monetization density of AI answers is unproven.** If AI Overviews reduce click-through to ads while queries rise, the unit economics shift in ways the top line won't reveal until later. The counter is that AI Mode queries carry richer intent and can carry transactions, not just clicks.
- **Agents.** If a shopping agent buys on the user's behalf, ads give way to offers/commissions. That favours whoever owns the agent (Google, OpenAI, Tencent via WeChat) over whoever only owns inventory.

### 5. What to track

- Price per ad vs impressions (Meta), and whether price growth decelerates when impression growth from low-monetizing regions slows.
- Search growth vs AI Mode/AI Overview query mix at Google; any disclosure on ads per AI query.
- Tencent ad load on Video Accounts and the share of ad revenue from closed-loop/WeChat-internal advertisers.
- Advertiser count and share of spend through automated products (Advantage+, AI Max/PMax, AIM+, QZT).
- Disclosed lift stats each quarter — when a platform stops citing new lift numbers, the easy gains may be done (AppLovin's Q2 is the warning).
- Capex and inference cost per unit of ad revenue.

Sources:
- [Meta Q2 2026 results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/)
- [Adweek — Meta Q2 2026](https://www.adweek.com/?p=1954104)
- [Alphabet Q2 2026 results (8-K)](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm)
- [PPC Land — Google Search ads Q2 2026](https://ppc.land/google-search-ads-gain-17-to-63-3-billion-while-network-drops-1/)
- [Search Engine Journal — Search growth eases](https://searchenginejournal.com/google-search-revenue-growth-eases-after-a-year-of-acceleration/583181)
- [Tencent Q2 2026 results](https://en.prnasia.com/releases/apac/tencent-announces-2026-second-quarter-results-543788.shtml)
- [Reuters via The Star — Tencent Q2 2026](https://www.thestar.com.my/tech/tech-news/2026/08/12/tencent-q2-revenue-climbs-11-on-ai-driven-ad-gains-but-profit-falls-short)
- [WARC — Tencent ad load](https://www.warc.com/content/feed/tencent-looks-to-increase-ad-load/10080)
- [Darkroom — Meta Andromeda/GEM](https://www.darkroomagency.com/observatory/meta-andromeda)
- [Moburst — Andromeda, Lattice, GEM](https://www.moburst.com/blog-meta-advantage-andromeda-lattice-and-gem-explained/)
- [PPC Land — GML 2026 backstage](https://ppc.land/google-gml-backstage-product-leaders-on-gemini-ai-max-and-measurement/)
- [Segwise — ChatGPT ads 2026](https://segwise.ai/blog/chatgpt-ads-2026-guide.md)
- [Common Thread — AppLovin Q2 2026](https://commonthreadco.com/blogs/coachs-corner/applovin-q2-2026-earnings-ecommerce-advertisers)
- [Zacks — Alibaba QZT and take rates](https://www.zacks.com/stock/news/2870586/)

## 2. "perform the analysis on this metric" (incremental ad revenue per incremental inference dollar)

Here's the analysis. Nobody reports inference cost, so I built the metric three ways from disclosed lines, each a different definition of "the inference dollar": all-in segment cost, cost of revenue (infrastructure-heavy), and depreciation (capex becoming expense). All figures are Q2 2026 vs Q2 2025 increments.

### The numbers

| | Δ ad/segment revenue | Δ all-in segment cost | Δ cost of revenue | Δ D&A | Δ capex |
|---|---|---|---|---|---|
| **Meta** (FoA, $B) | +12.8 ad / +13.2 FoA | +11.2 ex one-offs → **1.1x** | +2.8 (+33%) → **4.5x** | +2.0 (+46%) → **6.4x** | +14.1 → 0.9x |
| **Google** (Services, $B) | +10.3 ad / +12.0 Services | +4.0 ex $1.5B legal → **3.0x** | n/a by segment | +2.1 group dep (+42%) → **4.9x** | +22.5 |
| **Tencent** (Mktg Services, RMB B) | +7.8 | +3.4 → **2.3x** (incr. GM 56% vs 57% avg) | same as all-in (segment GP) | MS D&A −0.25 (content amort. fell) | +33.7 group |
| **AppLovin** ($M) | +665 | +73 adj. EBITDA cost → **9x** (89% incr. margin) | mgmt rule: $0.10 compute per $1 → **10x** | n/a | not disclosed |

Reading: on the serving-cost definition (CoR or D&A), every platform earns $4–6 of ad revenue per incremental infrastructure dollar. That's the mechanism from last time — prediction quality is cheap to serve relative to the auction value it unlocks. On the all-in definition, dispersion is wide: AppLovin ~9x, Google ~3x, Tencent ~2.3x, Meta ~1.1x.

### What the dispersion tells you

**Meta's problem is R&D, not inference.** Cost of revenue grew $2.8B; R&D grew $8.7B (+67%, including +$2.8B stock comp). That's the superintelligence lab and training compute, charged to Family of Apps but not a cost of serving ads. Even on the conservative definition — only the price-per-ad gain ($6.4B of the $12.8B increment) counts as "AI quality" revenue — Meta earns 2.2x on cost of revenue. The ad engine's unit economics are intact; the P&L is carrying a bet that sits on top of it.

**Google is the cleanest positive.** Services incremental margin was 67% ex the legal accrual, above the 42% average margin, with Search revenue growing faster than Services cost. Caveat: group depreciation is shared with Cloud, which added $11.1B revenue at a 54% incremental margin, so the Services number is flattered by Cloud absorbing a growing share of the infrastructure.

**Tencent is the best disclosed and the most instructive.** Marketing Services incremental gross margin (56%) ≈ average (57%): AI added revenue at constant margin, no leverage but no dilution. But segment D&A fell — the AI cost arrived as "technical infrastructure operations costs ex depreciation," up 102% to RMB15.2B group-wide, i.e. leased/prepaid compute, not owned-server depreciation. And Tencent ring-fences the non-ad AI bet: new AI products cost RMB10.5B of operating profit this quarter vs ~RMB3B a year ago. That is the disclosure Meta doesn't give.

**AppLovin shows the metric's failure mode.** Compute kept scaling at $0.10 per incremental dollar, but model improvements stalled in Q2, revenue missed, and the stock fell 57%. The ratio is coincident, not predictive: it only tells you compute paid off *after* the model lift lands, and lift is lumpy.

### Where this goes

Capex-to-D&A is 4.9x at Meta, 6.3x at Google, 4.7x at Tencent. Depreciation will roughly double over 2–3 years regardless of what revenue does. Illustrative: if D&A doubles in eight quarters and revenue compounds at 17.5%, D&A/revenue goes 10.5% → 15% at Meta and 5.9% → 8.6% at Google — a 3–5 point margin headwind, absorbable at current growth, painful if growth halves. That's the real test of the metric: the denominator is locked in; the numerator has to keep showing up.

### Caveats on attribution

- Revenue increments include non-AI drivers: World Cup (Google/YouTube), 618 festival (Tencent, +14% q/q), FX (~1pt at Meta), engagement growth. Price-per-ad vs impressions is the best available split for Meta; Google and Tencent give none.
- Infrastructure is shared with organic recommendation, AI assistants (Meta AI, Gemini, Yuanbao) and Cloud. Only Tencent allocates D&A by segment.
- Server useful-life extensions in 2023–25 understate depreciation vs cash cost; the capex/D&A gap is the tell.
- Accounting path differs: Tencent's compute shows as opex (prepayments jumped RMB24.5B → 91.2B in non-current prepayments), Meta's includes third-party AI token costs and cloud rental. D&A alone understates everywhere.

### Scorecard to track each quarter

1. Δ ad revenue / Δ cost of revenue (serving ROI) — healthy above 3x
2. Segment incremental margin vs average margin — the leverage test
3. Capex / D&A — the committed future denominator
4. Price per ad vs impressions (Meta); Search growth vs AI Mode mix (Google); MS incremental GM and new-AI-products drag (Tencent)
5. Disclosed model-lift stats — if they stop appearing, assume the numerator is slowing before the ratio shows it

Sources:
- [Meta Q2 2026 results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/)
- [Alphabet Q2 2026 earnings release](https://s206.q4cdn.com/479360582/files/doc_financials/2026/q2/2026q2-alphabet-earnings-release.pdf)
- [Hudson Labs — Alphabet Q2 2026 depreciation and one-offs](https://www.hudson-labs.com/research/alphabet-q2-2026-earnings)
- [Tencent 2Q2026 results announcement (HKEX)](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0812/2026081200296.pdf)
- [AppLovin Q2 2026 call — compute rule](https://www.marketbeat.com/earnings/reports/2026-8-4-applovin-co-stock/)
- [Phillip Securities — AppLovin R&D and compute costs](https://www.poems.com.sg/market-journal/applovin-strong-ad-growth-rising-compute-costs-us-610-target/)

## Evidence log

- 2026-10-07 — Theme note created from the imported chat above (Claude's framing, not Paul's view).
- 2026-11-26 — Imported into the vault from the Global Tech Project.

