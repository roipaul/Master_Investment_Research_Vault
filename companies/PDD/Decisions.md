---
type: document
doc: decisions
tickers: [PDD]
updated: 2026-11-24
sources: [skill:decision-record]
---

# PDD — Decisions

## 2026-11-24 — Pre-commitment (no position)

**Decision.** Pre-commit, not buying yet. No position, no size. Price reference: US$83.68 (close 2026-11-20, model v2.2 price; today's quote not confirmed).

**Why, in Paul's words (24 Nov 2026):** "Bull lean, needs more digging; price looks good on the surface."

**Order.** No frame (`VariantView.md`) is on file. That is not required for a pre-commitment, but it would be required before an initiate unless Paul overrides.

### Snapshot (Claude's figures, dated; Paul has not confirmed the figures)

| Item | Reading | Date / source |
|---|---|---|
| Track / zone | undecided / not set (no frame run) | hub, 2026-11-24 |
| Debate verdict | Business Inconclusive; price check Stretch (Claude's proposal) | [[Debate]] 2026-11-22; [[Thesis]] update 2026-11-24 |
| Paul's view | Triage Dig; thesis bull lean, needs more digging | 2026-11-24 |
| Latest earnings-update call | Q3 2026: thesis Intact; fresh money Wait at about US$86 (proposed) | [[earnings/FY2026-Q3]], 2026-11-20 |
| Variant views | None adopted. Candidates: V1 capital return more likely than the ~20% priced; V2 operating earnings ~6% a year vs ~0.6% priced | Chat, 2026-11-24 |
| Return at US$83.68, to end-2029 | Conservative (6% growth, 9x, cash never returned): ~4.5% a year. Central (6%, 9x, 35% chance of capital return): 14.6%. Harsh (−5% a year, 7x, cash at zero): −13.3% | model v2.2, Range of outcomes, 2026-11-24 |
| What the price implies | ~0.6% growth; ~20% chance capital is returned; 7.7x exit P/E ex cash | model v2.2, Price slider |
| Thesis as of | `Thesis.md` at commit b81d408 | vault |

### Pillars Paul accepts as his expectations (thresholds as drafted 2026-11-24)

| Pillar | Holds if | Check at |
|---|---|---|
| 1. Earnings floor | Domestic after-tax profit ≥ ~RMB 85bn a year (≈100bn now); growth ≥ 3–4%; take rate not structurally falling | Each quarter; Q3 2027 when the refund step laps |
| 2. Spending peaks | No programme beyond the two RMB 100bn commitments; Temu breakeven by ~2029; New Pinmu inventory + prepayments < RMB 30bn | Each quarter; FY2026 20-F (Apr 2027) |
| 3. Cash preserved, then returned | Surplus cash rising (≥ RMB 500bn now); equity book not ballooning; ≥ 35–40% chance of capital return by ~2029 | Each 20-F; every call |
| 4. Our claim intact | VIE and listing intact; offshore cash (~57%) movable; no fraud, sanctions or capital controls trapping it | Continuous |

**Accepted outcome:** if pillars 1, 2 and 4 hold and 3 does not turn, the return is dead money (about 4% a year). Owning means accepting that.

**Evidence deadline (capital return):** a payout signal (buyback, dividend or stated policy), or a shrinking equity book, by the FY2027 results (about March 2028). If none arrives, candidate V1 expires.

### Drawdown triggers (pre-committed; facts to check, not advice)

| If the price falls ~50% because of | Pillar hit | Pre-committed response |
|---|---|---|
| China or ADR selloff, tariff headlines, a delisting scare with no rule change, a fund dumping its position | None | Hold or add |
| Earnings miss, take-rate dip or higher Temu losses, with spending inside the caps | 1, mildly | Hold; add only after the next print confirms domestic profit ≥ ~RMB 85bn |
| A new spending programme, New Pinmu stock through RMB 30bn, a large equity purchase, or "investment phase" extended indefinitely | 2 or 3 | Stop adding (falsifier #2); hold only if pillars 1 and 4 are intact |
| A state fee cap or recurring large fines cutting domestic profit by more than ~15% | 1, structural | Re-underwrite at the new floor; exit if it falls below ~RMB 70–75bn |
| VIE challenged, forced delisting, capital controls on offshore cash, accounting fraud, US sanctions | 4 | Exit |

### What would make Paul start or add (from the thesis; as drafted)
- Any capital-return signal: buyback, dividend or payout policy.
- Q4 2026 online marketing growth of 8% or more, with no new spending programme.
- Merchant calls showing the take rate holding after the Q3 step, without higher bids.

### Rules check
- `settings.md` sets the hurdle (15% IRR over 3–5 years) and `max_active: 3`. No position limits are set, so there is nothing to breach.
- The central view returns 14.6% a year, below the 15% hurdle (fact).

**Review date:** Q4/FY2026 results call, about late March 2027 (e). Checks: capital-return language; online marketing growth (≥ 8%); any new programme; "investment phase" wording.

**Pre-mortem:** not given.
