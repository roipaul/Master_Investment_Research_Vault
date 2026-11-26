---
name: "policy-timeline"
description: "Build a dated policy/regulatory time series for any company or industry — actor, event, effect, source — aligned with the data series it moved: pricing rules, tariffs and export controls, reimbursement, subsidies, antitrust, labour, capital rules."
---

# Policy timeline

For many of the user's names the investment question is set by policy, and the sequence matters more than any single rule: who intervened, at what level, how fast the industry responded, and whether the effect held. Examples: China express pricing (反内卷), platform fee rules, VAT rebates, Medicare Advantage rates and PBM reform for managed care, semiconductor export controls and tariffs, alcohol excise and distribution law, bank capital and shareholder-return programmes (Basel, Korea Value-up, Japan TSE reforms), energy and emissions rules, antitrust cases against platforms.

This workflow builds the sequence as a table and lines it up with the data it moved. Use it inside `/full-primer` (Industry Overview) when the user asks for the regulatory history, or on its own to refresh a name.

## Inputs

- Company or industry, and the policy themes: pricing and fees, subsidies and tax, tariffs and export controls, reimbursement, antitrust and merger review, labour and safety, data and privacy, licensing, capital and governance rules, environment.
- Date range: usually the last two cycles, so the table shows whether a prior intervention faded.
- The data series to align: price, volume, share, margin, reimbursement rate, tariff rate, grant amounts, revenue per unit — whatever the policy was meant to move.

## Step 1 — Collect events

Search in the jurisdiction's language first, then English. Primary sources by jurisdiction: US — Federal Register, agency sites (CMS, FDA, FTC, DOJ, BIS, USTR, FERC, state regulators), Congress.gov; EU/UK — EUR-Lex, Commission decisions, legislation.gov.uk, CMA; Japan — e-Gov 法令, 官報, ministry and TSE/FSA releases; Korea — law.go.kr, FSC/FSS, KFTC; Taiwan — law.moj.gov.tw, FSC, MOEA; Hong Kong — gov.hk, HKEX, SFC; China — 国务院政策库, ministry and bureau sites, provincial and city notices; everywhere — the company's and peers' filings and calls, industry associations, courts.

For each event record:

| Field | Rule |
|---|---|
| Date | Day if available, else month. Separate issued, effective, draft and proposed |
| Actor | Named body at its level: supranational, central/federal, ministry/agency, state/province, city, court, industry association, the companies themselves |
| Event | What was issued, said or done; document title in the original language |
| Effect | What changed in the data and when; computed from the series where possible and marked [COMPUTED] |
| Source | Primary text if found; otherwise the best secondary, flagged "original not seen" |

Include the industry's own responses (price moves, M&A, capacity cuts, fee changes, lobbying, lawsuits) and the market's framing (broker notes, valuation percentile) as rows, labelled as such — the table should show cause and response, not only regulation.

Always compare the company's statutory filings (risk factors, regulation section) with its earnings-call language. If the filing is silent on a policy management credits or blames on calls, record the gap as a row or note.

## Step 2 — Align with the data

Build a second table: period | the data series | the events in that period. Then state the three or four features of the series in prose: how far up the chain the intervention came from, the lag from announcement to data, whether earlier interventions faded and over what period, who captured the effect (company, channel, customer, government) and what remains unresolved (draft laws, unpublished rules, court tests, elections).

Where a policy's beneficiary is ambiguous, estimate who captured it and mark the computation.

## Step 3 — Deliver

Markdown with the two tables and the prose, numbered sources. Pipe tables for pandoc; keep cells short and put long explanations in notes below the table. If it is going into a primer, write it to the industry part file and cite with the primer's `[n]` scheme. Otherwise save to the project as `<Industry or Company>_Policy_Timeline.md`.

## Standards

- Separate issued, effective and draft; separate central from local.
- Never summarise a rule from general knowledge without saying so; prefer the original text and quote under 15 words at most.
- Date every number, and say what [COMPUTED] figures are computed from.
- Plain English, no jargon left unexplained; original-language document titles kept alongside.