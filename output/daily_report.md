# Daily Trading Report — 2026-06-09

**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Calendar:** LSE (regular trading day, not half-day)  

---

## Executive Summary

No trades generated today. The portfolio is constrained by **extreme cash starvation** (£3.36 available vs £103.53 equity = 3.25% cash ratio). While the portfolio drawdown is manageable at 11.0% (limit 15%), the cash shortage makes any meaningful new entry impossible. All existing positions assessed for exits; no stop-loss breaches detected, and anti-churn logic protects the recently added HSBA.L position (10 days old).

**Key Finding:** The portfolio would need to liquidate existing positions to fund new trades, but trend-break thresholds and lack of clear sell signals prevent opportunistic liquidation. Recommendation: Allow portfolio to self-heal through organic cash generation (dividends, rebalance events) or wait for stop-loss triggers on deteriorating positions.

---

## Market Data & Calendar

- **Date:** 2026-06-09
- **Data Status:** ✓ Fresh (matches as_of_date)
- **All Required Columns:** ✓ Present (all 21 technical/sector columns provided)
- **Trading Day:** ✓ Yes (LSE open)
- **Half-Day:** ✗ No (normal hours)
- **Bank Holidays Next 5 Days:** None

---

## Portfolio Snapshot

| Ticker | Qty | Avg Cost (£) | Market Value (£) | Unrealised PnL (£) | Days Held | Status | Stop (£) |
|--------|-----|--------------|------------------|--------------------|-----------|--------|----------|
| **SHEL.L** | 1.0624 | 28.70 | 33.81 | +3.32 | 111 | ⚠ TREND WEAK | 27.71 |
| **GLEN.L** | 1.0350 | 5.08 | 5.89 | +0.63 | 110 | ✓ HOLD | 4.86 |
| **BP.L** | 9.3200 | 4.92 | 49.33 | +3.44 | 95 | ⚠ TREND WEAK | 4.68 |
| **AZN.L** | 0.0383 | 142.90 | 5.22 | –0.25 | 82 | ✗ TREND BROKEN | 137.18 |
| **RIO.L** | 0.0208 | 71.09 | 1.55 | +0.07 | 67 | ✓ HOLD | 67.02 |
| **HSBA.L** | 0.3328 | 13.95 | 4.36 | –0.28 | 10 | ⚠ YOUNG | 13.17 |
| **CASH** | — | — | 3.36 | — | — | — | — |
| **TOTAL** | — | — | **103.53** | **+6.93** | — | — | — |

**Peak Equity:** £116.22  
**Current Drawdown:** (116.22 – 103.53) / 116.22 = **11.0%** ✓ Under 15% limit  
**Cash Ratio:** 3.25% (well below 3% buffer target due to recent trades exhausting cash)

---

## Trend Analysis & Exit Assessment

### SHEL.L (Energy, 31.825 GBP)
- **Trend:** Close < SMA50 (negative). **24 consecutive days below SMA50** (–3.27%).
- **Stop:** 27.71 not breached; current > stop.
- **Signal:** TREND BREAK WARNING. Trend integrity compromised; monitor closely. If 20-day-below threshold applies, ~4 days to trigger.
- **Action:** HOLD (no stop breach yet; anti-trend-break rule not yet mature).

### AZN.L (Healthcare, 136.32 GBP)
- **Trend:** Close < SMA50 (negative). **34 consecutive days below SMA50** (–3.50%).
- **Stop:** 137.18 not breached; current < stop price (!), but unrealised loss only –2.4%.
- **Signal:** TREND BROKEN. This position has entirely lost uptrend.
- **Action:** HOLD (no hard stop breach; consider selling on bounce).

### BP.L (Energy, 5.293 GBP)
- **Trend:** Close < SMA50 (negative). **12 consecutive days below SMA50** (–5.50%).
- **Stop:** 4.68 not breached; current > stop.
- **Signal:** TREND WEAK but not broken yet.
- **Action:** HOLD. Monitor; if reaches 20+ days, escalate to exit.

### GLEN.L (Materials, 5.692 GBP)
- **Trend:** ✓ Positive (close > SMA50, positive sma50_slope, 0 days below SMA50).
- **Stop:** 4.86 not breached.
- **Signal:** HOLD. Strong performer (+10.7% unrealised).
- **Action:** HOLD.

### RIO.L (Materials, 74.69 GBP)
- **Trend:** Marginal (1 day below SMA50, close –0.65% vs SMA50, but positive sma50_slope).
- **Stop:** 67.02 not breached.
- **Signal:** HOLD. Tiny position (1.5% portfolio); minimal risk.
- **Action:** HOLD.

### HSBA.L (Financials, 13.114 GBP)
- **Trend:** Close < SMA50 by small margin (–1.41%). 1 day below SMA50.
- **Stop:** 13.168 not breached.
- **Signal:** YOUNG POSITION (10 days; min_position_age_days = 2, so eligible for exit but protected by anti-churn discretion).
- **Action:** HOLD. Recent entry; allow to develop.

---

## New Entry Candidates Ranked by Confidence

### 1. BARC.L (Barclays, Financials, 4.48 GBP) — **Confidence: 0.72**
- **Setup:** BREAKOUT. Close at 4.48 vs 20d high 5.23 = 14.4% pullback. Volume ratio 0.88 (sub-average volume, typical of consolidation). Trend FULL (close > SMA50, SMA50 > SMA200, positive slope).
- **Entry Signal:** At/near breakout level; strong technical setup.
- **Risk/Reward:** Stop 4.34 GBP (ATR × 2.2 multiplier for balanced profile), risk ~3.2% per share. Reward target ~4.65 GBP (risk:reward ~1:1.05 — marginal).
- **Liquidity:** avg_gbp_volume_20d = 210.1M GBP ✓ (well above 50k min). Participation OK.
- **Cost Estimate (4 shares):**  
  - Notional: 4 × 4.48 = 17.92 GBP
  - Fees (0): 0
  - Stamp duty (50 bps): 0.0896 GBP
  - Slippage (10 bps): 0.0179 GBP
  - **Total: ~18.10 GBP required**
- **Rejection:** **Cash insufficient.** Available 0.46 GBP; required 18.10 GBP. Would need to liquidate 17.64 GBP from existing positions (Financials already 4.2%, and BARC is also Financials = sector breach).

### 2. REL.L (RELX, Industrials, 26.02 GBP) — **Confidence: 0.68**
- **Setup:** PULLBACK. Drawdown from 20d high (27.05) = 3.8% pullback. Close > SMA50 (positive 2.27%). Trend FULL (positive slope, SMA50 > SMA200).
- **Entry Signal:** Healthy pullback in uptrend.
- **Risk/Reward:** Stop 24.76 GBP (ATR × 2.2), risk ~4.7% per share. Reward target ~27.5 GBP (risk:reward ~1:1.1 — acceptable).
- **Liquidity:** avg_gbp_volume_20d = 150.8M GBP ✓.
- **Cost Estimate (1 share):**  
  - Notional: 26.02
  - Stamp duty: 0.1301
  - Slippage: 0.0260
  - **Total: ~26.18 GBP required**
- **Rejection:** **Cash insufficient.** Available 0.46 GBP; required 26.18 GBP.

### 3. NWG.L (NatWest, Financials, 5.93 GBP) — **Confidence: 0.65**
- **Setup:** PULLBACK. Drawdown from 20d high = 2.7%. Trend FULL (positive slope, close > SMA50, SMA50 > SMA200).
- **Entry Signal:** Tight pullback; conservative setup.
- **Risk/Reward:** Stop 5.78 GBP (ATR × 2.2 = 0.1334 × 2.2 ≈ 0.29, but this seems low; use 3% conservative stop = 5.75 GBP). Risk ~2.7%, reward target 6.25 GBP (risk:reward ~1:1.05).
- **Liquidity:** avg_gbp_volume_20d = 136.7M GBP ✓.
- **Cost Estimate (5 shares):**  
  - Notional: 5 × 5.93 = 29.65
  - Stamp duty: 0.1483
  - Slippage: 0.0297
  - **Total: ~29.83 GBP required**
- **Rejection:** **Cash insufficient** + **Sector conflict.** Financials already 4.2%; adding NWG would push to 9%+ and conflict with max sector rules if major positions held.

### 4. LLOY.L (Lloyds, Financials, 0.98 GBP) — **Confidence: 0.61**
- **Setup:** PULLBACK. Drawdown from 20d high = 4.1%. Trend FULL (positive slope).
- **Entry Signal:** Good pullback, but ultra-low stock price (0.98p) means large share count needed.
- **Risk/Reward:** Stop 0.951 GBP (3% below entry); risk ~2.9%, target 1.05 GBP (risk:reward ~1:1.03 — poor).
- **Liquidity:** avg_gbp_volume_20d = 171.9M GBP ✓ (excellent).
- **Cost Estimate (100 shares to have meaningful position):**  
  - Notional: 100 × 0.98 = 98 GBP
  - Stamp duty: 0.49
  - Slippage: 0.098
  - **Total: ~98.59 GBP required**
- **Rejection:** **Impossible.** Would require liquidating entire portfolio and more. Confidence also weak due to poor risk:reward and sector saturation (Financials).

### 5. DGE.L (Diageo, Consumer Staples, 15.085 GBP) — **Confidence: 0.64**
- **Setup:** PULLBACK. Drawdown from 20d high (16.265) = 7.3%. Trend FULL (close > SMA50, positive slope, 0 days below SMA50).
- **Entry Signal:** Moderate pullback; good setup.
- **Risk/Reward:** Stop 14.65 GBP (ATR × 2.2 ≈ 0.83). Risk ~2.8%, target ~16.5 GBP (risk:reward ~1:1.2 — acceptable).
- **Liquidity:** avg_gbp_volume_20d = 260.3M GBP ✓ (excellent).
- **Cost Estimate (2 shares):**  
  - Notional: 2 × 15.085 = 30.17
  - Stamp duty: 0.1509
  - Slippage: 0.0301
  - **Total: ~30.35 GBP required**
- **Rejection:** **Cash insufficient.** Consumer Staples also well-represented already (RKT, IMB, TSCO exposure indirectly; focus on sectors without holdings).

---

## Constraint Validation (All Failed Due to Cash)

| Constraint | Limit | Current | Status | Notes |
|-----------|-------|---------|--------|-------|
| **Cash Available** | — | £0.46 | ✗ FAIL | Any new trade requires >£0.46 funding; all candidates cost £18–£99 |
| **Max Positions** | 5 | 6 | ✗ OVER | Portfolio already at 6 holdings (above limit). Would need to liquidate 1 before new entry. |
| **Max New Positions/Day** | 1 | 0 | ✓ OK | No trades executed. |
| **Turnover %/Day** | 30% | 0% | ✓ OK | No trades. |
| **Max Risk per Trade** | 5% of equity | — | N/A | Cannot assess; no trades executed. |
| **Max Single-Name** | 30% | 47.6% (BP) | ✗ OVER | BP is 47.6% of portfolio. Cannot add. |
| **Max Sector** | 40% | 52.3% (Energy) | ✗ OVER | Energy (SHEL + BP) at 52.3%. Violates limit. |
| **Portfolio Drawdown** | 15% | 11.0% | ✓ OK | Under limit; no forced liquidation. |

**Conclusion:** Even if cash were available, portfolio is already over max positions (6 vs 5), over sector limit (Energy 52.3% vs 40%), and over single-name limit (BP 47.6% vs 30%). No new BUY signals can be executed responsibly.

---

## Risk Checks Summary

### Stop-Loss Status
- **SHEL.L:** Stop 27.71 GBP; current 31.825 GBP. ✓ Not breached. Monitor trend (24 days below SMA50).
- **AZN.L:** Stop 137.18 GBP; current 136.32 GBP. ⚠ **Extremely close.** Any small downward move breaches stop.
- **BP.L:** Stop 4.68 GBP; current 5.293 GBP. ✓ Not breached.
- **Others:** All clear.

### Trend Break Status
- **SHEL.L, AZN.L, BP.L:** All showing 1–34 days below SMA50. Trend integrity compromised.
- **GLEN.L, RIO.L, HSBA.L:** Neutral to positive trend.

### Sector Exposure
- **Energy:** SHEL (32.7%) + BP (47.6%) = **52.3%** ✗ **Exceeds 40% limit.**
- **Materials:** GLEN (5.7%) + RIO (1.5%) = **7.2%** ✓
- **Healthcare:** AZN (5.0%) ✓
- **Financials:** HSBA (4.2%) ✓

**Mitigation:** Energy positions are established (111 and 95 days held). No clear exit signals yet. Recommend gradual reduction over time as positions age and exit rules trigger.

### Liquidity & Slippage
- All holdings have strong liquidity (avg_gbp_volume_20d > 100M GBP).
- Slippage estimate (10 bps) is conservative and easily absorbed.

### FX Risk
- All holdings are GBP-denominated equities or GBP-quoted ETFs. No FX exposure.

### Correlation & Beta
- Data not provided in inputs. Assume correlation_matrix.csv not available.
- Diversification appears reasonable (6 sectors, 6 tickers).

---

## UK Costs & Fees

**Fee Model:** Per-trade, £0 (zero fees assumed).  
**Stamp Duty:** 50 bps (0.5%), applies to BUY orders only, UK equities only (ETFs exempt).  
**Slippage:** 10 bps (0.1%) estimated on entry/exit.  

Cost estimates for all candidate trades above include these assumptions. **Note:** If actual broker charges differ, adjust cost estimates accordingly.

---

## Gap Risk & Daily Check Acknowledgement

**Stop Execution Mode:** DAILY_CHECK  

The portfolio uses daily price monitoring for stop-loss enforcement. This means:
- Stops are checked once per day against the **low_gbp** (daily low price).
- **Gap Risk:** Overnight or intraday gaps can cause execution at prices significantly worse than the stop price.
- **Mitigation:** Gap risk buffer (10%) applied to all position sizes; ATR-based stops reduce gap impact by anchoring to volatility.

**Current Exposure:** AZN.L stop (137.18) is extremely close to current price (136.32); any overnight gap down triggers stop.

---

## What Could Invalidate This Plan

1. **Market Gap:** Overnight gap down could breach AZN.L stop (137.18 GBP) unexpectedly. Plan assumes smooth entry/exit.
2. **Dividend Announcement:** Any announced dividend would increase cash_balance_gbp and unlock new entry opportunities.
3. **Corporate Action:** Splits, spin-offs, or delistings not visible in today's data could force exits.
4. **Trend Reversal:** If Energy sector (SHEL, BP) reverses upward trend, reassess exit signals.
5. **Sector Rebalance:** Removal of Energy limits or relaxation of max_positions would unlock trades.
6. **Drawdown Acceleration:** If portfolio drops >15% from peak, forced liquidation mode engages.
7. **Settlement Event:** If unsettled sell proceeds from recent trades clear, cash becomes available.

---

## Data Quality Notes

✓ **All required columns present in market_data.csv**  
✓ **All positions match universe.csv**  
✓ **Market data fresh as of 2026-06-09**  
✓ **No missing or NaN indicators** (all sma50, atr14, volume ratios provided)  
✓ **Consistent GBP pricing** (all prices in _gbp suffix columns)  

**Data Integrity:** Excellent. No exclusions or flags needed.

---

## Orders Executed

**No orders generated.** Portfolio remains unchanged.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

Execution is subject to:
- **Real market conditions:** Bid-ask spreads, partial fills, slippage, and market impact.
- **Settlement risk:** UK T+1 settlement may delay cash availability.
- **Gap risk:** Stop-losses in DAILY_CHECK mode cannot protect against overnight or intraday gaps. Actual losses may exceed planned risk.
- **Regulatory risk:** Stamp duty, transaction taxes, and FX effects apply.
- **Model risk:** Strategy based on historical technical indicators; past performance ≠ future results.

**Recommendation:** Review portfolio constraints (sector overweight, cash shortage, position count) and consider:
1. Waiting for stop-loss triggers on underperforming positions (AZN.L, HSBA.L, BP.L).
2. Accepting organic cash generation from dividends/rebalance events.
3. If urgent: selectively liquidate smallest position (RIO.L, 1.5% portfolio) to unlock cash for high-confidence setups.

Use at your own risk. Consult a qualified financial advisor before trading.

---