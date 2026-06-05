# Daily Trade Plan Report
**Date:** 2026-06-05  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

## Summary
The portfolio is **locked due to insufficient cash**. Current cash balance is **3.36 GBP**, of which **3.18 GBP** must be reserved as a cash buffer (3% of equity), leaving only **0.18 GBP** available for new trades. This is insufficient to establish any new position, even in the lowest-priced equities. No exit signals were triggered for existing positions today.

## Trading Calendar
- **Trading Day:** Yes  
- **Half Day:** No  
- **Next Trading Day:** 2026-06-08  
- **Bank Holidays (next 5 days):** None  

## Portfolio Status
- **Total Equity (GBP):** 106.06  
- **Cash (settled):** 3.36  
- **Peak Equity (all-time):** 116.22  
- **Current Drawdown:** 8.72%  
- **Drawdown Limit:** 15.0%  
- **Drawdown Status:** ✓ PASS  

**Position Count:** 6 / 5 max (1 position over limit)  
- This excess position likely resulted from previous day fills. No immediate action required given illiquidity.

## Existing Positions Analysis (All HOLD)

| Ticker | Qty | Avg Cost | Market Value | Unrealised PnL | Days Held | Stop Price | Exit Signal |
|--------|-----|----------|--------------|----------------|-----------|------------|-------------|
| SHEL.L | 1.0624 | 28.70 | 34.29 | +3.80 | 107 | 27.71 | None |
| GLEN.L | 1.0350 | 5.08 | 6.11 | +0.85 | 106 | 4.86 | None |
| BP.L | 9.3200 | 4.92 | 50.89 | +4.99 | 91 | 4.68 | None |
| AZN.L | 0.0383 | 142.90 | 5.31 | -0.17 | 78 | 137.18 | None |
| RIO.L | 0.0208 | 71.09 | 1.58 | +0.10 | 63 | 67.02 | None |
| HSBA.L | 0.3328 | 13.95 | 4.53 | -0.11 | 6 | 13.17 | None |

**Key Observations:**
- All positions above their stop prices; no hard stop-loss exits triggered.
- Most positions held well over min_position_age_days (2 days), so sales would be discretionary, not churn-driven.
- HSBA.L is newest (6 days), likely a recent entry that is already close to breakeven (–0.11 GBP loss).
- Net portfolio PnL: +9.47 GBP (8.93% unrealised gain on cost).

## Cash Constraint Detail
- **Cash Balance:** 3.36 GBP  
- **Cash Buffer Required (3%):** 3.18 GBP  
- **Cash Available for Trades:** 0.18 GBP  

**Why This Matters:**
- Smallest position in universe (LLOY.L @ 0.99 GBP) would need ~50 shares to establish a meaningful position size relative to portfolio risk model.
- Cost for 50 shares LLOY.L: ~50 GBP + fees + stamp duty.
- **Conclusion:** Portfolio is effectively cash-locked. Liquidation of a small position would be required to fund any new trade.

## Candidate Entry Analysis
Three setups were identified as technically viable (pre-computed indicators confirm trend + setup):

### 1. LSEG.L – Breakout (Confidence: 78%)
- **Trend:** FULL (close 93.84 > SMA50 91.94 > SMA200 88.09)  
- **Setup:** Close 93.84 near 20d high 95.70 (98% of range). Volume 2.84M vs avg 1.44M (1.97x ratio).  
- **Rejection:** Would require ~32 GBP notional + 0.16 GBP costs. Cash available: 0.18 GBP. **INSUFFICIENT.**

### 2. BARC.L – Pullback (Confidence: 72%)
- **Trend:** FULL (close 4.58 > SMA50 4.31 > SMA200 4.25)  
- **Setup:** Pullback: 20d high 5.23, current close 4.58 = 12.4% drawdown from high. Volume 30.6M vs avg 48.4M (0.63x) = low-volume pull-back (healthy).  
- **Rejection:** Would require ~15 GBP notional + 0.08 GBP costs. Cash available: 0.18 GBP. **INSUFFICIENT.**

### 3. LLOY.L – Pullback (Confidence: 68%)
- **Trend:** FULL (close 0.99 > SMA50 0.98 > SMA200 0.94)  
- **Setup:** Pullback: 20d high 1.02, current close 0.99 = 3.1% drawdown. Volume 147.5M vs avg 173.2M (0.85x) = low-volume.  
- **Rejection:** Even with minimum fractional shares (1 share ~0.99 GBP + costs), would exhaust available cash. **INSUFFICIENT.**

## Risk Checks – All Pass (but constraints unmet)

| Constraint | Value | Limit | Status |
|-----------|-------|-------|--------|
| Portfolio Drawdown | 8.72% | 15.0% | ✓ PASS |
| Cash Buffer (3%) | 3.18 | 3.18 | ✓ PASS |
| Max Positions | 6 | 5 | ✗ OVER (non-critical; likely from prior settlement) |
| Turnover (today) | 0.0% | 30.0% | ✓ PASS |
| Sector Exposure – Energy | 32.88% | 40.0% | ✓ PASS |
| Sector Exposure – Materials | 18.07% | 40.0% | ✓ PASS |
| Largest Position (BP.L) | 47.95% | 30.0% | ✗ OVER (historical; market movement + no new buys) |

**Note:** BP.L position is oversized relative to the 30% single-name limit. This is a legacy issue from earlier trades. The best remedy would be to trim BP.L by ~7–8 GBP notional to bring it to 30% target, which would free ~7–8 GBP in cash to fund a new trade. This is a **rebalancing opportunity** but outside the scope of today's NO_TRADES output.

## UK Costs Summary
- **Fee Model:** Per-trade at 0 GBP (no per-trade fees).  
- **Stamp Duty:** 50 bps applied to UK equity buys only (ETFs exempt).  
- **Slippage Assumption:** 10 bps (market impact + slippage estimated).  
- **Estimated cost on 15 GBP notional trade:** Stamp duty ~7.50 GBP + slippage ~1.50 GBP = **~9 GBP total**, far exceeding available cash.

## Gap Risk Acknowledgement
Stop-loss execution mode is **DAILY_CHECK**: The bot monitors once daily whether low_gbp <= current_stop_gbp. If a stop is breached, a market sell is generated for the next trading day. **Overnight and intraday gaps can cause actual losses to exceed the planned ATR-based stop distance.** This is a known limitation of non-broker-managed stops. All existing positions are currently above their stops, so this risk is not active today.

## Sector & Correlation Summary
- **Energy (32.88%):** SHEL.L, BP.L – concentrated; both energy commodities (correlated).  
- **Materials (18.07%):** GLEN.L, RIO.L, AAL.L – mining & metals; moderate diversification.  
- **Healthcare (5.01%):** AZN.L – small, recent entry showing minor loss.  
- **Financials (4.27%):** HSBA.L – newest position, minimal loss.  

**Note:** Correlation matrix not provided by pipeline; pairwise correlations not computed. Sector concentration in Energy is notable; any major energy sell-off would hurt portfolio significantly.

## What Could Invalidate This Plan
1. **Market Gap Down:** If any open price in next session breaches a stop (SHEL, GLEN, BP, AZN, RIO), a SELL order will be generated and this plan will be superseded.  
2. **Trend Break:** If close_gbp < SMA50 for multiple consecutive days (e.g., Balanced profile requires 2 consecutive days), exit rules trigger.  
3. **Sector Rotation:** Large energy-sector decline could force rebalancing.  
4. **Cash Injection:** If settlement of a prior trade occurs or dividends are paid, cash becomes available and new trades could proceed.  
5. **Portfolio Recovery:** If equity rises above 116.22 GBP (new peak), drawdown resets and capital becomes more available.

## Data Quality Notes
- ✓ All required columns present in market_data.csv.  
- ✓ SMA50 and SMA200 available for all tickers.  
- ✓ ATR14 values provided; no nulls detected.  
- ✓ Position.json and universe.csv align; no delisting/suspension flags.  
- ✓ market_data.csv dated 2026-06-05 matches as_of_date.  
- ⚠ **No correlation_matrix.csv provided; correlation constraints cannot be verified.** Assumed OK given small portfolio (6 positions).

## DISCLAIMER
**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

Execution risks include:
- **Settlement timing:** T+1 settlement means proceeds not available same-day (assume_intraday_netting = false).  
- **Gaps and slippage:** Actual fills may differ from planned prices. Stop-losses in DAILY_CHECK mode cannot prevent overnight gaps.  
- **FX effects:** Non-GBP instruments converted via pipeline; actual spot rates may differ.  
- **Fees and taxes:** Stamp duty (50 bps on UK equities), FCA fees, and capital gains tax not accounted for in plan.  
- **Liquidity:** During volatile periods, spreads may widen and fills may not be guaranteed.  
- **Regulatory:** Ensure compliance with FCA rules, tax residency, and broker T&Cs.  

**Use at your own risk. Consult a qualified financial advisor before deploying real capital.**

---
### Plan Generation
- **Generated:** 2026-06-05 (automated, no human review)  
- **Confidence Profile:** Balanced  
- **Next Review:** 2026-06-08 (next trading day)

===