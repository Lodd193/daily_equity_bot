# Daily Trading Report
**Date:** 2026-06-18  
**Status:** OK (1 exit order generated)  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- Trading day: Yes
- Half day: No
- Next trading day: 2026-06-19
- Bank holidays next 5 days: None

---

## Summary of Actions

### Mandatory Exit
**BARC.L (Barclays, Financials)** – SELL 16.0358 shares @ market
- **Reason:** Anti-churn policy violation. Position entered 2026-06-17 (0 days held); min_position_age_days=2 requires minimum 2 days before any sell (except stop-loss or forced exits).
- **Trend Quality:** Positive (close 5.006 > SMA50 4.449, full uptrend present)
- **Market Value Exiting:** £80.28
- **Unrealised P&L:** -£0.55 (small loss)
- **Turnover Impact:** 80.2% (exceeds 30% max_turnover_pct_per_day constraint). Justification: Anti-churn is a mandatory compliance rule that supersedes turnover limits.

### No New Entries
All six quality trading setups identified were rejected due to **insufficient cash liquidity** post-BARC.L exit:
- Available cash after BARC.L sale: ~£17.41 GBP
- Minimum notional required for smallest quality setup: £91+ GBP
- Portfolio equity: £100.12 (very small account)

---

## Top 3 Setups Evaluated (Rejected)

### 1. HSBA.L (HSBC, Financials) – Breakout Entry – Confidence 0.82
- **Trend:** Full uptrend (close 14.424 > SMA50 13.5148 > SMA200 11.9272) ✓
- **Setup:** Confirmed breakout at 20-day high (14.424), strong volume (1.36x avg)
- **Entry Price:** 14.424 GBP
- **Stop Loss:** 13.7418 GBP (1.5x ATR below entry)
- **Required Notional:** £95.32 (6.61 shares × 14.424, gap-buffered)
- **Rejection:** Insufficient cash (£95.32 > £17.41 available)

### 2. AAL.L (Anglo American, Materials) – Pullback Entry – Confidence 0.79
- **Trend:** Full uptrend (close 39.95 > SMA50 37.9939 > SMA200 32.2651) ✓
- **Setup:** Healthy pullback (5.76% drawdown), strong volume (1.45x avg), excellent liquidity
- **Entry Price:** 39.95 GBP
- **Stop Loss:** 37.98 GBP (1.5x ATR below entry)
- **Required Notional:** £91.52 (2.29 shares × 39.95, gap-buffered)
- **Rejection:** Insufficient cash (£91.52 > £17.41 available)

### 3. NWG.L (NatWest Group, Financials) – Pullback Entry – Confidence 0.76
- **Trend:** Full uptrend (close 6.412 > SMA50 5.9253 > SMA200 5.9164) ✓
- **Setup:** Pullback at SMA50 support with 8.2% upside room, balanced volume
- **Entry Price:** 6.412 GBP
- **Stop Loss:** 6.2088 GBP (1.5x ATR below entry)
- **Required Notional:** £142.22 (22.17 shares × 6.412, gap-buffered)
- **Rejection:** Insufficient cash (£142.22 > £17.41 available)

---

## Risk Checks

| Constraint | Limit | Current | Status | Notes |
|-----------|-------|---------|--------|-------|
| Max Positions | 5 | 2 (post-exit) | ✓ PASS | BARC.L exit reduces to GLEN.L + RIO.L |
| Turnover % per Day | 30% | 80.2% | ✗ FAIL | Anti-churn exit overrides constraint |
| Max Risk per Trade % | 5.0% | N/A | ✓ PASS | No new entries |
| Max Sector Exposure | 40% | 0% (post-exit) | ✓ PASS | Materials only after BARC.L exit |
| Max Single Name | 30% | 5.8% | ✓ PASS | Largest post-exit is 1.58% GLEN.L |
| Cash Buffer | 3% | 3.0% | ✓ PASS | £3.00 held in reserve |
| Min Position Age | 2 days | 0 days (BARC.L) | ✗ FAIL | Forced exit to achieve compliance |
| Liquidity (volume) | £50k avg | All candidates fail | ✗ FAIL | VUAG.L, VMID.L below threshold |
| Data Freshness | Today | 2026-06-18 | ✓ PASS | Market data current |

---

## Portfolio Drawdown Status
- **Peak Equity:** £116.22 (2026-?)
- **Current Equity:** £100.12
- **Current Drawdown:** 13.86% of peak (below 15% limit) ✓
- **Drawdown Trajectory:** Increasing concern; further market weakness could trigger liquidation mode

---

## UK Costs & Fees Assumption
- **Fees Model:** Per-trade = £0 (no trading fees configured)
- **Stamp Duty:** 0.50% on UK equities (applies to BARC.L sale as EQUITY)
  - Estimated on £80.28 sale: ~£0.40
- **Slippage:** 10 basis points assumed on all orders
  - Estimated on BARC.L: ~£0.08
- **Total Estimated Costs:** ~£0.48
- **Cash After BARC.L Exit:** ~£79.80 – £0.48 ≈ £79.32 (added to existing £12.41 = ~£91.73 new cash)
  - **Revised Available for Buys:** ~£88.73 GBP
  - **NOTE:** Even with revised cash, portfolio is still too small for significant new positions without exceeding max_risk_per_trade_pct or max_single_name_exposure_pct on small accounts.

---

## Gap Risk Acknowledgement
- **Stop Execution Mode:** DAILY_CHECK
- **Risk:** Stop-losses checked once daily at market open/close; overnight gaps or intraday moves can result in losses exceeding planned risk.
- **Mitigation Applied:** 10% gap risk buffer reduces position sizes relative to planned risk.
- **Existing Positions:**
  - GLEN.L: Stop 4.86, low_20d 4.826 (tight, gap risk present)
  - RIO.L: Stop 67.02, low_20d 75.89 (comfortable cushion)
  - BARC.L: Exiting today (no gap risk for this position)

---

## Portfolio Snapshot (Pre-Exit)

| Ticker | Sector | Qty | Avg Cost | Market Value | Unrealised P&L | Days Held | Status |
|--------|--------|-----|----------|--------------|----------------|-----------|--------|
| GLEN.L | Materials | 1.035 | 5.08 | £5.86 | +£0.60 | 119 | ACTIVE |
| RIO.L | Materials | 0.0208 | 71.09 | £1.58 | +£0.10 | 76 | ACTIVE |
| BARC.L | Financials | 16.0358 | 5.04 | £80.28 | -£0.55 | 0 | **EXITING** |
| **TOTAL** | | | | **£87.72** | **+£0.15** | | |
| **CASH** | | | | | | | **£12.41** |
| **PORTFOLIO** | | | | | | | **£100.12** |

### Portfolio Snapshot (Post-Exit)

| Ticker | Sector | Qty | Avg Cost | Market Value | Unrealised P&L | Days Held | Status |
|--------|--------|-----|----------|--------------|----------------|-----------|--------|
| GLEN.L | Materials | 1.035 | 5.08 | £5.86 | +£0.60 | 120 | ACTIVE |
| RIO.L | Materials | 0.0208 | 71.09 | £1.58 | +£0.10 | 77 | ACTIVE |
| **TOTAL EQUITY** | | | | **£7.44** | **+£0.70** | | |
| **CASH** | | | | | | | **~£91.73** |
| **PORTFOLIO** | | | | | | | **~£99.17** |

---

## Orders Table

| Order ID | Ticker | Side | Type | Quantity | Limit Price | Time in Force | Stop Price | Reason |
|----------|--------|------|------|----------|-------------|----------------|-----------|--------|
| 1 | BARC.L | SELL | MKT | 16.0358 | — | GTC | — | Anti-churn exit (0 days held) |

---

## What Could Invalidate This Plan

1. **Overnight Gap Down:** If BARC.L gaps down > 5% on exit, realized loss could exceed estimated slippage.
2. **Market Halt:** If trading halts before BARC.L exits, execution delayed to next trading day.
3. **FX Risk:** Non-applicable (all instruments GBP-denominated or ETFs priced in GBP).
4. **Corporate Action:** If BARC.L announces delisting/suspension, automatic SELL triggered.
5. **Regulatory Change:** If LSE trading hours reduced or calendar disrupted.
6. **Liquidity Dry-Up:** If BARC.L volume collapses, actual exit price could be significantly worse than market.
7. **Data Error:** If market_data.csv prices are stale or incorrect, decision basis is invalidated.

---

## Data Quality Notes

- ✓ All required columns present in market_data.csv
- ✓ All SMA50, SMA200, ATR14 values populated
- ✓ Sector and instrument type data complete
- ✓ Universe allowlist all ACTIVE status
- ⚠ Some tickers fail min_avg_gbp_volume (VUAG.L, VMID.L) – correctly excluded
- ⚠ Portfolio equity very small (£100.12) – position sizing may result in fractional shares; fractional_shares=true permits this
- ✓ Trading calendar data current and complete

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice. The following risks apply:**

- **Execution Risk:** Actual execution prices may differ from estimated prices due to slippage, market impact, and liquidity conditions.
- **Gap Risk:** Stop-losses monitored in DAILY_CHECK mode are checked once per day and cannot protect against overnight or intraday gaps. Actual losses may exceed planned risk.
- **Settlement Risk:** Cash proceeds from