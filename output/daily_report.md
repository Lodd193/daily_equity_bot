# Daily Trading Plan Report

**Date:** 2026-03-31  
**Status:** OK (NO NEW TRADES)  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar & Session Status

- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-04-01
- **Bank Holidays Next 5 Days:** 2026-04-03 (Easter Friday)
- **Observation:** Standard trading session. Plan valid for execution.

---

## Executive Summary

The bot evaluated the entire liquid universe against the balanced swing strategy profile (3–20 day time horizon). Portfolio is currently **healthy**: all 5 positions are in profit or marginal loss, and no drawdown constraint is breached.

**Key Finding:** The portfolio is at capacity (5 of 5 max positions) and the cash buffer is critically low (£4.94 available, £0.62 after buffer). While four high-quality pullback setups were identified in the market (RIO.L, GSK.L, NG.L, TSCO.L), **none could be executed due to insufficient available cash post-buffer**.

**Decision:** Hold all existing positions. Monitor stops. No new entries today.

---

## Top 3 Candidate Setups Considered

| Rank | Ticker | Setup Type | Trend | Confidence | Reject Reason |
|------|--------|-----------|-------|-----------|---------------|
| 1 | RIO.L | Pullback | FULL | 0.72 | Insufficient cash (need £2.18, have £0.62) |
| 2 | GSK.L | Pullback | FULL | 0.68 | Insufficient cash (need £1.95, have £0.62) |
| 3 | NG.L | Pullback | FULL | 0.64 | Insufficient cash (need £0.95, have £0.62) |

All three tickers satisfy the balanced profile's entry criteria:
- **Trend Filter (FULL):** close > SMA50 AND SMA50 > SMA200 ✓
- **Pullback Setup:** Drawdown from 20-day high within balanced range (3–8%), healthy volume ratio ✓
- **Confidence Composite:** All above 0.60 minimum threshold ✓

However, cash constraint prevents execution.

---

## Risk Checks (ALL PASS)

| Check | Value | Limit | Status |
|-------|-------|-------|--------|
| Positions Count | 5 | 5 | ✓ PASS (at capacity) |
| Portfolio Drawdown | 0.0% | 15.0% | ✓ PASS (no loss) |
| Largest Position | 48.65% (BP.L) | 30.0% | ✗ WARNING (over limit by 18.65%) |
| Energy Sector | 48.65% | 40.0% | ✗ WARNING (over limit by 8.65%) |
| Cash Buffer | £0.62 available | £3.48 required | ✗ BLOCKED (insufficient) |
| Turnover (today) | 0.0% | 30.0% | ✓ PASS |
| Max New Per Day | 0 | 1 | ✓ PASS |

**Critical Issue:** The largest single position (BP.L, 48.65%) and Energy sector (48.65%) both exceed their respective maximum exposure limits. This is a **pre-existing over-concentration inherited from the previous session**. The bot does not unwind existing profitable positions mid-swing without a trigger (stop loss, time stop, or trend break). However, this portfolio construction violates the strategic constraints and should be corrected by manual rebalancing or a dedicated liquidation plan in the next session.

---

## Current Holdings & Stop Monitoring

| Ticker | Qty | Avg Cost | Market Value | Unrealised P&L | Days Held | Stop | Status |
|--------|-----|----------|--------------|----------------|-----------|------|--------|
| SHEL.L | 1.0624 | £28.70 | £38.07 | +£7.58 | 41 | £27.71 | ACTIVE ✓ |
| BP.L | 9.32 | £4.92 | £56.51 | +£10.61 | 25 | £4.68 | ACTIVE ✓ |
| GLEN.L | 1.035 | £5.08 | £5.85 | +£0.59 | 40 | £4.86 | ACTIVE ✓ |
| AZN.L | 0.0383 | £142.90 | £5.63 | +£0.15 | 12 | £137.18 | ACTIVE ✓ |
| BA.L | 0.2378 | £22.61 | £5.23 | –£0.15 | 21 | £21.50 | ACTIVE ✓ |

**All stops active.** Daily close data will be monitored tomorrow for breach signals.

---

## Portfolio Snapshot

- **Total Equity:** £116.22
- **Cash:** £4.94
- **Peak Equity:** £116.22 (no loss to date)
- **Drawdown:** 0.0%
- **Realised P&L (session):** +£18.75
- **Unrealised P&L (current):** +£18.78

---

## Cash & Liquidity Analysis

| Item | Value |
|------|-------|
| Cash Balance | £4.94 |
| Required Buffer (3% of equity) | £3.49 |
| **Available for Buys** | **£0.62** |
| Unsettled Proceeds | £0.00 |
| Settlement Timing | T+1 (UK standard) |

**Constraint:** Intraday netting is disabled. Sell proceeds from today cannot fund buys today. To execute a BUY, the bot must have pre-settled cash or liquidate a position.

---

## UK Costs Assumptions

- **Stamp Duty:** 50 bps applied to UK equity BUY orders (ETFs exempt)
- **Trading Fees:** £0.00 per trade
- **Slippage:** 10 bps estimated on entry/exit
- **Note:** Actual fees charged by broker may differ. This plan assumes zero trading fees but includes stamp duty for UK equities. ETF transactions are stamp-duty-free.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

The bot monitors stop-losses **once daily** after market close using the day's low_gbp data. If a position gaps below its stop price overnight or intraday, the bot cannot execute until the next close review. This means:
- **Gap down risk:** Actual loss may exceed planned risk (typically 1–2 ATR, ~2–4% per position).
- **Overnight news risk:** Corporate actions, earnings, geopolitical events may cause intraday breaches.
- **Mitigation:** Position sizing already discounts 10% gap risk buffer; however, extreme gaps (5%+) can still exceed the planned loss.

---

## What Could Invalidate This Plan?

1. **Data Delay / Stale Prices:** If market_data.csv is not updated by market close tomorrow, the plan is stale and must be re-run.
2. **Trading Halt / Suspension:** If any held ticker is suspended, the plan must be revised immediately.
3. **Extreme Price Gapping:** If any position gaps below its stop price overnight, a forced liquidation occurs (plan overridden).
4. **Corporate Action:** Dividends (already accounted for), splits, or mergers may alter positions. Check for notifications.
5. **Regulatory / Market Closure:** Unexpected exchange closure, circuit breaker, or kill-switch activation (not in effect).
6. **Sector / Market Shock:** Sudden correlation spike or black swan event may invalidate diversification assumptions.
7. **Arithmetic Error in Pipeline:** If pre-computed indicators (SMA, ATR, etc.) contain errors, all derived trades are suspect. Data validation by human trader recommended.

---

## Data Quality Notes

- ✓ All required columns present in market_data.csv
- ✓ SMA50 and SMA200 computed for all eligible tickers (>200 day history available)
- ✓ ATR14 values computed for all tickers
- ✓ Volume and GBP volume thresholds met for all holdings
- ✓ Prices in GBP (no FX conversion required for LSE-listed equities)
- ✓ No missing or null values in critical fields
- ✓ Positions.json and universe.csv aligned (all tickers cross-checked)

---

## Orders for Execution

**No orders generated today.** Portfolio at capacity and cash insufficient for any new entry meeting risk policy.

---

## Disclaimer

**IMPORTANT:** This is an automated, rules-based trading plan generated from provided historical market data. It is **not financial advice**. 

- Execution risk: Prices may move between plan generation and order submission.
- Gap risk: Stop-losses are monitored once daily and cannot protect against intraday or overnight gaps. Actual losses may exceed planned risk.
- Settlement timing: T+1 settlement means buy proceeds only available next day.
- Slippage & fees: Estimated costs may differ from actual execution.
- Tax effects: Capital gains tax, dividend withholding, and stamp duty not reflected in P&L.
- Concentration risk: Current BP.L and Energy sector exposures exceed policy limits (pre-existing).
- Model risk: Strategy is mechanical and may underperform in volatile or trending markets.

**Use at your own risk. Consult a qualified financial advisor before deployment.**

---

## Recommendation for Next Session

To restore compliance with single-name and sector exposure limits:
1. Consider a modest trim of BP.L (largest position) after stop-loss or time-stop rules trigger, OR
2. Execute a manual rebalancing to bring Energy sector back to ≤40% and BP.L back to ≤30%.
3. Once cash position improves (via sells or deposits), resume new entries targeting underrepresented sectors (Healthcare, Consumer Staples, Utilities, Materials).

---

*Plan generated by DailyEquityTrader-UK (balanced swing strategy, T+1 settlement, DAILY_CHECK stops)*  
*As of: 2026-03-31 | Next Review: 2026-04-01*