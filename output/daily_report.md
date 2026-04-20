# Daily Trading Plan Report
**Date:** 2026-04-20  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (monitored daily, gap risk present)  

---

## Trading Calendar
- **Is Trading Day:** Yes (LSE open)
- **Is Half Day:** No
- **Next Trading Day:** 2026-04-21
- **Bank Holidays (next 5 days):** None

---

## Executive Summary
No trades will be executed today. The portfolio is constrained by two binding factors:
1. **Position Limit Exceeded:** Currently holding 6 positions against a maximum of 5
2. **Insufficient Cash:** After applying a mandatory 3% cash buffer (GBP 3.25), only GBP 0.20 remains available for new trades—far below the capital required for any meaningful position

While the strategy identified three high-confidence trade setups (REL.L breakout at 0.76 confidence, LSEG.L breakout at 0.74, and HSBA.L pullback at 0.71), all were rejected due to capital constraints.

---

## Top 3 Setup Candidates (Rejected)

### 1. REL.L (RELX) – BREAKOUT | Confidence 0.76
- **Setup:** Close at GBP 27.06 is within 2.2% of 20-day high (GBP 27.64), volume ratio 2.23x average (strong)
- **Trend:** Full uptrend (close > SMA50 > SMA200); positive SMA50 slope
- **Confidence Components:** Trend 1.0 | Setup 0.82 | Risk/Reward 0.68 | Liquidity 0.92 | Diversification 0.72
- **Rejection Reason:** Insufficient cash. Estimated entry notional GBP 20.27 exceeds available GBP 0.20 after buffer.

### 2. LSEG.L (London Stock Exchange) – BREAKOUT | Confidence 0.74
- **Setup:** Close GBP 94.12 within 2.8% of 20-day high (GBP 96.77), volume ratio 0.72x (moderate liquidity)
- **Trend:** Full uptrend; positive SMA50 slope
- **Confidence Components:** Trend 1.0 | Setup 0.80 | Risk/Reward 0.65 | Liquidity 0.88 | Diversification 0.70
- **Rejection Reason:** Insufficient cash. Estimated entry notional GBP 18.82 far exceeds available GBP 0.20.

### 3. HSBA.L (HSBC) – PULLBACK | Confidence 0.71
- **Setup:** Pullback at 1.16% from 20-day high, trading above SMA50 (GBP 12.73)
- **Trend:** Full uptrend; positive SMA50 slope; highest liquidity among candidates
- **Confidence Components:** Trend 1.0 | Setup 0.76 | Risk/Reward 0.62 | Liquidity 0.95 | Diversification 0.68
- **Rejection Reason:** Capital insufficient; also sector concentration risk (already 3 Financials positions).

---

## Risk Checks: All Constraints

| Constraint | Limit | Actual | Status |
|---|---|---|---|
| **Position Count** | 5 max | 6 current | ❌ **VIOLATED** |
| **Cash Buffer (3%)** | GBP 3.25 | GBP 3.45 available | ✓ Compliant |
| **Available for Buys (post-buffer)** | N/A | GBP 0.20 | ⚠️ **Critical** |
| **Portfolio Drawdown** | 15% max | 6.64% | ✓ Compliant |
| **Turnover (daily)** | 30% max | 0% | ✓ Compliant |
| **Largest Single Name** | 30% max | 47.9% (BP.L) | ⚠️ High but holding |
| **Sector Concentration (Energy)** | 40% max | 41.1% | ⚠️ At limit |
| **Min Position Age** | 2 days | 15–59 days held | ✓ All compliant |

---

## Portfolio Drawdown Analysis
- **Current Equity:** GBP 108.42
- **Peak Equity:** GBP 116.22
- **Drawdown:** 6.64%
- **Drawdown Limit:** 15%
- **Status:** ✓ Within limit; no forced liquidation required

---

## Stop-Loss Checks
**All existing positions remain active; no stop-loss triggers today:**
- SHEL.L: low GBP 32.41 > stop GBP 27.71 ✓
- GLEN.L: low GBP 5.45 > stop GBP 4.86 ✓
- BP.L: low GBP 5.524 > stop GBP 4.68 ✓
- BA.L: low GBP 22.245 > stop GBP 21.50 ✓
- AZN.L: low GBP 148.82 > stop GBP 137.18 ✓
- RIO.L: low GBP 73.14 > stop GBP 67.02 ✓

---

## Cost Model Assumptions
- **Fee Model:** Per-trade, GBP 0.00 per trade (no commission)
- **Stamp Duty:** 50 bps applied to UK equity BUY orders only (ETFs exempt)
- **Slippage Estimate:** 10 bps on market orders
- **Gap Risk:** 10% buffer applied to all position sizes (DAILY_CHECK mode only)
- **Cost Basis:** Included in orders if executed

**Note:** No costs incurred today as no trades executed.

---

## Gap Risk Acknowledgement
The bot operates in **DAILY_CHECK mode**. Stop-loss prices are monitored once daily (at this report generation). **Overnight gaps, intraday moves, and trading halts can cause losses to exceed planned risk.** Stop-losses cannot protect against gaps down past the stop price. Use at your own risk.

---

## Current Portfolio Snapshot

| Ticker | Sector | Qty | Avg Cost | Market Value | Unrealised P&L | Days Held | Stop Price | Status |
|---|---|---|---|---|---|---|---|---|
| SHEL.L | Energy | 1.0624 | GBP 28.70 | GBP 34.79 | +GBP 4.30 | 59 | GBP 27.71 | ACTIVE |
| GLEN.L | Materials | 1.0350 | GBP 5.08 | GBP 5.69 | +GBP 0.43 | 58 | GBP 4.86 | ACTIVE |
| BP.L | Energy | 9.3200 | GBP 4.92 | GBP 51.90 | +GBP 6.01 | 43 | GBP 4.68 | ACTIVE |
| BA.L | Industrials | 0.2378 | GBP 22.61 | GBP 5.33 | -GBP 0.05 | 39 | GBP 21.50 | ACTIVE |
| AZN.L | Healthcare | 0.0383 | GBP 142.90 | GBP 5.73 | +GBP 0.25 | 30 | GBP 137.18 | ACTIVE |
| RIO.L | Materials | 0.0208 | GBP 71.09 | GBP 1.54 | +GBP 0.06 | 15 | GBP 67.02 | ACTIVE |
| **Total** | — | — | — | **GBP 108.42** | **+GBP 10.99** | — | — | — |

**Portfolio Composition by Sector:**
- Energy: 41.1% (SHEL.L + BP.L)
- Materials: 6.6% (GLEN.L + RIO.L)
- Industrials: 4.9% (BA.L)
- Healthcare: 5.3% (AZN.L)
- **Cash: 3.2%**

---

## Orders
**None. No trades to execute.**

---

## What Could Invalidate This Plan?

1. **Overnight Gap Down:** Any position gapping down past its stop price before tomorrow's daily check would result in losses exceeding planned risk.
2. **Corporate Actions:** Dividend ex-dates, stock splits, or delisting notices could alter position values or eligibility.
3. **Sudden Liquidity Drain:** A sharp drop in volume or bid-ask spreads could prevent exits at planned prices.
4. **Sentiment Shock:** Major news (earnings misses, sector downgrades, macro events) could break trend filters and trigger unplanned exits.
5. **Broker Issues:** Settlement delays, trading halts, or system outages could prevent order execution.
6. **FX Movement:** (Non-applicable here; all holdings GBP-denominated.)

---

## Data Quality Notes
✓ All required columns present in market_data.csv  
✓ All tickers found in universe.csv with ACTIVE status  
✓ Market data is fresh (2026-04-20 matches as_of_date)  
✓ All required pre-computed indicators provided (SMA50, SMA200, ATR14, etc.)  
✓ Positions data consistent and non-null  
✓ No GBP FX conversions needed (all GBP listings)  

---

## Recommendation for Next Session
The portfolio is constrained by position count and capital availability. To unlock trading capacity:
- **Consider selling the smallest position (RIO.L, GBP 1.54)** to free capital and reduce position count.
- **Monitor REL.L, LSEG.L, and HSBA.L** for re-entry if pullbacks occur and capital becomes available.
- Once position count drops to ≤4, capital will be freed for new entries.

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution risk, gaps, slippage, FX effects, settlement timing, broker outages, and taxes/fees apply in live trading. Stop-losses in DAILY_CHECK mode are monitored once daily and **cannot protect against intraday or overnight gaps.** Actual losses may exceed planned risk. Stamp duty (50 bps on UK equity purchases), trading costs, and market impact are not guaranteed.

**Use at your own risk.** Consult a qualified financial adviser before deploying capital.

---

*Generated by DailyEquityTrader-UK on 2026-04-20 | Strategy: Balanced Swing (3–20 days) | Mode: Paper*