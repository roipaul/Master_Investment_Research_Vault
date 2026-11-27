---
type: system
doc: scheduled-tasks
updated: 2026-11-27
---

# Scheduled task prompts

Copies of the prompts of the four scheduled research tasks, as set in Claude on the date below. The live prompts are in Claude; editing a file here changes nothing there.

Since 2026-11-27 each prompt holds only its own job. The shared rules for unattended runs (the web, readings, limits, the waiting list, writing and the final message) sit once in the `research-kb` skill, section "Unattended runs", and the run limits are numbers in `settings.md` and `monitoring.md`.

| Task | Schedule (UTC) | File | Skill it runs | Limit read from |
|---|---|---|---|---|
| Earnings watch — daily | 23:43 daily | `earnings-watch-daily.txt` | earnings-update (detection steps are in the prompt) | `monitoring.md` `max_updates_per_run` |
| Buy list price watch | 08:47 and 21:47, Mon to Fri | `buy-list-price-watch.txt` | none (the procedure is in the prompt) | — |
| Market read — weekly digest | 00:37 Sat | `market-read-weekly-digest.txt` | market-read | `settings.md` `market_read_builds_per_run` |
| Cycle view — weekly check | 00:39 Sun | `cycle-view-weekly-check.txt` | cycle-view | `settings.md` `cycle_items_per_run` |

## Log
- 2026-11-27 — Prompts shortened and pointed at the shared section; copies filed here. The earlier, longer prompts were not kept.
