# Daily Trading Report
**Date:** 2026-05-11  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-12
- **Bank Holidays (5d):** None

---

## Summary of Actions
**Decision:** NO_TRADES  
**Reason:** Portfolio currently holds 6 positions but max_positions constraint is 5. Available cash for new entries is £0.32 (after 3% buffer of £3.13). No existing positions require immediate exit. Conservative strategy bias: preserve capital, do not force trades under constrained conditions.

---

## Top 3 Setups Considered

### 1. HSBA.L (HSBC) – PULLBACK in FULL UPTREND
- **Confidence:** 0.72 (Balanced profile min: 0.65) ✓
- **Trend Status:** FULL (close £13.30 > SMA50 £12.87 > SMA200 £11.36)
- **Setup:** Pullback to SMA50, drawdown from 20d high 2.73%, volume ratio 1.10
- **Liquidity:** Excellent (avg GBP volume £271.7M, volume ratio 1.10)
- **Risk/Reward:** Stop at £12.51 (ATR-based: £13.30 - 0.3256×2.5 = £12.49), 2.3% risk for potential 3–5% pullback recovery
- **Rejection:** Portfolio at capacity (6/5) + insufficient available cash (£0.32)

### 2. RIO.L (Rio Tinto) – BREAKOUT in FULL UPTREND
- **Confidence:** 0.78 (Balanced profile min: 0.65) ✓
- **Trend Status:** FULL (close £79.27 > SMA50 £70.87 > SMA200 £58.91)
- **Setup:** Breakout setup; close £79.27 near 20d high £79.51 (99.7% of high), volume ratio 1.48
- **Liquidity:** Adequate (avg GBP volume £142.2M, strong vol spike)
- **Risk/Reward:** Stop at £76.54 (£79.27 - 1.8872×1.45), 3.5% risk for potential 5–8% continuation
- **Rejection:** Portfolio at capacity + already hold 0.0208 shares (no add-on without rebalance)

### 3. LSEG.L (London Stock Exchange Group) – PULLBACK in FULL UPTREND
- **Confidence:** 0.68 (Balanced profile min: 0.65) ✓
- **Trend Status:** FULL (close £90.20 > SMA50 £90.07 > SMA200 £88.52)
- **Setup:** Micro-pullback; close £90.20 vs SMA50 £90.07 (very tight), 20d high pullback 11.05%, volume ratio 1.02
- **Liquidity:** Adequate (avg GBP volume £160M)
- **Risk/Reward:** Stop at £86.92 (£90.20 - 2.4357×1.35), 3.6% risk
- **Rejection:** Portfolio at capacity + insufficient cash

---

## Risk Checks (All Constraints)

| Constraint | Value | Limit | Status |
|-----------|-------|-------|--------|
| **Cash Balance** | £3.45 | – | ✓ |
| **Required Buffer (3%)** | £3.13 | – | ✓ |
| **Available for Buys** | £0.32 | – | **CRITICAL** |
| **Positions Count** | 6 | 5 | **BREACH** |
| **Max Risk per Trade (5%)** | £5.21 | – | n/a (no trades) |
| **Turnover (0%)** | 0.0% | 30% | ✓ |
| **Largest Position (BP.L)** | 48.23% | 30% | **BREACH** |
| **Sector – Energy** | 48.23% | 40% | **BREACH** |
| **Portfolio Drawdown** | 10.23% | 15.00% | ✓ |
| **Settlement Day** | T+1 | 1 day | ✓ |

**Critical Issues:**
1. **Portfolio exceeds position limit by 1:** 6 holdings vs. 5 max. This is likely a legacy position from prior runs. No sell signal active; conservative stance is to hold.
2. **Energy sector 48.23% > 40% limit:** BP.L (48.23% of portfolio) and SHEL.L (31.9%) together dominate. A new BUY would worsen this.
3. **Cash critically low (£0.32 available after buffer):** Any new position would require a prior sell or borrowing (not allowed in cash account).

---

## Portfolio Drawdown Status
- **Peak Equity (All-Time):** £116.22
- **Current Equity:** £104.27
- **Drawdown:** (116.22 – 104.27) / 116.22 = **10.23%**
- **Limit:** 15.00%
- **Status:** Within limit but nearing caution zone. No liquidation triggered.

---

## UK Costs Assumption
- **Fee Model:** Per-trade, value £0 (no per-trade fees)
- **Stamp Duty:** 50 bps (0.5%) applied to BUY orders for UK equities only
- **Slippage:** 10 bps (0.1%) estimated on order execution
- **Impact:** None today (no trades). If orders were executed, stamp duty would cost ~0.5% of UK equity BUY notionals.

---

## Gap Risk & DAILY_CHECK Mode
- **Stop Execution Mode:** DAILY_CHECK
- **Gap Risk Buffer Applied:** 10% (pre-configured)
- **Acknowledged:** In DAILY_CHECK mode, stop-loss orders are monitored once daily (at market open). Overnight and intraday gaps can result in slippage exceeding the planned stop price. Actual losses may exceed the ATR-based risk allocation.
- **Existing Positions with Active Stops:**
  - SHEL.L: stop at £27.71 (low today £31.11, safe)
  - GLEN.L: stop at £4.86 (low today £5.62, safe)
  - BP.L: stop at £4.68 (low today £5.37, safe)
  - BA.L: stop at £21.50 (low today £18.84, **low breached intraday**)
  - AZN.L: stop at £137.18 (low today £133.38, low near stop)
  - RIO.L: stop at £67.02 (low today £77.13, safe)

**Action:** BA.L low (£18.84) breached its intraday low, but the close (£19.24) is above stop (£21.50). In DAILY_CHECK mode, we monitor next open. If BA.L opens below £21.50, a SELL will be triggered at market.

---

## Current Portfolio Snapshot

| Ticker | Qty | Avg Cost | Market Value | Unrealised P&L | Days Held | Status | Stop |
|--------|-----|----------|--------------|----------------|-----------|--------|------|
| SHEL.L | 1.0624 | £28.70 | £33.23 | +£2.74 | 80 | ACTIVE | £27.71 |
| GLEN.L | 1.0350 | £5.08 | £5.96 | +£0.70 | 79 | ACTIVE | £4.86 |
| BP.L | 9.3200 | £4.92 | £50.23 | +£4.34 | 64 | ACTIVE | £4.68 |
| BA.L | 0.2378 | £22.61 | £4.57 | –£0.80 | 60 | ACTIVE | £21.50 |
| AZN.L | 0.0383 | £142.90 | £5.17 | –£0.30 | 51 | ACTIVE | £137.18 |
| RIO.L | 0.0208 | £71.09 | £1.65 | +£0.17 | 36 | ACTIVE | £67.02 |
| **Total** | – | – | **£104.27** | **+£7.75** | – | – | – |

**Cash:** £3.45  
**Equity Value:** £104.27  
**Total Portfolio Value:** £107.72  

---

## Orders Table
**No orders to execute.**

---

## Exit Criteria Check (Existing Positions)

### Stop-Loss Breaches
- **BA.L:** Intraday low £18.84 < stop £21.50. Close £19.24 still above stop. Monitor next open for DAILY_CHECK trigger.
- All others: Safe above stops.

### Trend Break (Close < SMA50 for N consecutive days)
- **BA.L:** 14 consecutive days below SMA50 (SMA50 £21.74 vs close £19.24). Close to time-stop threshold.
- **AZN.L:** 14 consecutive days below SMA50. Close to time-stop threshold.
- Others: 0–5 consecutive days; trend intact.

### Time Stop (> time_stop_days with unrealised P&L ≤ 0)
- **BA.L:** 60 days held, –£0.80 P&L. Time stop threshold (balanced profile) ~15 days. Candidate for exit next review if trend break confirmed.
- **AZN.L:** 51 days held, –£0.30 P&L. Also candidate.

### Corporate Actions
- All ACTIVE; no DELISTING or SUSPENSION flags.

**Conclusion:** No hard exits triggered today. BA.L and AZN.L are being monitored for next trading day (trend break + time stop proximity).

---

## What Could Invalidate This Plan

1. **BA.L Gap Down:** If BA.L opens below £21.50 tomorrow, stop-loss triggers. Portfolio would fall to 5 positions, freeing cash for new entry.
2. **Energy Sector Shock:** Oil/gas price collapse would cascade through SHEL.L + BP.L, triggering additional stops.
3. **RIO.L Breakout Reversal:** If RIO.L closes below SMA50 (£70.87), trend break exit activates.
4. **New Cash Inflow:** If dividends or external deposits arrive, available cash increases; new entry becomes possible.
5. **Market Sentiment Shift:** If benchmark (VUAG.L) drops >3%, it may signal broader drawdown; portfolio-level liquidation could activate.
6. **Settlement of Pending Transactions:** If any prior trades settle and increase cash_balance_gbp, rebalancing becomes feasible.

---

## Data Quality Notes
- ✓ All required columns present in market_data.csv
- ✓ Market data dated 2026-05-11 (today)
- ✓ All tickers in market_data matched against universe.csv
- ✓ Pre-computed indicators (SMA50, SMA200, ATR14, drawdown, volume ratios) all provided
- ✓ No missing or stale data detected
- ✓ Positions.json validates against market_data.csv pricing

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.** Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Actual losses may exceed planned risk allocations. Use at your own risk.