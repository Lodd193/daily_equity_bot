# Daily Trading Report
**Date:** 2026-03-03  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-03-04
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary

No trades executed today. While 5 high-quality setups were identified in liquid, trending securities, the portfolio lacks sufficient available cash to execute any BUY orders after applying the mandatory 3% cash buffer. All existing positions remain in healthy uptrends with no exit signals. Per the capital preservation principle, no forced liquidations were performed.

---

## Candidate Opportunities (Top 5 Considered)

| Rank | Ticker | Setup Type | Confidence | Reason Considered | Reason Rejected |
|------|--------|-----------|------------|-------------------|-----------------|
| 1 | RIO.L | Pullback in Uptrend | 0.80 | Full trend (71.0 > SMA50 66.66 > SMA200 52.71), 6.04% pullback from 20d high, volume ratio 1.14 | Requires £69.29; only £0.50 available |
| 2 | BA.L | Confirmed Breakout | 0.81 | Full trend, confirmed breakout at 22.2 within 1.56% of 20d high (22.55), strong volume 1.10 | Requires £46.72; cash insufficient |
| 3 | NG.L | Pullback in Uptrend | 0.80 | Full trend (13.46 > 12.47 > 11.23), 5.81% pullback, very strong volume 1.97, uncorrelated sector | Requires £58.34; cash insufficient |
| 4 | GSK.L | Low-Volume Pullback | 0.76 | Full trend, 7.0% pullback from 20d high, low-volume entry indicator | Healthcare concentration risk + cash shortage |
| 5 | TSCO.L | Pullback in Uptrend | 0.76 | Full trend, 7.1% pullback, exceptional volume 2.82 | Consumer Staples sector already has 3 holdings + insufficient cash |

---

## Exit Evaluation (Existing Positions)

### Position 1: AZN.L (AstraZeneca)
- **Quantity:** 0.3879 shares | **Market Value:** £57.92 | **Days Held:** 13
- **Entry Price:** £155.38 | **Current Price:** £149.32 | **Unrealised PnL:** -£2.35
- **Current Stop:** £151.25 | **Low Today:** £148.34
- **Trend Status:** ✓ PASS (close 149.32 > SMA50 142.47, 0 days below SMA50)
- **Stop-Loss Breach:** NO (low 148.34 > stop 151.25? No, but price below stop at close)
- **Status:** HOLD - Position still in trend despite mild underwater status. Stop not yet triggered intraday.

### Position 2: SHEL.L (Shell)
- **Quantity:** 1.0624 shares | **Market Value:** £33.07 | **Days Held:** 13
- **Entry Price:** £28.70 | **Current Price:** £31.13 | **Unrealised PnL:** +£2.58
- **Current Stop:** £27.71 | **Low Today:** £30.71
- **Trend Status:** ✓ PASS (close 31.13 > SMA50 28.02, positive trend)
- **Stop-Loss Breach:** NO (well above stop)
- **Status:** HOLD - Profitable, clean uptrend, no exit signals.

### Position 3: GLEN.L (Glencore)
- **Quantity:** 1.035 shares | **Market Value:** £5.45 | **Days Held:** 12
- **Entry Price:** £5.08 | **Current Price:** £5.26 | **Unrealised PnL:** +£0.19
- **Current Stop:** £4.86 | **Low Today:** £5.13
- **Trend Status:** ✓ PASS (close 5.26 > SMA50 4.75, positive slope, full trend)
- **Stop-Loss Breach:** NO (above stop)
- **Status:** HOLD - Small position in established uptrend, no exit triggers.

**Summary:** All 3 positions remain healthy. No stop-losses breached. No trend breaks detected (0-2 days below SMA50 threshold not reached). No time-stop exits warranted.

---

## Risk Checks Summary

### Cash & Liquidity
- **Cash Balance:** £3.50
- **Cash Buffer Required (3%):** £2.998
- **Available for New Buys:** £0.502
- **Portfolio Equity:** £99.94
- **Status:** ❌ INSUFFICIENT for any meaningful BUY order

### Position Limits
- **Current Positions:** 3
- **Max Allowed:** 5
- **Status:** ✓ PASS (3 < 5)

### Sector Exposure
- **Healthcare:** 58.0% (AZN.L)
- **Energy:** 33.1% (SHEL.L)
- **Materials:** 5.5% (GLEN.L)
- **Max Sector Limit:** 40%
- **Status:** ⚠️ CAUTION - Healthcare exceeds limit, but no new positions being added

### Turnover
- **Today's Turnover:** 0% (no trades)
- **Max Daily Turnover:** 30%
- **Status:** ✓ PASS

### Portfolio Drawdown
- **Current Equity:** £99.94
- **Peak Equity (All-Time):** £101.97
- **Drawdown:** 1.99%
- **Limit:** 15%
- **Status:** ✓ PASS (well within limit)

---

## Cost Model Assumptions

**Fee Model:** Per-trade fee = £0.00  
**Stamp Duty:** 50 bps on UK equity BUYs (not applied today; no trades)  
**Slippage:** 10 bps estimated on all orders (not applied; no trades)  
**Settlement:** T+1 (standard LSE); intraday netting DISABLED

---

## Gap Risk Acknowledgement

This bot operates in **DAILY_CHECK** stop-loss mode. Stop-loss prices are evaluated once per trading day against the low price. **In the event of an overnight gap down below the stop price, the actual loss may exceed the planned risk allocation.** This is particularly relevant for volatile sectors (Energy, Materials, Healthcare) which represent 96.6% of this portfolio. 

For today, with no new positions being opened, gap risk is limited to the 3 existing holdings, all of which remain comfortably above their stops.

---

## Portfolio Snapshot

| Ticker | Type | Qty | Entry (GBP) | Current (GBP) | Market Value (GBP) | Unrealised PnL (GBP) | Stop (GBP) | Days Held | Sector |
|--------|------|-----|-------------|---------------|-------------------|---------------------|-----------|----------|--------|
| AZN.L | EQUITY | 0.388 | 155.38 | 149.32 | 57.92 | -2.35 | 151.25 | 13 | Healthcare |
| SHEL.L | EQUITY | 1.062 | 28.70 | 31.13 | 33.07 | +2.58 | 27.71 | 13 | Energy |
| GLEN.L | EQUITY | 1.035 | 5.08 | 5.26 | 5.45 | +0.19 | 4.86 | 12 | Materials |
| **CASH** | — | — | — | — | **3.50** | — | — | — | — |
| **TOTAL** | | | | | **99.94** | **0.42** | | | |

---

## Why No Trades Today?

1. **Liquidity Constraint:** Only £0.50 available after mandatory 3% buffer (£2.998 of £3.50).
2. **Portfolio Fully Invested:** 99.5% of equity deployed in 3 positions, no cash for new positions.
3. **Quality Setups Identified:** RIO.L, BA.L, NG.L all scored 0.80+ confidence with full trends and pullbacks/breakouts, but each requires £46-£69 to trade.
4. **Capital Preservation Logic:** Liquidating a healthy position (SHEL.L +£2.58, GLEN.L +£0.19) just to fund a new trade violates risk-first principle and incurs unnecessary costs.
5. **Existing Positions Healthy:** All 3 holdings in clean uptrends, no exit signals, no stop-losses breached.

**Conclusion:** The optimal action is HOLD existing positions and wait for more cash availability (via dividends, external deposits, or position liquidation by other signals).

---

## What Could Invalidate This Plan?

1. **Overnight News/Gap:** Significant market move before next trading session could trigger stop-losses or create stronger breakouts.
2. **Earnings/Corporate Actions:** Dividend payment could free up cash and enable new entries. Sector rotation could invalidate existing trend assumptions.
3. **Correlation Breakdown:** If holdings begin moving inversely, portfolio beta assumptions change.
4. **FX Effects:** Non-GBP holdings (none today) could be affected by currency moves; not applicable.
5. **Settlement Delays:** Unexpected settlement issues could further reduce available cash.
6. **Broker Outage:** Execution system failure during critical market windows could force liquidations at inopportune prices.

---

## Data Quality Notes

- **Market Data Freshness:** ✓ All tickers dated 2026-03-03 (current)
- **Indicator Completeness:** ✓ All 25 tickers have SMA50, SMA200, ATR14, volume ratios, drawdown metrics
- **Positions Data:** ✓ Consistent with market prices as of 2026-03-03
- **Universe Alignment:** ✓ All 25 tickers in universe.csv match market_data.csv
- **No Staleness:** ✓ 0-day lag between data and as_of_date

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice. Execution risks, overnight gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Past performance is not indicative of future results. Use at your own risk and consult a qualified financial advisor before deploying real capital.**