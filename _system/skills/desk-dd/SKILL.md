---
name: "desk-dd"
description: "After a thesis debate on any company, plan the due diligence and run the desk part: registries, insider dealings, subsidies, regulator originals, litigation, customer-complaint data, analyst-sheet review; report what changed per question."
---

# Desk due diligence

This is the step after `/thesis-debate`. The debate ends with verdicts, probabilities and a list of what would settle each question. This workflow turns that list into a ranked DD plan, runs the part that can be done from a desk, and reports what changed. The user does the people part himself (he has no expert network or corporate access), so the plan must tell him exactly who to find and what to ask.

The user is an experienced equity analyst running his own and his family's money, with coverage across the US, Europe, Japan, Korea, Taiwan, Hong Kong and China. Facts with sources, inferences labelled as inferences, no opinions dressed as findings.

## Knowledge base (start)

Run the `research-kb` skill's read step: pull the vault, read the hub `companies/<TICKER>/<TICKER>.md`, `Debate.md`, and the theme, policy, entity and person notes the hub links to — a check already done for a peer (a regulator's action, a subsidy ban) may answer a question here. If the vault is unreachable, use the Project copies and say so.

## Inputs

1. **The debate document** (`Debate.md` in the vault, `<Company>_<TICKER>_Thesis_Debate.*`, the `d*.md` files, or the project doc). Take the scorecard: each question with verdict, probability, confidence and "what would change the verdict". If there is no debate, run `/thesis-debate` first.
2. **The primer** for the fact base: legal structure, subsidiaries, related parties, grants, regulators, peers, auditors.
3. **Anything the user attaches**: an analyst working sheet, broker notes, IR correspondence.

## Step 1 — The DD plan (always delivered, even when only the desk part is run)

Rank everything by how much it could move the call. Lead with the two or three questions the debate said the call depends on, then verification gaps (governance, earnings base, accounting), then the rest.

Tag each item with a bucket:

- **Desk**: public sources, done in this skill.
- **People**: needs a conversation. For each person type — IR/CFO, former employees, customers, channel partners, suppliers, franchisees/agents/gig workers, competitors, regulators' advisers, academics, local brokers — give: what they can settle, three to five questions to ask, and how to find them without an expert network (LinkedIn or local equivalents by title, trade-press bylines, conference speaker lists, creators and communities via `/scuttlebutt`, trade fairs and site visits, online surveys).
- **Wait**: answered by a dated event (next results, a filing deadline, a ruling, a listing). Give the date.

## Step 2 — Desk checks

Run independent checks in parallel subagents. Each subagent gets the primer facts it needs (entity names in the local language and script, registration numbers, insider names, subsidiary list), is told to return facts with source URLs and no verdicts, and to report exactly what was blocked. Search in the company's home language first. Registry and court sites often show partial data in search snippets even when the page itself is blocked. Do not contact anyone, do not collect private personal data, do not work around a blocked site.

### Checks (always consider all; drop the ones the questions don't need)

| Check | What to pull |
|---|---|
| Corporate registry | Shareholders of key subsidiaries, VIEs, JVs and any partnership holders (and their partners); directors shared with insider-linked entities; charges and pledges; changes in the last 2–3 years |
| Insider dealings | Every officer/director/major-holder trade with date, size, price; reconcile against the ownership table; flag sales outside a buyback, trades with a related party, pledged shares, 10b5-1-type plans |
| Related parties and group structure | Related-party footnotes, exhibit lists of subsidiaries, outside investors in consolidated subsidiaries (preferred terms, redemption rights), management prepayments or loans |
| Subsidies, grants, tax incentives | Programmes still in force, amounts by year, receivables at year-end, any national review or ban; tax holidays and their expiry |
| Regulator originals | Primary text of every rule cited in the primer or debate; status of drafts; enforcement actions naming the company or peers since the primer |
| Peer events | Listed peers' filings, IPO applications, redemption triggers, pricing or capacity moves with read-across |
| Litigation and penalties | Material disputes, regulatory penalties, class actions (settled or pending), auditor changes, going-concern language, short-seller reports and the company's replies |
| Customer and complaint data | Complaint databases, review sites, app-store ratings and trend, traffic/download direction |
| Sell-side and data terminal | Through `research-portals`: broker estimates of undisclosed KPIs and how far apart they are, channel checks, accounting changes brokers flag, transcripts (search for the items in question), consensus, insider activity. Where estimates diverge, build an implied-KPI cross-check against an official benchmark |
| Unexplained line items | For any large "other" or one-off line: check the annual-report notes and the release wording in both languages, then reconstruct it from dated, sized known events (fines, rulings, disposals, fair-value moves). State what is left unexplained and turn it into an IR question |
| Rule changes behind a KPI move | When a reported line steps up or down, date every platform and regulatory rule change around it (official notices first, then merchant-side sources) and say whether the step is one-off (laps in four quarters) or structural |
| Analyst working sheet (if supplied) | (a) reconcile every historical line to filings; list errors with cell references; (b) extract data not in filings and ask where it came from; (c) check annual columns equal the sum of quarters and forecasts are linked; (d) compare the forecast with the debate's bull case and say if it is beyond it |

### Where to look, by jurisdiction

| Jurisdiction | Registry | Insider dealings | Regulator / law | Courts & penalties | Complaints |
|---|---|---|---|---|---|
| US | State Secretary of State; Exhibit 21; OpenCorporates | EDGAR Forms 3/4/144, 13D/13G | Federal Register, agency sites (SEC, FTC, DOJ, CMS, FDA, FCC, CFPB, state AGs) | PACER/CourtListener, class-action trackers, Subsidy Tracker (Good Jobs First) | CFPB database, BBB, Trustpilot, app stores |
| UK / EU | Companies House; national registers; OpenCorporates | RNS/PDMR notifications; national regulator registers | legislation.gov.uk, EUR-Lex, EU state-aid register, national gazettes | BAILII, national court portals | Trustpilot, national consumer bodies |
| Japan | 法人番号 / 登記情報; EDINET exhibits | EDINET 大量保有報告書; TSE timely disclosure | e-Gov 法令, METI/MHLW/FSA sites, 官報 | 裁判所 判例検索 | 国民生活センター, 価格.com reviews |
| Korea | DART 사업보고서 계열회사; 등기 | DART 임원·주요주주 소유상황보고서, 5% 보고 | law.go.kr, FSC/FSS, KFTC | 대법원 종합법률정보 | 공정위, 소비자원 |
| Taiwan | 商工登記公示; MOPS 關係企業 | MOPS 內部人持股轉讓/持股變動 | law.moj.gov.tw, FSC, MOEA | 司法院 裁判書查詢 | 消基會, PTT/Mobile01 |
| Hong Kong | Companies Registry (ICRIS) | HKEX Disclosure of Interests | HKEX rules, SFC enforcement, gov.hk | Judiciary judgments | Consumer Council |
| China | 企查查 / 天眼查 / 爱企查 / 启信宝; 国家企业信用信息公示系统 | 20-F ownership tables + EDGAR for ADRs; 深沪交易所 董监高 for A-shares | 国务院政策库, ministry sites (交通运输部, 国家邮政局, 财政部, 市场监管总局…), local fiscal notices (财政奖励, 税收返还) | 裁判文书网, 信用中国, 处罚公示 | 黑猫投诉, 12315, app-store review mirrors, 雪球 (Xueqiu) investor and merchant posts |
| Other | OpenCorporates; local registrar | Local exchange disclosure | Local gazette | Local court portal | Local consumer body |

## Step 3 — Synthesis

Write `companies/<TICKER>/DD.md` (document frontmatter: `type: document`, `doc: dd`, `tickers`, `updated`, `data_through`, `sources: [skill:desk-dd]`):

1. **What changed** — numbered findings, most material first. Each: fact, source, effect on the number or the question. Mark inferences explicitly. Link the first mention of each theme, policy, entity and person with `[[...]]`.
2. **Analyst working sheet** (if any) — incremental data, errors, forecast assessment.
3. **Effect on the debate** — one line per affected question: old probability → new and why; then whether the overall call (Supported / Not supported / Inconclusive) and the price check (Reachable / Stretch / Unlikely) change. Probabilities move only on new evidence; otherwise say "unchanged".
4. **Still blocked or unknown** — what could not be reached and the best alternative route.
5. **People plan** — the People and Wait items from Step 1.
6. **IR questions** — three to five, one topic each. Each carries the figure and the filing note it refers to and ends in a question the company can answer, for example a reclassification, an unexplained loss, or how a portfolio is split.

## Knowledge base (end)

1. Update the hub: `updated`, the **Latest** line, the critical-questions table (new probabilities, dated), and a dated `## Log` line.
2. Create or append to policy notes for every regulator original retrieved (`policies/`, from `_templates/policy.md`, with `original_seen` set correctly), and to entity notes for peers checked. Append dated read-across lines to the theme notes touched (`## Evidence log`, `[[TICKER]]`).
3. Commit and push per `research-kb` (message `<TICKER>: desk-dd <date> — <one line>`); also `project_write` the findings to the Project while it is still in use.
4. Send working files, and give the user the three or four findings that matter in the reply.

## Standards

- Facts, management claims and inferences labelled as such; every finding carries a URL or filing reference.
- Quotes under 15 words, one per source; paraphrase otherwise.
- No price target, no buy/sell language.