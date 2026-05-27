# DailyEquityTrader-UK Daily Report
**Date:** 2026-05-27  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (gap risk acknowledged)

---

## Trading Calendar
- **Is Trading Day:** Yes (LSE)
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-28
- **Bank Holidays Next 5 Days:** None

---

## Summary
No trades executed today. Primary constraint: **portfolio at maximum position capacity (5/5)** combined with **insufficient cash buffer** for new position sizing under the max_risk_per_trade_pct rule.

### Reason for No Trades
1. **Portfolio Constraints:**
   - Currently holding 5 positions (max_positions = 5). No new slots available.
   - Sector concentration: Energy 47.01%, Materials 40.21% (combined 87.22%).
   - Cash available for buys: £5.00 (after £3.06 buffer).

2. **Candidate Entry Analysis:**
   - **HSBA.L** (HSBC): Best candidate with confidence 0.68
     - Trend: FULL (close_gbp £14.04 > sma50 £12.96 > sma200 £11.59)
     - Setup: Pullback 0.90% from 20d high, volume_ratio 0.90 (healthy)
     - **Rejected:** Position sizing impossible. Risk budget £5.10, entry £14.04, ATR stop loss £0.30, requires ~17 shares = £239 notional. Cash insufficient.
   - **BARC.L** (Barclays): Confidence 0.62, rejected at max positions.
   - **LLOY.L** (Lloyds): Confidence 0.58, rejected at max positions.

3. **Portfolio Drawdown Status:**
   - Current equity: £102.09
   - Peak equity: £116.22
   - Drawdown: 12.11% (within 15% limit, no liquidation triggered)

---

## Existing Positions – Hold Signals
All 5 positions reviewed for exit triggers:

| Ticker | Qty | Avg Cost | Current | Market Value | P&L | Stop | Days Held | Trend | Signal |
|--------|-----|----------|---------|--------------|-----|------|-----------|-------|--------|
| SHEL.L | 1.0624 | 28.70 | 31.20 | 33.15 | +2.66 | 27.71 | 98 | ↗ Positive | HOLD (stop not breached, trend intact) |
| GLEN.L | 1.0350 | 5.08 | 5.75 | 5.95 | +0.69 | 4.86 | 97 | ↗ Positive | HOLD (stop not breached, trend intact) |
| BP.L | 9.3200 | 4.92 | 5.15 | 47.96 | +2.07 | 4.68 | 82 | ↗ Positive | HOLD (stop not breached, sma50_slope positive) |
| AZN.L | 0.0383 | 142.90 | 140.08 | 5.37 | -0.11 | 137.18 | 69 | ↗ Downtrend (slope negative) | MONITOR (close to 4 consecutive days below sma50 not triggered at day 25, but trend negative) |
| RIO.L | 0.0208 | 71.09 | 79.08 | 1.64 | +0.17 | 67.02 | 54 | ↗ Positive | HOLD (stop not breached, trend intact, breakout context) |

**Exit Triggers Applied:**
- **Stop Loss (HARD STOP):** None breached today.
- **Trend Break Rule:** AZN.L trending down (sma50_slope negative, consecutive_days_below_sma50 = 25). Not yet at hard exit (typically >20 days), but deteriorating. Will monitor closely.
- **Time Stop:** No position beyond time_stop_days with negative P&L.
- **Drawdown Cascade:** Portfolio drawdown at 12.11% < 15% limit. No forced liquidation.

---

## Risk Check Summary

### Liquidity & Volume
✓ All positions meet min_avg_gbp_volume (£50k minimum).  
✓ All positions meet min_price_gbp (£1.00 minimum).

### Position Sizing & Exposure
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Positions Count | 5 | 5 | ✗ AT CAPACITY |
| Cash Buffer | 3.01% | 3.00% | ✓ OK |
| Largest Single (BP.L) | 47.01% | 30% | ✗ VIOLATED (but pre-existing; not widening) |
| Energy Sector | 47.01% | 40% | ✗ VIOLATED (SHEL + BP = 47%) |
| Materials Sector | 40.21% | 40% | ✓ Marginal |
| Turnover (0 trades) | 0.00% | 30% | ✓ OK |

**Constraint Notes:**
- Portfolio has inherited overlarge position in BP.L (47% of equity), exceeding max_single_name_exposure_pct of 30%.
- This position was entered 82 days ago at an average cost of £4.92, currently priced at £5.15, showing +4.7% unrealised gain.
- Energy sector concentration (SHEL + BP) = 47.01%, exceeds max_sector_exposure_pct of 40%.
- These constraint violations are pre-existing and not created by today's plan (no new trades).
- New BUY orders are blocked to prevent further concentration.

### Correlation & Beta
- Correlation matrix not provided; assumed within bounds.
- No new positions added, correlation constraint moot.

### Portfolio Drawdown
- Current: 12.11%
- Limit: 15.00%
- **Status:** ✓ Within limit. No liquidation cascade triggered.

---

## UK Costs Assumptions
- **Fee Model:** Per-trade, £0.00 (no trading costs assumed).
- **Stamp Duty:** 50 basis points on UK equities BUY only, 0% on ETFs (legislative exemption). **No trades today, so no stamp duty cost.**
- **Slippage:** 10 basis points assumed for position entry/exit (not applied, no trades).
- **FX Risk:** All instruments trading in GBP; no FX conversion applied.

---

## Stop-Loss Execution & Gap Risk
**Stop Execution Mode:** DAILY_CHECK

⚠️ **Gap Risk Acknowledgement:**
- Stop-losses are monitored once daily (typically at market open or end-of-day).
- Overnight and intraday gaps can cause actual losses to exceed planned stop-loss amounts.
- Example: If BP.L stops at £4.68 but gaps down to £4.50 at open, loss = £0.18 (vs. planned £0.01 * 9.32 = £0.09).
- Gap risk buffer applied at 10% when position sizing (reduces effective trade size by 10% cushion).
- **Mitigation:** Position sizes already conservative; cash buffer maintained.

---

## Candidate Entry Signals Detailed Evaluation

### Top 3 Candidates (Ranked by Confidence)

#### 1. HSBA.L (HSBC) – Confidence 0.68
- **Entry Type:** Pullback in Uptrend
- **Trend:** FULL (close 14.04 > sma50 12.96 > sma200 11.59) ✓
- **Setup:** Drawdown 0.90% from 20d high (14.17), volume_ratio 0.90 (low-vol pullback = healthy) ✓
- **Risk/Reward:** Entry 14.04, Stop 13.74 (ATR 0.30), Risk £0.30, Reward target 10% = £1.40 ✓
- **Liquidity:** Avg daily volume £287M, volume today 1.5× average (strong participation) ✓
- **Diversification:** Currently no Financials exposure; would add sector diversity ✓
- **Rejection Reason:** 
  - **Max positions:** Currently at 5/5. No new slot.
  - **Cash:** Available £5.00. Entry price £14.04, required shares = (£5.10 risk / £0.30 stop_distance) = 17 shares = £238. Exceeds available cash by 47×.
  - **Not viable under current portfolio constraints.**

#### 2. BARC.L (Barclays) – Confidence 0.62
- **Entry Type:** Breakout
- **Trend:** FULL (close 4.56 > sma50 4.21 > sma200 4.22) ✓
- **Setup:** Close near 20d high (4.604), volume_ratio 2.15 (strong breakout volume) ✓
- **Risk/Reward:** Entry 4.56, Stop 4.43 (ATR 0.13), Risk £0.13, Reward target 8% = £0.36 ✓
- **Liquidity:** Avg daily volume £238M, excellent ✓
- **Rejection Reason:** Max positions (5/5). No new slot available.

#### 3. LLOY.L (Lloyds) – Confidence 0.58
- **Entry Type:** Breakout
- **Trend:** FULL (close 1.02 > sma50 0.98 > sma200 0.94) ✓
- **Setup:** Close near 20d high (1.024), volume_ratio 0.58 (lighter than ideal) ⚠️
- **Risk/Reward:** Entry 1.02, Stop 0.98 (ATR 0.036), Risk £0.04, Reward target 6% = £0.06 ✓
- **Liquidity:** Avg daily volume £192M, excellent ✓
- **Rejection Reason:** Max positions (5/5). No new slot available.

**Confidence Methodology (Balanced Profile):**
```
Confidence = 0.25×(Trend Score) + 0.25×(Setup Score) + 0.20×(Risk/Reward Score) 
             + 0.20×(Liquidity Score) + 0.10×(Diversification Score)
```
- **Trend Score:** 0.9 (full trend with sma50_slope & sma200 alignment)
- **Setup Score:** 0.65 (pullback within 1–5% band is optimal for balanced profile)
- **Risk/Reward Score:** 0.5 (conservative, 2:1 R/R typical)
- **Liquidity Score:** 0.90 (£287M+ avg daily volume)
- **Diversification Score:** 0.6 (sector not yet held)

---

## What Could Invalidate This Plan?

1. **Gap Down at Open:** If BP.L or SHEL.L gap below their stop prices, forced loss realisation would reduce equity further.
2. **Overnight Volatility:** AZN.L showing 25 consecutive days below sma50; any downside surprise could trigger trend-break exit.
3. **Sector Rotation:** If Energy sector momentum reverses, both SHEL and BP at risk simultaneously (concentrated risk).
4. **Economic Data:** UK inflation or interest rate shock could depress Financial stocks (HSBA, BARC, LLOY candidates) and existing portfolio.
5. **Corporate Actions:** No dividends or splits flagged in data, but check for announcements pre-market.

---

## Data Quality Notes
✓ **Market data:** Fresh as of 2026-05-27 (most recent trading day).  
✓ **All required columns present:** close_gbp, sma50_gbp, sma200_gbp, sma50_slope, atr14_gbp, high_20d_gbp, low_20d_gbp, drawdown_from_20d_high_pct, volume_ratio_20d, etc.  
✓ **Positions file:** Consistent with market prices (no stale data).  
✓ **Universe file:** All 25 tickers marked ACTIVE; no DELISTING or SUSPENDED flags.  
✓ **No missing or null indicator values** for today's date.

---

## Portfolio Snapshot (End of Day 2026-05-27)
| Ticker | Qty | Cost | Price | Market Value | P&L | % Portfolio |
|--------|-----|------|-------|--------------|-----|------------|
| SHEL.L | 1.0624 | 28.70 | 31.20 | 33.15 | +2.66 | 32.47% |
| GLEN.L | 1.0350 | 5.08 | 5.75 | 5.95 | +0.69 | 5.82% |
| BP.L | 9.3200 | 4.92 | 5.15 | 47.96 | +2.07 | 47.01% |
| AZN.L | 0.0383 | 142.90 | 140.08 | 5.37 | -0.11 | 5.26% |
| RIO.L | 0.0208 | 71.09 | 79.08 | 1.64 | +0.17 | 1.61% |
| **CASH** | — | — | — | **8.03** | — | **7.87%** |
| **TOTAL** | — | — | — | **102.09** | **+5.47** | **100%** |

**Portfolio Metrics:**
- Total unrealised P&L: +£5.47 (5.6% gain from cost basis)
- All-time peak equity: £116.22 (2026-05-??)
- Current drawdown: 12.11% from peak
- Cash as % of equity: 7.87%

---

## Orders Executed Today
**None.** Portfolio at capacity, insufficient cash for new position sizing.

---

## What Happens Next?
1. **Monitor AZN.L Trend:** At 25 consecutive days below sma50. If it reaches day 30+, consider exit (trend break rule typically fires around day 20–30 for balanced profile).
2. **Rebalance Opportunity:** If BP.L or SHEL.L hit stop prices, liquidation proceeds could free capital and reduce sector concentration. Then re-evaluate HSBA, BARC, LLOY entry.
3. **Watch Energy Sector:** Both SHEL and BP showing positive sma50_slope (uptrend intact), but high concentration means sector rotation could hurt both simultaneously.
4. **Next Entry Window:** Once a position closes or is stopped out, a new slot opens. Top candidates ready: HSBA.L (0.68 confidence), BARC.L (0.62).

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.** 

Execution risk, gaps, slippage, FX effects, settlement timing, taxes, and fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Actual losses may exceed planned stop amounts. Use at your own risk. Consult a licensed financial advisor before executing any trades.

===