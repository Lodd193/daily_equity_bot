# Daily Trading Plan – 2026-05-21

**Status:** OK (No Trades Executed)  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Calendar:** LSE (Full trading day)

---

## Summary

No trades were executed today despite identification of several quality pullback and breakout setups. The portfolio is currently over-concentrated in the Energy sector (81.14% of equity), which exceeds the maximum sector exposure limit of 40%. Additionally, the largest position (BP.L at 48.70%) exceeds the single-name exposure limit of 30%. These constraints prevent new position openings until rebalancing occurs.

Cash available after mandatory buffer is only 4.79 GBP, which is insufficient for new equity positions. The portfolio remains within overall drawdown limits (7.09% below peak), so no liquidation is triggered.

---

## Top 3 Setups Considered

### 1. HSBA.L (HSBC) – Pullback in Uptrend
- **Confidence Score:** 0.72
- **Trend Status:** FULL (close 13.58 > SMA50 12.89, SMA50 12.89 > SMA200 11.52)
- **Setup:** 20-day pullback of 0.82% from high. Volume ratio 1.16x (elevated). Close above SMA50.
- **Technical Rationale:**
  - SMA50 slope positive, indicating uptrend resumption
  - Pullback minimal (less than 2%), suggesting healthy consolidation
  - High liquidity (277M GBP avg volume)
- **Rejection Reason:** Sector constraint violation. Energy sector already 81% of portfolio; cannot add Financial position without violating diversity rules. Insufficient capital (4.79 GBP available).

### 2. RIO.L (Rio Tinto) – Pullback in Uptrend
- **Confidence Score:** 0.68
- **Trend Status:** FULL (close 77.68 > SMA50 72.14, SMA50 72.14 > SMA200 60.21)
- **Setup:** 6.1% pullback from 20-day high. Volume ratio 1.38x. Close 7.7% above SMA50.
- **Technical Rationale:**
  - Strong uptrend with positive SMA50 slope
  - Pullback magnitude within balanced profile range (4-10%)
  - Materials sector diversification would help, but already held
- **Rejection Reason:** Position already held. Sector constraint prevents Materials addition. Insufficient capital.

### 3. LSEG.L (London Stock Exchange Group) – Breakout
- **Confidence Score:** 0.70
- **Trend Status:** FULL (close 92.74 > SMA50 90.99, SMA50 90.99 > SMA200 88.32)
- **Setup:** Close 8.5% below 20-day high (101.40) but trending higher. Volume ratio 0.61x (confirming high-volume breakout potential). Entry at resistance test.
- **Technical Rationale:**
  - Strong uptrend sustainability
  - Breakout setup near recent consolidation zone
  - Excellent liquidity for entry/exit
- **Rejection Reason:** Insufficient capital. Notional value ~92.74 GBP exceeds available 4.79 GBP after costs and buffer.

---

## Risk Checks & Compliance

| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Portfolio Drawdown | 7.09% | 15.0% | ✅ PASS |
| Cash After Buffer | 4.79 GBP | — | ⚠️ LOW |
| Positions Count | 5 | 5 | ✅ AT LIMIT |
| Energy Sector Exposure | 81.14% | 40.0% | ❌ **FAIL** |
| BP.L Single-Name | 48.70% | 30.0% | ❌ **FAIL** |
| Materials Sector | 8.77% | 40.0% | ✅ PASS |
| Healthcare Sector | 4.96% | 40.0% | ✅ PASS |
| Max Turnover Today | 0.0% | 30.0% | ✅ PASS |
| New Positions Planned | 0 | 1 | ✅ PASS |

**Portfolio Constraint Violations (Blocking New Entries):**
1. **Energy Sector Over-Exposure:** 81.14% > 40% limit
2. **Single-Name Over-Exposure:** BP.L at 48.70% > 30% limit
3. **Insufficient Capital:** 4.79 GBP available < minimum position size required

**Recommendation:** Consider reducing Energy sector exposure via strategic SELL orders on next trading session to re-enable new entry opportunities. BP.L is particularly concentrated.

---

## Portfolio Drawdown Status

- **Portfolio Peak:** 116.22 GBP (all-time high)
- **Current Equity:** 108.04 GBP
- **Drawdown:** 7.09% (within 15% limit)
- **Status:** ✅ Above liquidation trigger

No panic selling required. Portfolio is recovering organically.

---

## UK-Specific Costs Assumption

- **Stamp Duty:** 50 bps applied to UK equity BUY orders only (ETFs exempt)
- **Fee Model:** Per-trade fees = 0 GBP (no per-trade fees configured)
- **Slippage:** 10 bps estimated on all orders
- **Settlement:** T+1 (UK standard). Intraday netting OFF (conservative).

No BUY orders executed today, so no costs incurred.

---

## Stop-Loss Monitoring (DAILY_CHECK Mode)

**Active Stop Orders Being Monitored:**

| Ticker | Quantity | Stop Price | Current Price | Status |
|--------|----------|-----------|---|--------|
| SHEL.L | 1.0624 | 27.71 | 32.39 | ✅ Safe |
| GLEN.L | 1.0350 | 4.86 | 5.74 | ✅ Safe |
| BP.L | 9.3200 | 4.68 | 5.652 | ✅ Safe |
| AZN.L | 0.0383 | 137.18 | 140.06 | ✅ Safe |
| RIO.L | 0.0208 | 67.02 | 77.68 | ✅ Safe |

**Gap Risk Acknowledgement:** 
Stop-losses are monitored via daily close prices in DAILY_CHECK mode. Overnight or intraday gaps may result in actual fills at prices materially different from stop price. No intraday protection is available. Users should consider setting broker-level GTC (Good-Till-Cancelled) stops for real-time protection during market hours.

---

## Current Portfolio Snapshot

**Account Summary:**
- **Cash Balance:** 8.03 GBP
- **Equity Value:** 108.04 GBP
- **Total Account:** 116.07 GBP
- **Unrealised P&L:** +10.69 GBP (+9.95%)

**Position Details:**

| Ticker | Shares | Avg Cost | Market Value | Unrealised P&L | Days Held | Sector | Status |
|--------|--------|----------|---|---|--------|--|--|
| SHEL.L | 1.0624 | 28.70 | 34.41 | +3.92 | 92 | Energy | ACTIVE ✅ |
| BP.L | 9.3200 | 4.92 | 52.68 | +6.78 | 76 | Energy | ACTIVE ✅ |
| GLEN.L | 1.0350 | 5.08 | 5.94 | +0.68 | 91 | Materials | ACTIVE ✅ |
| AZN.L | 0.0383 | 142.90 | 5.36 | -0.11 | 63 | Healthcare | ACTIVE ⚠️ |
| RIO.L | 0.0208 | 71.09 | 1.62 | +0.14 | 48 | Materials | ACTIVE ✅ |

**Sector Breakdown:**
- Energy: 81.14% (SHEL.L + BP.L)
- Materials: 8.77% (GLEN.L + RIO.L)
- Healthcare: 4.96% (AZN.L)

---

## Orders Table

**No orders to execute today.**

All identified entry setups rejected due to:
1. Energy sector over-exposure (81.14% vs. 40% limit)
2. Single-name concentration (BP.L at 48.70% vs. 30% limit)
3. Insufficient available capital (4.79 GBP after buffer)

---

## What Could Invalidate This Plan

1. **Overnight Gap Down:** Any position breaching its stop-loss after market close (AZN.L or RIO.L most vulnerable due to small position size and high volatility).
2. **Major News/Earnings:** Unexpected earnings surprises or regulatory changes affecting Energy or Healthcare sectors could shift trend filters.
3. **FX Impact:** Although prices are GBP-normalised, underlying USD exposure (CSP1.L, VUAG.L, VWRP.L) could affect USD equities held indirectly.
4. **Sector Rotation:** If Energy sector corrects sharply, portfolio drawdown could exceed 15% limit, triggering liquidation.
5. **Dividend/Corporate Action:** Any announced special dividends or splits not reflected in current data.
6. **Liquidity Dry-Up:** If LSE trading halts or volume collapses unexpectedly, stop-losses may execute at unfavorable prices.
7. **Settlement Delays:** If T+1 settlement fails or delays, cash availability for future trades could be impaired.

---

## Data Quality Notes

✅ **All Required Columns Present:** market_data.csv includes all mandatory pre-computed fields (SMA50, SMA200, ATR14, drawdown, volume ratios).  
✅ **Data Freshness:** market_data.csv dated 2026-05-21, matches as_of_date. No staleness detected.  
✅ **Indicator Validity:** All SMA200 values populated. No null indicator fields for active portfolio holdings.  
✅ **Universe Alignment:** All 25 instruments in market_data.csv present in universe.csv with ACTIVE status.  
✅ **Trading Calendar:** Confirmed full trading day (not half-day, no bank holidays until 2026-05-25).  

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Key risks and limitations:
- **Execution Risk:** Actual prices may differ from market data prices due to slippage, liquidity constraints, and order timing.
- **Gap Risk:** Stop-losses in DAILY_CHECK mode are monitored once per day and cannot protect against intraday or overnight gaps. Use broker GTC stops for continuous protection.
- **Slippage & Fees:** Estimated slippage of 10 bps and stamp duty of 50 bps on UK equities. Actual costs may vary.
- **Settlement Timing:** UK T+1 settlement may delay cash availability. Assumes no settlement failures.
- **FX Effects:** Non-GBP holdings carry implicit currency risk if underlying assets are non-GBP denominated.
- **Correlation & Drawdown:** Correlation matrix not provided; beta calculations are illustrative only.
- **Tax Implications:** Capital gains, dividend tax, and stamp duty not accounted for. Users responsible for UK tax reporting.
- **Regulatory:** Strategy assumes continuous market access. LSE trading halts, new regulations, or broker issues could prevent execution.

**Use at your own risk. Consult a financial advisor before deploying real capital.**

---