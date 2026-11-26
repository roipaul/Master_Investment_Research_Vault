---
name: "primer-triage"
description: "Before a primer, a quick edge gate (why mispriced, who must sell, analyst coverage); after a full primer, decide Dig / Defer / Drop: quality is the only knockout, a Defer carries a trigger and revisit date, a Dig the research plan."
---

# Primer triage

A full primer takes effort to read and a thesis debate takes more to run. This step sits between them and decides whether the debate is worth running now. It also has a quick gate that runs before any primer is written, to decide whether the primer is worth writing at all. It is a short document, the user confirms each verdict himself, and the verdict is recorded so the name is not re-triaged from scratch later.

The user runs his own and his family's money with a quality-value lens: businesses that compound through revenue growth and margin expansion, bought when a valuation gap can close; hurdle 15% IRR over 3–5 years. He also studies companies for what they teach about an industry, but learning value never outranks candidacy.

## Pre-primer gate (before any primer is written)

Run as `/primer-triage TICKER gate`, or whenever the user asks to triage a name that has no primer yet. It takes minutes, not hours. A full primer is about a week of attention, so it should go to names where an edge is plausible, and most heavily covered large caps offer little room for one.

Collect, each dated and sourced:

1. **Size and liquidity** — market cap, average daily value traded, free float.
2. **Analyst coverage** — the number of analysts with estimates, in bands: 0–5 thin, 6–15 moderate, 16 or more heavy.
3. **Dislocation** — the price move over one and three years, and the multiple against its own history. Is something visibly wrong?
4. **Edge hypothesis** — one sentence on why this might be mispriced, typed as duration, magnitude, probability, framing or mechanism (the `/variant-view` types), or "price alone". Add which leg it would sit on, as a candidate: earnings (a different earnings path from the one the price implies), discount (the same earnings, marked down too far), or both. If the user has not stated one, propose a candidate and mark it as a candidate.
5. **Who is selling, and why they must** — index deletion, a listing change, mandate or country limits, redemptions, a spin-off, stigma, complexity. "Nobody; ordinary disagreement" is an allowed answer.
6. **Fit** — is it in a vertical the user knows deeply or a market he is well placed to research (Hong Kong, China, Japan, Korea, Taiwan), and can the deciding questions be answered from a desk?
7. **Deciding question and depth** — name the one or two questions the case turns on, then pick the cheapest document that answers them:
   - **Full primer** — the default when the case depends on understanding the business.
   - **Cycle note** (3–5 pages) — when the edge rests on a commodity price, a spread or a cycle (for example how long a metal-to-feedstock spread lasts). Cover cycle position, the cost curve and where the company sits on it, mid-cycle earnings, and governance and cash. Write the full primer only if the note passes.
   - **Abridged-depth primer** — for thinly covered small caps where primary sources are thin; say so rather than padding to length.
8. **Pipeline capacity** — count the names at an active stage against `max_active` in the vault's `settings.md`. If the pipeline is full, a passing name gets **Primer (queued)** with a proposed start date, or the user decides which active name to pause.

Verdict, for the user to confirm:

- **Primer** — an edge hypothesis is stated, plus at least one of: thin or moderate coverage, a named forced seller, a visible dislocation, or deep domain knowledge.
- **Watch** — a business worth knowing but no hypothesis yet. One line goes to the watchlist saying what would create one.
- **Skip** — no hypothesis, heavy coverage and no dislocation.

Heavy coverage is not a knockout. It raises the bar: the hypothesis must name the specific assumption in the price that the user would dispute. A name can still be primed purely to learn an industry; label it a **learning primer** so it is not mistaken for a candidate.

Output is the eight lines and the verdict in the reply, plus one line appended to `Watchlist.md`: date | company | gate verdict | depth (full / cycle note / abridged) | edge hypothesis | coverage count | queue position. No separate document.

## Inputs (post-primer triage)

1. **The primer** (`part*.md` files, the .docx/.pdf, or the project doc), including Section 5 questions and the "further research and companies to study" list.
2. **Price, market cap and a simple trailing/forward multiple**, dated — for timing only.
3. **The user's current pipeline**, if known from the project or memory (names already in Dig, sector studies under way), so the plan slots in.

## The decision, in order

1. **Business quality — the only hard knockout.** Is there evidence of durable economics: returns above cost of capital through a cycle, a reason for them (structure, cost position, switching costs, network, licence), and a growth runway? Score Pass / Marginal / Fail with the two or three facts that decide it. Fail → Drop regardless of price or learning value.
2. **Edge.** Is there something the market is likely mispricing that research can resolve: a reported-vs-underlying gap, a regulatory overhang with a knowable timeline, a structure the market reads as risk, a cycle trough? Name it in one sentence or say there is none. If a pre-primer gate was run, say whether its hypothesis is confirmed, changed or gone now that the primer exists. Record the analyst coverage count and who is likely on the other side, and give the edge a `/variant-view` type (duration, magnitude, probability, framing, mechanism, or price alone) so that skill can pick it up. No edge on a Pass business → Defer, not Dig.
3. **Timing.** Does the current price leave room for the 15% hurdle if the edge resolves favourably (a rough reverse-engineering, no price target)? Price never promotes a Fail and never demotes a Pass with edge; it decides whether Dig happens now or later.
4. **Learning value.** What studying this name teaches about the industry or a sister company in the pipeline. Ranked below edge and timing; can tip a Defer into Dig only when the research is cheap because it overlaps with work already under way.

## Verdicts

- **Dig** — produce the research plan: the High-materiality questions to debate (from Section 5, pruned or added to), which need desk DD (`/desk-dd`), scuttlebutt (`/scuttlebutt`) or a policy timeline (`/policy-timeline`), what data to request from the analyst, and the order of work with a rough time budget. The debate runs next.
- **Defer** — must carry: the trigger (a price level, an event, a disclosure), a revisit date, the three to five signals to track until then, and the one-paragraph view to be re-read at revisit. Logged to the watchlist.
- **Drop** — the reason in two sentences, and what would reopen it (usually a change in business quality, not price). Logged so it is not re-primed.

## Output

`<Company>_<TICKER>_Triage.md`, one to two pages:

```
Verdict: Dig / Defer / Drop (proposed; awaiting the user's confirmation)
1. Business quality: Pass / Marginal / Fail — deciding facts
2. Edge — one sentence with its type, analyst coverage count and likely seller; or "none identified"
3. Timing — price, multiple, rough hurdle test
4. Learning value — one or two lines
5. Plan (Dig) / Trigger, revisit date, signals (Defer) / Reason and reopen condition (Drop)
Sources (primer sections and the price source)
```

Save to the project with `project_write`. Also append one line to a `Watchlist.md` project doc (create it if absent): date | company | verdict | trigger or next step | revisit date. Reply with the proposed verdict and the deciding facts in three or four lines, and ask the user to confirm or overrule.

## Standards

- Short. If a section needs more than a paragraph, the primer should answer it, not the triage.
- Candidacy before curiosity: an interesting industry does not make a Dig.
- No price target, no buy/sell language.