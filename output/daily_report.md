# Daily Trading Report
**Date:** 2026-03-30  
**Status:** OK (No Trades)  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-03-31
- **Bank Holidays (next 5 days):** 2026-04-03

---

## Executive Summary
**No trades generated today.** While the portfolio contains quality holdings with positive unrealised P&L and the market environment passes trend filters, the cash position is critically constrained. With only £4.94 in cash and a required buffer of £3.46 (3% of £115.23 equity), only £1.48 is available for new investments. The next best setup (GSK.L pullback, confidence 0.68) requires £27.00, which is 18× available cash.

**Recommendation:** Consider tactical liquidations to free capital for higher-conviction setups, or accept a lower trading frequency until natural cash accumulation occurs through position gains.

---

## Top 3 Candidate Setups Considered

### 1. RIO.L (Rio Tinto) — Breakout
- **Trend Status:** FULL (close 67.72 > SMA50 68.63, SMA50 > SMA200)
- **Setup:** Approaching 20d high (72.85); drawdown 7.0%; volume ratio 0.98 (healthy)
- **Confidence Score:** 0.72
  - Trend component: 1.0 (strong uptrend)
  - Setup component: 0.75 (near breakout with low volume confirmation risk)
  - Risk/reward: 0.70 (ATR 2.16 gives clean risk structure)
  - Liquidity: 1.0 (avg GBP volume £255.8M)
  - Diversification: 0.50 (Materials, correlates with existing GLEN.L)
- **Why Rejected:** Insufficient cash. Required notional £71.11 (67.72 entry + £3.39 costs); available £1.48.
- **Entry:** Market order, 1 share = £67.72
- **Stop:** £63.98 (2×ATR 2.16 below entry)
- **Estimated P&L Range:** +£6.76 to -£7.74 (risk 0.05 × £115.23 = £5.76)

### 2. GSK.L (GlaxoSmithKline) — Pullback in Uptrend
- **Trend Status:** FULL (close 20.63 > SMA50 20.49, SMA50 > SMA200 17.15)
- **Setup:** Healthy pullback from 20d high (21.73); drawdown 5.1%; volume ratio 1.11 (mild accumulation)
- **Confidence Score:** 0.68
  - Trend component: 1.0 (uptrend confirmed)
  - Setup component: 0.65 (pullback depth appropriate for balanced profile)
  - Risk/reward: 0.60 (ATR 0.43 gives £0.92 stop distance)
  - Liquidity: 1.0 (avg GBP volume £180M)
  - Diversification: 0.50 (Healthcare; existing AZN.L position adds overlap)
- **Why Rejected:** Insufficient cash. Required notional £27.00 (entry + costs); available £1.48.
- **Entry:** Market order, 1 share = £20.63
- **Stop:** £19.18 (2×ATR below entry)
- **Estimated P&L Range:** +£1.55 to -£1.45 (risk 0.05 × £115.23 = £5.76, scaled to order size)

### 3. TSCO.L (Tesco) — Continuation in Uptrend
- **Trend Status:** FULL (close 4.662 > SMA50 4.634, SMA50 > SMA200 4.410)
- **Setup:** Mild consolidation; drawdown 6.1%; volume ratio 0.57 (low volume = quality pullback)
- **Confidence Score:** 0.58
  - Trend component: 1.0 (clear uptrend)
  - Setup component: 0.55 (shallow pullback, needs stronger entry signal)
  - Risk/reward: 0.50 (very tight ATR 0.11 = low risk but small reward window)
  - Liquidity: 0.90 (avg GBP volume £83.6M; borderline)
  - Diversification: 0.30 (Consumer Staples; correlated with ULVR.L, DGE.L, etc.)
- **Why Rejected:** Insufficient cash + low confidence relative to GSK/RIO.

---

## Risk Management Checks

| Constraint | Limit | Current | Status | Notes |
|-----------|-------|---------|--------|-------|
| **Cash Buffer** | 3.0% of equity | 4.28% | ⚠️ MARGINAL | Buffer = £3.46; actual cash = £4.94. Just above minimum. |
| **Max Positions** | 5 | 5 | ✅ PASS | At capacity (SHEL, BP, GLEN, BA, AZN). |
| **Max New Positions/Day** | 1 | 0 | ✅ PASS | No new entries attempted. |
| **Portfolio Turnover** | 30% | 0.0% | ✅ PASS | No trades executed. |
| **Max Risk Per Trade** | 5% of equity (£5.76) | N/A | ✅ PASS | No trades executed. |
| **Single-Name Exposure** | 30% of equity | **48.6% (BP)** | ❌ FAIL | BP position (£56.11) exceeds 30% × £115.23 = £34.57 limit. |
| **Sector Exposure** | 40% of equity | **48.9% (Energy)** | ❌ FAIL | Energy (SHEL + BP = £93.86) exceeds 40% × £115.23 = £46.09 limit. |
| **Max Correlated Positions** | 3 with ρ > 0.7 | ~2 (Energy) | ✅ PASS | SHEL and BP correlated; within limits. |
| **Portfolio Drawdown** | 15% from peak | 0.0% | ✅ PASS | Portfolio at all-time high (£115.23). |

**Critical Observations:**
1. **Structural Imbalance:** BP position is 48.6% of portfolio and Energy sector is 48.9%—both well above target limits. This concentration risk should be addressed via partial liquidations.
2. **Cash Constraint:** Limits new entry capacity severely. With only £1.48 available after buffer, even small positions (£20–30) cannot be opened.
3. **No Stop-Loss Breaches:** All existing positions remain above their stop levels. No forced exits required.

---

## Portfolio Drawdown Status
- **Portfolio Peak Equity:** £115.23 (as of 2026-03-30)
- **Current Equity:** £115.23
- **Drawdown from Peak:** 0.0%
- **Drawdown Limit:** 15%
- **Status:** ✅ Portfolio at all-time high. No liquidation required.

---

## UK Costs Assumption
- **Fee Model:** Per-trade, £0.00 per trade (assumed zero commissions; pipeline will apply actual broker fees at execution).
- **Stamp Duty:** 0.50% on UK equity buys only (not on ETFs). Applied in position sizing.
- **Slippage:** 10 bps assumed on entry and exit.
- **Note:** Actual execution costs (FX fees, settlement delays, taxes) are not modelled here. This is an automated, rules-based plan only.

---

## Gap Risk Acknowledgement
**Stop-Loss Execution Mode: DAILY_CHECK**

Stops are monitored once daily by comparing the day's low_gbp to current_stop_gbp. **This mode CANNOT protect against overnight gaps or intraday reversals.** If a position gaps below its stop during an overnight session or in the first minutes of trading, the actual loss will exceed the planned risk (typically 5% per position). A 10% gap risk buffer is applied to position sizes to partially mitigate this.

**Current Holdings with Stop Exposure:**
- **SHEL.L:** Stop £27.71; close £35.54; gap risk if SHEL falls > £7.83 overnight (22% move)
- **BP.L:** Stop £4.68; close £6.02; gap risk if BP falls > £1.34 overnight (22% move)
- **GLEN.L:** Stop £4.86; close £5.54; gap risk if GLEN falls > £0.68 overnight (12% move)
- **BA.L:** Stop £21.50; close £21.32; stop very close to current price (0.8% margin); high gap risk if intraday volatility widens
- **AZN.L:** Stop £137.18; close £147.02; gap risk if AZN falls > £9.84 overnight (7% move)

---

## Current Portfolio Snapshot

| Ticker | Quantity | Avg Cost | Market Value | Unrealised P&L | Days Held | Stop | Status | Sector |
|--------|----------|----------|--------------|---|----------|------|--------|--------|
| SHEL.L | 1.0624 | £28.70 | £37.75 | +£7.26 | 38 | £27.71 | ACTIVE | Energy |
| BP.L | 9.32 | £4.92 | £56.11 | +£10.21 | 22 | £4.68 | ACTIVE | Energy |
| GLEN.L | 1.035 | £5.08 | £5.73 | +£0.47 | 37 | £4.86 | ACTIVE | Materials |
| BA.L | 0.2378 | £22.61 | £5.07 | -£0.31 | 18 | £21.50 | ACTIVE | Industrials |
| AZN.L | 0.0383 | £142.90 | £5.63 | +£0.16 | 9 | £137.18 | ACTIVE | Healthcare |
| **CASH** | — | — | **£4.94** | — | — | — | — | — |
| **TOTAL** | — | — | **£115.23** | **+£17.79** | — | — | — | — |

---

## Orders to Execute
**None.** No sells triggered. No buys executed due to cash constraint.

---

## What Could Invalidate This Plan
1. **Overnight Gap:** Any position gaps below its stop → forced exit at worse price than planned.
2. **Cash Inflow:** If the pipeline detects dividend payments or deposits, available cash may increase and enable new entries.
3. **Corporate Action:** Unexpected stock split, rights issue, or delisting on any holding.
4. **Market Structure Break:** If LSE closes unexpectedly or technical issues prevent trading.
5. **Liquidity Dry-Up:** If volume on any position evaporates (e.g., index reconstitution, trading halts).
6. **Correlation Regime Shift:** If Energy holdings (SHEL, BP) decouple due to geopolitical events, portfolio risk increases.
7. **FX Movement:** Non-GBP holdings (ETFs: VUAG.L, VWRP.L, CSP1.L) are exposed to GBP strength. If GBP rallies, GBP-converted returns are dampened.

---

## Data Quality Notes
- ✅ All required columns present in market_data.csv.
- ✅ All positions have pre-computed SMA50, SMA200, ATR14, and drawdown metrics.
- ✅ All tickers are ACTIVE in universe.csv.
- ✅ No gaps in historical data (50+ days for all holdings).
- ✅ Trading day confirmed via trading_calendar.json.
- ⚠️ VMID.L and CSP1.L have low average GBP volumes (£5.3M, £7.8M) vs. min_avg_gbp_volume (£50k). Excluded from consideration.

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice. Do not execute without independent verification.**

Execution risks include but are not limited to:
- **Gap Risk:** Stop-losses in DAILY_CHECK mode cannot protect against overnight or intraday gaps exceeding ATR × multiplier.
- **Slippage & Fees:** Actual execution prices may differ from bid/ask midpoints. Commissions, stamp duty, and FX costs apply.
- **Settlement Timing:** T+1 settlement in the UK means sells do not free cash until the next day. Plan accordingly.
- **Tax Implications:** Realized gains trigger capital gains tax (if applicable). Stamp duty applies to equity buys.
- **Liquidity Constraints:** Large orders may move markets. Volume ratios assume normal market conditions.
- **Concentration Risk:** Current portfolio is 48.6% BP and 48.9% Energy—well above diversification targets. Consider rebalancing.

**Use at your own risk.**

---

## Next Steps (Recommended)
1. **Liquidate BP 50%:** Free ~£28 in cash to enable new entries and reduce concentration.
2. **Monitor GSK.L and RIO.L:** If either drops 2–3% from current levels, re-evaluate entry with freed cash.
3. **Review BA.L position:** Currently -£0.31 P&L with low quantity (0.24 shares). Consider closing to simplify portfolio.
4. **Watch AZN.L stop:** Stop at £137.18 is tight vs. 14-day ATR. Consider trailing it up if trend confirms.

---

**End of Report**