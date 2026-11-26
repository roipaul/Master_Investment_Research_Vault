---
name: "abridged-primer"
description: "Condense a full company primer into a ~10-page, all-prose abridged primer (business, competitive position, industry dynamics, risks and growth levers), cited and delivered as .docx and PDF. Use for /abridged-primer or a short version of a primer."
---

# Abridged Primer

An abridged primer is the ten-page version of a full primer. It keeps the mechanism of the business, its competitive position, the industry forces acting on it, and the main risks and growth levers, and drops the reference material: quarterly tables, guidance histories, corporate history, detailed geography and the long source list. A reader should finish it able to explain how the company makes money, who it competes with and on what, what drives the industry, and what could go right or wrong.

Like the full primer, it is descriptive: no thesis, no valuation, no recommendation. It is a condensation, not new research. Every fact comes from the full primer and carries the full primer's citation, renumbered.

## Input

The company's full primer: the part files (`part1_company.md` … `part5_questions.md`, `sources.md`) in the working directory, or the full primer .docx/.pdf attached or earlier in the conversation. If only a ticker is given and no full primer exists, say so and run the `full-primer` workflow first. Read the whole full primer before writing.

## Structure

Always this skeleton, matching the user's existing abridged primers:

```
Table of Contents
1. <Company Name>: Abridged Company Primer
   1.1 How the Business Works
   1.2 Market Position and Competitive Landscape
   1.3 Industry Dynamics and Strategic Drivers
   1.4 Key Risks and Growth Levers
Sources
```

Use the company's full legal-style name as the full primer does (e.g. "Domino's Pizza, Inc.", "UnitedHealth Group Incorporated", "Airtac International Group").

**Length.** 3,000–3,800 words of body text, about 9–11 pages. Budget by section:

| Section | Words | Draws mainly on (full primer) |
|---|---|---|
| 1.1 How the Business Works | 1,200–1,550 (~40%) | 1.1 Overview, Segments, Business Model, Products; 2.1–2.2 customers, channels, suppliers; headline unit economics and margins from 4.1–4.2 |
| 1.2 Market Position and Competitive Landscape | 500–700 | 3.2 landscape and shares, basis of competition, intensity; 2.3 geographic concentration where it shapes position |
| 1.3 Industry Dynamics and Strategic Drivers | 400–700 | 3.1 how the industry works, demand drivers and cyclicality, key trends; regulation |
| 1.4 Key Risks and Growth Levers | 600–850 | 4.3 capital allocation; 4.4 long-term targets and disclosed risks; growth initiatives from 1.1; risk discussion in 2.x and 3.x |

### What each section does

**1.1 How the Business Works.** Open with one paragraph that identifies the company: what it does, where it is incorporated and listed, its scale (revenue, and users, members or SKUs where that is the natural unit), and its segment or channel mix with percentages. Then explain the mechanism in the order a reader needs it: what the customer buys and why; how revenue is earned and recognized (subscription, premium, unit sale, royalty, take rate); the recurring versus cyclical parts of demand; how the product reaches the customer (channels, sales organization); the cost structure and the few margin figures that define the economics; and the growth model (how new revenue is added, cross-sell, pricing). Close with what ties the pieces together. This is the longest section because mechanism is what the reader comes for. For single-segment companies, say so and use the breakdowns the company does give.

**1.2 Market Position and Competitive Landscape.** Who the competitors are, with sourced and dated shares; how concentrated the market is and which way concentration is moving; how competition differs by tier or segment (premium versus mid-market, enterprise versus SMB); the basis of competition and how the company competes (price, product, speed, distribution); pricing behaviour and price-war history; and any concentration in the company's own position (one geography, one payer, one customer) that is both a strength and a vulnerability.

**1.3 Industry Dynamics and Strategic Drivers.** The industry's cycle pattern with its history; the secular driver; structural shifts (technology, substitution, regulation, policy, consolidation); seasonality where it matters. Use the company as the example, not the subject.

**1.4 Key Risks and Growth Levers.** The main growth levers with management's targets stated as management's, and the execution record against past targets; the margin levers; the main structural risks in order of weight (concentration, regulation, commodity or input costs, technology substitution, cycle); capital allocation (balance sheet, dividends, buybacks, capex intensity). End with a short balanced paragraph that sets management's framing against the evidence, e.g. "Investors should weigh management's optimistic cycle-duration commentary against the historical pattern of relatively short up-cycles." That sentence points to the tension and does not resolve it.

Do not carry over the full primer's Part 5 questions; the abridged primer is the descriptive read only.

## What to keep and what to cut

Keep:
- the numbers that define the business: scale, segment and geographic mix, market shares, the defining margins or unit economics, the key concentration figures, the targets management has set;
- the full primer's calibrated scepticism: where it noted that management framing is self-serving, that estimates diverge, or that something is not disclosed, keep one sentence of it;
- concrete examples that make a mechanism click ("a cylinder on an electronics assembly line pushes circuit boards into position; it does not ship inside the finished phone").

Cut:
- every table: the abridged primer is prose only;
- quarterly series, guidance-versus-actual histories, non-GAAP reconciliations, full income statement and balance sheet detail (keep at most the two or three figures that define the financial profile);
- corporate history beyond one sentence where it explains the current shape of the business;
- lists of products, brands, sites or subsidiaries (name the important ones in prose);
- market-size tables (keep one market-size figure with its source, and note dispersion in a clause if it matters).

## Writing standards

- Prose paragraphs of 80–180 words; no bullets, no tables, no bold run-in headings inside sections.
- Define a term the first time it appears ("Pneumatic systems use compressed air to create mechanical motion…").
- Attribute claims: "management describes…", "the company claims…", "LightCounting estimates…".
- Inline bracketed citations, usually at the end of the sentence or paragraph they support, as clusters such as `[4][9]`. Aim for 60–90 citations across the document.
- Plain English. Avoid "genuinely", "honestly", "straightforward". Do not hedge every sentence.
- Nothing that recommends, values or opines on the stock.

## Citations and sources

Every fact must trace to the full primer. When a sentence condenses a full-primer sentence, carry that sentence's citations across. Then renumber: build a map from full-primer source numbers to new numbers in order of first appearance in the abridged text, rewrite every inline citation with the map, and emit a `Sources` list containing only the sources actually cited, in the new order, copying each source's description from the full primer verbatim. Expect 13–30 sources. Do not add sources or facts the full primer does not contain. If the full primer is more than a quarter out of date, say so in the reply rather than refreshing silently; the user can rerun the full primer.

## Build

Write the body to `abridged.md` with this heading layout:

```
# <Company>: Abridged Company Primer
## 1.1 How the Business Works
...
## 1.2 Market Position and Competitive Landscape
...
## 1.3 Industry Dynamics and Strategic Drivers
...
## 1.4 Key Risks and Growth Levers
...
# Sources
1. ...
```

Assemble a final markdown file with a title line, a "Table of Contents" heading and list (1. <Company>: Abridged Company Primer; then 1.1–1.4 indented), then the body. Number the top heading "1." Convert:

```
pandoc in.md -o <Company>_<TICKER>_Primer_Abridged.docx --from markdown-tex_math_dollars-raw_tex --wrap=none
soffice --headless --convert-to pdf --outdir <dir> <Company>_<TICKER>_Primer_Abridged.docx
```

`-tex_math_dollars` is required: without it two `$` figures in one paragraph are read as TeX math and the text between them disappears. If the `full-primer` skill's `scripts/build_primer.py` is available, it can be adapted instead (one part file, title "Abridged Company Primer", no section renumbering of the `##` headings). Use the same file-name stem as the full primer with `Abridged` in place of `Full`.

## Checks before delivery

1. Word count of the body is 3,000–3,800 and each section is within its band.
2. No tables, bullets or valuation language.
3. Every number in the abridged primer appears in the full primer; spot-check at least ten against it.
4. Every inline citation number exists in the new Sources list, every listed source is cited, and the numbering runs in order of first use.
5. Render the PDF and Read the first two pages as images to confirm the TOC and headings.

Send the .docx and .pdf with `SendUserFile`, with a one-line caption giving the page count and the full primer it was condensed from.