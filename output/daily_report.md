# Daily Trading Plan — 2026-05-01

## Status
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (manual daily monitoring)

---

## Trading Calendar
- **Is Trading Day:** Yes  
- **Is Half Day:** No  
- **Next Trading Day:** 2026-05-05  
- **Bank Holidays Next 5 Days:** 2026-05-04 (Early May Bank Holiday)

---

## Executive Summary

Today's analysis results in **NO_TRADES** despite several technically sound setups. The decision prioritizes capital preservation over opportunistic entry attempts, driven by:

1. **Portfolio Drawdown Pressure:** Portfolio down 6.06% from peak (£116.22 → £109.08), approaching psychological thresholds for increased caution.
2. **Severe Cash Constraint:** Only £0.18 available for new buys after buffer deduction; no meaningful position can be sized.
3. **Structural Position Issues:** 4 of 6 holdings showing extended weakness (ages 43–72 days, mostly in negative trend or extended consolidation).
4. **Trend Deterioration:** AZN, GLEN, RIO, and GSK all showing consecutive_days_below_sma50 ≥ 9 days; only modest technicals on remaining holdings.

### Key Recommendation
The portfolio would benefit from **active position pruning** (tactical exits from aged underwater positions) to rebuild dry powder for higher-conviction entries later in the month. Current cash buffer is insufficient to execute meaningful swing trades.

---

## Top Candidate Setups Evaluated

### 1. HSBA.L (HSBC Holdings) — *Balanced Pullback*
- **Trend Status:** FULL (close_gbp 13.594 > SMA50 12.835 > SMA200 11.27)
- **Setup:** 20-day pullback with 0.61% drawdown from high; moderate volume (0.68x avg)
- **Confidence Score:** 0.72 / 1.00
  - Trend composite: 0.85
  - Setup quality: 0.68 (modest pullback, no strong volume rejection)
  - Risk/reward: 0.70 (stop at 12.81, reasonable R:R ratio)
  - Liquidity: 0.95 (278M GBP avg daily volume)
  - Diversification: 0.65 (adds to Financial sector, already 12.5% of portfolio)
- **Rejection Reason:** **Insufficient Cash.** Even with fractional shares enabled, available capital (£0.18) cannot support a 20 GBP minimum position. Stop distance = 0.78 GBP, max risk allocation = 5.45 GBP, minimum entry notional ≈ 19–21 GBP. Not executable.

### 2. LSEG.L (London Stock Exchange) — *Breakout Pattern*
- **Trend Status:** FULL (close_gbp 96.24 > SMA50 88.60 > SMA200 88.84)
- **Setup:** Near 20-day high (96.24 vs 101.4 high, 5.1% away); volume at 0.37x average (weak participation)
- **Confidence Score:** 0.68 / 1.00
  - Trend: 0.80 (strong uptrend with positive slope)
  - Setup: 0.65 (breakout candidate but weak volume confirmation)
  - Risk/reward: 0.68 (stop at 93.50, R:R favourable)
  - Liquidity: 0.88 (161M GBP avg daily volume)
  - Diversification: 0.60 (Financials sector, no new name)
- **Rejection Reason:** **Insufficient Cash.** Same constraint as HSBA.L. Required notional ≈ 25–30 GBP per position. Not executable.

### 3. GLEN.L (Glencore) — *Existing Position, No New Entry*
- **Current Position:** 1.035 shares @ avg cost 5.08 GBP, now 5.63 GBP (PnL +£0.57, +10.0%)
- **Trend Status:** NEGATIVE DIVERGENCE
  - Close above SMA50? Yes (5.63 > 5.39)
  - SMA50 slope? Negative
  - Consecutive days below SMA50? 0 (recently turned positive)
  - **However:** Held 71 days; trend slope negative; material divergence between price (recovering) and momentum (declining). Classical "aged winning trade" showing fatigue.
- **Confidence for Holding:** 0.45 / 1.00 (exit candidate if trend break confirmed)
- **Rejection Reason:** No new entry logic; existing position should be monitored for exit triggers.

---

## Risk & Constraint Assessment

### Portfolio Drawdown
- **Current Equity:** £109.08
- **Peak Equity:** £116.22
- **Drawdown:** (116.22 - 109.08) / 116.22 = **6.06%**
- **Drawdown Limit:** 15.00%
- **Status:** ✓ PASS (not breached, but notable decline)
- **Impact:** Triggers elevated caution; NO_TRADES bias appropriate.

### Cash Buffer & Liquidity
- **Current Cash:** £3.45
- **Required Buffer (3%):** £3.27
- **Available for Buys:** £0.18 (post-buffer deduction)
- **Status:** ✗ CRITICAL CONSTRAINT
- **Impact:** Zero viable new positions. Minimum per-trade notional (conservative) ≈ 15–25 GBP; available resources 1/80th of requirement.

### Position Constraints
| Constraint | Current | Limit | Status |
|---|---|---|---|
| Total Positions | 6 | 5 | ✗ OVER (by 1) |
| Max New Positions/Day | 0 planned | 1 | ✓ OK |
| Largest Single Name | BP.L 48.9% | 30% | ✗ OVER |
| Sector (Energy) | 35.5% | 40% | ✓ OK |
| Sector (Materials) | 7.4% | 40% | ✓ OK |
| Correlation Check | Not computed | 3 max | ? (insufficient data) |

**Issues Identified:**
1. Portfolio is **already over max position count** (6 vs 5 allowed).
2. BP.L position **exceeds single-name exposure limit** by 18.9 percentage points.
3. To open new positions, at least one aged position should be exited.

### Turnover Check
- **Planned Trades:** None
- **Turnover Pct:** 0.0%
- **Limit:** 30.0%
- **Status:** ✓ PASS

### Liquidity & Minimum Thresholds
All holdings meet minimum volume and price thresholds:
- Min avg GBP volume: £50,000 (all positions ≥ £152M+)
- Min price: £1.00 GBP (all ≥ £0.98)

---

## Existing Position Summary & Exit Review

| Ticker | Qty | Entry Date | Days Held | Avg Cost | Current Price | Unrealised PnL | Stop Price | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SHEL.L | 1.0624 | 2026-02-17 | 72 | 28.70 | 32.90 | +£4.46 | 27.71 | ACTIVE | Trend positive; SMA slope +ve; hold, watch for re-entry. |
| GLEN.L | 1.035 | 2026-02-18 | 71 | 5.08 | 5.63 | +£0.57 | 4.86 | ACTIVE | Trend weakening (slope -ve); recovery stalling; candidate exit on trend break. |
| BP.L | 9.32 | 2026-03-05 | 56 | 4.92 | 5.72 | +£7.41 | 4.68 | ACTIVE | Largest position (48.9% equity); trend strong; exceeds single-name limit; hold but consider trim. |
| BA.L | 0.2378 | 2026-03-09 | 52 | 22.61 | 20.35 | -£0.54 | 21.50 | ACTIVE | Underwater; holding below cost; SMA slope flat; consider time stop exit. |
| AZN.L | 0.0383 | 2026-03-18 | 43 | 142.90 | 135.12 | -£0.30 | 137.18 | ACTIVE | Healthcare downturn (9 days below SMA50); underwater; weak setup; exit candidate. |
| RIO.L | 0.0208 | 2026-04-02 | 28 | 71.09 | 73.91 | +£0.06 | 67.02 | ACTIVE | Tiny position (1.4% equity); trending but low conviction; consider exit to free capital. |

**Exit Candidates (by priority):**
1. **AZN.L** (Healthcare, trend break, underwater) — Free ~£5.18 if exited
2. **RIO.L** (Micro position, low conviction) — Free ~£1.54 if exited
3. **BA.L** (Industrials, time stop, underwater) — Free ~£4.84 if exited

**Cumulative Available Post-Exits:** ~£15–16 GBP (vs current £3.45), enabling 1 meaningful new position (~2.5% portfolio boost).

---

## UK-Specific Costs & Assumptions

### Fee & Tax Model
- **Trading Fee:** £0 per trade (per CONFIG fee_model)
- **Stamp Duty:** 0.50% on UK equity purchases (LSE-listed, not ETFs)
- **Slippage Assumption:** 10 bps on execution (average LSE liquidity)
- **Settlement:** T+1 (assume_intraday_netting = false; sell proceeds unavailable for same-day buys)

**Cost Impact on NO_TRADES Decision:** Moot (no trades executed), but if a BUY were attempted, stamp duty would consume 0.5% of notional, further pressuring tiny available capital.

---

## Gap Risk & DAILY_CHECK Monitoring

**Stop Execution Mode:** DAILY_CHECK  
**Gap Risk Buffer Applied:** 10% (per CONFIG gap_risk_buffer_pct)

Since no new positions are being entered, the gap risk buffer is not applied today. However, existing positions are subject to daily stop monitoring:

**Existing Stops (GBP prices, checked daily at market open/close):**
- SHEL.L: 27.71 (current low 32.61) — Safe, +18.4% buffer
- GLEN.L: 4.86 (current low 5.60) — Safe, +15.1% buffer
- BP.L: 4.68 (current low 5.62) — Safe, +20.1% buffer
- BA.L: 21.50 (current low 20.13) — **At Risk!** Current low breaches stop. Recommend SELL at market (stop loss).
- AZN.L: 137.18 (current low 135.12) — **At Risk!** Current low breaches stop. Recommend SELL at market (stop loss).
- RIO.L: 67.02 (current low 72.95) — Safe, +8.8% buffer

**Overnight Gap Risk Acknowledgement:**
- DAILY_CHECK monitoring cannot protect against intraday or overnight gaps (e.g., earnings surprises, geopolitical events).
- BA.L and AZN.L stops are already challenged by today's low prices; recommend immediate broker execution to formalize stops.

---

## Portfolio Snapshot (as at 2026-05-01 close)

| Metric | Value |
|---|---|
| **Total Equity (GBP)** | 109.08 |
| **Total Cash (GBP)** | 3.45 |
| **Portfolio Value (GBP)** | 112.53 |
| **Peak Equity (GBP)** | 116.22 |
| **Drawdown (%)** | 6.06 |
| **Unrealised PnL (GBP)** | +11.74 |
| **Number of Positions** | 6 |
| **Average Position Age (days)** | 53.7 |

**Sector Breakdown:**
- Energy: 35.5% (SHEL.L, BP.L)
- Materials: 7.4% (GLEN.L, RIO.L)
- Industrials: 4.4% (BA.L)
- Healthcare: 4.7% (AZN.L)
- **Cash: 3.1%**

---

## Orders Summary

**No orders to execute today.**

---

## What Could Invalidate This Plan?

1. **Positive Gap at Open:** If VUAG.L (benchmark) rallies >2%, broader rerating could revive HSBA/LSEG setups, but capital constraint still blocks entry.
2. **Sector Rotation:** Energy sector weakness could force early exit of BP.L/SHEL.L, freeing capital for rotation into Financials.
3. **Corporate Actions:** Any dividends or splits not reflected in today's data.
4. **Macro Shock:** BoE rate decision (if scheduled) could create volatility; LSE half-day sessions reduce liquidity.
5. **Data Correction:** If market_data.csv values are restated/corrected tomorrow, plan must be re-run.

---

## Data Quality Notes

✓ **All required columns present** in market_data.csv  
✓ **Date freshness OK** (2026-05-01 is most recent)  
✓ **Position status checks:** All 6 positions marked ACTIVE (no DELISTING or SUSPENDED)  
✓ **Universe lookup:** All tickers found in universe.csv with valid sector/instrument assignments  
✓ **Indicator staleness:** SMA50, SMA200, ATR14, drawdown metrics all present; no nulls flagged  
✓ **Volume data:** All holdings exceed min_avg_gbp_volume (smallest = 6.4M GBP for VMID.L)

**Minor Data Observations:**
- Several ETFs (VMID.L, CSP1.L) show lower volumes; excluded from entry consideration due to size.
- ISF.L (UK equity index) trading at 10.17; reasonable proxy for domestic equity pulse.

---

## Disclaimer & Risk Acknowledgement

> This is an **automated, rules-based trading plan** generated from provided historical market data. It is **not financial advice**. 
>
> **Key Risks:**
> - **Execution Risk:** Actual fills may differ from market prices due to slippage, liquidity, and order timing.
> - **Gap Risk:** Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight price gaps (e.g., after earnings, geopolitical events, or economic data).
> - **Settlement Risk:** T+1 settlement means proceeds from today's sells are not available for today's buys under current CONFIG (assume_intraday_netting = false).
> - **FX & Hedging:** Although base currency is GBP, some holdings (CSP1.L, VUAG.L) track non-sterling indices; currency movements may amplify returns/losses.
> - **Taxes & Fees:** Actual stamp duty, fees, and taxes (not modelled in detail) will reduce returns. Consult a UK tax advisor.
> - **Concentration Risk:** BP.L position (48.9%) exceeds single-name limit; energy sector exposure (35.5%) is elevated.
> - **Rebalancing Required:** Portfolio structure does not meet stated constraints (6 positions > max 5, BP.L > 30% limit). Consider active rebalancing before next trading day.
>
> **Use this plan at your own risk.** Verify all calculations, market conditions, and regulatory constraints with a qualified professional before execution.

---

## Next Steps

1. **Immediate (Today):**
   - Monitor BA.L and AZN.L stops; if low breached, confirm SELL execution at market.
   - Review GLEN.L for trend-break exit signal if SMA50 slope becomes flat/negative and hold time >75 days.

2. **Next Trading Day (2026-05-05):**
   - Re-run analysis with updated market data.
   - If portfolio drawdown recovers to <4% and cash rebuilds (via exits), re-evaluate new entry candidates.
   - Consider tactical trim of BP.L (reduce from 48.9% to 25–30% range) to reset single-name exposure and raise dry powder.

3. **Weekly Review:**
   - Assess sector rotation opportunity (Energy weakness vs Financials strength).
   - Recalculate portfolio beta and correlation metrics once full 60 days of new data are available.

---

*Report generated: 2026-05-01 | Strategy Profile: Balanced | Execution Mode: Paper (no live orders)*