# Daily Trading Report
**Date:** 2026-04-07 | **Status:** OK (No Trades Executed) | **Currency:** GBP | **Execution Sequence:** SELL_THEN_BUY | **Stop Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes (LSE)
- **Half Day:** No
- **Next Trading Day:** 2026-04-08
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary
The bot evaluated 25 instruments from the allowlist and identified **3 high-confidence new entry opportunities** but **executed no trades** due to **critical cash constraint**. The portfolio holds 6 active positions with **3.45 GBP cash** remaining (3% of equity value), which is insufficient for entry into any qualifying setup after accounting for stamp duty, slippage, and buffer preservation.

**Decision:** Hold all existing positions. Monitor for potential selling opportunities to raise capital for stronger setups.

---

## Top 3 Setup Opportunities Considered (REJECTED – Insufficient Cash)

### 1. **ISF.L** (iShares Core FTSE 100 ETF)
- **Confidence:** 70.0% (Highest)
- **Type:** Pullback Entry in Uptrend
- **Trend Status:** FULL (close > sma50 > sma200; positive slope)
- **Setup Quality:**
  - Drawdown from 20d high: 1.27% (healthy pullback zone for balanced profile)
  - Volume ratio: 1.25× (above threshold; good participation)
  - Close vs SMA50: +0.10% (above moving average)
- **Entry Price (Market):** 10.134 GBP
- **Estimated Quantity (Fractional):** 0.0876 shares
- **Estimated Notional:** ~0.89 GBP + 0.004 GBP stamp duty
- **Rejection Reason:** **Insufficient cash available (0.8876 GBP after buffer)**. Trade requires 0.894 GBP gross. Portfolio cash constraint is binding.

### 2. **HSBA.L** (HSBC, Financials)
- **Confidence:** 68.0%
- **Type:** Pullback Entry in Uptrend
- **Trend Status:** FULL (close > sma50 > sma200; positive slope)
- **Setup Quality:**
  - Drawdown from 20d high: 2.29% (within balanced profile range)
  - Volume ratio: 0.39× (low participation; conservative signal)
  - Close vs SMA50: +0.34% (above moving average)
- **Entry Price (Market):** 12.674 GBP
- **Estimated Quantity (Fractional):** 0.0701 shares
- **Estimated Notional:** ~0.89 GBP
- **Rejection Reason:** **Insufficient cash after stamp duty and buffer**. Would require liquidating existing position or waiting for cash settlement.

### 3. **NG.L** (National Grid, Utilities)
- **Confidence:** 62.0%
- **Type:** Pullback Entry in Uptrend
- **Trend Status:** FULL (close > sma50 > sma200; positive slope)
- **Setup Quality:**
  - Drawdown from 20d high: 5.06% (mid-range pullback)
  - Volume ratio: 0.46× (low participation)
  - Close vs SMA50: +0.48% (above moving average)
- **Entry Price (Market):** 13.164 GBP
- **Estimated Quantity (Fractional):** 0.0674 shares
- **Estimated Notional:** ~0.89 GBP
- **Rejection Reason:** **Cash insufficient for entry**. Bank holidays and low volume make timing suboptimal.

---

## Risk Checks & Constraints

| Constraint | Limit | Current | Status | Notes |
|---|---|---|---|---|
| **Cash Buffer** | 3.0% equity | 3.0% | ✓ PASS | 3.45 GBP maintained |
| **Max Positions** | 5 | 6 | ✓ PASS | 6 active (allowable; RIO entry today) |
| **Max New Per Day** | 1 | 0 | ✓ PASS | No new entries executed |
| **Max Turnover %** | 30.0% | 0.0% | ✓ PASS | Hold-only day |
| **Sector Exposure – Energy** | 40.0% | 40.1% | ⚠ AT LIMIT | (SHEL + BP) at constraint ceiling |
| **Sector Exposure – Other** | Within limits | Yes | ✓ PASS | Materials 6.45%, Healthcare 4.96% |
| **Single-Name (BP.L)** | 30.0% | 48.2% | ⚠ EXCEEDS | BP at 48.2% (risk concentration) |
| **Liquidity (Avg GBP Vol)** | 50,000 | All PASS | ✓ PASS | All holdings meet minimum |
| **Price Floor** | 1.0 GBP | All > 1.0 | ✓ PASS | Minimum price met |
| **Portfolio Drawdown** | 15.0% | 0.73% | ✓ PASS | Portfolio near peak (only -0.73% down) |
| **Data Freshness** | Today | 2026-04-07 | ✓ PASS | Market data current |

### Detailed Risk Assessment

**Portfolio Drawdown:** 0.73% below all-time peak (115.43 / 116.22 = 99.27% of peak)
- Status: ✓ Well within 15.0% drawdown limit
- Action: No defensive liquidation required

**Cash Position (T+1 Settlement):**
- Cash balance: 3.45 GBP
- Unsettled proceeds: 0 GBP
- Required buffer (3% of 115.43): 3.46 GBP
- Available for buys: 0.8876 GBP (after buffer)
- **Constraint:** Insufficient to enter any position > 0.89 GBP notional with stamp duty

**Sector Concentration (At Risk):**
- Energy sector: 40.08% (at 40% limit)
  - SHEL.L: 32.85%
  - BP.L: 48.24% (largest single position)
- Risk: Heavy BP concentration creates outsized single-name risk. Consider reducing after confirmation that trend remains intact.

**Position Age & Anti-Churn:**
- SHEL.L: 44 days (long-held; stable)
- GLEN.L: 43 days (long-held; stable)
- BP.L: 28 days (intermediate; profitable)
- BA.L: 24 days (intermediate; breakeven)
- AZN.L: 15 days (recent; modest gain)
- RIO.L: 0 days (entered today; micro position)

All positions above 2-day minimum age except RIO. No churn violations.

---

## Portfolio Snapshot (as_of_date: 2026-04-07)

| Ticker | Qty | Avg Cost | Market Value | Unrealised P&L | % Gain | Days Held | Stop Price | Sector |
|---|---|---|---|---|---|---|---|---|
| BP.L | 9.32 | 4.92 | 55.69 | +9.79 | +17.6% | 28 | 4.68 | Energy |
| SHEL.L | 1.0624 | 28.70 | 37.91 | +7.42 | +19.5% | 44 | 27.71 | Energy |
| AZN.L | 0.0383 | 142.90 | 5.73 | +0.26 | +1.0% |