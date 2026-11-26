---
type: theme
name: cybersecurity
tickers: [CHKP, PANW, FTNT, CRWD, ZS, OKTA]
updated: 2026-09-27
data_through: Q2 2026 / latest reported quarters as of 2026-09-27
status: imported
sources: [chat:https://claude.ai/chat/142b3f44-6be8-40fe-83c2-5c2f6cb301d8]
---

# Cybersecurity — industry structure and the three firewall-origin business models (2026-09-27)

Companies covered: [[CHKP]] (full write-up in [[companies/CHKP/Thesis|CHKP Thesis]]), Palo Alto Networks (PANW), Fortinet (FTNT), with CrowdStrike, Zscaler, Okta, Cisco and Microsoft as context. No hubs yet for the others.

> **Imported** on 2026-11-26 from the Global Tech Project chat "Cybersecurity stocks and Check Point business model" (first reply, 2026-09-27). Claude's reply is copied as written, with tool calls and the closing offer of further work removed. **Claude's framing, not Paul's view.**

## "Given the recent AI development, there have been a lot of discussion on cybersecurity demand, stocks such as PANW and FTNT have been rising quite a bit. I want to understand a bit better about this industry, and then I want to understand CHKP better. What is the difference in business model?"

**Why the sector is running**

The immediate trigger was mid-September: Dario Amodei called for slowing frontier AI development and Sam Altman backed the idea, and Wall Street shifted its AI narrative from pure productivity growth to defense, sparking a sharp rally across the major cybersecurity names. The Global X Cybersecurity ETF gained 10.7% from September 11 through 18; PANW climbed 10% and FTNT 8.8%. Year to date, Fortinet is up 125% and Palo Alto 113.5%. The narrative move sits on top of strong prints (both beat and raised), but note that Goldman's cybersecurity basket has more than doubled since its April low, so a lot is priced.

The demand logic has four legs:

1. **AI lowers the cost of attack.** Check Point's CEO put it well: AI, and particularly the latest frontier model, is driving a collapse in scarcity of adversarial capabilities. Phishing, exploit discovery and lateral movement get cheaper and faster, so defence has to move to machine speed.
2. **Agents expand the attack surface.** As companies move toward autonomous agentic AI systems that perform multi-step workflows across databases, the attack surface expands dramatically, and enterprise buyers are leaning into identity management. This is why identity names (Okta, CyberArk now inside PANW) and endpoint (CrowdStrike) led rather than firewalls.
3. **Securing AI itself** — prompt injection, runtime guardrails for models. PANW's Prisma AIRS reached $100 million in ARR within a year; Check Point launched an AI Network Firewall.
4. **AI data centre buildout needs high-throughput network security.** This is Fortinet's leg: product growth came from secure networking hardware and term licenses, including demand for higher performance products and deployments related to AI infrastructure.

Backdrop numbers: Gartner has enterprise cybersecurity budgets at $215 billion in 2026 and forecasts a 68.7% increase in AI security spend from 2026 to 2027.

**Industry structure in one paragraph**

Layers: network security (firewalls, SD-WAN, SASE) — PANW, FTNT, CHKP, Zscaler, Cisco; endpoint/XDR — CrowdStrike, Microsoft, SentinelOne; identity — Okta, CyberArk, Microsoft; cloud security — Wiz (Google), PANW; SOC/SIEM — Splunk (Cisco), PANW XSIAM, CrowdStrike. The structural trend is vendor consolidation: CISOs want fewer platforms, so the big three buy into adjacent layers (PANW–CyberArk, Google–Wiz, Cisco–Splunk) and Microsoft bundles. Scale in threat data and sales coverage compounds. That is the setup for the business model question, because the three firewall-origin companies have chosen very different answers to it.

**Three firewall companies, three business models**

| | Palo Alto | Fortinet | Check Point |
|---|---|---|---|
| Core idea | Software platform; consolidate the customer's whole security stack | Vertically integrated hardware + attached subscriptions | Annuity on a mature installed base |
| Hardware role | De-emphasised; excluded from headline metric (NGS ARR) | Customer acquisition engine — custom ASICs give cost/performance edge | Small, shrinking |
| Growth engine | Land-and-expand, "platformization" (free periods to displace rivals), large M&A | Organic; refresh cycles, SD-WAN/SASE, OT, AI data centre | Renewals, price, new subscriptions attached to gateways |
| Latest quarter | Revenue $3.41B, +34.5%; NGS ARR +63% to $9.1B (incl. CyberArk) | Revenue +26% to $2.05B; product +52% to $773M; service +14% to $1.27B | Revenue +1% to $674M; subscriptions +12% to $333M; product −14% |
| Profitability | Non-GAAP op margin 29.2%; adj FCF margin 38.4%; GAAP was a loss in FQ3 | GAAP op margin 34%, non-GAAP 38% | GAAP 27%, non-GAAP 39% |
| Capital allocation | Acquisitions (CyberArk, Chronosphere), heavy SBC | Buybacks, founder-owned, frugal | Buybacks (authorisation expanded by $2B), net cash, no big deals |
| Management | Nikesh Arora, dealmaker | Ken Xie, founder-engineer | Gil Shwed (founder, chairman) → Nadav Zafrir (CEO since late 2024) |

The plain-English version: Palo Alto sells an outcome ("we'll be your platform") and funds growth with stock and deals, so its economics look great on non-GAAP and modest on GAAP. Fortinet sells boxes cheaply because it makes its own chips, then monetises the subscriptions and support that ride on them — 90% of a quarter's service revenue was already sitting in deferred revenue at the start of it, which is what makes the hardware cyclicality tolerable. Check Point sells a gateway once and then charges for threat prevention, support and add-on subscriptions for years; it has historically maximised margin over growth, which is why it sits at a ~12x P/E while the others are software multiples.

**What's going on at Check Point specifically**

The stock has done the opposite of the sector: in early August it was down 33.7% year to date, trading at a 12.6x trailing P/E versus a five-year median above 20x. Two things are happening. First, the mature model is showing its age — appliance sales are falling and the recurring line grows low-double digits, netting to ~flat revenue. Second, Zafrir is reinvesting: a go-to-market reorganisation that disrupted firewall-appliance demand in the first half, plans to hire about 300 go-to-market employees for 2027, tuck-in acquisitions (Cyberint, Veriti, Lakera for AI security), a Wiz partnership for cloud, and a shift to an open platform where customers can manage different firewalls, even from its fiercest competitors. The new products are working at small scale: email security, CTEM and AI security together exceeded 40% ARR growth. Management says Q3 marks the trough with a stronger Q4.

So the CHKP question, in your framework, is whether this is a valuation-gap close (a 40%-margin, net-cash annuity being re-rated once growth re-accelerates under new management) or a melting ice cube (firewall share loss to Fortinet on price and Palo Alto on platform, with reinvestment eroding the margin that justified the multiple). The product revenue decline is the number to interrogate — how much is GTM disruption versus structural share loss.

Sources (named in the chat; links were not shown in this reply): company results releases for PANW, FTNT and CHKP; press coverage of the September 2026 sector rally; Gartner budget forecast as reported.

## Evidence log

- 2026-09-27 — Theme note created from the imported chat above (Claude's framing, not Paul's view).
- 2026-11-26 — Imported into the vault from the Global Tech Project.
