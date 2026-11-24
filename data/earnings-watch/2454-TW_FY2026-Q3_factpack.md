> Working file of the earnings watch, saved 2026-11-24 so the collection need not be repeated. It is the extract of MediaTek's Q3 2026 release, presentation, call script and two third-party transcripts made while checking readiness. It is data, not a note: no judgments, and nothing here has been reviewed by Paul. The update for this period is paused until the Q3 2026 financial statements can be read (see `monitoring.md`). Delete this file once `companies/2454-TW/earnings/FY2026-Q3.md` is written.

# MediaTek (TWSE 2454) — Q3 2026 fact pack

Quarter ended 2026-09-30. Results and call 2026-10-30. Compiled 2026-11-23/24 from pages fetched in this session only.

**How to read this file**

- Source tags `[S1]`…`[S20]` map to URLs in section 10.
- Three kinds of statement are kept apart: **Fact** (printed in a company document or filing), **Mgmt claim** (speaker named), **Computed** (my arithmetic from the facts; always labelled).
- All amounts are NT$ million unless stated. "bn" = billion.
- The fetch tool returns a model-made extraction of each page, not raw text. Tables below are as extracted; quotes are short fragments the tool returned as verbatim. Check any quote against the replay before publishing it.
- NOT FOUND means I could not read it in a fetched page. Nothing is filled from memory.

---

## 0. Readiness check (Part 1)

| Doc | Status | URL read | Gaps |
|---|---|---|---|
| (a) Press release | Read in full (6 pages, no truncation reported) | [S1] | Contains no 9M figures and no guidance. One wording error in the release on selling expenses (text contradicts its own table). |
| (b) Consolidated financial statements | **NOT READ** | Company PDF [B1] and reviewed consolidated report [B2] both refused by the fetch tool | Only summary IS / BS / CF from [S1] and [S2], plus 9M headline figures from the exchange filing [S8]. Missing: full balance sheet lines (PP&E, bonds payable, equity components), full cash flow lines (capex, D&A, dividends paid, bond proceeds), non-operating breakdown, diluted EPS, all notes. |
| (c) Presentation | Read in full (20 slides) | [S2] | None. |
| (d) Call transcript | Full third-party transcript read; company script read | [S4] Investing.com (best), [S5] gloom.sh, [S3] company script | See below. |

**Transcript detail**

- **Company script [S3]** (公司講稿, 6 pages): prepared remarks only, English then Chinese. Ends with a "[Q&A]" placeholder. No analyst questions.
- **Company "Transcript.pdf" [B3]**: listed on the IR page but refused by the fetch tool. Not read. (The Q1 and Q2 2026 company transcripts do include Q&A, so this file probably does too.)
- **Investing.com [S4]** — best available. Speakers: operator, Jessie Wang (IR), David Ku (CFO), Rick Tsai (CEO); analysts Gokul Hariharan (JPMorgan), Sunny Lin (UBS), Haas Liu (BofA), Charlie Chan (Morgan Stanley), Robert Sanders (Deutsche Bank), Arthur Lai (Macquarie). Six analysts, 17 exchanges as I number them (the tool counted 16 plus follow-ups). Runs to the operator's sign-off ("You may disconnect now. Thank you and goodbye."). No paywall cut-off.
  - Gaps: AI-generated transcript. One "[Foreign language]" tag in a Tsai answer to Haas Liu. A passage of untranslated Chinese in a Tsai answer to Charlie Chan. Known mis-transcriptions: operating income given as "NT$47.1B" (company figure is NT$27.1bn), "Richard" for Charlie, "M6" for N6. No "[indiscernible]" tags.
- **gloom.sh [S5]** — second full transcript, automated. Same six analysts, 21 question turns. Ends at "-End of Q&A session-" with no closing remarks. Used to cross-check [S4].
- One conflict between the two: [S4]'s extraction has Charlie Chan citing "Q1" operating margin guidance of ~19%; [S5] quotes him as "fourth quarter operating margin to be around 19%". Q4 is consistent with the guidance (45% − 26%).
- **Not readable**: stockanalysis [B4] (refused), GuruFocus [B5] and Yahoo Finance [B6] (site error), Quartr [S14] (summary only, no transcript text).

---

## 1. Income statement

### 1a. Quarterly (Fact — [S1], [S2])

| NT$ m | 3Q26 | 2Q26 | 3Q25 | QoQ | YoY |
|---|---|---|---|---|---|
| Net sales | 168,058 | 152,183 | 142,097 | 10.4% | 18.3% |
| Operating costs | (90,209) | (81,875) | (75,985) | | |
| Gross profit | 77,848 | 70,308 | 66,112 | 10.7% | 17.8% |
| Gross margin | 46.3% | 46.2% | 46.5% | +0.1pt | −0.2pt |
| Selling | (4,874) | (4,685) | (4,984) | | |
| G&A | (3,635) | (3,395) | (2,588) | | |
| R&D | (42,237) | (39,361) | (36,353) | | |
| Total opex | (50,746) | (47,440) | (43,924) | 7.0% | 15.5% |
| Operating income | 27,102 | 22,868 | 22,188 | 18.5% | 22.2% |
| Operating margin | 16.1% | 15.0% | 15.6% | +1.1pt | +0.5pt |
| Net non-operating income | 6,471 | 5,094 | 7,772 | | |
| Pre-tax income | 33,573 | 27,962 | 29,960 | | |
| Income tax | (5,374) | (3,357) | (4,509) | | |
| Net income | 28,199 | 24,605 | 25,451 | 14.6% | 10.8% |
| Owners of the parent | 27,882 | 24,335 | 25,221 | 14.6% | 10.6% |
| Non-controlling interests | 316 | 270 | 230 | | |
| EPS (NT$) | 17.50 | 15.28 | 15.84 | | |
| Avg USD/NTD | 31.99 | 31.60 | 29.95 | | |

% of revenue (Fact — [S1]): selling 2.9 / 3.1 / 3.5; G&A 2.2 / 2.2 / 1.8; R&D 25.1 / 25.9 / 25.6; non-operating 3.9 / 3.3 / 5.5; tax 3.2 / 2.2 / 3.2; net income 16.8 / 16.2 / 17.9.

Non-TIFRS (Fact — [S1], [S2])

| NT$ m | 3Q26 | 2Q26 | 3Q25 |
|---|---|---|---|
| Share-based compensation | 783 | 781 | 561 |
| Amortisation of acquisition-related assets | 38 | 38 | 95 |
| Tax effect | (125) | (119) | (98) |
| Non-TIFRS operating income | 27,923 | 23,687 | 22,843 |
| Non-TIFRS operating margin | 16.6% | 15.6% | 16.1% |
| Non-TIFRS net income | 28,895 | 25,305 | 26,007 |
| Non-TIFRS net income, owners | 28,563 | 25,020 | 25,762 |
| Non-TIFRS EPS (NT$) | 17.92 | 15.71 | 16.18 |

Computed from the table above:

| | 3Q26 | 2Q26 | 3Q25 |
|---|---|---|---|
| Opex / revenue | 30.2% | 31.2% | 30.9% |
| Tax / pre-tax income | 16.0% | 12.0% | 15.1% |
| Revenue in US$ at the average rate | US$5.25bn | US$4.82bn | US$4.74bn |
| US$ revenue growth | +9.1% QoQ, +10.7% YoY | | |

About 7.6 points of the 18.3% YoY NT$ revenue growth came from the weaker NT dollar (computed: 18.3% less 10.7%).

### 1b. Nine months

| NT$ m | 9M26 | 9M25 | YoY | Source |
|---|---|---|---|---|
| Revenue | 469,391 | 445,778 | +5.3% | 9M26 Fact [S8]; 9M25 Computed = 1H25 [S7] + 3Q25 [S1] |
| Gross profit | 217,211 | 213,799 | +1.6% | same |
| Gross margin | 46.3% | 48.0% | −1.7pt | Computed; matches [S12] |
| Operating expenses | 144,351 | 132,179 | +9.2% | Computed (gross profit − operating income) |
| Operating income | 72,861 | 81,620 | −10.7% | 9M26 Fact [S8]; 9M25 Computed |
| Operating margin | 15.5% | 18.3% | −2.8pt | Computed |
| Net non-operating income | 15,693 | NOT FOUND | | 9M26 Computed (pre-tax − operating income) |
| Pre-tax income | 88,554 | NOT FOUND | | Fact [S8] |
| Income tax | 11,374 | NOT FOUND | | Computed; 12.8% of pre-tax |
| Net income | 77,180 | 83,044 | −7.1% | 9M26 Fact [S8]; 9M25 Computed |
| Owners of the parent | 76,371 | 82,394 | −7.3% | same |
| Basic EPS (NT$) | 47.94 | 51.76 | −7.4% | 9M26 Fact [S8]; 9M25 Computed (35.92 + 15.84) |

Cross-check: 1Q26 + 2Q26 + 3Q26 from [S1] and [S10] sum to the [S8] figures on every line. R&D, selling and G&A for 9M: 9M26 computed from the three quarters = R&D 119,943, selling 14,574, G&A 9,834. 9M25 split NOT FOUND.

### 1c. Q3 guidance (given 2026-07-31) against actual

| Item | Guided [S9], [S10] | Actual [S1] | Result |
|---|---|---|---|
| Revenue | NT$152.2–159.8bn (flat to +5% QoQ, +7% to +12% YoY) | NT$168.058bn | Above the top end by NT$8.3bn, 5.2% (computed) |
| Gross margin | 46% ± 1.5pt | 46.3% | In range |
| Opex ratio | 31% ± 2pt | 30.2% (computed) | In range |
| USD/NTD | 32.0 assumed | 31.99 realised | In line |
| Mobile Phone | flat to down mid-single digit QoQ | −1% | In range |
| Smart Edge Platforms | up mid-to-high single digit QoQ | +20% | Well above |
| Power IC | roughly flat QoQ | +1% | In line |

Mgmt claim (Tsai, [S3]): revenue "beat the guidance range again" on better-than-expected customer demand and improving supply; gross margin in line with expectations.

---

## 2. Revenue by product group, Q3 2026 (Fact — [S2] slide 19, [S3])

| Group | Share | QoQ | YoY | Approx. NT$bn (computed from rounded share) |
|---|---|---|---|---|
| Mobile Phone | 37% | −1% | −17% | 62.2 |
| Smart Edge Platforms | 58% | +20% | +63% | 97.5 |
| Power IC | 5% | +1% | +18% | 8.4 |
| Total | 100% | +10% | +18% | 168.1 |

Prior quarters for reference (Fact): 2Q26 = 41% / 53% / 6% [S10]; 1Q26 = 49% / 46% / 5% [S11].

- **No change in segment definitions** between the Q2 and Q3 presentations [S10], [S2]. There is **no separate data-centre / AI ASIC line**. The ASIC business sits inside Smart Edge Platforms ("customized service for consumer/enterprise platforms"); the offering circular confirms it is reported within Smart Edge Platforms [S7].
- Mgmt claims (Tsai, [S3]):
  - Mobile: flagships outperformed; first 2nm Dimensity 9600 Pro launched.
  - Smart Edge: growth from volume production of a 5G thin modem for a new smartphone customer, AI tablets, AI PCs and automotive cockpits; TV SoC revenue up on "higher DRAM content" than a year ago. Note the thin modem is booked in Smart Edge, not Mobile.
  - Power IC: growth mainly from share gains in data-centre-related business.
- Initial AI accelerator shipments began in September (Tsai, [S3]). The Q3 revenue amount from them is NOT FOUND.

---

## 3. Balance sheet and cash flow

### 3a. Balance sheet summary (Fact — [S1], [S2] slide 15; 1Q26 from [S10])

| NT$ m | 3Q26 | 2Q26 | 1Q26 | 3Q25 |
|---|---|---|---|---|
| Cash & current financial assets | 278,320 | 198,403 | 194,779 | 210,604 |
| Accounts receivable | 80,296 | 76,981 | 79,245 | 67,168 |
| Inventories | 153,531 | 98,421 | 85,470 | 56,964 |
| Other current assets | 34,595 | 23,200 | 18,690 | 24,215 |
| Funds and investments | 182,116 | 181,064 | 172,265 | 157,900 |
| Intangible assets | 101,793 | 97,509 | 87,580 | 80,240 |
| Other non-current assets | 135,855 | 111,869 | 100,746 | 90,762 |
| Total assets | 966,505 | 787,448 | 738,776 | 687,852 |
| Short-term loans | 41,950 | 17,100 | 16,440 | 15,423 |
| Accounts payable | 79,530 | 51,328 | 49,559 | 37,855 |
| Other current liabilities | 219,735 | 251,891 | 243,808 | 178,226 |
| Total non-current liabilities | 151,078 | 34,488 | 30,522 | 27,803 |
| Total equity | 474,212 | 432,642 | 398,447 | 428,544 |

Other facts at 2026-09-30 ([S8]): total liabilities NT$492,293m; equity attributable to owners NT$465,427m.

Working-capital days (Fact — [S1]): receivables 43 days (2Q26 47, 3Q25 44); inventory 127 days (2Q26 102, 3Q25 68). Payables days: not disclosed.

Computed:

- Inventories +NT$55.1bn, +56.0% QoQ; +169.5% YoY.
- Accounts payable +NT$28.2bn, +54.9% QoQ.
- Short-term loans +NT$24.9bn QoQ.
- Non-current liabilities +NT$116.6bn QoQ (the convertible bond closed 2026-09-08; the bond's carrying amount is NOT FOUND).
- Non-controlling interests ≈ NT$8,785m (474,212 − 465,427).
- Cash and current financial assets less short-term loans less bond face value (NT$123.4bn) ≈ NT$113bn. Uses face value, not carrying value.

### 3b. Cash flow summary (Fact — [S1], [S2] slide 16; 1Q26 from [S10])

| NT$ m | 3Q26 | 2Q26 | 1Q26 | 3Q25 |
|---|---|---|---|---|
| Operating activities | (4,256) | 24,251 | (17,657) | 39,181 |
| Investing activities | (23,417) | (19,590) | (4,091) | (3,370) |
| Financing activities | 107,703 | (12) | (31,138) | (31,020) |
| FX effect | 27 | (162) | 2,110 | 7,631 |
| Net change in cash | 80,057 | 4,486 | (50,775) | 12,421 |
| Cash at period end | 269,058 | 189,001 | 184,515 | 197,770 |

- 9M26 operating cash flow = NT$2,338m (computed: −17,657 + 24,251 − 4,256). 1H26 operating cash flow NT$6,594m against NT$59,092m in 1H25 (Fact, [S7]).
- **Capex, Q3 2026: NOT FOUND** (full cash flow statement not read). Reference facts: 1Q26 purchase of PP&E NT$4,260m [S13]; 1H26 capex on PP&E and intangibles NT$20,742m; FY2025 NT$25,420m; FY2024 NT$22,513m [S7].
- **Free cash flow, Q3 2026: NOT FOUND** for the same reason. Operating plus investing cash flow = −NT$27,673m (computed; investing includes financial assets, so this is not free cash flow).
- The release gives no reason for the negative operating cash flow or the inventory build. Neither was raised on the call ([S4], [S5]).
- 1H26 cash flow shows an inventory increase of NT$31,300m and a rise in refundable deposits of NT$6,567m (Fact, [S7]).

### 3c. Convertible bond (Fact — offering circular [S7] unless stated)

| Term | Detail |
|---|---|
| Instrument | Currency-Linked Zero Coupon Convertible Bonds due 2031, US$-denominated |
| Size | US$3,900,000,000 (Rule 144A and Regulation S) |
| Priced / closed | 2026-08-31 / 2026-09-08 (expected closing date in the circular) |
| Maturity | 2031-09-08, redeemed at 100% |
| Coupon / issue price / yield | Zero / 100% / 0.00% |
| Conversion price | NT$4,513.75 per share |
| Reference share price | NT$3,925.00 (TWSE close 2026-08-31) |
| Premium | 15.0% (computed) |
| Fixed exchange rate | NT$31.6430 = US$1 |
| Conversion period | 2026-12-09 to 2031-08-29, excluding closed periods |
| Holder puts | Delisting / 30-day trading suspension; change of control |
| Issuer calls | Clean-up when over 90% converted or redeemed; tax redemption |
| Use of proceeds | "procurement of raw materials in foreign currencies"; no further breakdown |
| Named investor | NVIDIA subscribed US$3.5bn on the same terms as other holders |
| Alphabet | Participation stated by Tsai on the call [S3]. Amount NOT FOUND; not named in the 300k characters of the circular I read |
| Bookrunner / listing | Morgan Stanley Asia (sole) / SGX-ST |
| Lock-up | Company, 90 days from closing |
| As-adjusted bonds payable | NT$123,408m at the fixed rate, before any equity/derivative split |

- Dilution (computed): US$3.9bn × 31.6430 ÷ 4,513.75 ≈ 27.3m shares, about 1.7% of ~1,604.9m shares.
- Conversion is suspended 2026-12-15 to 2027-01-11 for the dividend record date; last application date 2026-12-11 (Fact, [S15]). Any dividend adjustment to the conversion price: NOT FOUND.
- Mgmt claim (Tsai, [S3]/[S5]): the bond strengthens partnerships and "enhanced our ability to secure capacity for critical components".
- Only characters 0–300,000 of the 1.45m-character circular were read. Capitalisation table read; full terms and conditions not read.
- A secondary article [S16] gives the maturity as 2027; the circular says 2031.
- Earlier context (Mgmt claim, Ku, 2Q26 call [S9]): the board approved a discretionary US$5bn financing budget to secure supply-chain capacity; cash then "over US$7B".

### 3d. Dividends and share count

| Item | Fact | Source |
|---|---|---|
| 1H26 dividend, board resolution 2026-10-30 | NT$24.5 per share cash, all from earnings; total NT$39,320,596,791 | [S17], [S15] |
| Ex-dividend / record / payment | 2027-01-05 / 2027-01-11 / 2027-01-29 | [S15], [S6] |
| Prior half-year dividends | FY2025: 1H NT$29.00, 2H NT$24.50. FY2024: 1H NT$29.00, 2H NT$25.00. FY2023: 1H NT$24.60, 2H NT$30.40 | [S7] |
| Cash dividends paid, 1Q26 | NT$46,287m | [S13] |
| Payment date of the 2H25 dividend | 2026-07-31 (falls in Q3 2026) | [S6] |
| Share capital at 2026-06-30 | NT$16,038,954 thousand at NT$10 par | [S7] |
| Dividend policy | Half-yearly distribution permitted; may distribute up to all distributable profits | [S7] |

Computed: share count ≈ 1,603.9m at 2026-06-30 (share capital ÷ par); ≈ 1,604.9m implied by the dividend total ÷ NT$24.5. 1H26 payout = 24.5 ÷ 30.44 (1H26 basic EPS, [S7]) = 80%. Dividends were not mentioned on the call ([S4], [S5]).

---

## 4. Earnings quality

| Item | What was read | Source |
|---|---|---|
| Inventory write-downs / reversals | NOT FOUND (needs the notes) | — |
| FX on revenue | NT$ weaker: 31.99 vs 31.60 QoQ and 29.95 YoY. US$ revenue +9.1% QoQ, +10.7% YoY (computed) vs NT$ +10.4% / +18.3% | [S1] |
| FX on gross margin | NOT FOUND; company says only "Gross margin remained stable" | [S1] |
| FX gains/losses in non-operating | NOT FOUND | — |
| Non-operating income | NT$6,471m; "mainly from interest income and dividend income". Line-item split NOT FOUND | [S1] |
| Investment gains | NOT FOUND | — |
| Tax rate | 16.0% in 3Q26 vs 12.0% in 2Q26 and 15.1% in 3Q25 (computed). 1H26 rate was lowered by an adjustment to prior tax estimates and lower Pillar Two expense | [S1], [S7] |
| Stock compensation | NT$783m (2Q26 781; 3Q25 561) | [S1] |
| One-offs in Q3 | None identified by the company | [S1], [S3] |
| Pass-through revenue | TV SoC revenue lifted by higher DRAM content | [S1], [S3] |
| Price increases | Ku: price adjustment for non-data-centre business "starting from third quarter", to reflect supply-chain cost increases | [S5] |
| Base effects | 2Q25 gross margin had a one-time benefit (Ku, 2Q26 call); 2025 costs included a one-time reversal of capacity-related costs | [S9], [S7] |
| Concentration | Two customers above 10% of sales in 1H26, 20.3% combined (three in 2025, 38.9%). Top three suppliers 82.5% of purchases in 1H26 | [S7] |

---

## 5. Guidance

### 5a. Q4 2026 (Fact — [S2] slide 11; [S3])

| Item | Guidance |
|---|---|
| Revenue | NT$210.1–221.8bn; +25% to +32% QoQ; +40% to +48% YoY — **confirmed** |
| USD/NTD | 31.7 |
| Gross margin | 45% ± 1.5pt (down from 46% ± 1.5pt guided for Q3) |
| Opex ratio | 26% ± 2pt (down from 31% ± 2pt guided for Q3) |

Computed from the guidance:

- Revenue in US$: US$6.63–7.00bn.
- Implied operating margin ≈ 19% at the mid-points (45% − 26%); implied operating income ≈ NT$41bn at the revenue mid-point, against NT$27.1bn in Q3.
- US$2.5bn of accelerator revenue at 31.7 = NT$79.3bn = 36–38% of guided Q4 revenue. Analysts on the call spoke of "about 30%".
- Guided revenue less NT$79.3bn = NT$130.9–142.6bn. That is 15–22% below Q3 revenue and 5–13% below 4Q25 revenue of NT$150.2bn [S18]. This assumes all US$2.5bn lands in Q4; Ku's wording was "mainly for fourth quarter".
- October revenue was NT$55.025bn (−0.7% MoM, +5.8% YoY) [S19]; November plus December must total NT$155.1–166.8bn to land in the range.

### 5b. Full-year 2026

- Mgmt claim (Tsai, [S3]): full-year US$ revenue growth now expected "to exceed our previous target" of high-single-digit growth. No new number given.
- Computed: 9M actual plus Q4 guidance = NT$679.5–691.2bn, +14% to +16% on FY2025's NT$596.0bn [S7]. In US$ at quarterly average rates ≈ US$21.4–21.8bn, +12% to +14% on US$19.1bn [S18].
- Gross margin: "Quarterly gross margin is expected to be within the current range" (Tsai, [S3]).

### 5c. AI accelerator / data centre (Mgmt claims — [S3], [S4], [S5])

| Topic | Statement | Speaker |
|---|---|---|
| Q4 2026 revenue | "confident of delivering $2.5 billion revenue in the fourth quarter"; previously "slightly higher than $2 billion" | Tsai; prior figure per analyst |
| 2026 total | "'26, we deliver… $2.5 billion", "mainly for fourth quarter" | Ku |
| 2027 revenue | First accelerator to reach "the high end of our revenue target range of approximately US$16 billion" | Tsai |
| 2027 share | "around 20% of the total AI accelerator ASIC market" | Tsai |
| 2027 operating margin (company) | "20% plus, if not slightly higher" | Ku |
| Data-centre margin | Gross margin below corporate average; operating margin accretive "starting from fourth quarter" | Ku |
| 2028 | "another year of strong growth"; no figure, supply still being finalised | Ku |
| Second accelerator | High-volume production on track for 1Q28; "multiple times higher performance per watt" | Tsai |
| Second-gen tape-out | "a couple dies have been taped out already"; one large die takes "a couple three weeks longer"; die count not disclosed | Tsai |
| Second customer | Confirmed; joint design kicked off; first revenue 2028; "not coming from China"; identity not given | Ku |
| Third generation | No comment | Tsai |
| Customers named | None named for the ASIC. NVIDIA and Alphabet named only as bond investors; NVIDIA as NVLink Fusion and N1X partner | Tsai |
| Number of projects | "several customers" in engagement; one in production, one follow-on, one second customer | Tsai, Ku |
| Process node | Not stated for the ASIC on this call. 448G SerDes test design taped out on N6 | Tsai |
| Packaging | "US IDM packaging process as our absolute priority"; working with a Japanese and a Taiwanese supplier on yield; "not dependent on one supplier"; "TSMC is our most important partner, period" | Tsai |
| EMIB-T / CoWoS | Named only by analysts. Management did not use either term on this call | — |
| Capacity | Outlook "supported by supply"; seeking additional capacity; multiple substrate suppliers added | Tsai |
| Technology | 448G SerDes, 3.5D packaging, co-packaged optics; rack solutions via NVLink Fusion and UALink | Tsai |
| Vendor financing | Would consider "if it's necessary", with the right customer | Ku |

CoWoS capacity figures: NOT FOUND. Dollar size of the 2027 market: not given on this call (US$80bn SAM was given in July, [S9]).

### 5d. Other topics

| Topic | Q3 call | Earlier 2026 statements |
|---|---|---|
| Smartphone market | Not discussed | Units expected down about 15% in 2026 (Tsai, [S9], [S11]) |
| Flagship SoC share | "Flagship outperformed"; no share figure | Further flagship share gains expected in 2027 (Tsai, [S9]) |
| Wafer / memory cost inflation | No figures. Ku: price adjustments "to reflect… the cost increase for the whole supply chain" | "rising costs across the supply chain have become an industry-wide reality" (Tsai, [S9]); aim is to hold, not raise, gross margin (Ku, [S9]) |
| Gross margin trajectory | Q4 guided 1 point lower because data-centre margin is below average (Ku) | Per-generation ASIC gross margin "slightly diluted" vs corporate (Ku, [S9]) |
| Opex growth | Not discussed beyond the Q4 ratio | Ratio to fall substantially; absolute opex to rise slightly (Ku, [S9]) |
| Dividend policy | Not discussed | — |
| 2027 revenue (company total) | No figure | — |

---

## 6. The call (2026-10-30, 3:00pm Taiwan time)

### 6a. Prepared remarks ([S3], cross-checked with [S4])

- Ku read the results table (section 1a). No commentary on balance sheet, cash flow, inventory or the bond.
- Tsai stressed, in order:
  1. Revenue above guidance again on demand and supply.
  2. The US$3.9bn convertible bond with NVIDIA and Alphabet.
  3. First AI accelerator: shipments from September, US$2.5bn in Q4, high end of ~US$16bn in 2027, about 20% share.
  4. Second accelerator on track for high-volume production in 1Q28.
  5. Move from chips into system and rack solutions (NVLink Fusion, UALink).
  6. Edge: RTX Spark AI PC with the N1X chip on sale since mid-October; second-generation SoC with NVIDIA started; Dimensity 9500 in Samsung Galaxy Tab S12.
  7. Segment results and Q4 guidance; full-year US$ growth above the prior target.

### 6b. Q&A ([S4] and [S5]; answers paraphrased, quotes are short fragments)

| # | Analyst | Question | Answer | Type |
|---|---|---|---|---|
| 1 | Gokul Hariharan, JPMorgan | Reports of second-gen ASIC design and tape-out delays; milestones to 1Q28; 2028 revenue and share | Tsai: on schedule; "a couple dies have been taped out already"; the large die will take "a couple three weeks longer"; die count not disclosed. Ku: 2027 aims at the high end of the US$16bn range; 2028 "another year of strong growth", no detail | Schedule answered qualitatively; 2028 not answered |
| 2 | Gokul Hariharan | Is the US IDM packaging choice final or hedged; is packaging the main limit on 2028 | Tsai: US IDM packaging is the "absolute priority"; new manufacturing team; yield work with the IDM, a Japanese and a Taiwanese supplier; "very high confidence that the yield will go up very quickly" | Qualitative; limiting-factor part not answered |
| 3 | Sunny Lin, UBS | Third-gen ASIC (ramp late 2029); growth into 2029–30 | Tsai: cannot speak for the customer; next chip still being defined | Not answered |
| 4 | Sunny Lin | New cloud ASIC engagements; 2027 revenue from them. Follow-up: is it a different customer | Ku: second customer confirmed, project kicking off, first revenue 2028. "Yes… different customer" | Answered with a date; no revenue size |
| 5 | Haas Liu, BofA | Why Q4 ASIC is US$2.5bn vs just over US$2bn before (volume or price); how gross margin holds at 44–46% with ASIC ~30% of Q4. Follow-up: operating margin accretive from Q4 | Tsai: strong demand and supply work, multiple suppliers including substrates. Ku: data-centre gross margin below average, so "we guide down… one percentage point"; price adjustments reflect supply-chain cost; operating margin accretive "starting from fourth quarter" | Numbers on margin; volume/price split not answered |
| 6 | Haas Liu | Does 2028 revenue from the second customer imply a design milestone | Ku: joint design kick-off has happened; more later | Qualitative |
| 7 | Charlie Chan, Morgan Stanley | Q4 guidance implies ~19% operating margin; is data centre ~10 points above average and will the gap widen | Ku: data-centre operating margin is higher, not quantified; Q4 also reflects a price adjustment "starting from third quarter for non-data center business" | Not quantified |
| 8 | Charlie Chan | Is the second customer an AI lab or tied to NVLink Fusion; if CSP capex slows, GPU or ASIC first | Ku: second customer "not coming from China". Tsai: compute demand keeps growing over one to three years; "a huge TAM"; strong co-designed chips "will win out" | Identity not answered; rest qualitative |
| 9 | Robert Sanders, Deutsche Bank | Dependence on EMIB-T; could Intel tie packaging to its foundry | Tsai: "we are not dependent on one supplier"; "TSMC is our most important partner, period" | Qualitative |
| 10 | Robert Sanders | A competitor offers aggressive financing; is it worth serving loss-making frontier model companies | Ku: vendor financing considered "if it's necessary" with the right customer; "at least one of the new frontier models is actually about to file for IPO"; customers' revenue-to-capex has improved for six quarters | Qualitative |
| 11 | Arthur Lai, Macquarie | Long-term operating margin; is Q4's level sustainable | Ku: Q4 is the starting point; 2027 full year "20% plus, if not slightly higher"; gross margin slightly dilutive, operating margin accretive | Answered with numbers |
| 12 | Arthur Lai | How many years ahead on EMIB-T and HBM5 | Tsai: the barrier is integrating technologies into a manufacturable, scalable product; would not claim to be far ahead | Not quantified |
| 13 | Gokul Hariharan | How NVLink Fusion is integrated; customer benefit | Tsai: credentials with NVIDIA "can match anybody"; a chassis customers drop their XPU or CPU into, sold as a rack | Qualitative |
| 14 | Gokul Hariharan | Early customer feedback on NVLink Fusion | Ku: several potential customers in discussion with NVIDIA; positive feedback; hopes to announce a case near term | Qualitative |
| 15 | Gokul Hariharan | Does MediaTek become majority source for the lead customer in 2028; second-gen competitiveness | Ku: "multiple times better" performance and better TCO; competing projects "not even close" | Majority-source part not answered |
| 16 | Charlie Chan | Is 448G SerDes for the third-gen project or the second customer | Tsai: 448G is "a must"; an N6 design has taped out and is in silicon measurement; "will not be on the critical path" | Qualitative |
| 17 | Charlie Chan | 2028 revenue size and margin of the second customer; if EMIB-T supply falls short, does gen-1 extend or demand move to a rival on CoWoS | Ku: too early; 2026 delivers about US$2.5bn mainly in Q4; 2027 targets the high end. Gen-1 demand good; gen-2 deliverable on current yield; "you can't really find… the replacement" | Size not answered; rest qualitative |

Not raised by any analyst and not addressed by management: the NT$55bn inventory build, negative operating cash flow, use of bond proceeds, dividends, smartphone market, memory prices, tax rate, 2027 opex, the next results date.

---

## 7. The presentation ([S2]; compared with Q2 [S10])

- 20 slides, same order and titles as Q2: revenue, gross margin, opex, operating income and margin, net income and margin, EPS, business outlook, TIFRS statements, balance sheet summary, cash flow summary, non-TIFRS reconciliation, product group breakdown.
- **Nothing added, dropped or redefined.** No slide on the AI accelerator, the convertible bond, inventory or the 2027 targets. All of that is in the spoken remarks only.
- Slide 11 (outlook): opex ratio guide drops from 31% to 26%; gross margin guide from 46% to 45%.
- Slide 15: total assets up NT$179bn in one quarter; inventories NT$153.5bn; non-current liabilities NT$151.1bn.
- Slide 16: operating cash flow negative NT$4.3bn; financing inflow NT$107.7bn.
- Slide 19: Smart Edge Platforms 58% of revenue, up from 53% in Q2 and 46% in Q1.

---

## 8. Guidance log (Mgmt claims from each quarter's company transcript)

| Date / call | 2026 revenue | Data-centre ASIC 2026 | 2027 | Market size and share | Second ASIC | Other |
|---|---|---|---|---|---|---|
| 2026-02-04, 4Q25 [S18] | Growth, no figure | "more than 1 billion US dollars" | "multiple billion US dollars" | SAM ~US$50bn, possibly ~US$70bn by 2028; share 10–15% | Follow-on project, revenue from 2028 | Gross margin "around 46%" |
| 2026-04-30, 1Q26 [S11] | US$ up mid-to-high single digit | About US$2bn in Q4 2026 | Multiple billions | US$70–80bn in 2027; share 10–15% | Mass production by end-2027 | Smartphone units about −15% |
| 2026-07-31, 2Q26 [S9] | High end of high-single-digit US$ growth | Above US$2bn | "scaling substantially" | 2027 SAM US$80bn; share 15–20% | Early production early 2028; high volume 2028 | US$5bn financing budget; first ASIC production from Q4 |
| 2026-10-30, 3Q26 [S3]–[S5] | Above the prior high-single-digit target | US$2.5bn in Q4 | High end of ~US$16bn; operating margin 20%+ | About 20% share | High-volume production 1Q28 | Second customer, revenue 2028 |

Computed: 15–20% of US$80bn = US$12–16bn, which matches the "range of approximately US$16 billion" wording. The 1Q26 row is from the tool's summary of the company transcript; the "end-2027" wording should be checked against the PDF before it is used to argue a slip.

Quarterly guidance record (Fact): 1Q26 guided NT$141.2–150.2bn, actual NT$149.2bn [S18], [S11]. 2Q26 guided NT$140.2–149.2bn, actual NT$152.2bn [S11], [S10]. 3Q26 guided NT$152.2–159.8bn, actual NT$168.1bn.

---

## 9. Q4 2026 results date

**NOT FOUND — no date announced.** The company's IR events page [S6] lists nothing for 4Q26 results. Its upcoming entries are: November sales 2026-12-10; ex-dividend 2027-01-05; December sales 2027-01-08; dividend payment 2027-01-29; January sales 2027-02-11. For reference, the 4Q25 call was held 2026-02-04 [S6].

---

## 10. Sources

**Read**

| Tag | What | URL |
|---|---|---|
| S1 | 3Q26 press release (company) | https://www.mediatek.com/hubfs/MediaTek-Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q3/Press%20Release.pdf |
| S2 | 3Q26 presentation (company) | https://www.mediatek.com/hubfs/MediaTek-Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q3/Presentation.pdf |
| S3 | 3Q26 call script, prepared remarks only (company) | https://www.mediatek.com/hubfs/MediaTek-Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q3/%E5%85%AC%E5%8F%B8%E8%AC%9B%E7%A8%BF.pdf |
| S4 | 3Q26 full call transcript, AI-generated (Investing.com) | https://www.investing.com/news/transcripts/earnings-call-transcript-mediatek-tops-q3-2026-estimates-as-stock-falls-93CH-4989438 |
| S5 | 3Q26 full call transcript, automated (gloom.sh) | https://gloom.sh/stocks/2454:twse/transcripts/q3-2026 |
| S6 | Company IR events calendar | https://www.mediatek.com/investor-relations/ir-events |
| S7 | Convertible bond final offering circular, 2026-08-31 (SGX); first 300k characters read | https://links.sgx.com/FileOpen/MediaTek%20Inc.%20-%20Final%20Offering%20Circular%20dated%2031%20August%202026.ashx?App=Prospectus&FileID=70978 |
| S8 | Exchange filing: board approval of 3Q26 consolidated report, 9M figures (MoneyDJ) | https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=38276f68-988a-41ff-9dc5-680219d64ecf |
| S9 | 2Q26 call transcript with Q&A (company) | https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q2/Transcript.pdf |
| S10 | 2Q26 presentation (company) | https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q2/Presentation.pdf |
| S11 | 1Q26 call transcript with Q&A (company) | https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q1/%E8%AA%AA%E6%98%8E%E6%9C%83%E9%80%90%E5%AD%97%E7%A8%BF.pdf |
| S12 | Focus Taiwan / CNA news report, 2026-10-31 | https://focustaiwan.tw/business/202610310007 |
| S13 | 1Q26 financial statements (company) | https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q1/Financial%20Statements.pdf |
| S14 | Quartr event page, summary only | https://quartr.com/events/mediatek-2454-q3-2026_F96vz9IM |
| S15 | Exchange filing: 1H26 ex-dividend record date (Yahoo Taiwan) | https://tw.stock.yahoo.com/news/%E5%85%AC%E5%91%8A-%E8%81%AF%E7%99%BC%E7%A7%91%E6%B0%91%E5%9C%8B115%E5%B9%B4%E4%B8%8A%E5%8D%8A%E5%B9%B4%E5%BA%A6%E4%B9%8B%E7%8F%BE%E9%87%91%E8%82%A1%E5%88%A9%E9%99%A4%E6%81%AF%E5%9F%BA%E6%BA%96%E6%97%A5-092649210.html |
| S16 | Secondary article on the bond (KuCoin / CryptoBriefing) | https://www.kucoin.com/news/flash/alphabet-and-nvidia-invest-in-mediatek-s-3-9b-convertible-bond-for-ai-expansion |
| S17 | Exchange filing: board dividend resolution (Yahoo Taiwan) | https://tw.stock.yahoo.com/news/%E5%85%AC%E5%91%8A-%E8%91%A3%E4%BA%8B%E6%9C%83%E6%B1%BA%E8%AD%B0%E8%82%A1%E5%88%A9%E5%88%86%E6%B4%BE-092647995.html |
| S18 | 4Q25 call transcript (company) | https://www.mediatek.com/hubfs/MediaTek%20Assets/Pdfs/Quarterly%20Earnings%20Release/2025/Quarterly%20Earnings%20Release-2025Q4/%E8%AA%AA%E6%98%8E%E6%9C%83%E9%80%90%E5%AD%97%E7%A8%BF.pdf |
| S19 | October 2026 revenue (TechNews) | https://technews.tw/2026/11/10/mediateks-october-revenue-increased-by-5-8-year-on-year/ |
| S20 | Other secondary reads: Jon Peddie Research; TrendForce; StockFeel summary; Yahoo Taiwan 3Q26 report filing; company financial-information index page | https://www.jonpeddie.com/news/mediateks-q326-financial-results/ · https://www.trendforce.com/news/?p=66010 · https://www.stockfeel.com.tw/?p=278716 · https://tw.stock.yahoo.com/news/%E5%85%AC%E5%91%8A-%E8%81%AF%E7%99%BC%E7%A7%912026%E5%B9%B4%E7%AC%AC3%E5%AD%A3%E5%90%88%E4%BD%B5%E8%B2%A1%E5%8B%99%E5%A0%B1%E5%91%8A-091314031.html · https://www.mediatek.com/investor-relations/financial-information |

**Not read (blocked or failed)**

| Tag | What | URL | Why |
|---|---|---|---|
| B1 | 3Q26 Financial Statements (company) | https://www.mediatek.com/hubfs/MediaTek-Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q3/Financial%20Statements.pdf | Fetch refused (provenance); not in search index |
| B2 | 3Q26 reviewed consolidated report with notes (company) | https://www.mediatek.com/hubfs/MediaTek-Assets/Pdfs/Financial%20Reports/2026/Q3%20Consolidated%20Report.pdf | Fetch refused |
| B3 | 3Q26 company transcript | https://www.mediatek.com/hubfs/MediaTek-Assets/Pdfs/Quarterly%20Earnings%20Release/2026/Quarterly%20Earnings%20Release-2026Q3/Transcript.pdf | Fetch refused |
| B4 | stockanalysis transcript | https://stockanalysis.com/quote/tpe/2454/transcripts/720948-q3-2026/ | Fetch refused |
| B5 | GuruFocus transcript | https://www.gurufocus.com/stock/TPE:2454/transcripts/9000002 | Site error |
| B6 | Yahoo Finance transcript | https://finance.yahoo.com/quote/2454.TW/earnings/2454.TW-Q3-2026-earnings_call-720948.html | Site error |
| B7 | Exchange copy of the presentation | https://mopsov.twse.com.tw/nas/STR/245420261030M001.pdf | Fetch refused; company copy [S2] read instead |

B1–B3 URLs are as listed on the company's financial-information page [S20]; they were relayed by the fetch tool and may not be character-exact.
