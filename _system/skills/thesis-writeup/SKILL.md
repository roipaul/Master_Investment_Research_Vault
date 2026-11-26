---
name: "thesis-writeup"
description: "Write the compact investment thesis (5–8 pages, the user's pitch order) from a primer, thesis debate, DD findings and any model: thesis, business, management, opportunity, return drivers with scenarios, open questions, risks, tracking, falsifiers."
---

# Thesis write-up

The primer describes, the debate judges, the DD verifies. This document is the destination: the thesis as the user would defend it, short enough to re-read before every results day and to turn into a pitch. It is written in his fixed pitch order, in plain English, and it states what the return depends on and what it does not.

The user is an experienced equity analyst running his own and his family's money. Verdict on the business first; valuation as a gap to close, never a price target.

## Knowledge base (start)

Run the `research-kb` skill's read step first: pull the vault, read `companies/<TICKER>/<TICKER>.md` (the hub), `Debate.md`, `VariantView.md`, `DD.md`, `Scuttlebutt.md` if present, and the theme and policy notes the hub links to, for read-across from other companies. If the vault is unreachable, read the equivalent docs from the claude.ai Project and say so.

## Inputs (use whatever exists; say what is missing)

1. **Full primer** — fact base, industry structure, Section 5 questions.
2. **Thesis debate** — scorecard with verdicts, probabilities, confidence; price check. Also the **variant-view frame and ledger**, if they exist: the priced-in table with positions, what the thesis rests on, how the return arrives, and each view's why-the-market-is-wrong block.
3. **Desk DD findings, scuttlebutt, policy timeline** — what changed since the debate, per question.
4. **Model or analyst sheet** — if a `/value-dcf-model` or scenario model exists, take the driver paths from it; otherwise build the scenario table in this skill.
5. **Price and share count**, dated and sourced, on the day of writing.

If there is no debate, say so and either run `/thesis-debate` or write the document with the open questions carrying the debate's role (no probabilities invented).

## Document structure (fixed order)

```
Header: company, ticker, date, data-through quarter, next results date, price
        and market cap with date, sources used, "(e)" convention for estimates.

1. Thesis
   One paragraph: what the business is, how the market prices it (the gap), what
   the business is doing (the compounding). Then the return in numbered parts:
   earnings compounding (growth × margin), the gap closing (what re-rates it and
   when), cash return. Then "What the thesis does NOT rely on" — the optionality
   and broker assumptions excluded. End with "the central judgment": the one or
   two risks the multiple must compensate for, and the bear/base/bull asymmetry
   in a sentence. Close with the action line: what would strengthen the case,
   what would break it, and the date the deciding evidence arrives. Refer to the
   Section 8 rows for thresholds instead of restating them. Use buy/add/cut
   wording only when the user has asked for a call.
2. Business description
   What it does and how it earns (revenue-line table: line, size, share, trend,
   mechanics, and which segment carries its funding, losses and capital; keep a
   table only if a later judgment depends on it); unit economics and cost structure; what drives it across cycles
   (volume, price, mix — with how it behaved in the last downturn); industry
   structure (fragmentation, consolidation in progress, supplier/platform
   concentration, policy); competitive advantages and their limits.
3. Management
   Execution record in crises and in the recent past; ownership, control and pay;
   points of concern (related-party dealings, disclosure quality, insider sales)
   with amounts, and a one-line judgment of what they add up to. Never dropped,
   even in a short version; include the controlling holders' other businesses
   that deal or compete with the company.
4. Current situation: what creates the opportunity
   Why the price is where it is — the few things that hit at once — and which of
   them are self-inflicted/temporary vs real; the facts that matter for value
   that did not deteriorate. Then four short items, taken from the
   variant-view frame and ledger: (a) what the price implies, beside sell-side
   consensus and the user's own numbers, with his position against each;
   (b) what the thesis rests on (near-term cash flows, duration, or a discount
   that should narrow), with the covered share; (c) why the market is wrong:
   the mechanism, the evidence for it, what ends it, and the strongest case
   that the market is right; (d) how the return arrives: the part the business
   pays with no change in the multiple, and the part that needs a re-rating,
   with the event and date.
5. Return drivers
   Driver table: driver | base assumption | evidence. Scenario table: bear/base/
   bull | key assumptions | earnings CAGR | terminal-year earnings | multiple |
   value | vs market cap (%). Cash credit (how much of balance-sheet cash to count
   and why). Runway (why the growth rate is sustainable for several years: pool,
   penetration, ceiling, what is out of reach).
6. Open questions, with materiality
   Table: question | why it matters | High/Medium/Low. Carry the debate's
   unresolved items and the DD's "still blocked" list.
7. Risks
   Numbered, ranked by impact, each with a sized effect where possible ("a 15%
   fee cut takes ~RMB0.7bn off operating profit").
8. What to track
   One table: judgment it tests | metric | reading that says right / wrong |
   when it shows. Cover operations, regulation, governance and industry, and
   name the next results date with what to look for. This table is the single
   home for thresholds; Sections 1 and 9 point to it.
9. What would falsify the thesis
   3–7 observable outcomes, taken from the "wrong" readings in Section 8 with
   the same thresholds.
```

## Workflow

1. **Reconcile the inputs.** Where the DD changed a debate probability or an earnings base, use the updated number and say so in one clause. Where the analyst sheet and the debate disagree, follow the debate and note the gap in Section 6.
2. **Build the scenario table.** Each scenario is defined by how the thesis-critical debate questions resolve, not by arbitrary growth rates: bear = the critical questions go bear; base = the debate's favoured outcomes; bull = the bull outcomes plus a catalyst. Compute terminal-year earnings ex-interest if cash is being credited separately; strip interest income when stripping cash. Show the arithmetic; mark estimates (e). If the user wants live formulas, write a one-sheet xlsx (`openpyxl`, formulas not values) alongside. Then add two bridges under the scenario table. (a) The profit increment split by driver (volume, price or take rate, funding cost or rates, mix, one-offs such as tax steps), never by segment: a segment's share of growth is not a driver's share. (b) The return in local currency (earnings growth + yield + multiple change) carried to the user's currency, with the FX assumption stated and kept consistent with the model's price and inflation assumptions (a weaker currency raises import prices). Check that the current-year figures match year-to-date actuals.
3. **Size the asymmetry** in Section 1 from the table (e.g. −10% / +35% / +80%). State the bear probability at which the expected return falls to the hurdle. If a plausible change in a subjective probability would flip the conclusion, anchor the conclusion on the asymmetry and on when the deciding evidence arrives, not on the weighted number alone.
4. **Write Sections 2–4 by condensing**, not re-researching: 1–2 pages each, numbers carried from the primer with its latest refresh. Add nothing that is not in the inputs except the current price. The four items that close Section 4 come from the variant-view frame and ledger. If none exists, say so and run `/variant-view TICKER frame` first, or carry the items as open questions in Section 6. Never write a reason the market is wrong that the user has not stated.
5. **Write 6–9 from the debate and DD**: the "what would change the verdict" signals become Section 8; the "Not supported" conditions become Section 9.
6. **Check**: every number in Sections 1 and 5 traces to a table or input; each reason in Section 1 has its evidence in the body and a row in Section 8; no price target, and buy/sell wording only in the action line when the user asked for a call; the thesis paragraph and the scenario table agree; the header dates are right. After any round of edits, re-check consistency: each threshold, count of conditions and figure that appears in more than one place (thesis, tracking table, falsifiers) is identical; the hurdle is the same everywhere; every comparison names a like-for-like benchmark; and each claim in the thesis paragraph still has its supporting evidence somewhere in the body.

## Delivery and knowledge base (end)

1. Write `companies/<TICKER>/Thesis.md` in the vault with document frontmatter (`type: document`, `doc: thesis`, `tickers`, `updated`, `data_through`, `next_checkpoint`, `sources: [skill:thesis-writeup]`), linking the first mention of each covered company, theme, policy, entity and person with `[[...]]`.
2. Update the hub: `verdict`, `price_check`, `updated`, `data_through`, `next_checkpoint`, the **Latest** line, the "Thesis in one paragraph" section, and a dated `## Log` line.
3. Append read-across lines to the theme and policy notes the thesis relies on (`## Evidence log`, dated, linking `[[TICKER]]`).
4. Commit and push per `research-kb`; also `project_write` the markdown to the claude.ai Project while the Project is still in use.
5. Convert to .docx/.pdf with pandoc (`--from markdown+pipe_tables-tex_math_dollars-raw_tex --wrap=none`) only if the user wants a file. Length 5–8 pages. Reply with the thesis paragraph and the asymmetry line, nothing more.

## Standards

- Plain English, no jargon left unexplained; tables for numbers, prose for argument.
- Fact, management claim and inference kept distinct.
- Avoid "genuinely", "honestly", "straightforward"; no hedging boilerplate — uncertainty lives in the scenarios and the open questions.