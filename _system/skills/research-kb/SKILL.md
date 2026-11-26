---
name: "research-kb"
description: "How to read from and write to the user's investment research vault, a private GitHub repo of markdown notes: the read step, where each document goes, hub updates, links and commits. The other research skills call it."
---

# Research knowledge base

The vault is the private GitHub repository `roipaul/Master_Investment_Research_Vault`: plain markdown notes that also open as an Obsidian vault. Every research skill begins with this skill's **read step** and ends with its **write step**, so that work on one company is found again and reused for the next. Keep it simple; an earlier version of the user's system failed by being over-built and by mixing fast-moving data into notes that then went stale.

## Three rules

1. **Notes hold judgments, not data.** No price histories or time series. Any number in a note carries its date and its source.
2. **Append, never rewrite.** Add dated sections or dated log lines; leave earlier entries as written. The one exception is current-state fields (hub frontmatter, the **Latest** line, the hub tables): overwrite those, and record each change as a dated `## Log` line, which is where the history lives.
3. **Data stays apart from notes.** Screen and consensus exports go under `data/`. A note may cite a file there but never pastes its contents.

## Read step

1. **Get the vault.** If it is already cloned in this session, `git pull --rebase`. If not, attach the repository with push access (owner `roipaul`, repo `Master_Investment_Research_Vault`) and clone it. If GitHub is not connected or the repository cannot be reached, say so in one line, work from the claude.ai Project copies or the files in the conversation, and at the end send the files you would have written. Never say something was saved to the vault when it was not.
2. **Read `settings.md`** for the hurdle, the flow mode and the limits.
3. **Read the hub** `companies/<TICKER>/<TICKER>.md`. If the company has no folder, create it from `_templates/hub.md` with ticker, name, exchange and sector filled in and `stage: gate`, and say it is new.
4. **Read the documents the calling skill names**, then the notes listed under the hub's Links, one level deep. Read-across is the point: a regulator's action or a base rate logged for a peer may already answer a question here.
5. For triage and decisions, also check `watchlist.md` and `track-record.md` for the ticker.

## Write step

**Where things go:**

| File | Written by |
|---|---|
| `companies/<TICKER>/<TICKER>.md` (hub) | every skill |
| `Primer.md`, `Abridged.md` | `/full-primer`, `/abridged-primer` |
| `Triage.md` | `/primer-triage` |
| `VariantView.md` | `/variant-view` |
| `Prior.md` | `/read-across` (the pack of what earlier work on adjacent companies established) |
| `MarketRead.md` | `/market-read`, and the "Market read — weekly digest" scheduled task |
| `PriceAlone.md` | `/price-alone` |
| `Debate.md` | `/thesis-debate` |
| `DD.md`, `Scuttlebutt.md` | `/desk-dd`, `/scuttlebutt` |
| `Thesis.md` | `/thesis-writeup`; `/thesis-update` appends |
| `Decisions.md` | `/decision-record` |
| `companies/<TICKER>/files/` | Word, PDF and Excel outputs, under about 10 MB each |
| `policies/`, `themes/` | `/policy-timeline`, driver maps, base-rate files. Industry notes `themes/<industry>.md` and business-model notes `themes/model-<tag>.md` also hold the learnings table that `/read-across` appends to; `themes/README.md` holds the list of business-model tags |
| `cycles/index.md` (the registry), `cycles/<slug>.md`, `macro/<market>.md` | `/cycle-view`, and the "Cycle view — weekly check" scheduled task |
| `macro/where-we-stand.md` | a view rebuilt by `/cycle-view stand` |
| `watchlist.md`, `price-alone-basket.md`, `decisions-log.md`, `track-record.md`, `pipeline.md`, `calendar.md` | the skill that owns each log (`pipeline.md` and `calendar.md` are views rebuilt by `/research-flow`) |
| `buylist.md` | rows by `/decision-record`; the last-price, gap and alert columns and the alerts log by the "Buy list price watch" scheduled task |
| `overview.md` | a view rebuilt by `/research-flow overview` |

**Frontmatter.** Documents use `_templates/document.md`: `type`, `doc`, `tickers`, `updated`, `data_through`, `next_checkpoint`, `sources`.

**Hub update.** Every run sets `updated`, the **Latest** line, the Documents list, the date under `steps:` for the step just run, and a dated `## Log` line. In addition each skill sets the fields it owns:

| Skill | Hub fields |
|---|---|
| `/primer-triage` | `stage`, `verdict`, `awaiting` |
| `/variant-view` | `zone`, `track`, `conviction`, `price_check`, `conservative_return`, `base_return`, `harsh_case`, the variant-views table |
| `/price-alone` | `track`, `verdict`, `conservative_return`, `harsh_case` |
| `/read-across` | `industry`, `model_tags`, `adjacent` (written to both companies' hubs), `learnings_filed`, and its lines in `awaiting` |
| `/market-read` | `market_focus`, `sentiment`, `market_read` (the date), and its flags in `awaiting` |
| `/cycle-view` | `cycle`, `cycle_phase`, `mid_cycle_note` (the date of the note), and the two dial markets. The confirmed `dials:` in `settings.md` change only when the user confirms |
| `/thesis-debate`, `/desk-dd` | the critical-questions table |
| `/thesis-writeup`, `/thesis-update` | `verdict`, `price_check`, `data_through`, `next_checkpoint`, `next_results`, "Thesis in one paragraph" |
| `/decision-record` | `held`, `list`, `buy_price`, `buy_action`, `buy_basis`, `buy_set`, `buy_review_by` |
| `/earnings-update`, `/variant-view`, `/price-alone` | `entry_level`, whenever they compute the price at which a named case clears the hurdle |
| "Buy list price watch" (scheduled task) | `alert` |

**Buy price kept in step with the work.** When a skill writes a new `entry_level` on a hub with `list: buy`, compare it with `buy_price`. If the price at which the case behind his basis clears the hurdle has moved more than 10% away from his buy price, or a falsifier named in his conditions is triggered, add "buy price review: <reason>" to `awaiting`. Never change `buy_price` yourself.

Returns and prices in the hub always sit beside the `price_check` date, so a reader can see how old they are.

**Catalysts.** The hub's `catalysts:` field lists dated future events that bear on the name. Each item has:
- `date`: a day, or a month or quarter when only that is known;
- `event`;
- `type`: one of regulatory, corporate, forced flow (index change, lockup, spin-off, placement), industry data, macro, or review;
- `tests`: the debate question, variant view or falsifier it bears on, or `none`;
- `status`: confirmed or expected;
- `source`.

Any skill that comes across such an event during its run adds it, and updates an item whose date is confirmed or moves. Add the field if the hub lacks it. When an event has passed, remove it from the field and write what happened in a dated `## Log` line. Results dates stay in `next_results`, and variant-view resolution dates and evidence deadlines stay in `VariantView.md`; do not copy them here. A macro event goes in only when a theme or policy note names it as a trigger for this name.

**Links.** Link the first mention of a company, theme, policy, entity or person with `[[...]]`. Create a three-line stub note only when the thing matters to two or more companies; otherwise leave it as plain text.

**Commit.** One commit per skill run: `git add -A`, commit with the message `<TICKER>: <skill> <date> — <one line>`, `git pull --rebase`, `git push`. Commits go straight to `main`; this is a notes vault, so no branches or pull requests. Never force-push. If a pull conflicts, keep both sides' lines (append-only notes make this safe) and tell the user if a hub field was in conflict. Never delete a note unless the user asks.

**Project mirror.** When working inside a claude.ai Project that still holds the same documents, also `project_write` the result there.

## What stays out of the vault

- Price histories, time series and raw data.
- Credentials, account numbers, or anything that identifies an account beyond the label the user gives it. Decision sizes are recorded as percentages only.
- The full text of sell-side or other copyrighted reports; cite and summarise.

## Housekeeping

`/research-kb check` reports, without fixing: hubs with missing frontmatter fields, documents not listed in their hub, broken links, and inbox notes older than 30 days. Fix only what the user confirms.