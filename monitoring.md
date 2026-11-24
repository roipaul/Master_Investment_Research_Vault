---
type: log
doc: monitoring
updated: 2026-11-20
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
| [[NVDA]] | NVIDIA | EDGAR 8-K item 2.02, CIK 0001045810; company IR | FY2027-Q3 | Q4 FY27: late Feb 2027 (not set) | done FY2027-Q3; 10-Q addendum due when filed (EDGAR could not be queried on 2026-11-20; check next run) |
| [[TME]] | Tencent Music | EDGAR 6-K, CIK 0001744676; company IR | FY2026-Q3 | Q4 2026: about 2027-03-17 (not announced) | done FY2026-Q3 |
| [[0700-HK]] | Tencent | HKEXnews; company IR | FY2026-Q3 | FY2026: about 2027-03-18 (not announced) | done FY2026-Q3 |
| [[YMM]] | Full Truck Alliance | EDGAR 6-K, CIK 0001838413; ir.fulltruckalliance.com (PDFs sit on filecache.investorroom.com, blocked to the watch) | none | Q3 2026: released 2026-11-19 (PR Newswire, 05:00 ET), call held 06:00 ET the same day. Q4 2026: March 2027 (e) | awaiting upload: "Q3 2026 Full Truck Alliance Investor Presentation" (PDF, Webcast & Presentations page) and the company's "3Q 26 Earnings Transcript" (PDF, Quarterly Results page). Release and full statements already read (StockTitan copy of the PR Newswire release); the Motley Fool transcript is readable (8 analyst questions) but carries no financial review or guidance section. Paused on day one because the block will not clear by waiting. Asked 2026-11-20; next reminder 2026-11-27 |
| [[6417-T]] | Sankyo | TDnet; company IR (Japanese: translate) | none (primer through H1 FY3/2027) | Q3 FY3/2027: early Feb 2027 (e) | waiting |
| [[000807-SZ]] | Yunnan Aluminium | cninfo / SZSE; company IR (Chinese) | none (primer through Q3 2026) | FY2026 annual: Mar-Apr 2027 (e) | waiting |
| [[POOL]] | Pool Corporation | EDGAR 8-K item 2.02, CIK 0000945841; company IR | none | Q4 2026: mid-Feb 2027 (e) | ready (backfill #6: Q3 2026, released 2026-10-22) |
| [[1590-TW]] | Airtac | TWSE MOPS; company IR | none | Q4 2026: Feb-Mar 2027 (e) | ready (backfill #10: Q3 2026, released 2026-10-29) |
| [[105560-KS]] | KB Financial | DART; EDGAR 6-K, CIK 0001445930; kbfg.com (Fact Book and webcast script readable; results deck PDF blocked to the watch) | FY2026-Q3 | Q4/FY2026: early Feb 2027 (e; not announced; FY2025 was 2026-02-05) | done FY2026-Q3, sign-off pending |
| [[2454-TW]] | MediaTek | TWSE MOPS; company IR | none | Q4 2026: late Jan-early Feb 2027 (e) | ready (backfill #3: Q3 2026, released 2026-10-30) |
| [[ZTO]] | ZTO Express | EDGAR 6-K, CIK 0001677250; decks at zto.investorroom.com/Investor-Presentations (PDFs blocked to the watch); HKEXnews (2057) | none | Q3 2026: released 2026-11-17 US ET (6-K 0001104659-26-129305), call held 19:30 ET the same evening | awaiting upload: "ZTO 3Q 2026 Corporate Presentation" (English PDF) and "3Q26 Financial Details For Earnings Call" (PDF). Release and full transcript (Motley Fool) already readable. Asked 2026-11-19; next reminder 2026-11-26 |
| [[3690-HK]] | Meituan | HKEXnews; company IR | none | Q3 2026: 2026-11-27 (HKEX notice of board meeting, 2026-11-17) | waiting |
| [[JD]] | JD.com | EDGAR 6-K, CIK 0001549802; ir.jd.com (deck under Presentations); HKEXnews (9618) | FY2026-Q3 | Q4/FY2026: about early March 2027 (e; FY2025 call was 2026-03-05) | done FY2026-Q3; addendum due by 2026-11-28 (Alibaba and PDD report 2026-11-19, Meituan 2026-11-27) |
| [[TCOM]] | Trip.com | EDGAR 6-K, CIK 0001269238; investors.trip.com; HKEXnews (9961) | none | Q3 2026: 2026-12-01 after the US close (2026-12-02 before the Hong Kong open); call 19:00 ET on 2026-12-01 (company announcement, 6-K and HKEX, 2026-11-19) | waiting |
| [[0268-HK]] | Kingdee | HKEXnews; company IR | none | FY2026 annual: mid-late Mar 2027 (e) | waiting |
| [[0669-HK]] | Techtronic | HKEXnews; company IR | none | FY2026 annual: early Mar 2027 (e) | waiting |
| [[WCC]] | Wesco | EDGAR 8-K item 2.02, CIK 0000929008; company IR | none | Q4 2026: mid-Feb 2027 (e) | ready (backfill #4: Q3 2026, released 2026-10-29) |
| [[FDR-MC]] | Fluidra | CNMV; company IR | none | FY2026: late Feb 2027 (e) | ready (backfill #5: 9M 2026, released 2026-10-29) |
| [[STZ]] | Constellation Brands | EDGAR 8-K item 2.02, CIK 0000016918; company IR | none | Q3 FY2027: early Jan 2027 (e) | ready (backfill #9: Q2 FY2027, released 2026-10-06) |
| [[UNH]] | UnitedHealth | EDGAR 8-K item 2.02, CIK 0000731766; company IR | none | Q4 2026: mid-Jan 2027 (e) | ready (backfill #7: Q3 2026, released 2026-10-13) |
| [[AA]] | Alcoa | EDGAR 8-K item 2.02, CIK 0001675149; company IR | none | Q4 2026: mid-Jan 2027 (e) | ready (backfill #8: Q3 2026, released 2026-10-15) |
| [[KSPI]] | Kaspi.kz | EDGAR 6-K, CIK 0001985487; ir.kaspi.kz (deck at ir.kaspi.kz/media/, readable) | FY2026-Q3 | Q4 2026: late Feb 2027 (e) | done FY2026-Q3, sign-off pending |

## Peers only

Read for the cycle section when a watch-list name reports. They never get an update of their own.

| Ticker | Company | Read for | Where results appear |
|---|---|---|---|
| PNR | Pentair | POOL, FDR-MC | EDGAR, CIK 0000077360 |
| HAYW | Hayward Holdings | POOL, FDR-MC | EDGAR, CIK 0001834622 |
| LESL | Leslie's | POOL | EDGAR, CIK 0001821806 |
| HD | Home Depot | POOL, 0669-HK | EDGAR, CIK 0000354950 |

Each hub's Links section names the other peers read for that company. The same set is read every period.

## Backfill queue

Approved by Paul on 2026-11-19. These results came out before `watch_from`, so detection would not pick them up; they are run as backfills instead. The daily watch runs them after any newly released name, within `max_updates_per_run`, in the order below. Each still has to pass the Step C readiness check; a name whose transcript or deck cannot be read is paused for upload as usual. When one is written, mark it done here.

| # | Ticker | Period | Released | Notes for the run | Done |
|---|---|---|---|---|---|
| 1 | [[KSPI]] | 3Q / 9M 2026 | 2026-11-09 | Marketplace GMV guidance cut to about 12% (was about 20%); tenge weakness. 9M interim statements on 6-K of 2026-11-12. Deck on ir.kaspi.kz | done 2026-11-20 |
| 2 | [[105560-KS]] | Q3 2026 | 2026-10-29 | Use the amended figures: 6-K/A of 2026-11-12 cut Q3 net profit to KRW 1.76tn after regulatory fines (Kookmin Bank, KB Securities). The Motley Fool transcript has gaps: look for a complete one before Step C  done 2026-11-24 |
| 3 | [[2454-TW]] | Q3 2026 | 2026-10-30 | Q4 guide NT$210-222bn on AI ASIC revenue; US$3.9bn convertible. Company PDF has prepared remarks only; full transcript elsewhere. Read with [[ai-infrastructure-cycle]] and [[NVDA]] | |
| 4 | [[WCC]] | Q3 2026 | 2026-10-29 | FY26 EPS guide raised to US$18.00-18.50; data centres. Read with [[ai-infrastructure-cycle]] | |
| 5 | [[FDR-MC]] | 9M 2026 | 2026-10-29 | Guidance narrowed on weak new-pool construction. Run on the same day as POOL; read PNR, HAYW, LESL from "Peers only" | |
| 6 | [[POOL]] | Q3 2026 | 2026-10-22 | EPS flat; Team Horner acquisition agreed 2026-11-16. Read with FDR-MC | |
| 7 | [[UNH]] | Q3 2026 | 2026-10-13 | FY26 adjusted EPS guide raised to at least US$20.50 | |
| 8 | [[AA]] | Q3 2026 | 2026-10-15 | South32 aluminium assets deal (US$3.1bn) heading to close in H1 2027. Read with [[000807-SZ]] primer | |
| 9 | [[STZ]] | Q2 FY2027 | 2026-10-06 | New CEO; comparable EPS guide reaffirmed. Q3 FY2027 due early Jan 2027 | |
| 10 | [[1590-TW]] | Q3 2026 | 2026-10-29 | Payout ratio raised to 65%. Q3 consolidated report approved 2026-11-12 | |

Not queued: Sankyo H1 and Yunnan Aluminium Q3 (already in their primers); Techtronic and Kingdee (half-yearly; next in March); TCOM (Q3 date not announced).

## Waiting on Paul

- **Sign-off:** KSPI FY2026-Q3 — proposed thesis Intact (against a provisional baseline), fresh money Wait at US$85.80 (2026-11-19). Confirm or override with `/earnings-update KSPI confirm`.
- **Upload:** YMM FY2026-Q3 — "Q3 2026 Full Truck Alliance Investor Presentation" (PDF, ir.fulltruckalliance.com/Webcast-Presentations) and the company's "3Q 26 Earnings Transcript" (PDF, ir.fulltruckalliance.com/Quarterly-Results). Put them in `inbox/uploads/YMM/` or a chat with `/earnings-update YMM`. Asked 2026-11-20.
- **Upload:** ZTO FY2026-Q3 — "ZTO 3Q 2026 Corporate Presentation" (English PDF) and "3Q26 Financial Details For Earnings Call" (PDF), both listed at zto.investorroom.com/Investor-Presentations. Put them in `inbox/uploads/ZTO/` or a chat with `/earnings-update ZTO`. Asked 2026-11-19.
- **Baseline:** JD's and KSPI's updates use provisional baselines that are Claude's framing; each needs Paul's view or imported work.
- **Import earlier work:** the 16 hubs created on 2026-11-19 hold no primer, thesis or model yet (POOL, 1590-TW, 105560-KS, 2454-TW, ZTO, 3690-HK, JD, TCOM, 0268-HK, 0669-HK, WCC, FDR-MC, STZ, UNH, AA, KSPI). Until then their updates use a provisional baseline.

## Log

- 2026-11-19 — Watch list set up with 23 names and 4 peers, confirmed by Paul. 16 hubs created. Replaces the "POOL Tracker — Daily EDGAR Watch" scheduled task.
- 2026-11-19 — First daily run. JD FY2026-Q3 update written (proposed: thesis Intact against a provisional baseline, fresh money Wait at US$25.43). ZTO paused for upload: release and transcript read, but the Q3 deck and financial-details PDF on the IR site are blocked to the watch and were not furnished to the SEC; paused on day one of the two-day window because the block will not clear by waiting. YMM due today, not out at run time. NVDA 10-Q not yet on EDGAR. TCOM: no 6-K since 2026-09-16, Q3 date still unconfirmed. Housekeeping: CIKs filled for NVDA, TME, YMM, JD; Meituan Q3 date confirmed as 2026-11-27.
- 2026-11-19 — self-test OK: vault push works; skills available: research-kb, earnings-update
- 2026-11-19 — Sign-offs recorded: Paul confirmed TME, 0700-HK and JD FY2026-Q3 as proposed (thesis Weakened, Weakened, Intact; fresh money Wait on all three). Watchlist updated.
- 2026-11-19 — Backfill approved by Paul: ten names that reported before `watch_from` (KSPI, 105560-KS, 2454-TW, WCC, FDR-MC, POOL, UNH, AA, STZ, 1590-TW) set to `ready (backfill)` and queued in that order. CIKs filled for KB, WCC, STZ, UNH, AA, KSPI.
- 2026-11-20 — Daily run. KSPI FY2026-Q3 backfill written (proposed: thesis Intact against a provisional baseline, fresh money Wait at US$85.80). YMM released Q3 2026 on 2026-11-19 and held its call; paused for upload because the Q3 investor presentation and the company transcript sit on a file host the watch cannot open (same host family as ZTO). TCOM Q3 date confirmed: 2026-12-01 US time. One update only this run; nine backfills remain, KB Financial next. Tooling note: EDGAR's full-text search endpoint and IR home pages typed by hand were refused this run (the fetch tool asked for an approval nobody was there to give); pages found through web search opened normally. NVDA's 10-Q was therefore not checked.
