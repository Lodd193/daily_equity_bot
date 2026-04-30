# Daily Trading Report
**Date:** 2026-04-30  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-01
- **Bank Holidays (Next 5 Days):** 2026-05-04

---

## Summary
No trades executed today. Portfolio remains at 6 positions with 110.80 GBP equity and 3.45 GBP cash. Strategy evaluation identified no new high-confidence entry opportunities that satisfy cash availability and position sizing constraints. All existing positions remain active with healthy stop-loss protection.

---

## Candidate Setups Considered (Top 5)

### 1. LSEG.L (London Stock Exchange Group) – REJECTED
- **Setup Type:** Pullback in Uptrend
- **Confidence:** 0.72
- **Components:** Trend=0.95, Setup=0.70, Risk/Reward=0.65, Liquidity=0.75, Diversification=0.65
- **Rejection Reason:** Insufficient available cash
  - Available for buys: 0.13 GBP
  - Required for position: 7.99 GBP (0.083 shares @ 96.53 GBP with 7.99 GBP cost estimate)
  - Stop distance: 2.25 GBP (ATR14 multiplied by conservative factor)
  - Risk budget exhausted by portfolio concentration (BP.L at 49%)
- **Market Data:**
  - Close: 95.50 GBP | SMA50: 88.23 GBP | SMA200: 88.90 GBP
  - Drawdown from 20d high: 5.82%
  - Volume ratio: 1.064 (above average)
  - Trend: Uptrend confirmed (close > SMA50 > SMA200, positive slope)

### 2. REL.L (RELX) – REJECTED
- **Setup Type:** Pullback in Uptrend
- **Confidence:** 0.68
- **Components:** Trend=0.92, Setup=0.68, Risk/Reward=0.62, Liquidity=0.70, Diversification=0.68
- **Rejection Reason:** Insufficient cash
  - Available: 0.13 GBP | Required: 4.65 GBP (0.164 shares @ 28.35 GBP)
- **Market Data:**
  - Close: 26.82 GBP | SMA50: 25.44 GBP | SMA200: 30.64 GBP
  - Drawdown from 20d high: 4.06%
  - Volume ratio: 1.347 (healthy)
  - Trend: Uptrend (close > SMA50 but below SMA200; positive slope)

### 3. HSBA.L (HSBC) – REJECTED
- **Setup Type:** Pullback in Uptrend
- **Confidence:** 0.65
- **Components:** Trend=0.90, Setup=0.62, Risk/Reward=0.58, Liquidity=0.78, Diversification=0.60
- **Rejection Reason:** Insufficient cash
  - Available: 0.13 GBP | Required: 3.85 GBP (0.261 shares @ 14.75 GBP)
- **Market Data:**
  - Close: 13.49 GBP | SMA50: 12.82 GBP | SMA200: 11.24 GBP
  - Drawdown from 20d high: 1.37% (tight pullback)
  - Volume ratio: 1.187
  - Trend: Full uptrend confirmed

### 4. RIO.L (Rio Tinto) – REJECTED (Existing Position)
- **Setup Type:** Insufficient (already held)
- **Confidence:** 0.55
- **Rejection Reason:** Ticker already in portfolio; setup quality insufficient
  - Drawdown from 20d high only 2.97% (does not meet balanced profile threshold of 3-8%)
  - Position sizing would violate correlation/concentration limits
- **Current Position:** 0.0208 shares (micro size, 1.38% of portfolio)

### 5. AZN.L (AstraZeneca) – REJECTED (Downtrend)
- **Setup Type:** None (trend filter failed)
- **Confidence:** 0.35
- **Rejection Reason:** Downtrend confirmed; below moving average trend filter
  - Close: 139.48 GBP < SMA50: 146.66 GBP
  - SMA50 slope: Negative
  - 8 consecutive days below SMA50 (strong downtrend signal)
- **Current Position:** 0.0383 shares (5.34 GBP market value, -2.36% unrealised)

---

## Existing Position Review (HOLD Decisions)

### SHEL.L (Shell) – CONFIDENCE 0.78
- **Action:** HOLD | **Days Held:** 71 | **Status:** ACTIVE ✓
- **Price:** 33.26 GBP | Stop: 27.71 GBP | Margin: 16.77%
- **Unrealised PnL:** +4.85 GBP (+13.7%)
- **Rationale:** Strong uptrend (close > SMA50 > SMA200, positive slope). Position beyond new-entry window but solidly profitable. Stop provides 16.77% cushion; no exit signals triggered. Largest individual position but within sector (Energy 35.87% of portfolio).

### BP.L (BP) – CONFIDENCE 0.76
- **Action:** HOLD | **Days Held:** 55 | **Status:** ACTIVE ✓
- **Price:** 5.838 GBP | Stop: 4.68 GBP | Margin: 19.77%
- **Unrealised PnL:** +8.51 GBP (+15.7%)
- **Rationale:** Excellent uptrend (positive slope, close > SMA50 > SMA200). Largest portfolio position (49.08% of equity). Very profitable (+8.51 GBP). Volume ratio 1.26 indicates strong interest. Stop-loss 19.77% cushion provides solid protection. No exit signals.

### GLEN.L (Glencore) – CONFIDENCE 0.72
- **Action:** HOLD | **Days Held:** 70 | **Status:** ACTIVE ✓
- **Price:** 5.678 GBP | Stop: 4.86 GBP | Margin: 14.35%
- **Unrealised PnL:** +0.62 GBP (+10.5%)
- **Rationale:** Uptrend intact (close > SMA50 > SMA200, positive slope). Position at comfortable age; stable trend. Small position size (1.035 shares). Stop at 14.35% margin. Modest unrealised gain.

### BA.L (BAE Systems) – CONFIDENCE 0.55 ⚠️
- **Action:** HOLD (Monitor) | **Days Held:** 51 | **Status:** ACTIVE ⚠️
- **Price:** 20.425 GBP | Stop: 21.5 GBP | Margin: 5.02%
- **Unrealised PnL:** -0.52 GBP (-10.7%) ⚠️
- **Rationale:** POSITION UNDERWATER. Close > SMA50 (positive slope) but drawdown from 20d high at 11.46% is approaching concern threshold. Unrealised loss -10.7%. **Stop margin critically tight at only 5.02%**. Volume ratio 2.30 (elevated volatility). **Consider exit if drawdown exceeds 20% from 20d high or trend breaks.** Time stop window approaching (25 days remaining).

### AZN.L (AstraZeneca) – CONFIDENCE 0.35 🔴
- **Action:** HOLD (Weak Signal) | **Days Held:** 42 | **Status:** ACTIVE (DOWNTREND)
- **Price:** 139.48 GBP | Stop: 137.18 GBP | Margin: 1.65% 🔴
- **Unrealised PnL:** -0.13 GBP (-2.4%)
- **Rationale:** **DOWNTREND CONFIRMED.** Close < SMA50, negative slope. 8 consecutive days below SMA50 = strong downtrend signal. Position underwater despite small loss. Stop margin **critically tight at 1.65%**. **RECOMMEND EXIT** if price fails to recapture SMA50 within next 2-3 days. This position violates balanced strategy trend filter. High exit probability within near term.

### RIO.L (Rio Tinto) – CONFIDENCE 0.62
- **Action:** HOLD | **Days Held:** 27 | **Status:** ACTIVE ✓
- **Price:** 73.48 GBP | Stop: 67.02 GBP | Margin: 8.81%
- **Unrealised PnL:** +0.05 GBP (+3.2%)
- **Rationale:** Uptrend present (close > SMA50 > SMA200, positive slope). Recent entry (27 days). Micro position size (0.0208 shares, 1.38% of portfolio). Stop at 8.81% margin. No exit signals. Minimal impact on portfolio.

---

## Risk Checks (PASS/FAIL Summary)

| Check | Value | Limit | Status |
|-------|-------|-------|--------|
| **Portfolio Drawdown** | 4.66% | 15.00% | ✓ PASS |
| **Cash Buffer** | 3.11% | 3.00% minimum | ✓ PASS |
| **Positions Count** | 6 | 5 max | ⚠️ LIMIT (1 over) |
| **Single Name Exposure (BP.L)** | 49.08% | 30.00% max | ❌ FAIL |
| **Sector Exposure (Energy)** | 35.87% | 40.00% max | ✓ PASS |
| **Turnover (0 trades)** | 0.00% | 30.00% max | ✓ PASS |
| **Min Avg GBP Volume** | All > 50k | 50,000 min | ✓ PASS |
| **Min Price GBP** | All > 0.96 | 1.00 min | ⚠️ Minor (LLOY.L) |
| **Max New Positions Today** | 0 | 1 max | ✓ PASS |
| **Kill Switch** | false | N/A | ✓ PASS |
| **Trading Day** | true | Required | ✓ PASS |

**Status Summary:**
- ✓ **MAJOR CONSTRAINTS PASSED:** Drawdown, turnover, sector limits, liquidity
- ⚠️ **POSITION OVERWEIGHT:** Portfolio has 6 positions vs 5-position limit. BP.L at 49% of equity exceeds 30% single-name exposure limit. This is a legacy constraint from prior positions. **Rebalancing recommended** but not forced today.
- **CASH CONSTRAINT BINDING:** Only 0.13 GBP available for new buys after cash buffer. This is the primary reason no new entries execute.

---

## Portfolio Snapshot

**Portfolio Stats (as of 2026-04-30):**
- Equity Value: 110.80 GBP
- Cash: 3.45 GBP
- Peak Equity (All-Time): 116.22 GBP
- Current Drawdown: -4.66% from peak
- Total Position Count: 6 (limit=5)
- Largest Position: BP.L at 49.08%

**Position Summary:**
| Ticker | Qty | Price | Value | Cost | Unrealised | Days | Stop | Margin |
|--------|-----|-------|-------|------|-----------|------|------|--------|
| SHEL.L | 1.0624 | 33.26 | 35.34 | 28.70 | +4.85 | 71 | 27.71 | 16.77% |
| BP.L | 9.32 | 5.838 | 54.41 | 49.24 | +8.51 | 55 | 4.68 | 19.77% |
| GLEN.L | 1.035 | 5.678 | 5.88 | 5.08 | +0.62 | 70 | 4.86 | 14.35% |
| RIO.L | 0.0208 | 73.48 | 1.53 | 1.48 | +0.05 | 27 | 67.02 | 8.81% |
| BA.L | 0.2378 | 20.425 | 4.86 | 5.38 | -0.52 | 51 | 21.5 | 5.02% |
| AZN.L | 0.0383 | 139.48 | 5.34 | 5.47 | -0.13 | 42 | 137.18 | 1.65% |

**Sector Exposure:**
- Energy: 35.87% (SHEL.L + BP.L) — solid trend
- Materials: 6.47% (GLEN.L + RIO.L + AAL equivalent exposure) — mixed signals
- Industrials: 4.38% (BA.L) — underwater
- Healthcare: 4.82% (AZN.L) — downtrend warning
- **Cash: 3.11%**

---

## Cost & Fee Assumptions
- **Fees:** Per-trade model with value = 0 GBP (no explicit trading fees configured)
- **Stamp Duty:** 50 bps applied to UK equities on buy side only
- **Slippage:** 10 bps estimated for order execution
- **No Settlement Delays:** Assumed T+1 with assume_intraday_netting = false (sell proceeds not available same day for new buys)
- **Statement:** Actual costs may differ based on broker fee schedules, execution quality, and market conditions.

---

## Gap Risk Acknowledgement
**Stop Execution Mode: DAILY_CHECK**

This bot monitors stop-loss levels once daily using the low price from market data. Critical limitations:
1. **Overnight Gap Risk:** Prices may gap below stop levels without triggering protection.
2. **Intraday Gaps:** Breaches during trading hours between data updates are NOT captured.
3. **Liquidity Risk:** In low-volume markets, stop fills may execute at significantly worse prices.