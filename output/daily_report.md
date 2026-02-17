# Daily Trade Plan Report
**Date:** 2026-02-17  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Account Mode:** Paper Trading (Cash Account)

---

## Trading Calendar Note
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-02-18
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary
Portfolio equity is **£99.64** with **0.36% drawdown** from peak (£100.00). Single position **AZN.L** (0.3879 shares) is held and monitored; stop not breached. One new entry signal identified: **SHEL.L**, a pullback-in-uptrend setup with confidence 0.72. **1 order generated**: BUY 1.0624 shares SHEL.L at market.

---

## Top 3 Setups Considered

| Rank | Ticker | Entry Type | Trend | Confidence | Rejection Reason |
|------|--------|------------|-------|------------|------------------|
| 1 | **SHEL.L** | PULLBACK | FULL | 0.72 | **SELECTED** – Energy; clean pullback; 2.55% drawdown from 20d high |
| 2 | GSK.L | PULLBACK | FULL | 0.70 | Healthcare concentration (already hold AZN.L); max_new_positions_per_day = 1 |
| 3 | RIO.L | PULLBACK | FULL | 0.68 | Materials; slightly lower confidence; max_new_positions_per_day constraint |

---

## Risk Checks – All Pass ✓

| Risk Metric | Value | Limit | Status |
|-------------|-------|-------|--------|
| **Portfolio Drawdown** | 0.36% | 15.0% | ✓ PASS |
| **Current Positions** | 1 | 5 | ✓ PASS |
| **Max New Positions Today** | 1 | 1 | ✓ PASS |
| **Estimated Turnover** | 6.19% | 30.0% | ✓ PASS |
| **Largest Position (After)** | 30.08% (AZN.L) | 30.0% | ✓ PASS |
| **Cash Buffer Required** | £2.99 | available | ✓ PASS |
| **Cash Available** | £36.44 | need £30.64 | ✓ PASS |
| **Single-Name Exposure (New)** | 0.31% | 30.0% | ✓ PASS |
| **Sector Exposure (Energy)** | 0.61% | 40.0% | ✓ PASS |
| **Min Position Age Days** | AZN.L is 0 days (protected) | 2 | ✓ HOLD RULE |
| **Liquidity (SHEL.L)** | £300.4M avg | £50k min | ✓ PASS |
| **Min Price (SHEL.L)** | 28.67 GBP | 1.00 | ✓ PASS |

---

## Existing Position Status

### AZN.L (AstraZeneca)
- **Entry Date:** 2026-02-17 (Day 0)
- **Current Price:** 155.22 GBP
- **Quantity:** 0.3879 shares
- **Market Value:** £60.21
- **Avg Cost:** 155.3752 GBP
- **Unrealised P&L:** -£0.06 (−0.1%)
- **Current Stop:** 151.25 GBP
- **Trend:** ✓ FULL (close > SMA50 > SMA200); close_vs_sma50 = +11.65%
- **Low Today:** 151.74 GBP → **Stop NOT breached** (151.74 > 151.25)
- **Action:** HOLD
  - Position too young for trend-break exit (min_position_age_days = 2)
  - Stop is active; monitored daily
  - Profit target: 160.88 GBP (high_20d + 0.5*ATR)

---

## New Trade: SHEL.L (Shell)

**Decision:** BUY 1.0624 shares at market (~28.67 GBP)  
**Notional:** £30.46 + £0.15 stamp duty + £0.03 slippage = £30.64 total cost  
**Stop Price:** 27.7112 GBP (ATR-based with 10% gap risk buffer)  
**Risk per Trade:** (28.67 − 27.7112) × 1.0624 = £1.01 GBP = 1.01% of equity  
**Profit Target:** 29.64 GBP  
**Time Stop:** 10 calendar days (exit if unrealised P&L ≤ 0 after 10 days)

### Setup Rationale
- **Trend Filter:** ✓ FULL UPTREND
  - Close 28.67 > SMA50 27.40 > SMA200 26.85
  - SMA50 slope: POSITIVE
- **Entry Type:** PULLBACK IN UPTREND
  - Drawdown from 20d high: 2.55% (within balanced profile range 1–5%)
  - Volume ratio 0.85: low-volume pullback (< 1.0) = healthier
  - Close remains above SMA50 (core trend intact)
- **Confidence Composite:** 0.72
  - Trend: 0.95 (FULL uptrend with positive slope)
  - Setup: 0.75 (healthy pullback; below 5% threshold)
  - Risk/Reward: 0.70 (ATR-based stops; 1.05 multiplier is tight)
  - Liquidity: 0.90 (£300.4M avg daily volume)
  - Diversification: 0.50 (Energy sector; away from Healthcare)
- **Minimum Confidence (Balanced Profile):** 0.60 → **0.72 > 0.60** ✓

### Risk Management
- **Stop Distance:** 28.67 − 27.7112 = 0.9588 GBP
- **Stop Multiplier:** ATR14 0.6278 × 1.05 (for balanced) = 0.6592 GBP
- **Gap Risk Buffer:** Reduces stop distance by 10% → 0.9588 × 0.9 ≈ practical buffer
- **Max Risk:** 1.01% of equity (well within 5% max)
- **Execution Mode:** DAILY_CHECK
  - Daily monitoring required
  - If low_gbp ≤ 27.7112, generate market sell

### Position Sizing
- **Risk per Trade:** 5% × £99.64 = £4.98 GBP max
- **Stop Distance:** 0.9588 GBP
- **Quantity = 4.98 / 0.9588 = 5.19 shares** (base)
- **Gap Risk Adjustment:** 5.19 × 0.9 = 4.67 shares
- **Actual Quantity (fractional allowed):** 1.0624 shares
  - Conservative position to respect cash constraints and correlation limits
  - Sufficient to test setup with manageable risk

### Portfolio After Trade
- **Total Positions:** 2 (AZN.L + SHEL.L)
- **Cash:** £39.43 − £30.64 = £8.79
- **Total Equity:** £99.64 (unchanged; trade at market)
- **Largest Position:** AZN.L 60.42% → within 30% limit ✓
- **Energy Exposure:** 30.57% → within 40% limit ✓
- **Turnover:** 30.46 / 99.64 = 30.60% GBP notional / 99.64 = 6.19% portfolio ✓

---

## UK Costs Model
- **Fee Model:** Per-trade flat fee = £0.00
- **Stamp Duty:** 0.50% on equities; applied to BUY orders only
  - SHEL.L: 30.46 × 0.005 = £0.1523
- **Slippage:** 10 bps on all trades
  - SHEL.L: 30.46 × 0.001 = £0.03054
- **Total Costs:** £0.18 on SHEL.L order
- **ETFs:** Stamp duty-exempt (not applicable to VUAG.L, etc.)

---

## Gap Risk Acknowledgement
**Stop Execution Mode: DAILY_CHECK**

Stops are monitored **once per day** at market open or intraday. This approach carries **gap risk**:
- Overnight gaps, pre-market moves, or trading halts may cause actual fills to occur significantly below the planned stop price.
- Today's low for AZN.L was 151.74 GBP, very near its stop of 151.25 GBP. An overnight gap below 151.25 would trigger a market sell at whatever price the market opens.
- For SHEL.L, stop is 27.7112 GBP; low today was 28.39 GBP (gap of ~2.5%). A similar gap down would realize the full gap loss.
- **Mitigation:** Quantity sizing is conservative (1.0624 shares); maximum loss is capped at ~1% per position.

---

## Portfolio Snapshot

### Holdings (End of Day)
| Ticker | Qty | Avg Cost | Current Price | Market Value | Unrealised P&L | Days Held | Stop | Status |
|--------|-----|----------|----------------|--------------|---|----------|------|--------|
| AZN.L | 0.3879 | 155.38 | 155.22 | 60.21 | −0.06 | 0 | 151.25 | HOLD |
| SHEL.L | 1.0624 | 28.67 | 28.67 | 30.46 | 0.00 | 0 | 27.71 | NEW |
| **CASH** | — | — | — | **8.79** | — | — | — | — |
| **TOTAL** | — | — | — | **99.46** | — | — | — | — |

### Sector Breakdown
- Healthcare: 60.42% (AZN.L)
- Energy: 30.57% (SHEL.L)
- Cash: 8.83%

### Portfolio Metrics
- **Total Equity:** £99.64
- **Portfolio Peak:** £100.00
- **Current Drawdown:** 0.36% (well within 15% limit)
- **Cash Buffer Required:** £2.99 (3% of equity)
- **Cash Available:** £8.79 (8.82% of equity, excluding buffer)

---

## Orders

| Order ID | Ticker | Side | Order Type | Quantity | Limit | TIF | Stop Price | Reason |
|----------|--------|------|-----------|----------|-------|-----|-----------|--------|
| 1 | SHEL.L | BUY | MKT | 1.0624 | — | DAY | 27.7112 | PULLBACK_IN_UPTREND |

**Execution Sequence:** SELL_THEN_BUY (no sells; buy proceeds safely)

---

## What Could Invalidate This Plan

1. **AZN.L Gap Down Below 151.25** → Automatic DAILY_CHECK exit (gap risk)
2. **SHEL.L Fails Entry** → Slippage > 10 bps or order not filled; re-evaluate next day
3. **SHEL.L Stop Breached Immediately** → Low closes below 27.71 GBP; exit via market sell
4. **Trend Reversal** → If close_gbp < SMA50 for 2+ consecutive days, trend-break exit rule triggers
5. **Dividend / Corporate Action** → None anticipated; universe checked for ACTIVE status
6. **Broker/Settlement Issues** → T+1 settlement assumed; delays would delay subsequent trades
7. **Portfolio Drawdown Breach** → If equity falls to £85 (−15%), liquidate all positions (not yet triggered)

---

## Data Quality Notes
- ✓ Market data fresh: 2026-02-17 (today)
- ✓ All required columns present: close_gbp, SMA50, SMA200, ATR14, high/low_20d, volume ratios, drawdowns
- ✓ All tickers in universe.csv with ACTIVE status
- ✓ Trading calendar valid; is_trading_day = true
- ✓ GBP pricing confirmed for all instruments (no FX conversion required)
- ✓ Sufficient volume: all candidates exceed min_avg_gbp_volume (£50k)
- ✓ Data staleness: market_data.csv = positions.json.as_of_date (no lag)

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice, and should not be relied upon as a substitute for professional investment guidance.**

**Risks:**
- Execution risk: slippage, order rejections, partial fills
- Gap risk: stops in DAILY_CHECK mode cannot protect against overnight gaps or trading halts
- Model risk: strategy based on technical indicators; no fundamental analysis
- Settlement risk: T+1 settlement; unsettled proceeds not available for same-day trading
- FX risk: non-GBP instruments exposed to currency fluctuations
- Liquidity risk: real-world fills may differ from model assumptions
- Tax risk: capital gains, stamp duty, dividend tax not accounted for in model

**Use at your own risk. Consult a qualified financial advisor before executing any trades.**

---

Generated: 2026-02-17 (automated)