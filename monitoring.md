---
type: log
doc: monitoring
updated: 2026-11-19
watch_from: 2026-11-16      # results released before this date are not picked up; ask for a backfill instead
max_updates_per_run: 2
---

# Earnings watch

The list of companies whose results are followed automatically. A scheduled task ("Earnings watch — daily") reads this file once a day, looks for new results, waits until the call has been held and the documents can be read, then runs `/earnings-update` and writes the result to the company's folder. The thesis and fresh-money calls it writes are **proposed** until Paul confirms them.

**To add or drop a name:** add or delete its row in the watch list (a new name also needs a hub under `companies/`). Confirmed by Paul on 2026-11-19: 23 names for full updates, 4 as peers only.

**When documents cannot be reached:** the watch does not write an update. It sets the row to `awaiting upload`, names the documents, and tells Paul. He either uploads them in a chat with `/earnings-update TICKER`, or puts them in `inbox/uploads/<TICKER>/`, where the next run finds them.

**Status values:** `waiting` (nothing new) · `released <date>, waiting for call` · `ready` · `awaiting upload: <documents>` · `done <period>, sign-off pending` · `done <period>`.

Dates marked (e) are estimates from past reporting patterns, not company announcements. The watch replaces each one with the announced date when the company publishes it, and fills in the missing source details (CIK, IR page) as it goes.

## Watch list

| Ticker | Company | Where results appear | Last period done | Next results | Status |
|---|---|---|---|---|---|
| [[FISV]] | Fiserv (held) | EDGAR 8-K item 2.02, CIK 0000798354; company IR | FY2026-Q3 | Q4 2026: around 2027-02-10 (not announced) | done FY2026-Q3 |
| [[NVDA]] | NVIDIA | EDGAR 8-K item 2.02, CIK 0001045810; company IR | FY2027-Q3 | Q4 FY27: late Feb 2027 (not set) | done FY2027-Q3; 10-Q addendum due when filed |
| [[TME]] | Tencent Music | EDGAR 6-K, CIK 0001744676; company IR | FY2026-Q3 | Q4 2026: about 2027-03-17 (not announced) | done FY2026-Q3, sign-off pending |
| [[0700-HK]] | Tencent | HKEXnews; company IR | FY2026-Q3 | FY2026: about 2027-03-18 (not announced) | done FY2026-Q3, sign-off pending |
| [[YMM]] | Full Truck Alliance | EDGAR 6-K, CIK 0001838413; ir.fulltruckalliance.com | none | Q3 2026: 2026-11-19 before the US open, call 06:00 ET (company release, 2026-10-28) | waiting: due 2026-11-19; no 6-K on EDGAR at 05:30 UTC that day. Check release, call and transcript next run |
| [[6417-T]] | Sankyo | TDnet; company IR (Japanese: translate) | none (primer through H1 FY3/2027) | Q3 FY3/2027: early Feb 2027 (e) | waiting |
| [[000807-SZ]] | Yunnan Aluminium | cninfo / SZSE; company IR (Chinese) | none (primer through Q3 2026) | FY2026 annual: Mar-Apr 2027 (e) | waiting |
| [[POOL]] | Pool Corporation | EDGAR 8-K item 2.02, CIK 0000945841; company IR | none | Q4 2026: mid-Feb 2027 (e) | waiting |
| [[1590-TW]] | Airtac | TWSE MOPS; company IR | none | Q4 2026: Feb-Mar 2027 (e) | waiting |
| [[105560-KS]] | KB Financial | DART; EDGAR 6-K (CIK to fill); company IR | none | Q4 2026: early Feb 2027 (e) | waiting |
| [[2454-TW]] | MediaTek | TWSE MOPS; company IR | none | Q4 2026: late Jan-early Feb 2027 (e) | waiting |
| [[ZTO]] | ZTO Express | EDGAR 6-K, CIK 0001677250; decks at zto.investorroom.com/Investor-Presentations (PDFs blocked to the watch); HKEXnews (2057) | none | Q3 2026: released 2026-11-17 US ET (6-K 0001104659-26-129305), call held 19:30 ET the same evening | awaiting upload: "ZTO 3Q 2026 Corporate Presentation" (English PDF) and "3Q26 Financial Details For Earnings Call" (PDF). Release and full transcript (Motley Fool) already readable. Asked 2026-11-19; next reminder 2026-11-26 |
| [[3690-HK]] | Meituan | HKEXnews; company IR | none | Q3 2026: 2026-11-27 (HKEX notice of board meeting, 2026-11-17) | waiting |
| [[JD]] | JD.com | EDGAR 6-K, CIK 0001549802; ir.jd.com (deck under Presentations); HKEXnews (9618) | FY2026-Q3 | Q4/FY2026: about early March 2027 (e; FY2025 call was 2026-03-05) | done FY2026-Q3, sign-off pending; addendum due by 2026-11-28 (Alibaba and PDD report 2026-11-19, Meituan 2026-11-27) |
| [[TCOM]] | Trip.com | EDGAR 6-K, CIK 0001269238; company IR; HKEXnews (9961) | none | Q3 2026: to confirm (third-party calendars disagree: 16 or 23 Nov 2026) | waiting; check on first pass |
| [[0268-HK]] | Kingdee | HKEXnews; company IR | none | FY2026 annual: mid-late Mar 2027 (e) | waiting |
| [[0669-HK]] | Techtronic | HKEXnews; company IR | none | FY2026 annual: early Mar 2027 (e) | waiting |
| [[WCC]] | Wesco | EDGAR 8-K item 2.02 (CIK to fill); company IR | none | Q4 2026: mid-Feb 2027 (e) | waiting |
| [[FDR-MC]] | Fluidra | CNMV; company IR | none | FY2026: late Feb 2027 (e) | waiting |
| [[STZ]] | Constellation Brands | EDGAR 8-K item 2.02 (CIK to fill); company IR | none | Q3 FY2027: early Jan 2027 (e) | waiting |
| [[UNH]] | UnitedHealth | EDGAR 8-K item 2.02 (CIK to fill); company IR | none | Q4 2026: mid-Jan 2027 (e) | waiting |
| [[AA]] | Alcoa | EDGAR 8-K item 2.02 (CIK to fill); company IR | none | Q4 2026: mid-Jan 2027 (e) | waiting |
| [[KSPI]] | Kaspi.kz | EDGAR 6-K (CIK to fill); company IR | none | Q4 2026: late Feb 2027 (e) | waiting |

## Peers only

Read for the cycle section when a watch-list name reports. They never get an update of their own.

| Ticker | Company | Read for | Where results appear |
|---|---|---|---|
| PNR | Pentair | POOL, FDR-MC | EDGAR, CIK 0000077360 |
| HAYW | Hayward Holdings | POOL, FDR-MC | EDGAR, CIK 0001834622 |
| LESL | Leslie's | POOL | EDGAR, CIK 0001821806 |
| HD | Home Depot | POOL, 0669-HK | EDGAR, CIK 0000354950 |

Each hub's Links section names the other peers read for that company. The same set is read every period.

## Waiting on Paul

- **Sign-off:** TME FY2026-Q3 (thesis Weakened, fresh money Wait); 0700-HK FY2026-Q3 (thesis Weakened, fresh money Wait); JD FY2026-Q3 (thesis Intact against a provisional baseline, fresh money Wait). Confirm with `/earnings-update TICKER confirm`.
- **Upload:** ZTO FY2026-Q3 — "ZTO 3Q 2026 Corporate Presentation" (English PDF) and "3Q26 Financial Details For Earnings Call" (PDF), both listed at zto.investorroom.com/Investor-Presentations. Put them in `inbox/uploads/ZTO/` or a chat with `/earnings-update ZTO`. Asked 2026-11-19.
- **Baseline:** JD's update uses a provisional baseline that is Claude's framing; it needs Paul's view or imported work.
- **Import earlier work:** the 16 hubs created on 2026-11-19 hold no primer, thesis or model yet (POOL, 1590-TW, 105560-KS, 2454-TW, ZTO, 3690-HK, JD, TCOM, 0268-HK, 0669-HK, WCC, FDR-MC, STZ, UNH, AA, KSPI). Until then their updates use a provisional baseline.

## Log

- 2026-11-19 — Watch list set up with 23 names and 4 peers, confirmed by Paul. 16 hubs created. Replaces the "POOL Tracker — Daily EDGAR Watch" scheduled task.
- 2026-11-19 — First daily run. JD FY2026-Q3 update written (proposed: thesis Intact against a provisional baseline, fresh money Wait at US$25.43). ZTO paused for upload: release and transcript read, but the Q3 deck and financial-details PDF on the IR site are blocked to the watch and were not furnished to the SEC; paused on day one of the two-day window because the block will not clear by waiting. YMM due today, not out at run time. NVDA 10-Q not yet on EDGAR. TCOM: no 6-K since 2026-09-16, Q3 date still unconfirmed. Housekeeping: CIKs filled for NVDA, TME, YMM, JD; Meituan Q3 date confirmed as 2026-11-27.
