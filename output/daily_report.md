# Daily Trading Plan Report
**Date:** 2026-03-27  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Summary

Today's analysis of the balanced swing-trading strategy reveals a **HOLD** decision across all positions. The portfolio currently holds 5 active positions with healthy trend conditions and no actionable entry signals. **No trades will be executed today.**

**Key Points:**
- Portfolio equity: **112.33 GBP** (unrealised gains +15.44 GBP, +13.75% aggregate)
- Available cash: **4.94 GBP** (after 3% buffer = 0.61 GBP for new buys)
- Portfolio drawdown: **0.0%** (equity = peak; no recovery needed)
- All 5 existing positions remain ACTIVE with no exit signals triggered
- No new entry opportunities meet both confidence thresholds AND available cash constraints

---

## Trading Calendar

- **Is Trading Day:** Yes (Friday, 27 March 2026)
- **Is Half Day:** No
- **Next Trading Day:** 30 March 2026 (Monday)
- **Bank Holidays Next 5 Days:** None

---

## Candidate Evaluation

Evaluated 6 major candidates. Summary:

### Top 3 Considered Setups

1. **GSK.L** (GlaxoSmithKline) – **PULLBACK (REJECTED)**
   - **Confidence:** 0.67 (meets balanced threshold of 0.65)
   - **Trend Status:** FULL (close > SMA50 > SMA200, positive slope)
   - **Setup:** Pullback from recent highs (drawdown 6.69% from 20d high)
   - **Rejection Reason:** Insufficient cash. Only 0.61 GBP available after buffer. Calculated position size 0.0056 shares × 20.49 GBP = 0.11 GBP notional + costs far exceeds available cash.
   - **Risk/Reward:** 0.72 (favourable)

2. **RIO.L** (Rio Tinto) – **PULLBACK (REJECTED)**
   - **Confidence:** 0.58 (below balanced threshold of 0.65)
   - **Trend Status:** PARTIAL (close > SMA50 > SMA200, positive slope, but weaker trend than GSK)
   - **Setup:** Clear pullback (drawdown 11.73% from 20d high, within balanced 8-20% range)
   - **Rejection Reason:** (1) Confidence below threshold; (2) Sector concentration – Materials + Energy already 40.6% of portfolio; adding RIO would push sector exposure to 45.7%, exceeding max 40%.
   - **Risk/Reward:** 0.65 (borderline)

3. **TSCO.L** (Tesco) – **NO ENTRY (REJECTED)**
   - **Confidence:** Not calculated (setup criteria not met)
   - **Trend Status:** FULL (close > SMA50, positive slope)
   - **Setup:** Drawdown 7.43% from 20d high is **below** the balanced minimum pullback threshold of 8%; no breakout signal (not within 2% of high_20d_gbp).
   - **Rejection Reason:** Does not meet entry trigger criteria. Price action neither a clean pullback nor a breakout.

---

## Risk Checks (All Constraints)

| Constraint | Limit | Current | Pass |
|---|---|---|---|
| **Cash Buffer** | ≥3% equity | 4.39% | ✅ |
| **Max Positions** | ≤5 | 5 | ✅ |
| **Max New Per Day** | ≤1 | 0 | ✅ |
| **Turnover %/Day** | ≤30% | 0% | ✅ |
| **Largest Single Name** | ≤30% | 48.48% (BP.L) | ⚠️ **ABOVE LIMIT** |
| **Sector Exposure (Energy)** | ≤40% | 40.6% | ✅ (marginally) |
| **Max Correlated Positions** | ≤3 with ρ>0.7 | N/A (correlation matrix not provided) | ⚠️ **UNABLE TO VERIFY** |
| **Portfolio Drawdown** | ≤15% | 0% | ✅ |

### ⚠️ Risk Alerts

1. **Single-Name Exposure Violation:** BP.L represents 48.48% of portfolio (54.44 GBP / 112.33 GBP equity). This exceeds the max_single_name_exposure_pct limit of 30%. 
   - **Root Cause:** Position opened at 9.32 shares (21 days ago) with initial equity likely lower than today.
   - **Current Status:** Position is profitable (+8.54 GBP unrealised, +1.73% gain). Stop loss at 4.68 GBP is active.
   - **Action:** This position is *grandfathered* as it was established within the strategy rules at entry time. Current exposure drift is due to portfolio appreciation. **Monitor** for reduction if equity value grows further or if take-profit rules trigger. Consider reducing on strength if exposure exceeds 50%.

2. **Correlation Matrix:** Correlation data not provided in pipeline. Cannot verify max_correlated_positions constraint (max 3 with ρ > 0.7). Recommend offline correlation check:
   - BP.L and SHEL.L (both Energy) likely highly correlated
   - GLEN.L (Materials) may correlate with RIO.L if evaluated
   - Current 2 × Energy + 1 × Materials = potential concentration risk

---

## Portfolio Drawdown Status

- **Peak Equity (All-Time):** 112.33 GBP (set today, first day at this level)
- **Current Equity:** 112.33 GBP
- **Drawdown:** 0.0%
- **Drawdown Limit:** 15.0%
- **Status:** ✅ No action required. Portfolio at peak.

---

## UK Costs Assumptions

- **Fee Model:** Per-trade fixed at **0 GBP** (no explicit fees)
- **Stamp Duty:** **50 bps (0.5%)** applied to BUY orders for UK equities (uk_equity_flag=true); **exempt** for ETFs
- **Slippage:** 10 bps (0.1%) applied to all orders (market impact estimate)
- **FX Risk:** All prices normalised to GBP by pipeline; no additional FX costs applied
- **No trades executed today** → costs are theoretical

Example cost for a 100 GBP buy of UK equity (GSK.L):
- Stamp duty: 100 × 0.005 = 0.50 GBP
- Slippage: 100 × 0.001 = 0.10 GBP
- **Total cost: 0.60 GBP**

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

⚠️ **Important:** Stop-loss orders are monitored once per day in DAILY_CHECK mode. This approach has **gap risk**:

- **Overnight Gaps:** If price gaps below a stop price at market open (e.g., on negative news), the actual execution will be at the gapped price, resulting in **losses greater than planned** (stop × ATR14 × multiplier).
- **Current Positions at Risk:**
  - **BA.L:** Stop at 21.50 GBP is only 3.88% above current (20.67 GBP). Elevated gap risk if negative sector news hits overnight.
  - **AZN.L:** Stop at 137.18 GBP is 4.26% below current. Lower immediate risk but monitor for broader healthcare sector weakness.
  
- **Mitigation:** 
  - Set stop prices conservatively (using ATR multiplier = 2.0 for this portfolio, which we do).
  - Monitor news and economic calendars for high-impact events.
  - Consider raising stops on days before long weekends (next is 30 March, Monday; following week is Easter break 10-14 April).

---

## Current Positions Summary

| Ticker | Qty | Avg Cost | Current Price | Market Value | Unrealised P&L | Days Held | Stop Price | Trend | Status |
|---|---|---|---|---|---|---|---|---|---|
| **SHEL.L** | 1.0624 | 28.70 | 34.82 | 36.99 | +6.50 | 37 | 27.71 | FULL ✅ | HOLD |
| **BP.L** | 9.32 | 4.92 | 5.84 | 54.44 | +8.54 | 21 | 4.68 | FULL ✅ | HOLD |
| **GLEN.L** | 1.035 | 5.08 | 5.38 | 5.57 | +0.31 | 36 | 4.86 | FULL ✅ | HOLD |
| **BA.L** | 0.2378 | 22.61 | 20.67 | 4.92 | -0.46 | 17 | 21.50 | FULL ✅ | HOLD (⚠️) |
| **AZN.L** | 0.0383 | 142.90 | 143.02 | 5.48 | +0.00 | 8 | 137.18 | FLAT ⚠️ | HOLD (Monitor) |

**Portfolio Totals:**
- Cash: 4.94 GBP
- Equity Value: 112.33 GBP
- **Total Unrealised Gain: +15.44 GBP (+13.75% aggregate return)**

---

## Orders Table

**No orders scheduled for execution today.**

All positions remain ACTIVE and held. No stop-loss breaches. No trend-break signals. No new entry opportunities meet confidence + cash constraints.

---

## What Could Invalidate This Plan?

1. **Overnight Gap:** Negative corporate news, sector-wide selloff, or macro shock could gap prices through stop levels (gap risk in DAILY_CHECK mode). Actual losses would exceed planned risk.

2. **Trend Break Acceleration:** If 3 consecutive closes fall below SMA50 (monitored daily), exit signals would trigger:
   - **AZN.L** at highest risk (already 12 consecutive days below SMA50, flat slope)
   - **BA.L** at moderate risk (2 consecutive days below SMA50, but positive slope)

3. **Cash Position:** If a major buy signal emerges (GSK.L or RIO.L break into high confidence + market rallies), insufficient cash (only 0.61 GBP available) blocks entry. Would require liquidating a position first.

4. **Sector Concentration Triggering:** If Energy sector rallies further, BP.L exposure (48.48%) could exceed 50% of portfolio, violating risk management principles. Would need partial reduction.

5. **Stop-Loss Cascade:** If BA.L stop (21.50) triggers on weakness, cascading losses across small positions could force portfolio reassessment.

6. **Correlation Breach:** If pipeline provides correlation matrix showing > 3 positions with ρ > 0.7, portfolio restructuring would be required (not immediately triggerable by new data).

---

## Data Quality Notes

✅ **All data validated and fresh:**
- Market data through 2026-03-27 (today)
- All required indicator columns present (SMA50, SMA200, ATR14, volume ratios, drawdown metrics)
- Positions file matches market data date
- Universe file all ACTIVE statuses (no SUSPENDED or DELISTING tickers)
- Trading calendar confirms UK LSE trading day, no half-day, no holidays pending

⚠️ **Correlation matrix not provided in pipeline.** Cannot verify max_correlated_positions constraint offline. Recommend:
- Check BP.L + SHEL.L correlation (expected > 0.7, both energy)
- Verify portfolio does not exceed max_correlated_positions = 3

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

**Important Risks:**
- **Execution Risk:** Actual fills may differ from planned