---
type: system
doc: tools
updated: 2026-11-27
---

# Tools

`check.py` is the vault check. Every skill run calls it through `research-kb`: once at the start (`python3 _tools/check.py start`) and once before each commit (`python3 _tools/check.py`, with `--unattended` in a scheduled run). It reads the vault and git and never changes a note.

**Errors** stop the commit until they are fixed or reported:
- a company page whose frontmatter cannot be read, or with an empty required field, or an unknown stage;
- a buy-list name with no buy price, or a buy price on a name that is not on the buy list;
- a note deleted;
- a file over 10 MB in a `files/` folder;
- in a scheduled run only: a run limit passed, a new name started while the waiting list is over its cap, a change to `verdict`, `zone`, `conviction`, `held`, `list` or `buy_price`, or a change to the confirmed dials.

**Warnings** are reported and do not stop the commit: documents not listed on their page, a dated step with no file, work out of order (often an import), a stale frame, a passed checkpoint, a folder with no page, the waiting list over its cap, and a run limit passed in a run Paul is present for.

The limits are read from `settings.md` and `monitoring.md`. The waiting count is every item in every page's `awaiting` field, which is wider than the ranked list's ranks 2 to 5.

## Log
- 2026-11-27 — First version. On the vault as it stood: 0 errors, 4 warnings. Tested against a deliberate breach (a protected field changed, three cycle items against a limit of two, a deleted note): 4 errors, exit code 1.
