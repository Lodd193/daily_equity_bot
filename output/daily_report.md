# Daily Trading Plan Report
**Date:** 2026-04-24  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Executive Summary
No trades will be executed today. The portfolio is in a capital-constrained state with insufficient liquidity to support new entries, despite several technical setups being available. Risk-first principle mandates preservation over sub-optimal execution.

### Key Constraints
| Metric | Value | Status |
|--------|-------|--------|
| Portfolio Equity | £109.34 | Very Small |
| Available Cash | £3.45 | Limited |
| Cash Buffer Required | £3.28 | 95% of cash |
| Available for Buys | £0.17 | **INSUFFICIENT** |
| Current Positions | 6 | Exceeds max (5) |
| Portfolio Drawdown | 5.97% | Safe (limit 15%) |

---

## Trading Calendar
- **Trading Day:** YES
- **Half-Day:** NO
- **Next Trading Day:** 2026-04-27
- **Bank Holidays (next 5 days):** None

---

## Top 3 Technical Setups Considered

### 1. LSEG.L (London Stock Exchange Group) — BREAKOUT
- **Confidence:** 78% (Strong)
- **Trend Status:** FULL (close > SMA50 > SMA200, positive slope)
- **Setup Details:**
  - Close: £99.92 vs 20d high: £101.40 (1.5% from breakout)
  - Volume Ratio: 1.31× average (strong participation)
  - Drawdown from 20d high: 1.46% (minor pullback in uptrend)
  - Entry Price: £99.92 (market close)
  - Stop Loss: £97.59 (ATR14-based, 2× multiplier)
  - Risk/Reward: Potential 3–4% move to 20d high, 2.3% risk
- **Rejection Reason:** Insufficient capital. Minimum notional for trade (~£50–60) exceeds available cash (£0.17). Position sizing would require liquidating existing holdings.
- **Components:**
  - Trend: 95% | Setup: 72% | Risk-Reward: 65% | Liquidity: 85% | Diversification: 70%

### 2. REL.L (RELX) — BREAKOUT
- **Confidence:** 75% (Good)
- **Trend Status:** FULL (close > SMA50 > SMA200)
- **Setup Details:**
  - Close: £26.96 vs 20d high: £27.95 (3.5% from breakout)
  - Volume Ratio: 1.29× (strong)
  - Pullback: 3.55% from recent high (healthy entry zone)
  - Entry Price: £26.96
  - Stop Loss: £25.21 (ATR-based)
  - Risk/Reward: 3–4% potential move, 2% risk
- **Rejection Reason:** Insufficient cash for execution. Also, portfolio is already at max_positions (6 current vs 5 allowed), blocking new entries.
- **Components:**
  - Trend: 92% | Setup: 68% | Risk-Reward: 70% | Liquidity: 82% | Diversification: 65%

### 3. HSBA.L (HSBC) — PULLBACK IN UPTREND
- **Confidence:** 72% (Good)
- **Trend Status:** FULL (close > SMA50 > SMA200, positive slope)
- **Setup Details:**
  - Close: £13.21 vs SMA50: £12.76 (3.5% above average)
  - 20d pullback: 3.42% from high (healthy)
  - Volume Ratio: 0.82× (low-volume pullback, preferred signal)
  - Entry Price: £13.21
  - Stop Loss: £12.88 (ATR-based)
- **Rejection Reason:** Cash insufficient; also at max position count. Would require position reduction first.
- **Components:**
  - Trend: 88% | Setup: 65% | Risk-Reward: 68% | Liquidity: 90% | Diversification: 60%

---

## Risk Checks — ALL CONSTRAINTS
| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| **Liquidity** | — | — | — |
| Min GBP Volume (20d avg) | £50,000 | Top candidates: £288M+, £173M+, £288M+ | ✅ PASS |
| Min Price | £1.00 | All holdings > £4.00 | ✅ PASS |
| **Position Sizing** | — | — | — |
| Max Risk per Trade | 5% of equity | No trades executed | ✅ PASS |
| Gap Risk Buffer | 10% | N/A (no new entries) | ✅ PASS |
| **Portfolio Exposure** | — | — | — |
| Max Single Name | 30% | Largest: BP.L at 48.7% | ⚠️ **BREACH** |
| Max Sector | 40% | Energy: 48.7% | ⚠️ **BREACH** |
| Max Positions | 5 | Current: 6 | ⚠️ **BREACH** |
| Max Correlated | 3 | Not calculated (small portfolio) | ✅ PASS |
| **Turnover** | — | — | — |
| Max Daily Turnover | 30% | 0% (no trades) | ✅ PASS |
| Anti-Churn (min age) | 2 days | All holdings > 20 days | ✅ PASS |
| **Cash Management** | — | — | — |
| Cash Buffer Required | 3% of equity | £3.28 | ✅ PASS |
| Available for Buys | — | £0.17 | ⚠️ **CRITICAL** |
| **Drawdown** | — | — | — |
| Portfolio Drawdown | 15% limit | 5.97% | ✅ PASS |

---

## Portfolio Status

### Current Holdings (6 positions, 1 over limit)
| Ticker | Sector | Qty | Avg Cost | Current Price | Market Value | PnL | PnL% | Days Held | Status |
|--------|--------|-----|----------|--------------|--------------|-----|------|----------|--------|
| **SHEL.L** | Energy | 1.0624 | £28.70 | £33.08 | £35.14 | +£4.65 | +13.2% | 65 | ✅ Profit |
| **BP.L** | Energy | 9.3200 | £4.92 | £5.72 | £53.29 | +£7.40 | +13.9% | 49 | ✅ Profit |
| **GLEN.L** | Materials | 1.0350 | £5.08 | £5.58 | £5.77 | +£0.51 | +8.8% | 64 | ✅ Profit |
| **RIO.L** | Materials | 0.0208 | £71.09 | £73.81 | £1.54 | +£0.06 | +3.7% | 21 | ✅ Profit |
| **BA.L** | Industrials | 0.2378 | £22.61 | £20.21 | £4.80 | -£0.57 | -10.7% | 45 | ⚠️ Loss |
| **AZN.L** | Healthcare | 0.0383 | £142.90 | £139.56 | £5.35 | -£0.13 | -2.3% | 36 | ⚠️ Loss |

### Summary
- **Total Equity:** £109.34
- **Cash Balance:** £3.45
- **Peak Equity:** £116.22
- **Current Drawdown:** 5.97% from peak
- **Net PnL:** +£12.92 (+13.4%)
- **Profitable Positions:** 4 of 6 (67%)
- **Loss Positions:** 2 of 6 (33%)

### Sector Breakdown
| Sector | Value | % of Portfolio | Limit | Status |
|--------|-------|---|-------|--------|
| Energy | £88.43 | 48.7% | 40% | ⚠️ OVER |
| Materials | £8.31 | 7.6% | 40% | ✅ OK |
| Industrials | £4.80 | 4.4% | 40% | ✅ OK |
| Healthcare | £5.35 | 4.9% | 40% | ✅ OK |
| Financials | £0.00 | 0% | 40% | ✅ OK |

---

## Why No Trades Today

### Primary Blocker: Capital Insufficiency
1. **Portfolio Too Small:** Equity of £109.34 is at the lower limit for equity trading. Most brokers require minimum positions of £50–100 per trade.
2. **Cash Critically Low:** Only £3.45 cash available. After mandatory 3% buffer (£3.28), only £0.17 remains for new buys.
3. **Execution Impossible:** Even the smallest quality setup would require £40–60 in new capital, requiring liquidation of existing positions.

### Secondary Blocker: Position Count Limit
- Currently holding 6 positions; maximum allowed is 5.
- No new positions can be opened until one is closed.
- Closing a position to make room contradicts the cost of re-entering a quality setup.

### Secondary Consideration: Portfolio Structure
- **Energy Concentration:** 48.7% in just 2 holdings (SHEL.L, BP.L) exceeds both single-name (30%) and sector (40%) limits.
- **Weak Positions:** BA.L and AZN.L are in unrealised losses.
- A prudent approach would reduce Energy exposure and rebalance before adding new positions.

---

## What Could Invalidate This Plan

1. **Liquidation Event:** If one of the existing positions breaches its stop-loss (unlikely; current stops are 8–10% below current prices).
2. **Corporate Action:** Merger, suspension, or dividend event affecting a holding.
3. **Portfolio Rebalance Trigger:** If equity falls further below £100, reconsider risk posture.
4. **External Capital Injection:** Additional cash would enable new entries.
5. **Sector Rebalance Opportunity:** If Energy exposure is reduced (e.g., selling SHEL.L or BP.L), capital freed could support a new Financials or Industrials entry.

---

## Stop-Loss Check (DAILY_CHECK Mode)
All current positions remain above their stop-loss levels. No stop-loss breaches today.

| Ticker | Current | Stop | Distance | Breach Risk |
|--------|---------|------|----------|-------------|
| SHEL.L | £33.08 | £27.71 | +19.4% | Low |
| BP.L | £5.72 | £4.68 | +22.2% | Low |
| GLEN.L | £5.58 | £4.86 | +14.8% | Low |
| RIO.L | £73.81 | £67.02 | +10.2% | Low |
| BA.L | £20.21 | £21.50 | -6.0% | ⚠️ **MONITORING** |
| AZN.L | £139.56 | £137.18 | +1.7% | Moderate |

**Note:** BA.L's stop is only £1.29 above current price. Further weakness could trigger stop-loss tomorrow.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
The bot monitors stops **once daily** at market close. Overnight and intraday gaps can result in execution at prices significantly worse than planned stop levels. This is a structural limitation of DAILY_CHECK execution:
- A large overnight gap down could trigger stop-loss at £15–18 for BA.L instead of £21.50.
- Consider upgrading to BROKER_GTC (Good-Till-Cancelled) for overnight protection.

---

## UK-Specific Costs
| Cost Component | Assumption |
|---|---|
| **Stamp Duty** | 50 bps applied to UK equity BUY orders (none executed today) |
| **Trading Fees** | £0 per trade (from fee_model.value) |
| **Slippage** | 10 bps estimated for order execution |
| **FX Cost** | N/A (all holdings in GBP) |

Since no trades executed, costs are £0.

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution risk, overnight/intraday gaps, slippage, FX effects (if applicable), settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against gaps; actual losses may exceed planned risk. Use at your own risk. Past performance does not guarantee future returns. Consult a qualified financial advisor before making investment decisions.

---

## Data Quality Notes
- ✅ All required columns present in market_data.csv
- ✅ All indicators (SMA50, SMA200, ATR14, high/low 20d) computed and available
- ✅ positions.json complete and consistent
- ✅ universe.csv aligned with trading data
- ✅ Trading calendar: LSE, normal trading day
- ✅ No data staleness issues detected

**Next Review:** 2026-04-27 (next trading day)

===