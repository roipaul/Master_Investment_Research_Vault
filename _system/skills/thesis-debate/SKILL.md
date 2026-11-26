---
name: "thesis-debate"
description: "Debate the High-materiality questions from a company primer: bull vs bear per question, a verdict with probability and confidence, and a final Supported/Not supported/Inconclusive call. Use for /thesis-debate or requests to develop a view."
---

# Thesis Debate

A thesis debate is the step after the full primer. The primer describes the business and ends with the questions that matter (Section 5). This workflow answers them: for each important question it builds the strongest bull case and the strongest bear case from evidence, judges which is more likely, and then rolls those judgments into one conclusion on the investment thesis.

The user is an experienced equity analyst running his own and his family's money. He wants a judgment, not a survey. Each question gets a side, a probability and a confidence level, and the document ends with a call. "Inconclusive" is an allowed and respectable call when the evidence does not support one side, as long as it says what would settle it and when.

## Inputs

1. **The primer.** Find the company's full primer: `part5_questions.md` and the other part files in the working directory, or the primer .docx/.pdf in attachments or earlier in the conversation. If no primer exists, say so and run the `full-primer` workflow first; the debate depends on its fact base and question list.
2. **The questions.** Take every question marked **High** materiality in primer Section 5.1. Medium questions are not debated; each gets one line in the "Remaining open questions" section. If the user names specific questions (e.g. "/thesis-debate COHR Q1 Q5 Q9"), debate those instead.
3. **The standard.** The thesis being tested is the user's usual one: the business compounds through revenue growth and margin expansion, and the stock offers a valuation gap that can close. The main verdict is on the **business**. Valuation enters only as a closing **price check** against his hurdle: **15% IRR over a 3–5 year hold**. Never give a price target or fair value.

## Workflow

1. **Refresh the facts.** Check what has happened since the primer's latest reported quarter: new earnings, guidance changes, major customer or competitor news, regulatory decisions. Search "<TICKER> earnings" and "<TICKER> news" for the current date. Note anything that changes a primer fact, and use the updated fact.

2. **Plan each question.** For each High question, write down before researching: what would have to be true for the bull side, what would have to be true for the bear side, and which evidence would tell them apart. This keeps the research aimed at the deciding evidence rather than at background. Make it concrete: for each side, write what it predicts about timing (did the change start before or after the supposed cause?), magnitude (do the flows add up?) and peers (did competitors who should be unaffected move the same way?). Evidence that both sides predict equally does not decide anything. For any slowdown or acceleration, also classify it before extrapolating: one-off level reset (a tax step, a rule that cuts eligibility once), cyclical (rates, FX-driven prices), or structural (saturation, share loss); check whether a plateau began before the event blamed for it.

3. **Research bull and bear separately.** Search deliberately for evidence against whichever side the primer seems to lean toward; the primer is built largely from company sources and leans toward management's framing. For every question aim for:
   - at least one source independent of the company (competitor filings, customer disclosures, industry data firms, trade press, regulators, expert commentary);
   - a historical analogue or base rate where one exists (how did similar companies, cycles or technology transitions play out?);
   - the numbers that decide it, computed rather than asserted (margins, unit economics, share, capacity, ASP trends);
   - like-for-like benchmarks only: same product, geography, currency basis and definition. Before comparing credit, impairment or coverage ratios, read the accounting policy (write-off threshold, staging, bans on selling bad loans) that moves them;
   - podcasts, broker summaries and AI summaries of filings used as hypothesis generators: list their claims, check each against filings, and carry only the verified ones;
   - sell-side and data-terminal evidence through `research-portals`, when the user has access:
     - Bernstein and CLSA estimates of KPIs the company does not disclose, and how far apart they are;
     - their channel checks;
     - Capital IQ transcripts and insider data;
     - Xueqiu for Chinese names.

     Treat broker estimates as estimates and check them against official or third-party data. A broker's channel check can count as the independent source. Do this research in the main thread, not in subagents, because the portals run in the user's signed-in browser.

   With more than ~6 questions, split the research across parallel subagents by question group. Give each the primer facts relevant to its questions and the bull/bear framing from step 2. Ask for evidence with source URLs, and no verdict. Write all the verdicts yourself afterwards so the probabilities are calibrated against each other.

4. **Write each debate** in the format below, to markdown files in the working directory.

5. **Roll up the verdicts** into the final conclusion using the rules below, then do the price check.

6. **Assemble, check and deliver** (see Build and Checks).

## Debate format (one per question)

Use the primer's question number and wording as the heading, e.g. `### Q9. Why is gross margin below Eoptolink and Lumentum despite owning its lasers?`

- **Why it matters.** Two or three sentences: what in the thesis depends on this answer.
- **Bull case.** The strongest argument for the favourable answer, in prose, with the evidence and citations. Steelman it: write it as its smartest advocate would.
- **Bear case.** The strongest argument for the unfavourable answer, built to the same standard. If one side is thin on evidence, say so rather than padding it.
- **Weighing the evidence.** Which claims are verified and which rest on management assertion; what the historical analogue suggests; which facts the two cases disagree on and which way those facts point. This is where the reasoning happens, so make it explicit.
- **Verdict.** One line in this form: `Verdict: Bear more likely — ~65%; confidence: Medium.`
- **What would change the verdict.** One to three observable signals, each with where or when it would show up (a metric in a specific report, a competitor disclosure, a regulatory decision).
- **Implication for the thesis.** One or two sentences: what this verdict does to the revenue-growth or margin-expansion leg, or to the risk.

Probability is the likelihood that the favoured side's answer turns out true over the 3–5 year horizon. Calibrate:

| Probability | Meaning | Required evidence |
|---|---|---|
| 50–55% | Toss-up; state "Balanced" rather than picking a side | Evidence roughly even, or key data unavailable |
| 55–65% | Lean | Some independent evidence favours one side |
| 65–80% | Clear | Independent, quantified evidence and a supportive analogue |
| >80% | Strong | Hard data that the other side cannot easily explain; use rarely |

Confidence is separate from probability. It measures how good the evidence is. High means verified data from multiple independent sources; Medium means a mix of independent and company sources; Low means mostly management claims, one source, or a forecast. A 70% verdict on Low-confidence evidence is allowed but must say so.

## Final conclusion rules

First classify each debated question as **thesis-critical** (if the bear side is true, the compounding thesis fails) or **thesis-shaping** (it changes the size of the outcome, not whether it happens). Mark this in the scorecard. Usually 2–4 questions are critical.

Then apply these rules for the business verdict:

- **Supported**: every thesis-critical question leans bull at ≥60% with at least Medium confidence, and no thesis-shaping question is a Clear bear (≥65%) that would on its own cut the expected growth or margin path materially.
- **Not supported**: any thesis-critical question is a Clear bear (≥65%) at Medium or High confidence.
- **Inconclusive**: anything else. This includes critical questions at or below 60%, critical questions resting on Low-confidence evidence, or bull and bear Clear verdicts on critical questions that offset each other.

Conviction for Supported or Not supported is High (every critical question Clear at Medium or High confidence), Medium, or Low (the rules are only just met). Name the two or three questions the call depends on most.

An Inconclusive call must list the specific evidence that would resolve it, with dates where possible (next earnings, a customer's capex guidance, a regulatory ruling). That turns "we don't know" into a tracking plan.

Use judgment where the rules give an odd result, but if the stated verdict departs from them, explain why in a sentence.

**Price check** (after the business verdict, and never changing it):

1. Get the current share price and diluted share count, with the date and source.
2. Reverse-engineer what the price implies: the revenue growth and margin (or EPS/FCF path) needed to justify it at a reasonable exit multiple for the sector, stated as assumptions.
3. Compare that implied path with the path the verdicts support.
4. State whether a 15% IRR over 3–5 years looks **Reachable** (the verdicts support a path at or above what is needed), a **Stretch** (it needs mostly bull outcomes) or **Unlikely** (it needs outcomes the verdicts reject).

Show the arithmetic in a small table. Add three checks to it: (a) the nearest listed local peer's multiples and the local cost of equity used by others, with a sentence on why this company should differ; (b) a currency bridge from local earnings growth plus yield to the user's currency, with the FX assumption stated; (c) the probability of the bear outcome at which the expected return falls to the hurdle. Use one hurdle throughout. Give no price target, fair value, or buy/sell language.

## Document structure (the user's pitch order)

```
1. Thesis and Verdict
   Business verdict (Supported / Not supported / Inconclusive) with conviction;
   price check result (Reachable / Stretch / Unlikely); the 2–3 questions the call
   depends on; a one-paragraph statement of the thesis as it now stands.
   Scorecard table: Q# | Question (short) | Critical/Shaping | Verdict | Prob. | Confidence
2. Business Description
   What drives the business across cycles, industry structure (including supplier
   and platform concentration), and the business model. 1–2 pages condensed from
   the primer, updated with refreshed facts. No new debate here.
3. Management
   Behaviour in past crises and downturns (COVID, prior cycles, predecessor
   companies if the team is new), incentive alignment (ownership, pay design).
   Search the controlling and large holders' other businesses (banks, competitors,
   suppliers, related parties), their share sales and the stated reasons, and the
   current status of any short report or litigation (filed, dismissed, settled).
   Management questions are debated here in the debate format.
4. Current Situation: What Creates the Opportunity
   Why the question is live now: recent results, the debate the market is having,
   what has changed. Short.
5. Return Drivers: The Key Debates
   Revenue-growth, margin and cash-conversion debates, grouped as in primer Section 5.
   Industry-structure and geopolitical debates go here too.
6. Remaining Open Questions
   Medium-materiality questions not debated, one line each, with materiality, plus
   any new questions the research surfaced.
7. Risks
   The bear cases that remain plausible (verdict probability against them ≥30%),
   ranked by impact, plus risks outside the questions.
8. Price Check
   As above.
9. What to Track
   Table: Signal | Where/when | Which question it updates | What reading would
   strengthen or weaken the thesis.
10. What Would Falsify the Thesis
   3–5 specific observable outcomes, with thresholds where possible.
Sources
```

Valuation-gap questions from the primer (e.g. "what does the price imply?", "what is a normalized year?") are debated inside Section 8 rather than Section 5; normalized-earnings questions can sit in Section 5 if they are mainly about the business.

## Writing standards

- Plain English, no jargon left unexplained. Prose for arguments; tables for scorecards, numbers and tracking.
- Every factual claim carries a bracketed citation `[n]` to a numbered source list. Reuse primer sources where they apply (renumber them in this document's own list) and add new ones. Expect 40–80 sources.
- Separate fact, management claim and inference explicitly ("management says…", "LightCounting estimates…", "this implies…").
- Keep each side equally rigorous. If you notice that all the verdicts lean one way, re-check the weaker side's research before concluding.
- Avoid "genuinely", "honestly", "straightforward". No hedging boilerplate; uncertainty belongs in the probability and confidence fields.
- Length: about 25–40 pages. Each debate is roughly 1–2 pages.

## Build

Write each section to its own markdown file (`d1_thesis.md` … `d10_falsify.md`, `sources.md`), then assemble them into one markdown file with a title line (`% <Company> (<TICKER>) — Thesis Debate`), a table of contents, numbered headings (`# ` → "1.", `## ` → "1.1") and the sources appended. Convert it with:

```
pandoc in.md -o out.docx --from markdown+pipe_tables-tex_math_dollars-raw_tex --wrap=none
soffice --headless --convert-to pdf --outdir <dir> out.docx
```

The `-tex_math_dollars` flag is required: without it, two `$` signs on one line (e.g. `$M` in a header) turn a whole table into raw text. After pandoc, use python-docx to set table fonts to 9pt for 4–5 columns, 8pt for 6–7 and 7.5pt for 8+, before converting to PDF. For text-heavy tables, set relative widths with dash counts in the separator row (e.g. `|--|--------|-----|-----|---|---|`).

Name the files `<Company>_<TICKER>_Thesis_Debate.docx` and `.pdf`. If the `full-primer` skill's `scripts/build_primer.py` is available, you can copy it and adapt its `PARTS` list and title instead of writing the assembler from scratch.

## Checks before delivery

1. Every debated question has a bull case, a bear case, a verdict line in the standard form and at least one independent source.
2. The scorecard matches the verdict lines exactly, and the business verdict follows the conclusion rules (or explains why not).
3. The share price used in the price check is dated and sourced, and there is no price target or buy/sell language anywhere.
4. Facts updated in the refresh step are used consistently throughout.
5. Render the PDF and Read the first page and one debate page as images to confirm the tables rendered.

Then send both files with `SendUserFile`. In the reply, give the business verdict, conviction, price check result and the two or three deciding questions in a few lines.