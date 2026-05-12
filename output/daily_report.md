# Daily Trading Plan — 2026-05-12

**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Day:** Yes (LSE open)  
**Half Day:** No  

---

## Market Summary

- **Date:** 2026-05-12
- **Portfolio Equity:** £105.37
- **Cash Balance:** £3.45
- **Drawdown from Peak:** 9.40% (peak: £116.22, limit: 15.0%)
- **Active Positions:** 6 (limit: 5)

---

## Why No New Trades Today

The portfolio is **constrained by hard limits** that prevent new entries:

### 1. **Position Count Exceeded**
- **Current:** 6 active positions
- **Maximum:** 5
- **Status:** LOCKED — no new buys until position count ≤ 4

### 2. **Single-Name Exposure Limit Breached**
- **BP.L exposure:** 48.33% of portfolio
- **Maximum allowed:** 30.0%
- **Breach amount:** +18.33 percentage points

### 3. **Sector Exposure Limit Breached**
- **Energy sector (BP.L + SHEL.L):** 79.64% of portfolio
- **Maximum allowed:** 40.0%
- **Breach amount:** +39.64 percentage points

### Risk Implication
The portfolio is heavily concentrated in Energy sector equities. While the drawdown (9.40%) is within acceptable limits, the **structural concentration risk exceeds policy thresholds**. Any adverse news in energy markets could trigger cascading losses.

**Action Required:** Reduce Energy exposure to below 40% before considering new positions.

---

## Existing Positions & Stop-Loss Monitoring

| Ticker | Qty | Avg Cost | Market Price | Market Value | PnL | Stop Price | Days Held | Status |
|--------|-----|----------|--------------|--------------|-----|------------|-----------|--------|
| SHEL.L | 1.0624 | £28.70 | £31.58 | £33.55 | +£3.06 | £27.71 | 83 | ACTIVE |
| GLEN.L | 1.0350 | £5.08 | £5.73 | £5.93 | +£0.67 | £4.86 | 82 | ACTIVE |
| BP.L | 9.3200 | £4.92 | £5.47 | £50.94 | +£5.05 | £4.68 | 67 | ACTIVE |
| BA.L | 0.2378 | £22.61 | £19.26 | £4.58 | −£0.80 | £21.50 | 63 | ACTIVE |
| AZN.L | 0.0383 | £142.90 | £137.48 | £5.27 | −£0.21 | £137.18 | 54 | ACTIVE |
| RIO.L | 0.0208 | £71.09 | £79.20 | £1.65 | +£0.17 | £67.02 | 39 | ACTIVE |

**All positions** have active stop-loss orders set. In DAILY_CHECK mode, stops are evaluated daily against `low_gbp`. If breached, a SELL at market will be triggered.

---

## Top Candidate Setups Evaluated (All Rejected)

### Candidate 1: RIO.L (Rio Tinto)
- **Entry Type:** Pullback in uptrend
- **Confidence:** 0.72 (Above 0.60 threshold for balanced profile)
- **Trend:** FULL (close > SMA50 > SMA200, SMA50 slope positive)
- **Setup:**
  - Drawdown from 20d high: 1.07% (mild pullback, healthy)
  - Volume ratio: 1.96× (elevated, indicates conviction)
  - Close vs SMA50: +11.5% (strong uptrend position)
- **Risk/Reward:** ATR = £1.86, stop ~£67.02, risk per share ~£11.48
- **Liquidity:** avg GBP volume £152.5M, volume participation <1% ✓
- **Rejection Reason:** **Portfolio constraint: exceeds max_positions limit.** High-quality setup, but cannot execute.

### Candidate 2: LSEG.L (London Stock Exchange Group)
- **Entry Type:** Pullback in uptrend
- **Confidence:** 0.65 (borderline balanced threshold)
- **Trend:** FULL (close > SMA50 > SMA200, SMA50 slope positive)
- **Setup:**
  - Drawdown from 20d high: 7.81% (moderate pullback, within balanced range)
  - Volume ratio: 0.89× (below-average volume, slightly concerning)
  - Close vs SMA50: +3.59% (moderate uptrend)
- **Risk/Reward:** ATR = £2.54, stop ~£89.28
- **Liquidity:** avg GBP volume £162.4M ✓
- **Rejection Reason:** **Portfolio constraint: exceeds max_positions limit.**

### Candidate 3: AAL.L (Anglo American)
- **Entry Type:** Breakout
- **Confidence:** 0.61 (below optimal for balanced, but acceptable)
- **Trend:** FULL (close > SMA50 > SMA200, SMA50 slope positive)
- **Setup:**
  - Close within 0.4% of 20d high (£39.98 vs £40.00)
  - Volume ratio: 1.68× (elevated, strong breakout signal)
  - Close vs SMA50: +13.80% (strong trend)
- **Risk/Reward:** ATR = £1.35, stop ~£34.49
- **Liquidity:** avg GBP volume £196.5M ✓
- **Rejection Reason:** **Portfolio constraint: exceeds max_positions limit.**

---

## Risk Checks

| Check | Value | Limit | Status |
|-------|-------|-------|--------|
| Max positions | 6 | 5 | ❌ **BREACH** |
| Single-name (BP.L) | 48.33% | 30.0% | ❌ **BREACH** |
| Sector (Energy) | 79.64% | 40.0% | ❌ **BREACH** |
| Portfolio drawdown | 9.40% | 15.0% | ✓ OK |
| Cash buffer | 3.28% | 3.0% | ✓ OK |
| Half-day trading | No | — | ✓ Normal hours |

**Summary:** Three hard constraints breached. Trading blocked.

---

## Portfolio Drawdown Status

- **Current Portfolio Value:** £105.37
- **Peak Portfolio Value:** £116.22
- **Drawdown:** (116.22 − 105.37) / 116.22 = 9.40%
- **Drawdown Limit:** 15.0%
- **Status:** ✓ Within acceptable range (6.6 percentage points of cushion)
- **Implication:** Liquidation mode NOT triggered; portfolio may continue to be held.

---

## UK Costs Assumption Statement

- **Stamp Duty:** 50 bps applied to UK equity BUY orders (not applicable today; no trades executed)
- **Trading Fees:** £0.00 per trade (fee_model.value = 0)
- **Slippage Allowance:** 10 bps budgeted for all orders
- **No FX Costs:** All data GBP-normalised; no currency conversion

---

## Gap Risk Acknowledgement

**DAILY_CHECK Stop-Loss Mode:**
- Stop-loss prices are checked once per trading day against `low_gbp`.
- If overnight or intraday gaps occur **before** the daily check, actual execution price may be materially worse than the planned stop price.
- **Example:** If BP.L (stop = £4.68) gaps down to £4.50 at open, the sell will execute at market (likely £4.50 or worse), incurring additional loss.
- **Gap Risk Buffer Applied:** 10% reduction in position quantity for new entries (not applicable today; no new entries).
- **Mitigation:** Recommend tighter stops on high-volatility holdings (e.g., LLOY.L, BARC.L) or use broker-managed GTC orders if available.

---

## Portfolio Snapshot

**Sector Breakdown:**
- Energy: £84.49 (79.64%)
- Materials: £7.58 (6.74%)
- Industrials: £4.58 (4.35%)
- Healthcare: £5.27 (5.0%)
- Cash: £3.45 (3.28%)

**Unrealised Gains/Losses:**
- Total unrealised PnL: +£8.66
- Largest winner: BP.L (+£5.05)
- Largest loser: BA.L (−£0.80)

**Concentration Risk:**
- Top 1 position (BP.L): 48.33% — **EXCEEDS 30% limit**
- Top 2 positions (BP.L + SHEL.L): 79.64% — **EXCEEDS 40% sector limit**

---

## Orders Execution

**NO ORDERS TO EXECUTE**

All new entry candidates fail the hard constraint check (max_positions exceeded). The portfolio must be rebalanced before any new positions can be opened.

---

## What Could Invalidate This Plan

1. **Stop-Loss Triggers:** If any position's `low_gbp` breaches the `current_stop_gbp`, a SELL at market will execute immediately (DAILY_CHECK mode). This would free up cash and reduce position count below 5, unlocking new entry candidates.

2. **Position Exits:** Manual liquidation of one or more holdings to bring position count to ≤4 would unlock the constraint.

3. **Overnight Corporate Actions:** Delisting, suspension, or dividend events (not visible in provided data) could trigger automatic exits.

4. **Significant Price Changes:** If BP.L or SHEL.L declines sharply, their notional values would shrink, reducing both position count concern and sector exposure. However, this would also trigger stop-losses if breaches occur.

5. **Market-Wide Correction:** If portfolio declines >15% from peak (£116.22 → <£98.79), drawdown limit would trigger full liquidation. Current value £105.37 is still 10.1% above this threshold.

---

## Data Quality Notes

✓ **market_data.csv:** All required columns present. 25 tickers with complete pre-computed indicators (SMA50, SMA200, ATR14, drawdown, volume ratios, slopes).  
✓ **positions.json:** 6 active positions with valid entry dates, costs, stops, and PnL data.  
✓ **universe.csv:** 25 tickers, all with ACTIVE status. No delistings or suspensions.  
✓ **trading_calendar.json:** 2026-05-12 confirmed as LSE trading day. No half-day or holidays.  
✓ **No data staleness issues detected.**

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution risk, gaps, slippage, settlement delays, and tax consequences apply. Stop-losses in DAILY_CHECK mode are monitored once daily and **cannot protect against intraday or overnight price gaps**. Actual losses may exceed planned risk. All positions are subject to market risk, including total loss of capital.

Use this plan at your own risk. Consult a qualified financial advisor before deploying real capital.

---

**Plan Generated:** 2026-05-12 (algorithmic, rule-based)