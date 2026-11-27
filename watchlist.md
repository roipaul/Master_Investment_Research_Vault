---
type: log
updated: 2026-11-27
---

# Watchlist

Two parts. **Current watchlist** is the list as it stands: names Paul has decided to watch, with what is still needed before he sets a buy price. It is rebuilt from the hubs (`list: watch`) whenever `/decision-record` changes it. A name leaves it for the buy list ([[buylist]]) when Paul sets a buy price, or leaves it with `/decision-record TICKER unlist`. **Log** below keeps every gate verdict, Defer and confirmed Wait, and is never rewritten.

## Current watchlist

| Ticker | Company | On list since | Basis | Work still missing before a buy price | Reference entry level (Claude's, not a buy price) | Revisit |
|---|---|---|---|---|---|---|
| [[NVDA]] | NVIDIA | 2026-11-18 | Fresh money Wait (confirmed) | No primer, frame, debate or thesis; provisional baseline only | About US$142 for a 20% base-case return (earnings-update FY2027-Q3) | 2026-12-15 |
| [[TME]] | Tencent Music | 2026-11-24 | Watch: monitor (Paul) | No triage, frame or thesis since the primer | About US$8.30 probability-weighted; US$8.10 conservative (2026-11-24) | 2027-03-17 |
| [[0700-HK]] | Tencent | 2026-11-19 | Fresh money Wait (confirmed) | No triage, frame or thesis since the primer refresh | About HK$285 for the conservative case to clear 15% (2026-11-19) | 2027-03-18 |
| [[JD]] | JD.com | 2026-11-19 | Fresh money Wait (confirmed) | No primer, frame or thesis in the vault; provisional baseline only | About US$21 for the conservative case to clear 15% (2026-11-19) | 2027-03-05 |
| [[PDD]] | PDD Holdings | 2026-11-24 | Pre-commitment, not buying yet (Paul, [[PDD/Decisions]]) | No frame; merchant, seller and IR calls open; debate sign-off open | About US$53 for the conservative case to clear 15% (2026-11-20); central view 14.6% at US$83.68 | 2027-03-31 |
| [[YMM]] | Full Truck Alliance | 2026-11-26 | Watch: views not yet tested (Paul) | His earnings numbers; three deciding questions (cash, commission cap, growth); Q3 update; debate, views and write-up | Not computed: the conservative case clears 15% only if all the cash is credited (2026-11-26) | 2027-03 |
| SK Square (402340.KS) | SK Square | 2026-11-15 | Gate: Watch (confirmed) | No hub or primer; trigger is the holding discount above 55% or a hard fall in Hynix | — | 2027-03-31 |

Carried over on 2026-11-24 from the confirmed entries in the log below. Fiserv is held, so it sits in [[overview]] under Held, not here.

## Log

Gate verdicts, Defers and confirmed Waits. One line per entry, newest at the bottom.

| Date | Company | Verdict | Edge hypothesis or trigger | Coverage count | Revisit date |
|---|---|---|---|---|---|
| 2026-11-13 | Full Truck Alliance (YMM) | Gate: Primer (confirmed) | Take-rate cap risk over-weighted (probability); order runway (duration) | 15 | — |
| 2026-11-15 | Odawara Engineering (6149.T) | Gate: Primer (confirmed; first in queue) | Magnitude: FY12/2026 guidance (recurring ¥1.24bn, -61%) looks stale after H1 operating profit of ¥1.5bn; net cash about two-thirds of market cap at 0.65x book. Check first: FY2025 operating cash flow only ¥0.1bn | 0 | — |
| 2026-11-15 | Sankyo (6417.T) | Gate: Primer (confirmed; queued second) | Duration/framing: priced as a dying pachinko maker, but it holds over 30% pachinko share and strong pachislot; 50% payout with a 5% DOE floor (yield about 5%); gambling exclusions as a structural seller | 12 | — |
| 2026-11-15 | Yunnan Aluminium (000807.SZ) | Gate: Primer (confirmed; queued third; overlaps the Alcoa work) | Duration: 5.7x 2026E P/E prices a peak, while China's 45mt capacity cap is binding (98% utilisation). Chalco (2600.HK) is the alternative | 18 | — |
| 2026-11-15 | SK Square (402340.KS) | Gate: Watch (confirmed) | Discount already about 44%, near the narrow end of its 36-77% range; company targets 30% by 2028, so the closing is consensus. Revisit if the discount widens above 55% or Hynix falls hard | 20 | 2027-03-31 |
| 2026-11-18 | NVIDIA (NVDA) | Earnings-update: fresh money Wait (confirmed) | Evidence: a clean 10-Q (legal and investigation disclosures, by about mid-Dec 2026); the 75% FY28 outlook holding after the new BIS export rule; 2027 hyperscaler capex guides and Q4 FY27 (late Jan to late Feb 2027). Price: about $142 for a 20% base-case return | — | 2026-12-15 |
| 2026-11-18 | Fiserv (FISV) | Earnings-update: fresh money Wait (confirmed); held | Evidence: Q4 2026 organic growth of about 5% or more (Merchant +6-8%, Clover double digits) and a 2027 guide of at least 3% organic with a higher margin (Feb 2027). Price: about US$52 for the conservative case to clear 15% | 31 | 2027-02-15 |
| 2026-11-19 | Tencent Music (TME) | Earnings-update: fresh money Wait (confirmed) | Evidence: Q4 organic membership flat or better and year-end paying users of 125m or more (FY2026 results, about mid-March 2027). Price: about US$8.10 for the conservative case to clear 15% | — | 2027-03-17 |
| 2026-11-19 | Tencent (0700-HK) | Earnings-update: fresh money Wait (confirmed) | Evidence: Q4 ex-AI operating margin at or above 41% with the AI drag at or below RMB 15bn, and an FY2026 buyback of at least HK$50bn or a stated 2027 figure (FY2026 results, about 2027-03-18). Price: about HK$285 for the conservative case to clear 15% | — | 2027-03-18 |
| 2026-11-19 | JD.com (JD) | Earnings-update: fresh money Wait (confirmed) | Evidence: a Q4 New Businesses loss at or below RMB 9bn with a 2027 budget, and an annual dividend of at least US$1.00 per ADS with repurchases resumed (Q4/FY2026 results, about early March 2027). Price: about US$21 for the conservative case to clear 15% | — | 2027-03-05 |
| 2026-11-20 | PDD Holdings (PDD) | Triage: Dig (proposed); earnings-update fresh money Wait (proposed) | Framing/duration: market reads the 2024-26 investment phase as a permanent margin reset while online marketing re-accelerates (+12% in Q3). Wait evidence: Q4 online marketing ≥10% and S&M ≤26% of revenue (late Mar 2027), HNTE confirmed in FY2026 20-F. Price: about US$53 for the conservative case to clear 15% | 35 | 2027-03-31 |
| 2026-11-24 | Tencent Music (TME) | Watch: monitor (Paul, 2026-11-24); fresh money Wait | Evidence unchanged: Q4 organic membership flat or better and year-end paying users of 125m or more (FY2026 results, about mid-March 2027); also ByteDance/Soda licence renewals and whether TME keeps up its free-tier response. Price: about US$8.30 for the probability-weighted case (30/50/20) to clear 15%; US$8.10 for the conservative case | — | 2027-03-17 |
| 2026-11-26 | Full Truck Alliance (YMM) | Watch (Paul, 2026-11-26; short path) | Views not yet tested: a commission cap comes much later (probability); fulfilment has runway (duration). Drop if a large commission cap, or order growth well below 10% for two quarters | 15 | 2027-03 |
| 2026-11-27 | Sankyo (6417.T) | Triage: Dig, narrow (proposed) | Next: frame, then likely price-alone check; desk work on the earnings base and governance | 4 | — |
| 2026-11-27 | Yunnan Aluminium (000807.SZ) | Triage: Defer (proposed) | Trigger: about RMB 18-21 (Claude's arithmetic), the aluminium cycle at Downturn or Trough, or ten-year margins showing a higher mid-cycle | 18 | 2027-04 |
| 2026-11-27 | Sankyo (6417.T) | Triage: Dig, narrow (confirmed by Paul) | Next: frame, then likely price-alone check | 4 | — |
| 2026-11-27 | Yunnan Aluminium (000807.SZ) | Triage: Defer (confirmed by Paul) | Trigger: about RMB 16-19 (Claude's arithmetic, revised after the cycle-note check), the aluminium cycle at Downturn or Trough, or a lasting alumina glut that lifts mid-cycle | 18 | 2027-04 |
