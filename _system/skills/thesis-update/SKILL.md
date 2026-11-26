---
name: "thesis-update"
description: "After a filing, a ruling, a deal or news on a company with a saved thesis (not results days, which go to earnings-update): update the tracking table, re-score the affected debate questions, check the falsifiers, refresh the price check, and append a dated update to the thesis doc."
---

# Thesis update

Once a thesis exists, every material event between results days is the same job: read what happened, compare it with what the thesis said to watch for, and decide whether the thesis is intact, strengthened, weakened or falsified. This skill does that job the same way each time so updates are comparable across events and across companies.

The user is an experienced equity analyst running his own and his family's money. No buy/sell language; the output is a judgment on the thesis and a refreshed tracking table.

**Results days belong to `/earnings-update`.** For a quarterly, half-year or annual results release, run that skill instead: it does the deep read and all the bookkeeping below, and writes its own short update into `Thesis.md`. Use this skill for everything else: a filing, a regulator's ruling, a deal, a management change, a peer's event, news.

## Knowledge base (start)

Run the `research-kb` skill's read step: pull the vault, read the hub `companies/<TICKER>/<TICKER>.md` and `companies/<TICKER>/Thesis.md` (including all earlier `## Update` sections), and the theme and policy notes the hub links to, so a read-across from a peer's event is not missed. If the vault is unreachable, use the Project copy and say so.

## Inputs

1. **The thesis** — `Thesis.md` from the vault (or the thesis-debate doc if no write-up exists). Take Sections 5 (driver assumptions and scenarios), 8 (what to track) and 9 (falsifiers), and the debate scorecard.
2. **The event** — the results release, call transcript, filing, regulator notice or news. Fetch primary sources; if the user supplied a file, use it. When primary sources are not enough, use `research-portals`:
   - Capital IQ for transcripts, filings and insider transactions;
   - Bernstein and CLSA for the brokers' read of the event and any change to their estimates;
   - Xueqiu for Chinese merchant and investor reaction.

   Label broker numbers as estimates. Pull the prior quarter's and the year-ago numbers for comparison.
3. **Price and share count**, dated.

## Workflow

1. **Facts first.** Extract the reported numbers for every tracked metric and the guidance given; compute growth, margins and any derived metrics the thesis uses (fee per order, revenue per unit, net cash, payout). Note disclosure changes (a metric dropped or added) — those are findings in themselves.
2. **Tracking table.** For each signal in "What to track": expected reading (from the thesis) | actual | verdict (ahead / in line / behind / not disclosed) | which debate question it updates. Add any new signal the event made relevant.
3. **Falsifiers.** Go through Section 9 line by line: triggered / not triggered / partially, with the number.
4. **Re-score.** For each debate question the event touches: old probability → new, with the evidence. Move probabilities only on evidence from the event, and keep calibration consistent with the debate's table (50–55 toss-up, 55–65 lean, 65–80 clear, >80 strong). Unchanged questions are listed as unchanged.
5. **Driver assumptions.** If a reported trend breaks a base-case assumption (order growth, pricing, margin, cash return), restate the assumption and recompute the affected scenario figure; otherwise leave the scenario table alone. Keep a guidance log: what management guided, what it delivered, cumulative beat/miss pattern.
6. **Price check.** Current price vs the scenario table: which scenario the price now implies, and whether a 15% IRR over 3–5 years looks Reachable / Stretch / Unlikely. No price target.
7. **Call.** One of: **Intact**, **Strengthened**, **Weakened**, **Falsified** (a Section 9 trigger hit), with the two or three readings that decided it and what to watch at the next checkpoint. If a reading needs follow-up (an IR question, a desk check), list it.

## Output and knowledge base (end)

Append a dated section to `Thesis.md` in the vault (never rewrite earlier updates), in this form:

```
## Update — <date>: <event>
Call: Intact / Strengthened / Weakened / Falsified — one sentence.
Tracking table (as above).
Falsifiers checked.
Questions re-scored (old → new, why).
Assumption changes, if any, with recomputed scenario figures.
Guidance log (cumulative).
Price check.
Next checkpoint: date, what to look for.
Follow-ups.
Sources.
```

Then:
1. Update the thesis header (data-through quarter, next results date, price) and, if an assumption changed, the affected cell in Section 5 with a footnote pointing to the update.
2. Update the hub: `verdict` (if the call changes it), `price_check`, `updated`, `data_through`, `next_checkpoint`, the **Latest** line, the critical-questions table probabilities, and a dated `## Log` line.
3. Append read-across to any theme or policy note the event bears on (`## Evidence log`, dated, `[[TICKER]]`), and to `[[entity]]` notes for peers mentioned.
4. `watchlist.md`: add a line if the call changed. `track-record.md`: add a line if Falsified. A closed position is logged by `/decision-record`, not here.
5. Commit and push per `research-kb` (message `<TICKER>: thesis-update <date> — <call>`); also `project_write` the thesis to the Project while it is still in use.

Reply with the call, the deciding readings and the next checkpoint in a few lines.

## Standards

- Reported numbers carry the source and period; computed ones say what they are computed from.
- Management's explanation of a miss is a claim, not a fact, until a number supports it.
- The same table shape every quarter, so quarters can be read side by side.