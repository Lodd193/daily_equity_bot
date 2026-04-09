# Daily Trading Report
**Date:** 2026-04-09  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-04-10
- **Bank Holidays (Next 5 Days):** None

---

## Summary
No trades were executed today. The portfolio has insufficient cash available for new position sizing after the mandatory 3% cash buffer requirement.

**Key Metrics:**
- **Portfolio Equity:** £112.75
- **Cash Balance:** £3.45
- **Required Buffer (3%):** £3.38
- **Available for Buys (after buffer):** £0.07
- **Portfolio Drawdown from Peak:** 3.01% (Limit: 15.0%)

The portfolio is currently holding 6 positions across Energy, Materials, Healthcare, and Industrials sectors. All positions remain above their stop-loss levels.

---

## Entry Opportunities Evaluated (Top 3 Candidates)

### 1. HSBA.L (HSBC Holdings)
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 13.34 > SMA50 12.66 > SMA200 10.93)
- **Confidence Score:** 0.62
- **Components:**
  - Trend: 1.0 (Full uptrend intact)
  - Setup: 0.45 (1.88% drawdown from 20d high; borderline pullback)
  - Risk/Reward: 0.50 (ATR 0.47, stop ~12.90, potential 8-12% upside)
  - Liquidity: 0.95 (18.9M shares, £410M daily vol)
  - Diversification: 0.60 (Financials; slight sector overlap)
- **Rejection Reason:** Insufficient cash (£3.45) vs. required position size (£8+). After buffer deduction, effectively £0.07 remaining.

### 2. LSEG.L (London Stock Exchange Group)
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 89.88 > SMA50 82.57 > SMA200 89.84 with caution)
- **Confidence Score:** 0.58
- **Components:**
  - Trend: 1.0 (Positive slope, above SMA50)
  - Setup: 0.40 (2.03% drawdown; marginal pullback)
  - Risk/Reward: 0.45 (ATR 2.46, wider stops needed)
  - Liquidity: 0.85 (1.5M shares, £206M daily vol)
  - Diversification: 0.55 (Financials; overlaps HSBA)
- **Rejection Reason:** Insufficient cash.

### 3. GLEN.L (Glencore) - Already Held
- **Entry Type:** NONE (position review)
- **Trend Status:** FULL (close 5.61 > SMA50 5.20 > SMA200 3.90)
- **Confidence Score:** 0.61 (if entry considered)
- **Current Position:** 1.035 shares @ £5.80 market value
- **Status:** Position meets trend criteria. Held for 49 days (well above min_position_age_days). No anti-churn violation. Continue holding.

---

## Risk Checks Summary

| Check | Result | Pass/Fail |
|-------|--------|-----------|
| **Portfolio Drawdown** | 3.01% < 15.0% limit | ✓ PASS |
| **Max Positions** | 6 current, 5 allowed | ⚠ CAUTION (at capacity) |
| **Sector Exposure (Energy)** | 36.02% < 40% limit | ✓ PASS |
| **Single Name (BP.L)** | 47.98% ≈ 48% < 30% limit | ✗ FAIL (overweight) |
| **Cash Buffer** | 3.45 GBP available, 3.38 GBP required | ✓ PASS (marginal) |
| **Turnover Limit** | 0.0% (no trades) < 30% | ✓ PASS |
| **Liquidity (min avg vol £50k)** | All > £50k except VMID, CSP1, others excluded | ✓ PASS |

**Critical Issue:** Position in BP.L has grown to 48% of portfolio equity, well above the 30% single-name exposure limit. This position should be monitored for reduction on future rebalance opportunities.

---

## Portfolio Drawdown Status
- **Peak Equity:** £116.22 (recorded)
- **Current Equity:** £112.75
- **Drawdown:** 3.01%
- **Limit:** 15.0%
- **Status:** ✓ Within acceptable range. No forced liquidation triggered.

---

## UK Costs Assumption Statement
- **Stamp Duty:** 50 bps applied to UK equities only on BUY orders (ETFs exempt)
- **Trading Fees:** £0 per trade (fee_model.value = 0)
- **Slippage Assumption:** 10 bps on market entries
- **Note:** No trades executed today; cost estimates not applicable.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
The bot monitors stop-losses once daily (at open/market hours). In DAILY_CHECK mode:
- **Risk:** Overnight or intraday gaps can cause actual losses to exceed planned risk.
- **Gap Risk Buffer:** 10% reduction applied to position sizing (CONFIG: gap_risk_buffer_pct = 0.1) when calculating fractional shares.
- **Impact:** Today's situation: no new trades, so buffer not applied. Existing positions carry inherent gap risk on stop-loss execution.
- **Mitigation:** Consider tighter stops or broker GTC (Good-Till-Cancelled) orders if available.

---

## Existing Positions Snapshot

| Ticker | Qty | Avg Cost | Market Value | P&L (GBP) | P&L (%) | Days Held | Stop Loss | Status | Sector |
|--------|-----|----------|--------------|-----------|---------|-----------|-----------|--------|--------|
| SHEL.L | 1.0624 | 28.70 | 36.64 | 6.15 | 16.8% | 50 | 27.71 | ACTIVE | Energy |
| GLEN.L | 1.0350 | 5.08 | 5.80 | 0.54 | 10.3% | 49 | 4.86 | ACTIVE | Materials |
| BP.L | 9.3200 | 4.92 | 54.10 | 8.21 | 17.9% | 34 | 4.68 | ACTIVE | Energy |
| BA.L | 0.2378 | 22.61 | 5.40 | 0.02 | 0.3% | 30 | 21.50 | ACTIVE | Industrials |
| AZN.L | 0.0383 | 142.90 | 5.85 | 0.38 | 6.9% | 21 | 137.18 | ACTIVE | Healthcare |
| RIO.L | 0.0208 | 71.09 | 1.51 | 0.03 | 1.9% | 6 | 67.02 | ACTIVE | Materials |
| **TOTAL** | — | — | **109.30** | **15.33** | **16.3%** | — | — | — | — |

**Cash:** £3.45  
**Total Portfolio:** £112.75

---

## Orders to Execute
**No orders today.**

---

## What Could Invalidate This Plan?
1. **Gap Down at Open:** If SHEL.L, BP.L, or another large position gaps below its stop-loss overnight, the plan to hold would be breached. Actual exit would occur at lower prices.
2. **Major News/Earnings:** Unannounced corporate actions, profit warnings, or sector shocks could trigger trend breaks.
3. **Dividend Payments:** If dividends are paid and reinvested, cash position changes.
4. **Settlement Changes:** If T+1 settlement advances or delays occur, availability of buy-side cash may shift.
5. **Correlation Breakdown:** If held positions suddenly diverge in trend, rebalancing may become necessary.
6. **Liquidity Dry-Up:** If trading volumes collapse (e.g., market stress), actual fill prices may deviate significantly from VWAP.

---

## Data Quality Notes
✓ **market_data.csv:** All required pre-computed columns present (SMA50, SMA200, ATR14, drawdown, volume ratio, etc.)  
✓ **positions.json:** Current portfolio snapshot provided, all positions ACTIVE.  
✓ **universe.csv:** 25 tickers (20 equities, 5 ETFs) all marked ACTIVE in LSE.  
✓ **trading_calendar.json:** Confirmed trading day, no bank holidays.  
✓ **Data Freshness:** Market data dated 2026-04-09 matches as_of_date. No staleness issue.  

**Excluded Tickers:** None (all data complete).

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution involves risks including but not limited to:
- **Overnight/intraday gaps:** Stop-losses monitored once daily cannot protect against gap moves.
- **Slippage:** Actual execution prices may deviate from market prices; 10 bps assumed.
- **Stamp Duty & Fees:** 50 bps UK stamp duty on equities; costs may vary by broker.
- **FX Risk:** Non-GBP holdings subject to currency fluctuation (none in this portfolio).
- **Settlement:** T+1 in UK; proceeds not available same-day for reinvestment under current settings.
- **Taxation:** Profits/losses subject to UK Capital Gains Tax. No tax optimization applied.
- **Model Risk:** Strategy assumes historical relationships persist; momentum reversals may occur.

**Use at your own risk. Backtest results do not guarantee future performance.**

---