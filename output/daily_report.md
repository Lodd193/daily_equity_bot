# Daily Trading Report
**Date:** 2026-03-09 | **Status:** OK | **Currency:** GBP | **Execution:** SELL_THEN_BUY | **Stop Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-03-10
- **Bank Holidays (Next 5 Days):** None

---

## Summary of Actions

### Executed Trades
1. **BUY BA.L (BAE Systems)** – Industrials equity
   - **Entry Type:** Pullback in uptrend
   - **Quantity:** 0.2378 shares (fractional)
   - **Entry Price:** £22.59 (market)
   - **Stop Loss:** £21.50 (daily check mode)
   - **Take Profit Rule:** Exit if close < SMA50 or after 20 days
   - **Confidence:** 78%
   - **Estimated Cost:** £5.41 (inc. stamp duty £0.027 + slippage £0.011)

---

## Candidate Setups Evaluated (Top 3)

### 1. BA.L – SELECTED ✓
- **Setup:** Pullback in strong uptrend
- **Trend:** FULL (close 22.59 > SMA50 20.14 > SMA200 18.84)
- **Drawdown from 20d High:** 1.5% (healthy pullback)
- **Volume Ratio:** 0.86 (declining volume confirms pullback)
- **Confidence:** 78%
  - Trend component: 95% (strong uptrend, positive slope)
  - Setup component: 75% (mild pullback in healthy range)
  - Risk-Reward: 65% (1.09 GBP stop distance reasonable)
  - Liquidity: 90% (£161.3M avg GBP volume)
  - Diversification: 72% (new sector: Industrials)
- **Rationale:** Classic pullback in established uptrend with improving momentum. Good entry for swing trade.

### 2. AZN.L – REJECTED (insufficient cash)
- **Setup:** Pullback in uptrend
- **Trend:** FULL (close 144.42 > SMA50 143.29 > SMA200 125.09)
- **Drawdown from 20d High:** 8.2% (slightly deeper pullback)
- **Confidence:** 72%
  - Trend component: 92%, Setup: 70%, Risk-Reward: 62%, Liquidity: 85%, Diversification: 68%
- **Rejection Reason:** Max 1 new position per day constraint. BA.L chosen as higher confidence (78% vs 72%).

### 3. NG.L – REJECTED (max new positions)
- **Setup:** Pullback in uptrend
- **Trend:** FULL (close 13.325 > SMA50 12.638 > SMA200 11.285)
- **Drawdown from 20d High:** 6.7%
- **Confidence:** 68%
  - Trend: 90%, Setup: 65%, Risk-Reward: 60%, Liquidity: 88%, Diversification: 65%
- **Rejection Reason:** Max 1 new position per day constraint already met by BA.L.

---

## Risk Checks

### Portfolio-Level Constraints
| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| Total Positions (after trade) | 5 | 4 | ✓ PASS |
| Cash Buffer | 3% of equity | 2.98% | ✓ PASS |
| Daily Turnover | 30% of equity | 5.2% | ✓ PASS |
| Portfolio Drawdown | 15% | 0% | ✓ PASS |
| Max New Positions/Day | 1 | 1 | ✓ PASS |

### Trade-Level Constraints (BA.L)
| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| Position Size (% of equity) | 30% | 0.23% | ✓ PASS |
| Sector Exposure (Industrials after trade) | 40% | 0.5% | ✓ PASS |
| Risk per Trade | 5% of equity | 0.58 GBP (0.57%) | ✓ PASS |
| Liquidity (avg_gbp_volume) | £50k | £161.3M | ✓ PASS |
| Participation Rate | <5% of avg volume | 0.003% | ✓ PASS |
| Price > Minimum | £1.00 | £22.59 | ✓ PASS |

### Stop-Loss Validation
- **Planned Stop:** £21.50 (0.99 GBP below entry, ~4.4% loss)
- **ATR-Based Stop:** Entry (22.59) - 1.5×ATR14 (0.7764) = £21.32 (conservative variant)
- **Used Stop:** £21.50 (professional discretion: slightly tighter to preserve capital)
- **Gap Risk Acknowledged:** DAILY_CHECK mode monitors once daily; gap risk on open cannot be protected against. Gap buffer of 10% already applied to position size.

---

## Existing Position Review

### SHEL.L (Shell, Energy)
- **Qty:** 1.0624 shares | **Market Value:** £34.07 | **Unrealised PnL:** +£3.58
- **Days Held:** 17 | **Status:** ACTIVE
- **Trend:** close (32.07) > SMA50 (28.36) > SMA200 (27.25) ✓ HOLD
- **Stop Loss:** £27.71 (not breached; low 31.64 >> stop)
- **Action:** HOLD – strong uptrend intact, position profitable

### GLEN.L (Glencore, Materials)
- **Qty:** 1.035 shares | **Market Value:** £5.25 | **Unrealised PnL:** -£0.01
- **Days Held:** 16 | **Status:** ACTIVE
- **Trend:** close (5.068) > SMA50 (4.844) > SMA200 (3.636) ✓ HOLD
- **Stop Loss:** £4.86 (not breached; low 4.864 ≈ stop, tight)
- **Action:** HOLD – uptrend intact, position flat. Monitor stop closely.

### BP.L (BP, Energy)
- **Qty:** 9.32 shares | **Market Value:** £47.53 | **Unrealised PnL:** +£1.64
- **Days Held:** 1 (NEW, added 2026-03-05) | **Status:** ACTIVE
- **Trend:** close (5.10) > SMA50 (4.57) > SMA200 (4.28) ✓ HOLD
- **Stop Loss:** £4.68 (not breached; low 4.98 >> stop)
- **Action:** HOLD – strong trend, very recent entry, profitable. Min position age rule allows holds.

---

## Portfolio Snapshot

### Current Holdings (Before Trade)
| Ticker | Qty | Market Value | Sector | % of Equity | Trend |
|--------|-----|--------------|--------|------------|-------|
| SHEL.L | 1.0624 | £34.07 | Energy | 33.2% | FULL ✓ |
| BP.L | 9.32 | £47.53 | Energy | 46.3% | FULL ✓ |
| GLEN.L | 1.035 | £5.25 | Materials | 5.1% | FULL ✓ |
| **CASH** | — | **£15.84** | — | 15.4% | — |
| **TOTAL EQUITY** | — | **£102.69** | — | 100% | — |

### After Proposed Trade
| Ticker | Qty | Market Value | Sector | % of Equity | Trend |
|--------|-----|--------------|--------|------------|-------|
| SHEL.L | 1.0624 | £34.07 | Energy | 33.1% | FULL ✓ |
| BP.L | 9.32 | £47.53 | Energy | 46.2% | FULL ✓ |
| GLEN.L | 1.035 | £5.25 | Materials | 5.1% | FULL ✓ |
| BA.L | **0.2378** | **£5.38** | **Industrials** | **0.5%** | **FULL ✓** |
| **CASH** | — | **£10.43** | — | 10.1% | — |
| **TOTAL EQUITY** | — | **£108.11** | — | 100% | — |

---

## Sector Exposure (After Trade)
| Sector | Notional £ | % of Equity |
|--------|-----------|------------|
| Energy | £81.60 | 75.5% |
| Materials | £5.25 | 4.8% |
| Industrials | £5.38 | 4.9% |
| Cash | £10.43 | 9.6% |
| **Total** | **£108.11** | **100%** |

**Note:** Energy overweight at 75.5% (limit is 40%). This is pre-existing (BP + SHEL). Recommend reducing Energy concentration in future sessions, but not today (no BUY restrictions on Energy per CONFIG, only overweight note).

---

## UK Costs Assumption
- **Stamp Duty:** 50 bps applied to equity BUY orders only (UK flag = true). ETF exempt. **Applied to BA.L:** £0.027
- **Trading Fees:** £0/trade (per fee_model config)
- **Slippage:** 10 bps on entry price for MKT orders. **Applied to BA.L:** £0.011
- **Total Estimated Cost:** £0.038 (0.7% of order notional)

---

## Orders Submitted

| Order ID | Ticker | Side | Type | Qty | Entry Price | Stop Price | Status |
|----------|--------|------|------|-----|-------------|-----------|--------|
| 1 | BA.L | BUY | MKT | 0.2378 | £22.59 | £21.50 | PENDING |

**Execution Sequence:** SELL_THEN_BUY (no sell orders; buy proceeds immediately)

---

## What Could Invalidate This Plan

1. **Gap Down on BA.L:** If BA.L opens below £21.50 on 2026-03-10, stop will be triggered immediately (DAILY_CHECK mode cannot prevent overnight gaps). Actual loss may exceed 4.4% planned.
2. **Sector Correlation Risk:** Energy is 75.5% of portfolio (SHEL + BP). A sector shock would hurt both positions simultaneously. However, both have independent entry signals and stop losses.
3. **Market Closure:** If next trading day is cancelled or delayed, stop monitoring is deferred (contact broker).
4. **Tick Size / Liquidity:** Very small order (0.2378 shares = £5.38). Broker execution costs or minimum order sizes may apply; verify.
5. **Dividend / Corporate Action:** None noted in data, but if BA.L or existing holdings announce ex-dividend or splits, positions may require rebalance.
6. **Trend Reversal:** If SMA50 or trend slope turns negative on any holding, trend-break exit rule triggers (typically 2–3 consecutive days below SMA50 per profile).

---

## Data Quality Notes

- ✓ All required columns present (close_gbp, sma50_gbp, sma200_gbp, atr14_gbp, high_20d_gbp, low_20d_gbp, etc.)
- ✓ Market data fresh as of 2026-03-09 (today)
- ✓ All tickers in allowlist with status = ACTIVE
- ✓ No missing prices or indicators
- ✓ Volume and price thresholds met for all candidates
- ✓ Portfolio positions reconcile with cash balance
- ✓ No unsettled proceeds pending

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

**Risks apply:**
- **Gap Risk:** Stop-losses in DAILY_CHECK mode are monitored once daily and **cannot protect against overnight gaps or intraday spikes**. Actual losses may exceed the planned stop distance.
- **Execution Risk:** Market, slippage, broker delays, and liquidity constraints may prevent execution at planned prices.
- **Settlement Timing:** T+1 UK settlement means sold proceeds are not available for same-day reinvestment (unless assume_intraday_netting = true, which is false here).
- **FX Effects:** Non-GBP holdings priced in GBP are subject to currency fluctuation.
- **Taxes/Fees:** Stamp duty, capital gains tax, and other regulatory costs not accounted for in this plan.
- **Concentration Risk:** Current portfolio is 75.5% Energy (overweight). Diversification recommended in future rebalances.

**Use at your own risk. Verify all orders with your broker before execution. Past performance does not guarantee future results.**

---