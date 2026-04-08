```markdown
# Daily Trading Report
**Date:** 2026-04-08 (Wednesday)
**Status:** NO_TRADES
**Currency:** GBP
**Execution Sequence:** SELL_THEN_BUY
**Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar
✓ Is trading day: YES
✓ Is half-day: NO
✓ Next trading day: 2026-04-09
✓ Bank holidays next 5 days: NONE

---

## Executive Summary

**No trades executed today due to portfolio constraint violations.**

The portfolio currently violates multiple hard risk constraints that prevent new position entry:
1. **Position count:** 6 active positions vs. max 5 allowed
2. **Energy sector exposure:** 80% vs. 40% maximum
3. **Single-name concentrations:** BP.L at 47.4%, SHEL.L at 32.6% (max 30% each)
4. **Cash balance:** 3.45 GBP (insufficient to fund new entries)

While one eligible swing trade candidate was identified (NG.L with 0.88 confidence score), it cannot be executed due to insufficient cash and portfolio constraint violations.

**Recommendation:** Operator should rebalance portfolio in next trading session by trimming Energy sector exposure (sell either SHEL.L or BP.L) to restore compliance with risk policies.

---

## Existing Position Reviews

All 6 existing positions remain ACTIVE with no stop-loss breaches or trend breaks:

| Ticker | Qty | Avg Cost | Current Price | PnL | Days Held | Stop | Trend |
|--------|-----|----------|---------------|-----|-----------|------|-------|
| SHEL.L | 1.0624 | 28.70 | 34.01 | +5.64 GBP | 49 | 27.71 | UP (close > sma50 > sma200) |
| GLEN.L | 1.0350 | 5.08 | 5.628 | +0.57 GBP | 48 | 4.86 | UP |
| BP.L | 9.3200 | 4.92 | 5.627 | +6.55 GBP | 33 | 4.68 | UP |
| BA.L | 0.2378 | 22.61 | 22.885 | +0.06 GBP | 29 | 21.50 | UP |
| AZN.L | 0.0383 | 142.90 | 152.16 | +0.35 GBP | 20 | 137.18 | UP |
| RIO.L | 0.0208 | 71.09 | 73.32 | +0.05 GBP | 5 | 67.02 | UP |

**All positions are profitable and trend-intact. No exits triggered.**

---

## New Entry Opportunities Evaluated

### Top 3 Candidates Ranked by Confidence

#### 1. NG.L (National Grid) — PULLBACK — Confidence: 0.88
- **Trend Status:** FULL (close 13.316 > sma50 12.127 > sma200 11.534)
- **Setup:** Pullback from 20d high (13.865), drawdown 3.96% (healthy for swing)
- **Volume:** ratio 0.86 (< 1.0, indicating low-volume pullback—preferred)
- **Risk/Reward:** Favorable. ATR14 = 0.3331 GBP, stop at 12.65 GBP = 0.67 GBP risk
- **Confidence Components:** Trend 0.40 + Pullback setup 0.25 + Risk/Reward 0.15 + Liquidity 0.08 = **0.88**
- **Position Sizing:** 7.47 shares (after 10% gap buffer) × 13.316 = 99.5 GBP notional + 0.60 GBP costs = **100.1 GBP required**
- **Rejection Reason:** **INSUFFICIENT CASH** (3.45 GBP available vs. 100.1 GBP required). Additionally, portfolio is in constraint violation, preventing new entries.
- **Sector Impact:** Utilities (not currently held). Would diversify away from Energy concentration.

#### 2. HSBA.L (HSBC) — PULLBACK — Confidence: 0.65
- **Trend Status:** FULL (close 13.348 > sma50 12.650 > sma200 10.909)
- **Setup:** Very shallow pullback (1.8% drawdown), weak entry signal
- **Volume:** ratio 1.11 (neutral-to-high)
- **Confidence:** 0.40 + 0.10 + 0.10 + 0.05 = **0.65** (below 0.70 threshold)
- **Rejection Reason:** WEAK_SETUP (shallow drawdown, confidence below threshold)

#### 3. TSCO.L (Tesco) — PULLBACK — Confidence: 0.65
- **Trend Status:** FULL (close 4.8565 > sma50 4.6952 > sma200 4.4295)
- **Setup:** Shallow pullback (2.2% drawdown), high volume ratio 1.27
- **Confidence:** 0.40 + 0.10 + 0.10 + 0.05 = **0.65** (below threshold)
- **Rejection Reason:** WEAK_SETUP (shallow drawdown, less ideal volume pattern)

---

## Risk Constraint Compliance Check

| Constraint | Limit | Current | Status | Notes |
|-----------|-------|---------|--------|-------|
| **Max Positions** | 5 | 6 | ❌ VIOLATED | Portfolio has 6 active positions; max 5 allowed. |
| **Max Sector (Energy)** | 40% | 80.0% | ❌ VIOLATED | SHEL.L + BP.L = 88.57 GBP of 110.65 total = 80%. Excessive concentration. |
| **Max Single-Name (BP.L)** | 30% | 47.4% | ❌ VIOLATED | BP.L market value 52.44 GBP / equity 110.65 = 47.4%. |
| **Max Single-Name (SHEL.L)** | 30% | 32.6% | ❌ VIOLATED | SHEL.L market value 36.13 GBP / equity 110.65 = 32.6%. |
| **Max Correlated Positions** | 3 | N/A | ✓ OK | Correlation matrix not provided; flagged for future monitoring. |
| **Cash Available** | > 0 | 3.45 GBP | ⚠️ TIGHT | After 3% buffer (3.32 GBP required), only 0.13 GBP surplus. Insufficient for new buys. |
| **Max Turnover (Daily)** | 30% | 0% | ✓ OK | No trades proposed. |
| **Portfolio Drawdown** | ≤ 15% | 4.80% | ✓ OK | Current equity 110.65 vs. peak 116.22 = -4.80% drawdown. Well within limit. |

**Conclusion:** Portfolio is in constraint violation and does NOT comply with hard risk limits. New positions cannot be opened until constraints are restored.

---

## Cash & Liquidity Analysis

| Item | Value (GBP) |
|------|-------------|
| Settled Cash | 3.45 |
| Unsettled Proceeds | 0.00 |
| Total Available | 3.45 |
| **Required Buffer (3%)** | 3.32 |
| **Surplus After Buffer** | 0.13 |
| NG.L Buy Notional (with costs) | 100.10 |
| **Cash Shortfall** | **-99.97** |

**Liquidity Status:** INSUFFICIENT. Even the smallest eligible trade (NG.L) requires 30x current liquid cash.

---

## Portfolio Composition & Concentration

### By Sector (Current)
- **Energy:** 80.0% (SHEL.L 32.6% + BP.L 47.4%) — **VIOLATES 40% MAX**
- **Materials:** 5.3% (GLEN.L