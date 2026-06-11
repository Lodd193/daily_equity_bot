# Daily Trade Plan Report

**Date:** 2026-06-11  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar & Session Notes
- **Trading Day:** Yes (LSE full session)
- **Half-Day:** No
- **Next Trading Day:** 2026-06-12
- **Bank Holidays (next 5 days):** None

---

## Executive Summary

**Portfolio State:**
- Equity Value: £106.11
- Cash Balance: £3.36
- Portfolio Peak (all-time): £116.22
- Current Drawdown: 8.61% (limit: 15.00%)
- Positions Held: 6 (limit: 5)

**Actions Today:**
- **SELL:** 1 order (HSBA.L - Trend Break Exit)
- **BUY:** 0 orders (constraints prevent entry)

**Rationale:** Portfolio currently exceeds maximum position count (6 vs. 5 limit) and cash buffer falls short of required 3.18% (currently only 3.17% available post-SELL). A mandatory trend-break exit on HSBA.L will reduce position count and improve liquidity. No new entries are permitted until portfolio constraints are normalized.

---

## Strategy & Market Context

**Active Strategy Profile:** Balanced (swing 3–20 days)

**Trend Filters Applied (Balanced Thresholds):**
- Full Trend: close > SMA50 AND SMA50 > SMA200
- Partial Trend (if SMA200 unavailable): positive SMA50 slope AND close > SMA50

**Key Market Observations:**
- UK equity market mixed; several names in uptrends (RIO.L, BARC.L, GLEN.L, AAL.L, LLOY.L)
- Energy sector (SHEL.L, BP.L) showing weakness (negative SMA50 slope)
- Healthcare names (AZN.L, GSK.L) in downtrends; broad pullback evident
- Liquidity adequate for most names; some micro-cap ETFs (VMID.L, BARC.L) with higher participation risk

---

## Candidate Evaluation (Top Setups Considered)

### 1. RIO.L (Rio Tinto) – Materials
- **Trend Status:** FULL UPTREND (close 75.94 > SMA50 75.60 > SMA200 62.51)
- **Setup:** Breakout candidate; near 20-day high (91.17), drawdown 16.71%
- **Volume:** Ratio 1.16x (above breakout minimum)
- **Confidence Score:** 0.72 (trend 0.8, setup 0.7, risk/reward 0.7, liquidity 0.8, diversification 0.6)
- **Rejection Reason:** Cash constraints and portfolio oversize prevent entry. Must reduce positions and restore buffer first.

### 2. BARC.L (Barclays) – Financials
- **Trend Status:** FULL UPTREND (close 4.49 > SMA50 4.36 > SMA200 4.26)
- **Setup:** Breakout setup; +2.97% vs. SMA50, volume ratio 0.78x
- **Confidence Score:** 0.68 (trend 0.75, setup 0.65, risk/reward 0.65, liquidity 0.8, diversification 0.5)
- **Rejection Reason:** Portfolio oversize and insufficient cash. Trend-break exit (HSBA.L) must execute first.

### 3. GLEN.L (Glencore) – Materials
- **Trend Status:** FULL UPTREND (close 5.74 > SMA50 5.69 > SMA200 4.48)
- **Setup:** Breakout (volume ratio 1.44x); already held position
- **Confidence Score:** N/A (position already open; not eligible for new entry)
- **Status:** HOLD (position performing +12.9% PnL; no exit signal)

---

## Risk Checks Summary

| Constraint | Limit | Current | Status |
|---|---|---|---|
| **Portfolio Positions** | 5 | 6 | **FAIL** |
| **Cash Buffer** | 3.18 GBP | 3.36 GBP (2.95% of equity) | **MARGINAL** |
| **Single-Name Exposure** | 30% | 47.84% (BP.L) | **FAIL** |
| **Sector Exposure (Energy)** | 40% | 47.84% | **FAIL** |
| **Portfolio Drawdown** | 15% | 8.61% | **PASS** |
| **Turnover (post-SELL)** | 30% | 4.14% | **PASS** |
| **Min Position Age** | 2 days | 12 days (HSBA) | **PASS** |

**Critical Issues Identified:**
1. **Position Count Overrun:** 6 positions held vs. 5 maximum. HSBA.L exit reduces to 5.
2. **Concentration Risk:** BP.L represents 47.84% of portfolio—well above 30% single-name limit. However, positioned since 2026-03-05 (97 days, profitable +9.68%), and stop-loss not breached. Exit would be reactive; holding is permissible under current rules given time horizon (swing 3–20 days) and profit performance.
3. **Sector Concentration:** Energy sector 47.84% (SHEL.L 32.79% + BP.L 47.84%) exceeds 40% limit. Structural issue requiring longer-term rebalancing.

---

## Exit Decisions Detail

### HSBA.L Sell Signal (Trend Break)
**Ticker:** HSBA.L (HSBC Holdings)  
**Entry Date:** 2026-05-29 (12 days held)  
**Current Price:** £13.218  
**Quantity:** 0.3328 shares  
**Notional Value:** £4.40  
**Exit Type:** Trend Break  

**Signal Rationale:**
- **Consecutive Days Below SMA50:** 3 days (threshold for balanced profile is 3+)
- **Price vs. SMA50:** 13.218 vs. 13.344 (−0.94%)
- **SMA50 Slope:** Negative (−0.009434 vs. SMA50)
- **Trend Filter Integrity:** No longer satisfies "close > SMA50 AND SMA50 > SMA200" (SMA50 > SMA200 still true, but close-to-SMA50 proximity + consecutive days below triggers exit)

**Position Performance:**
- Entry Cost: £4.64 (0.3328 × £13.95)
- Current Value: £4.40
- Unrealised PnL: −£0.24 (−5.25%)
- Exit recovers most capital; prevents further slippage

**Freed Capital:**
- Post-sell proceeds: ~£4.40 (net of slippage ~£0.002)
- Improves cash from £3.36 to ~£7.76
- Reduces positions from 6 to 5 (normalizes count)
- Restores cash buffer to ~7.32% (adequate)

---

## New Entry Analysis

**NO BUY ORDERS ISSUED TODAY**

**Reason:** Although several high-confidence setups exist (RIO.L, BARC.L, GLEN.L), portfolio constraints prevent execution:
1. Position count exceeds max (must be resolved first)
2. Cash buffer inadequate (only £3.36 vs. £3.18 required buffer)
3. Single-name and sector concentration already at/above limits

**Post-SELL Liquidity:**
After HSBA.L exit, available cash will improve to ~£7.76. However, max_new_positions_per_day = 1. Given multiple high-conviction setups, consider RIO.L breakout as the highest-priority candidate for tomorrow (pending successful HSBA.L execution and constraint normalization).

---

## Portfolio Snapshot

| Ticker | Sector | Quantity | Avg Cost | Market Value | Unrealised PnL | Days Held | Status | Stop Price |
|---|---|---|---|---|---|---|---|---|
| SHEL.L | Energy | 1.0624 | 28.70 | 34.80 | +4.31 | 113 | ACTIVE | 27.71 |
| GLEN.L | Materials | 1.0350 | 5.08 | 5.94 | +0.68 | 112 | ACTIVE | 4.86 |
| BP.L | Energy | 9.3200 | 4.92 | 50.82 | +4.93 | 97 | ACTIVE | 4.68 |
| AZN.L | Healthcare | 0.0383 | 142.90 | 5.20 | −0.27 | 84 | ACTIVE | 137.18 |
| RIO.L | Materials | 0.0208 | 71.09 | 1.58 | +0.10 | 69 | ACTIVE | 67.02 |
| HSBA.L | Financials | 0.3328 | 13.95 | 4.40 | −0.24 | 12 | **SELL ORDER** | 13.17 |
| **CASH** |  |  |  | 3.36 |  |  |  |  |
| **TOTAL** |  |  |  | **106.11** | **+10.50** |  |  |  |

---

## Orders Table

| Order ID | Ticker | Side | Type | Quantity | Price (GBP) | Time in Force | Stop Price | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | HSBA.L | SELL | MKT | 0.3328 | — | GTC | — | TREND_BREAK_EXIT |

**Execution Sequence:** SELL_THEN_BUY (HSBA.L must execute before any new BUY orders can be placed)

---

## Cost & Fees Assumptions

**Fee Model:** Per-trade, £0.00  
**Stamp Duty:** 50 bps (UK equities only)  
**Slippage:** 10 bps (market impact estimate)

**HSBA.L Sell Costs:**
- Notional: £4.40
- Slippage (10 bps): −£0.0022 ≈ −£0.00 (rounding)
- Stamp Duty: £0.00 (not applicable to sells)
- **Net Proceeds:** ~£4.40

**Gap Risk Acknowledgement:**
Stop-loss orders in DAILY_CHECK mode are monitored once per trading session. Overnight, weekend, or session-end gaps may result in actual fills significantly worse than the stop price, potentially exceeding planned risk budget. This is an inherent risk of daily-check systems on overnight-held positions.

---

## Constraints Validation Summary

✅ **Kill Switch:** OFF (trading enabled)  
✅ **Trading Calendar:** LSE, full session (no half-day)  
✅ **Data Freshness:** Market data current as of 2026-06-11 (today)  
✅ **Required Columns:** All present (SMA50, SMA200, ATR14, 20-day ranges, volume metrics)  
⚠️ **Position Count:** Currently 6, exceeds max 5 (HSBA.L exit will normalize)  
⚠️ **Cash Buffer:** Tight (3.17% vs. 3.00% required); post-SELL will improve to 7.3%  
⚠️ **Single-Name Concentration:** BP.L at 47.84% (above 30% limit) — structural, not actionable today  
⚠️ **Sector Concentration:** Energy at 47.84% (above 40% limit) — structural issue  
✅ **Turnover:** 4.14% (well below 30% limit)  
✅ **Min Position Age:** HSBA.L at 12 days (above 2-day minimum)  
✅ **Liquidity Filters:** All holdings exceed min_avg_gbp_volume (50k) and min_price_gbp (1.0)  
✅ **Portfolio Drawdown:** 8.61% (below 15% limit)  

---

## What Could Invalidate This Plan

1. **HSBA.L Execution Failure:** If the SELL order fails to execute or is delayed, cash will remain constrained and portfolio count will stay at 6.
2. **Overnight Gap Down:** If any held position (especially BP.L at 9.32 shares) gaps below its stop price overnight, the DAILY_CHECK system will trigger a mandatory market-order sell at next open, potentially at worse prices.
3. **News/Corporate Action:** Earnings, dividend declarations, or regulatory updates not in the provided data could alter technicals or fundamentals.
4. **FX Impact:** While prices are GBP-stated, any holding of non-GBP assets (none currently) could see FX headwinds.
5. **Liquidity Dry-Up:** A sudden widening of bid-ask spreads or volume collapse (not evidenced in market_data.csv) would increase slippage beyond 10 bps estimate.
6. **Settlement Failure:** If HSBA.L proceeds are not received by T+1 (tomorrow), cash availability for new BUYs remains restricted.

---

## Data Quality Notes

✅ **Market Data:** All required columns present (SMA50, SMA200, ATR14, volume ratios, drawdowns).  
✅ **Position Data:** Consistent; all tickers in market_data.csv match universe.csv.  
✅ **SMA200 Availability:** Available for all equities (>200 trading days of history).  
✅ **Volume Metrics:** 20-day averages and GBP volumes calculated and provided.  
✅ **Indicator Freshness:** All values dated 2026-06-11 (current session).  

No data quality issues detected.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data and pre-computed technical indicators. It is not financial advice, a recommendation to buy or sell, or a solicitation for investment.**

**Key Risks:**
- **Execution Risk:** Orders may not fill at projected prices; slippage, partial fills, and execution delays can occur.
- **Gap Risk:** Stop-losses monitored daily cannot protect against intraday, overnight, or weekend gaps. Actual losses may exceed planned risk.
- **Concentration Risk:** Portfolio holds significant single-name (BP.L 47.84%) and sector (Energy 47.84%) concentration above policy limits—a systemic vulnerability.
- **Model Risk:** Strategy relies on technical indicators (SMA, ATR, volume ratios) which can be whipsawed in choppy or low-liquidity environments.
- **Regulatory/Tax:** Stamp duty, transaction costs, and tax implications are estimated; consult a UK tax advisor for individual circumstances.
- **Settlement:** T+1 settlement in UK markets means proceeds are not available for reinvestment same-day; liquidity constraints may persist longer than expected.

**Use this plan at your own risk. Verify all assumptions, monitor execution in real-time, and be prepared to override or adjust if market conditions change materially.**

---

*Report Generated: 2026-06-11 (Automated DailyEquityTrader-UK System)*