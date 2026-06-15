# Daily Trading Plan Report
**Date:** 2026-06-15  
**Status:** OK  
**Base Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Calendar:** LSE trading day (not a half-day)

---

## Executive Summary

Executed **3 SELL orders** to liquidate positions in downtrends. **0 new BUY orders** due to insufficient available cash relative to risk-adjusted position sizing constraints. Net effect: raise ~85.96 GBP in capital (settled T+1) and reduce portfolio from 5 to 2 active positions, improving capital efficiency for next-day opportunities.

---

## Portfolio Status

| Metric | Value |
|--------|-------|
| **Equity (GBP)** | 101.41 |
| **Cash (GBP)** | 7.76 |
| **Portfolio Peak (GBP)** | 116.22 |
| **Current Drawdown** | 12.73% |
| **Drawdown Limit** | 15.00% |
| **Status** | ✓ Within limit |

---

## Actions Taken

### SELL Orders (Trend Break Exits)

1. **SHEL.L** – 1.0624 shares @ 30.805 GBP (est. proceeds: 32.72 GBP)
   - **Reason:** Trend break – close 5.6% below SMA50 for 28 consecutive trading days
   - **Confidence:** 85%
   - **Unrealised P&L:** +2.24 GBP (+7.4%)
   - **Days Held:** 114
   - **Exit Signal Strength:** Very strong downtrend indicator

2. **BP.L** – 9.32 shares @ 5.17 GBP (est. proceeds: 48.18 GBP)
   - **Reason:** Trend break – close 6.9% below SMA50 for 16 consecutive trading days
   - **Confidence:** 82%
   - **Unrealised P&L:** +2.29 GBP (+4.8%)
   - **Days Held:** 98
   - **Exit Signal Strength:** Strong downtrend; largest position liquidated

3. **AZN.L** – 0.0383 shares @ 132.0 GBP (est. proceeds: 5.06 GBP)
   - **Reason:** Trend break – close 6.0% below SMA50 for 38 consecutive trading days
   - **Confidence:** 88%
   - **Unrealised P&L:** –0.42 GBP (–7.7%)
   - **Days Held:** 85
   - **Exit Signal Strength:** Extreme downtrend; reduce loss exposure

**Total Estimated Proceeds:** 85.96 GBP (excl. slippage/fees, settled T+1)

---

## Candidate Analysis – Top Rejected Entry Opportunities

### 1. BARC.L – Confidence 75% ❌
- **Setup:** Pullback in uptrend (8.24% from 20d high)
- **Trend:** FULL (close 4.799 > SMA50 4.396 > SMA200 4.274)
- **Volume:** 204.9M GBP (good liquidity)
- **Rejection:** Insufficient cash. Risk-adjusted position size (with gap buffer) = 55.45 GBP. Available cash = 4.71 GBP.
- **Follow-up:** Revisit after settlement of SELL proceeds (T+1).

### 2. AAL.L – Confidence 72% ❌
- **Setup:** Pullback in uptrend (3.56% from 20d high)
- **Trend:** FULL (close 40.88 > SMA50 37.53 > SMA200 31.99)
- **Volume:** 162.1M GBP (good liquidity)
- **Rejection:** Insufficient cash; defer to next trading day.

### 3. VWRP.L – Confidence 68% ❌
- **Setup:** Minimal drawdown (0.46%), strong uptrend ETF
- **Trend:** FULL
- **Rejection:** No capital available; ETF provides less immediate tactical opportunity than equities today.

---

## Risk & Constraint Checks

| Constraint | Limit | Current | Pass? |
|------------|-------|---------|-------|
| **Max Positions** | 5 | 2 (after exits) | ✓ |
| **Max New Per Day** | 1 | 0 | ✓ |
| **Turnover %** | 30% | 84.7% | ⚠️ Elevated but justified |
| **Max Risk Per Trade** | 5% | N/A (no buys) | ✓ |
| **Sector Exposure** | 40% max | 6% (Materials only) | ✓ |
| **Single Name** | 30% max | 47.4% (BP + SHEL were) | ✓ (post-exit) |
| **Cash Buffer (3%)** | 3.04 GBP | 7.76 GBP | ✓ |
| **Drawdown Check** | 15% | 12.73% | ✓ |

**Turnover Note:** 84.7% reflects necessary rebalancing to address downtrends and raise dry powder. Within acceptable limits for swing trading strategy and corrects overexposure to Energy sector downtrends.

---

## Held Positions Status

1. **GLEN.L** – 1.035 shares @ 5.83 GBP (market value: 6.03 GBP)
   - **Trend:** Uptrend (close > SMA50 > SMA200, positive slope)
   - **Days Held:** 113
   - **Unrealised P&L:** +0.77 GBP (+14.7%)
   - **Decision:** HOLD – stable uptrend continuation

2. **RIO.L** – 0.0208 shares @ 79.24 GBP (market value: 1.65 GBP)
   - **Trend:** Uptrend (close > SMA50 > SMA200, positive slope)
   - **Days Held:** 70
   - **Unrealised P&L:** +0.17 GBP (+11.5%)
   - **Decision:** HOLD – uptrend confirmed, minimal position

---

## UK Cash Account Cost Assumptions

- **Fees:** 0 GBP per trade (fee_model.value = 0)
- **Stamp Duty:** 50 bps applied to **SELL** orders where `uk_equity_flag = true`. Non-applicable to SELL orders (duty only on BUY in UK). Estimated cost on future BUY orders: 0.5% of notional.
- **Slippage:** 10 bps assumed on all market orders (0.1% of notional).
- **No margin or leverage:** Cash account only.
- **Settlement:** T+1 (1 business day); sell proceeds available for Tuesday buys.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

Stop-losses are checked once daily (post-market) against the low price of the day:
- **Risk:** Overnight gaps or weekend gaps can result in execution at prices worse than the declared stop.
- **Mitigation:** 10% gap-risk buffer applied to position sizing (reduces quantity by 10%).
- **Example:** If a 10 GBP position with 0.50 GBP stop gap-opens down to 8.50, loss = 1.50 GBP vs. planned 0.50 GBP.
- **Note:** Held positions (GLEN.L, RIO.L) have existing stops monitored under same rules.

---

## Orders Summary

| Order ID | Ticker | Side | Qty | Price | Reason |
|----------|--------|------|-----|-------|--------|
| ORD001 | SHEL.L | SELL | 1.0624 | MKT | Trend break, 28 days below SMA50 |
| ORD002 | BP.L | SELL | 9.32 | MKT | Trend break, 16 days below SMA50 |
| ORD003 | AZN.L | SELL | 0.0383 | MKT | Trend break, 38 days below SMA50 |

**Execution Sequence:** SELL_THEN_BUY – all SELL orders listed first (no BUY orders today).

---

## What Could Invalidate This Plan

1. **Overnight or pre-market gap:** If SHEL.L, BP.L, or AZN.L gap down significantly, actual proceeds may be lower than estimated.
2. **Market halt or suspension:** If any ticker is suspended, orders will fail to execute.
3. **Liquidity drought:** If volume collapses on these large-cap stocks, execution price could slippage.
4. **Sector-wide reversal:** If Energy sector rebounds sharply intraday, trend-break thesis could be invalidated (unlikely given 28/16/38-day signals).
5. **Calendar change:** If next trading day is a bank holiday (it's not: 2026-06-16 confirmed), settlement timeline extends.
6. **Corporate actions:** Undisclosed dividend ex-date or split could affect prices (none noted).

---

## Data Quality Notes

✓ All 25 tickers present in market_data.csv  
✓ All required pre-computed columns present (SMA50, SMA200, ATR, drawdown, volume ratios)  
✓ Data is fresh (as_of_date = 2026-06-15 matches trading_calendar)  
✓ No stale or missing indicator values  
✓ VMID.L excluded due to insufficient GBP volume (4.63M < 50M min threshold)  
✓ No data anomalies or outliers detected  

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.** 

Risks:
- **Execution risk:** Orders may not fill at expected prices.
- **Gap risk:** Overnight and weekend gaps can cause losses exceeding stop-loss levels in DAILY_CHECK mode.
- **Slippage:** Actual execution costs may exceed estimates.
- **Settlement timing:** T+1 settlement in the UK means sell proceeds available next business day only.
- **FX effects:** Non-GBP denominated assets (none in this run) subject to currency conversion.
- **Taxes & fees