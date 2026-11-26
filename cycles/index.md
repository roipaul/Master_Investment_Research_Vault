---
type: registry
doc: cycle-index
updated: 2026-11-26
sources: [skill:cycle-view]
---

# Cycle and market registry

The `cycle-view` skill reads this file. It lists every cycle note and market read, whether it is active, the names it covers and its fixed indicators with a source for each. Change a status from `later` to `active` to have a note built. Changes to an indicator set are logged at the bottom with the reason.

Phase 1 (agreed 2026-11-26): three full cycle notes and two market reads are active. The rest wait until Paul has judged the first ones after an earnings season.

## Cycle notes

| Slug | Type | Depth | Status | Names |
|---|---|---|---|---|
| aluminium | Commodity and spread | Full | active | [[000807-SZ]], AA |
| us-housing-channel | Industry demand; inventory | Full | active | POOL, PNR, FDR, 0669-HK |
| china-freight-parcel | Industry demand and price | Full | active | [[YMM]], ZTO |
| factory-automation | Inventory and capex | Full | later | 1590-TW, [[6149-T]] |
| chips-handsets | Industry demand; inventory | Full | later | 2454-TW |
| china-internet-competition | Industry competition and subsidy | Full | later | 3690-HK, JD, TCOM |
| korea-credit | Credit | Full | later | 105560-KS |
| memory-chip-capex | Commodity; capex | Light | later | none held |
| china-property-credit | Credit; industry demand | Light | later | none held |
| oil-energy-shipping | Commodity; capex | Light | later | none held |
| us-consumer-credit | Credit; industry demand | Light | later | none held |

## Market reads

| Market | Status |
|---|---|
| us | active |
| china-hk | active |
| japan | later |
| korea | later |
| taiwan | later |

## Indicator sets (active items)

### aluminium
| Indicator | Source | Frequency |
|---|---|---|
| China aluminium price | SHFE and Changjiang spot, via SMM and Mysteel | Daily |
| Alumina price | SMM, Mysteel | Daily / weekly |
| Ratio of aluminium to alumina price | Computed from the two above | Monthly |
| Industry average full cost and profit per tonne, with lowest and highest cost | SMM monthly cost note; Mysteel | Monthly |
| China operating capacity against the 45 Mt cap | SMM | Monthly |
| Global and China output | International Aluminium Institute, via AL Circle, CRU or Mysteel (the institute's page shows no numbers to the fetch tool) | Monthly |
| Social ingot inventories | SMM, Mysteel | Weekly |
| Yunnan hydropower and curtailment orders (dry season, November to May) | SMM, Reuters | Event-driven |

Paid gap: a smelter-by-smelter cost curve (CRU, Wood Mackenzie). Free substitute: the SMM and Mysteel averages and range; Alcoa's slides for its global quartile.

### us-housing-channel
| Indicator | Source | Frequency |
|---|---|---|
| Housing starts and permits | Census Bureau; FRED series HOUST, PERMIT | Monthly |
| Existing home sales | National Association of Realtors | Monthly |
| 30-year mortgage rate | Freddie Mac PMMS; FRED MORTGAGE30US | Weekly |
| Remodelling outlook | Harvard JCHS LIRA | Quarterly |
| Building-materials retail sales | Census retail trade | Monthly |
| Big-box comparable sales | Home Depot, Lowe's results | Quarterly |
| Channel inventory | Pool Corp, Hayward, Pentair results; the vault's earnings files | Quarterly |
| New pool construction and installed base | Pool Corp filings (installed-base table drawn from P.K. Data) | Annual; direction quarterly |

Paid gap: P.K. Data. Free substitute: Pool Corp's annual table and call commentary.

### china-freight-parcel
| Indicator | Source | Frequency |
|---|---|---|
| Parcel volume and revenue (gives revenue per parcel) | State Post Bureau, via Sina, ITHome or gov.cn | Monthly |
| Express development index | State Post Bureau | Monthly |
| Listed couriers' price per parcel | YTO, Yunda, STO, SF exchange filings | Monthly |
| Road freight price index | China Federation of Logistics and Purchasing, via Zhitong or CLS | Monthly and weekly |
| Logistics prosperity index | China Federation of Logistics and Purchasing | Monthly |
| Road freight volume | Ministry of Transport | Monthly |
| Heavy truck sales | CAAM; cvworld.cn | Monthly |
| Platform orders and take rate | YMM and ZTO results; the vault's earnings files | Quarterly |

### us (market read)
| Block | Indicators | Source |
|---|---|---|
| Economy | Growth, inflation, policy rate, unemployment, profit margins against history | BEA, BLS, Federal Reserve (on FRED) |
| Credit cycle | High-yield and investment-grade spreads; lending standards; financial conditions; quality of new issuance | FRED (BAMLH0A0HYM2, BAMLC0A0CM); Fed Senior Loan Officer Survey; Chicago Fed NFCI; PitchBook LCD headlines |
| Psychology | Margin debt; sentiment; fund flows; IPO activity | FINRA; AAII; Investment Company Institute; Renaissance Capital |
| Price of risk | Shiller CAPE; forward P/E; implied equity risk premium; earnings yield less the 10-year Treasury yield | Shiller data; FactSet Earnings Insight; Damodaran |

### china-hk (market read)
| Block | Indicators | Source |
|---|---|---|
| Economy | Growth, consumer and producer prices, PMI, loan prime rate, the renminbi | NBS; Caixin; People's Bank of China |
| Credit cycle | Total social financing, M2, new loans, developer funding | People's Bank of China; CRIC |
| Psychology | Margin financing balance; new accounts; fund launches; IPO count; Stock Connect flows; Hong Kong turnover and short-selling share | Securities Times; Shanghai exchange; AMAC; HKEX Monthly Market Highlights |
| Price of risk | CSI 300 P/E against its range; Hang Seng P/E and dividend yield; earnings yield less the 10-year government bond yield | China Securities Index Co.; Hang Seng Indexes; MSCI factsheets; Siblis Research |

The full source catalogue for every item, including those marked `later`, is in the sheet "Data sources for cycle notes and market reads".

## Change log
- 2026-11-26: registry created; phase 1 items set active.
