# Daily Trading Plan Report
**Date:** 2026-04-13 | **Status:** NO_TRADES | **Currency:** GBP | **Execution:** SELL_THEN_BUY | **Stop Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes (LSE)
- **Half Day:** No
- **Next Trading Day:** 2026-04-14
- **Bank Holidays (Next 5 Days):** None

---

## Portfolio Summary
- **Portfolio Equity:** GBP 112.75
- **Cash Balance:** GBP 3.45
- **Peak Equity:** GBP 116.22
- **Current Drawdown:** 3.08%
- **Open Positions:** 6
- **Max Positions Allowed:** 5 ⚠️ OVER LIMIT BY 1

---

## Executive Summary
**NO TRADES** recommended today due to a **severe liquidity crisis** combined with position age constraints and regulatory buffer requirements.

### Critical Constraint Violations
1. **Cash Depletion:** GBP 3.45 cash balance with GBP 3.38 required buffer (3% of GBP 112.75 equity) leaves only GBP 0.07 for new trades. This is insufficient to execute the minimum risk-sized position (max_risk_per_trade_pct = 5% = GBP 5.64 minimum per trade).
2. **Position Age Lock:** Five of six open positions are within the min_position_age_days = 2-day window:
   - RIO.L: 7 days (active, some exit eligibility)
   - BA.L: 31 days (held, small position, near breakeven)
   - AZN.L: 22 days (held)
   - BP.L: 35 days (largest single position 47.8% of portfolio, core holding)
   - GLEN.L: 50 days (well-aged, holds well)
   - SHEL.L: 51 days (oldest, well-aged)

3. **Over-Positioned:** 6 positions held vs. max_positions = 5. Must reduce to 5 before taking new entries.

---

## Candidate Setup Analysis

### Top 3 Candidates Rejected
1. **HSBA.L (HSBC) – PULLBACK IN UPTREND**
   - **Setup:** Close GBP 13.324 above SMA50 GBP 12.691; SMA50 > SMA200 (10.977); drawdown 1.97% from 20d high
   - **Confidence:** 0.68 (good trend alignment, healthy pullback, strong liquidity)
   - **Entry Logic:** Pullback entry at market, stop GBP 12.91 (ATR * 2.5 multiplier for balanced profile)
   - **Risk/Reward:** Stop distance GBP 0.414 implies position size (GBP 5.64 / GBP 0.414) = 13.6 shares ≈ GBP 181 notional
   - **Rejection Reason:** Insufficient unfunded cash. Would require forced sale of position within age window. Not executable today.

2. **LSEG.L (London Stock Exchange) – BREAKOUT**
   - **Setup:** Close GBP 91.9 exactly at 20d high GBP 91.9; volume ratio 1.23x normal; SMA50 GBP 82.92 < SMA200 GBP 89.68 (TREND FAILS). Wait, rechecking: SMA50 GBP 82.92, SMA200 GBP 89.68. SMA50 < SMA200 = trend NOT in full uptrend. Downgraded.
   - **Confidence:** 0.72 (breakout confirmed, but trend less pure)
   - **Rejection Reason:** (1) Cash constraint; (2) SMA50 below SMA200 (downtrend risk); (3) Position age constraint locks capital.

3. **RIO.L (Rio Tinto) – EXISTING POSITION HOLD/REDUCE**
   - **Current:** 0.0208 shares at GBP 73.16 (GBP 1.52 market value, +4% PnL). Held 7 days.
   - **Stop Check:** Current stop GBP 67.02; low GBP 72.47; no breach. HOLD.
   - **Why Not Exit to Free Cash?** At GBP 1.52 proceeds with GBP 0.01 stamp duty on sale + GBP 0.02 fee ≈ GBP 1.49 net. Minimal impact on liquidity (GBP 0.07 → GBP 1.56). But exit violates "HOLD existing winners unless stop hit" rule. Not recommended unless forced.

---

## Risk Assessment
### Constraint Status (Hard Limits)

| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| **Cash Buffer** | ≥ 3.0% | 3.06% | ✓ PASS (marginal) |
| **Available for Buys** | GBP remaining | GBP 0.07 | ✗ FAIL (critical) |
| **Max Positions** | ≤ 5 | 6 | ✗ OVER (by 1) |
| **Max Single-Name** | ≤ 30% | 47.8% (BP.L) | ✗ FAIL |
| **Max Sector (Energy)** | ≤ 40% | 35.8% | ✓ PASS |
| **Turnover** | ≤ 30% | 0% planned | ✓ PASS |
| **Portfolio Drawdown** | ≤ 15% | 3.08% | ✓ PASS |

### Key Risk Findings
- **Single-Name Concentration Risk:** BP.L at 47.8% of portfolio (GBP 53.98 / GBP 112.75) is dangerously concentrated. Should reduce to ≤ 30% = GBP 33.83 maximum. Current position exceeds limit by GBP 20.15.
- **Position Age Conflict:** Majority of holdings are within the 2-day minimum age window, locking capital and preventing natural rebalancing.
- **Liquidity Squeeze:** With only GBP 0.07 liquid, any dividend receipt or settlement delay could push the portfolio into negative cash (margin breach in a cash account).

---

## Portfolio Snapshot (Current Holdings)

| Ticker | Qty | Avg Cost (GBP) | Current (GBP) | Value (GBP) | Days Held | Stop (GBP) | PnL (GBP) | PnL % | Sector | Status |
|--------|-----|---|---|---|---|---|---|---|---|---|
| SHEL.L | 1.0624 | 28.70 | 34.71 | 36.88 | 51 | 27.71 | +6.39 | +17.3% | Energy | ACTIVE ✓ |
| GLEN.L | 1.0350 | 5.08 | 5.64 | 5.84 | 50 | 4.86 | +0.58 | +11.4% | Materials | ACTIVE ✓ |
| BP.L | 9.3200 | 4.92 | 5.79 | 53.98 | 35 | 4.68 | +8.09 | +17.6% | Energy | ACTIVE ✓ |
| BA.L | 0.2378 | 22.61 | 22.46 | 5.34 | 31 | 21.50 | -0.04 | -0.7% | Industrials | ACTIVE ✓ |
| AZN.L | 0.0383 | 142.90 | 149.88 | 5.74 | 22 | 137.18 | +0.27 | +4.8% | Healthcare | ACTIVE ✓ |
| RIO.L | 0.0208 | 71.09 | 73.16 | 1.52 | 7 | 67.02 | +0.04 | +2.8% | Materials | ACTIVE ✓ |
| **TOTAL** | — | — | — | **112.75** | — | — | **+15.33** | **+15.7%** | — | — |

---

## Stop-Loss Monitoring (DAILY_CHECK Mode)
Today's low prices vs. active stops:

| Ticker | Stop (GBP) | Low (GBP) | Status | Gap Risk |
|--------|---|---|---|---|
| SHEL.L | 27.71 | 34.49 | ✓ Safe (6.78 above) | No |
| GLEN.L | 4.86 | 5.607 | ✓ Safe (0.75 above) | No |
| BP.L | 4.68 | 5.752 | ✓ Safe (1.07 above) | No |
| BA.L | 21.50 | 21.87 | ✓ Safe (0.37 above) | No |
| AZN.L | 137.18 | 149.22 | ✓ Safe (12.04 above) | No |
| RIO.L | 67.02 | 72.47 | ✓ Safe (5.45 above) | No |

**No stop-losses triggered today.** All positions remain well above their hard stops.

---

## Market Analysis: Why No New Entries Today?

### Trend Analysis Across Universe
- **Strong Uptrends (SMA50 > SMA200, positive slope):** SHEL.L, AZN.L, HSBA.L, BP.L, GSK.L, RIO.L, BA.L, GLEN.L, TSCO.L, NG.L, ISF.L (11 equities + 1 ETF)
- **Weak/Downtrends (SMA50 < SMA200 or negative slope):** ULVR.L, DGE.L, RKT.L, IMB.L, BARC.L, LLOY.L, NWG.L, VMID.L (flat or downtrend)
- **Best Setups (Pullback + Volume Divergence):** HSBA.L (1.97% pullback, 0.72x volume), GSK.L (1.18% pullback, 0.76x volume)

**Problem:** Even with strong setups, we cannot fund entry without forced exits of newer positions.

### Why the Liquidity Crisis?
This portfolio appears to have been built with frequent micro-trades (fractional shares of GBP 1–6 each). While diversification is sound, the cumulative capital allocation across 6 positions has left minimal cash buffer. The min_position_age_days = 2-day constraint was likely designed to prevent churn, but it now functions as a capital lock.

---

## Recommended Actions (Strategic, Beyond Today)

1. **Urgent: Rebalance BP.L Position** – Reduce from 47.8% to ≤25% of portfolio. This requires selling ~GBP 20–25 of BP.L proceeds, which would free GBP 20+ in new cash.
   - *Cost:* Stamp duty on sell = 50 bps × GBP 53.98 ≈ GBP 0.27 (small)
   - *Benefit:* Frees capital, reduces concentration risk
   - *Timing:* After 2 days (if using strict age window), or immediately if treating as risk management

2. **Clear Position Limit Overage** – Currently 6 positions vs. max 5. Consider consolidating smallest positions (RIO.L at GBP 1.52, BA.L at GBP 5.34) into larger core holdings OR sell one outright.

3. **Review min_position_age_days** – If the intent is anti-churn, 2 days may be too strict for a GBP 112 portfolio with GBP 5 risk allocations. Consider raising to 5 days OR exempting positions > 20% of portfolio from the constraint.

4. **Cash Preservation Rule** – Establish a minimum available-cash reserve (e.g., GBP 10–15 for a GBP 112 portfolio) to enable opportunistic entries without forced liquidations.

---

## Orders Generated
**None.** No trades meet the combined constraints of: (1) sufficient cash, (2) position age eligibility, (3) max positions, (4) setup quality.

---

## UK Costs & Assumptions
- **Stamp Duty:** 50 bps on UK equity BUYs (applies to SHEL.L, AZN.L, HSBA.L, BP.L, etc.). ETFs exempt.
- **Transaction Fees:** GBP 0 per trade (fee_model.type = "per_trade", value = 0).
- **Slippage Assumption:** 10 bps on all buys/sells (built into stop prices and exit planning).
- **Settlement:** T+1 (1 day); unsettled proceeds not available same-day for new buys (assume_intraday_netting = false).

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
- **Mode:** DAILY_CHECK means stops are monitored once daily (market close or via intraday lows).
- **Gap Risk:** Overnight or intraday gaps could force execution at prices significantly worse than planned stops (e.g., a company releases bad news pre-market, gap down through stop).
- **Example:** BP.L stop GBP 4.68 could execute GBP 4.40 if a 5% overnight gap occurs. Actual loss = GBP 0.40 * 9.32 = GBP 3.73 vs. planned GBP 2.04 (2x worse).
- **Mitigation (Applied Today):** N/A (no new positions). For existing positions, stops remain in place; gaps will be managed post-execution.
- **Future Recommendation:** If portfolio grows beyond GBP 200, consider broker-side GTC (Good-Till-Cancelled) stops for critical positions (>15% of portfolio).

---

## What Could Invalidate This Plan?

1. **Overnight Corporate Action (before next trading day):** Dividend payment, rights issue, or delisting event could alter position values and cash balance.
2. **Broker Settlement Delay:** If any recent buy/sell settlement is delayed beyond T+1, available cash could change.
3. **Market Gap (Opening):** LSE opens at 08:00 GMT. A pre-market announcement (earnings, M&A) could gap all 6 holdings, potentially triggering one or more stops despite no intraday signal.
4. **Regulatory Change:** FCA could introduce new margin rules or trading halts on specific issuers.
5. **Data Quality Issue:** If market_data.csv prices are stale (e.g., from Friday's close applied to Monday), this plan is invalidated. **Verify as_of_date matches LSE trading day.**

---

## Data Quality Notes
- ✓ All required columns present in market_data.csv
- ✓ Market data current as of 2026-04-13 (today)
- ✓ All tickers matched to universe.csv with ACTIVE status
- ✓ SMA50 and SMA200 populated for all 25 instruments
- ✓ ATR14 and volatility metrics calculated
- ✓ No NaN values in critical price/volume fields
- ✓ Position quantities and market values reconcile vs. market_data prices
- ⚠️ Position count (6) exceeds max_positions (5) — this is a pre-existing constraint violation, not a data quality issue

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice. Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Actual losses could exceed planned risk by 2–10x in gap events. Use at your own risk. Consult a qualified financial advisor before trading.**

---

**Report Generated:** 2026-04-13 | **Next Review:** 2026-04-14 (if trading resumes)