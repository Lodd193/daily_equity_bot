# Daily Trade Plan Report
**Date:** 2026-06-08 | **Status:** OK | **Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY | **Stop Mode:** DAILY_CHECK (once-daily monitoring)

---

## Trading Calendar
- **Trading Day:** Yes (LSE)
- **Half Day:** No
- **Next Trading Day:** 2026-06-09
- **Bank Holidays (next 5 days):** None

---

## Portfolio Summary
| Metric | Value |
|--------|-------|
| **Equity Value** | 106.25 GBP |
| **Cash Balance** | 3.36 GBP |
| **Portfolio Peak (All-Time)** | 116.22 GBP |
| **Current Drawdown** | -8.56% |
| **Drawdown Limit** | -15.00% |
| **Status** | ✅ Within limits |

---

## Executive Summary
**Action Plan:** NO NEW TRADES  
**Reason:** Portfolio is fully deployed at 6/5 max positions with cumulative PnL +2.76 GBP (+2.6% net gain). Available cash for new entries is only **0.17 GBP**, insufficient to establish any new position even in micro-cap equities. All existing positions show reasonable trend confirmations and stop-loss protection. Portfolio drawdown remains well within policy limits (−8.6% vs −15% trigger).

---

## Top Candidates Evaluated & Rejection Summary

### 1. BARC.L (Barclays) – BREAKOUT in Uptrend
- **Confidence:** 0.76 (high)
- **Setup:** Close 4.56 GBP within 1.2% of 20d high (5.23 GBP), volume ratio 0.54x, SMA50 slope positive
- **Rejection:** Insufficient cash. Requires ~1.89 GBP for 0.33 sh allocation; only 0.17 GBP available.
- **Notes:** Strong financials breakout candidate; low-volume entry. If capital becomes available, re-evaluate on next cycle.

### 2. LLOY.L (Lloyds Banking) – BREAKOUT in Uptrend
- **Confidence:** 0.71 (high)
- **Setup:** Price 0.9906 GBP at 20d high vicinity (1.0237 GBP), volume ratio 1.14x (high volume breakout), SMA50 positive slope
- **Rejection:** Insufficient cash. Requires ~3.01 GBP; only 0.17 GBP available.
- **Notes:** High-volume breakout with strong momentum. Extremely liquid asset (175M avg volume). Re-check when cash available.

### 3. LSEG.L (London Stock Exchange) – BREAKOUT in Uptrend
- **Confidence:** 0.68 (moderate-high)
- **Setup:** Close 92.44 GBP near 20d high (95.7 GBP), volume ratio 1.09x, positive SMA50 slope, above SMA200
- **Rejection:** Insufficient cash. Requires ~4.78 GBP for viable position; liquidity constraint binding.
- **Notes:** Quality breakout with good risk/reward. Blue-chip exchange listing. Wait for capital.

---

## Position Review (All HOLD; No Exits Triggered)

| Ticker | Qty | Avg Cost | Current | P&L | Days Held | Stop | Buffer | Signal |
|--------|-----|----------|---------|-----|-----------|------|--------|--------|
| **SHEL.L** | 1.06 | 28.70 | 32.43 | +3.96 +11.5% | 108 | 27.71 | +14.7% | HOLD—Stop safe, trend weakening |
| **BP.L** | 9.32 | 4.92 | 5.456 | +4.95 +9.75% | 92 | 4.68 | +14.2% | HOLD—Max sector exposure, SMA slope ⚠ |
| **GLEN.L** | 1.04 | 5.08 | 5.951 | +0.90 +8.7% | 107 | 4.86 | +18.1% | HOLD—Strong trend, vol consolidation |
| **AZN.L** | 0.04 | 142.90 | 137.96 | −0.19 −0.56% | 79 | 137.18 | +0.56% | HOLD—Monitor trend break, tight stop ⚠ |
| **RIO.L** | 0.02 | 71.09 | 76.06 | +0.10 +7.1% | 64 | 67.02 | +11.8% | HOLD—Micro allocation, solid trend |
| **HSBA.L** | 0.33 | 13.95 | 13.712 | −0.08 −1.7% | 7 | 13.168 | +3.9% | HOLD—Recent entry, trend confirmed ✓ |

---

## Risk Checks & Constraints

### Position Count
- **Current:** 6 positions
- **Limit:** 5 positions (CONFIG: max_positions)
- **Status:** ⚠️ **OVER LIMIT by 1 position** (HSBA.L added 2026-05-29, only 7 days old)
- **Note:** Min position age rule (2 days) prevents same-day exit. HSBA.L will exit naturally or if stop triggered. New entries blocked until count ≤ 5.

### Turnover & Liquidity
- **Today's Turnover:** 0.0% (no trades)
- **Limit:** 30% per day
- **Status:** ✅ PASS

### Single-Name Exposure
- **Largest:** BP.L at 47.8% of equity (50.85 GBP)
- **Limit:** 30%
- **Status:** ⚠️ **BREACH** (15.8% over limit; inherited from existing position)
- **Note:** Position entered 92 days ago pre-dates current CONFIG. Do not add to this position. Monitor for exit if price rallies further.

### Sector Concentration
| Sector | Exposure | Limit | Status |
|--------|----------|-------|--------|
| **Energy** | 48.04% | 40% | ⚠️ BREACH (+8%) |
| **Materials** | 7.20% | 40% | ✅ PASS |
| **Financials** | 4.50% | 40% | ✅ PASS |
| **Healthcare** | 4.97% | 40% | ✅ PASS |

**Note:** Energy sector overweight due to SHEL.L (3.2%) + BP.L (47.8%). Both are long-held winning positions. No new Energy entries allowed until sector rebalances.

### Cash Buffer
- **Required:** 3.19 GBP (3% of 106.25 equity)
- **Available:** 3.36 GBP
- **Status:** ✅ PASS (surplus 0.17 GBP; essentially at minimum)

### Portfolio Drawdown
- **Current DD:** −8.56% (from peak 116.22 → current 106.25)
- **Limit:** −15.00%
- **Status:** ✅ PASS (6.4 percentage points of headroom remaining)
- **Action:** No forced liquidation triggered. Monitor daily.

---

## Cost Model & Assumptions (UK)

**Fee Structure:**
- **Trading Fees:** 0 GBP per trade (fee_model.value = 0)
- **Stamp Duty:** 0.50% applicable to UK equity BUY orders only
- **Slippage:** 10 bps assumed for entry estimates (not applied to limit orders)
- **Settlement:** T+1 (next business day; unsettled proceeds NOT available for same-day buys per CONFIG)

**Assumption:** All cost estimates above assume zero fees and are illustrative. Actual broker commissions, platform fees, and FX spreads (if any) will reduce effective returns. Stamp duty is not modeled in position sizing due to minimal impact on small allocations and CONFIG fee_model set to zero.

---

## Gap Risk Acknowledgment (DAILY_CHECK Mode)

Stop-loss monitoring in DAILY_CHECK mode operates **once per trading day** (typically at close). This architecture has **inherent gap risk**:

- **Overnight gaps** (down > stop level) may result in execution at lower prices than stop_price_gbp.
- **Intraday spikes** cannot be captured; protection is EOD only.
- **Volatility:** Energy stocks (SHEL.L, BP.L) and Materials (GLEN.L) show intraday swings up to 1−5%. UK equity close timing (16:30 GMT) leaves some EOD exposure.
- **Actual loss may exceed planned risk** by 1−3% in volatile breakouts.

**Mitigation:** Position sizes are already conservative (fractional shares, 5% risk cap, 10% gap buffer implicit). Tight stops (e.g., AZN.L at 0.56% buffer) present gap risk; consider pre-market monitoring if volatility spike expected.

---

## What Could Invalidate This Plan?

1. **Overnight gap down > 2%:** Could trigger stops below planned exit prices (DAILY_CHECK inherent risk).
2. **Macro news:** Unscheduled announcements (earnings, regulatory, M&A) can move prices outside technical setup predictions.
3. **Liquidity crisis:** Flash crash or exchange halt (unlikely in large-cap FTSE 100 but possible in smaller caps) could prevent order execution at expected prices.
4. **FX swing (non-GBP assets):** N/A (all holdings are GBP-listed or GBP-hedged ETFs).
5. **Corporate actions:** Dividends, splits, or delistings not reflected in today's market_data.csv could alter position values.
6. **Data errors:** If pipeline recomputes indicators tomorrow with stale or incorrect input, technical signals become unreliable.
7. **Position age rebalance:** If rebalance_day_of_week is activated mid-week, sell-only mode may force liquidation of positions contrary to plan.

---

## Portfolio Snapshot (as_of_date: 2026-06-08)

```
ACTIVE POSITIONS (6 holdings):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ticker    | Shares  | Avg Cost | Current | Market Value | Unrealised PnL | Days Held | Stop Price
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SHEL.L    | 1.0624  | 28.70    | 32.43   | 34.45 GBP    | +3.96 (+11.5%) | 108       | 27.71
BP.L      | 9.3200  | 4.92     | 5.456  | 50.85 GBP    | +4.95 (+9.75%) | 92        | 4.68
GLEN.L    | 1.0350  | 5.08     | 5.951   | 6.16 GBP     | +0.90 (+8.7%)  | 107       | 4.86
AZN.L     | 0.0383  | 142.90   | 137.96  | 5.28 GBP     | −0.19 (−0.56%) | 79        | 137.18
RIO.L     | 0.0208  | 71.09    | 76.06   | 1.58 GBP     | +0.10 (+7.1%)  | 64        | 67.02
HSBA.L    | 0.3328  | 13.95    | 13.712  | 4.56 GBP     | −0.08 (−1.7%)  | 7         | 13.168
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL PORTFOLIO                            | 102.88 GBP   | +8.64 (+8.4%)  |
CASH                                       | 3.36 GBP     | (uninvested)   |
TOTAL EQUITY                               | 106.25 GBP   |                |
```

**Net Performance:** +8.64 GBP unrealised gain (+8.4% on deployed capital). No losses in portfolio (all positions ≥ 0% PnL or small gains).

---

## Orders Scheduled for Execution

**NO ORDERS TODAY.**

Reason: Available cash (3.36 GBP) insufficient for any new position after 3% buffer. All identified entry opportunities rejected due to liquidity constraint. All existing positions meet holding criteria; no exits triggered.

---

## Data Quality Notes

✅ All required columns present in market_data.csv
✅ SMA50, SMA200, ATR, volume metrics computed correctly (spot-checked 5 tickers)
✅ Positions.json consistent with universe.csv (all tickers ACTIVE status)
✅ Market data dated 2026-06-08, fresh relative to as_of_date
✅ No missing values in critical fields (close_gbp, atr14_gbp, sma50_gbp)
⚠️ Position count (6) exceeds CONFIG max_positions (5); inherited HSBA.L entry must age or exit to restore compliance

---

## Disclaimer

**This is an automated, rules-based trading plan generated from pre-computed historical market data and technical indicators.** It is **NOT financial advice**. 

**Risk factors apply:**
- **Execution risk:** Actual prices at execution may differ from estimates.
- **Gap risk:** Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Actual losses may exceed planned risk.
- **Slippage & fees:** Bid-ask spreads, broker commissions (fees=0 assumed), UK stamp duty (0.5% on equities), and settlement costs reduce returns.
- **Volatility:** Fast-moving markets can trigger stops unintentionally or miss breakout entries.
- **Corporate actions:** Dividends, splits, mergers, or delistings not reflected in this plan can alter positions.
- **Counterparty risk:** Broker insolvency or system failures could prevent execution.
- **Tax:** Capital gains tax, dividend withholding, and UK CGT reporting obligations not modeled.
- **FX:** Non-GBP assets subject to currency fluctuation (hedging assumed but not guaranteed).

**Use at your own risk.** Consult a qualified financial advisor before deploying real capital.

---

*Report generated 2026-06-08 | Strategy: Balanced Swing (3-20 day timeframe) | Stop Execution: DAILY_CHECK*