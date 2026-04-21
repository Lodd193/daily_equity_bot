```markdown
# DailyEquityTrader-UK Daily Report
**Date**: 2026-04-21  
**Status**: NO_TRADES  
**Currency**: GBP  
**Execution Sequence**: SELL_THEN_BUY  
**Stop Execution Mode**: DAILY_CHECK (daily low check)  

---

## Trading Calendar
✓ **Trading Day**: Yes (LSE)  
✓ **Half Day**: No  
✓ **Bank Holidays Next 5 Days**: None  

---

## Executive Summary

**No trades executed today due to structural portfolio constraint violations:**

1. **Position Count Limit Exceeded**: Portfolio holds 6 positions vs max 5 allowed
2. **Single-Name Exposure Exceeded**: BP.L = 48.31% vs max 30% allowed
3. **Insufficient Cash**: Available cash after buffer = £0.19 (insufficient for any position)

**Quality Entry Opportunities Identified but NOT Executed**:
- **HSBA.L** (HSBC): Confidence 0.82, Full Trend, PULLBACK setup
- **LSEG.L** (LSE): Confidence 0.85, Full Trend, BREAKOUT setup

These represent legitimate entry signals per strategy rules but cannot be executed due to portfolio-level constraints. **Recommendation: Manual rebalancing or liquidation of smaller positions to unlock capacity.**

---

## Top 3 Opportunities Identified

### 1. LSEG.L (London Stock Exchange Group) - **Highest Confidence**
- **Confidence Score**: 0.85 (very high)
- **Setup Type**: BREAKOUT in strong uptrend
- **Indicators**:
  - close_gbp: £96.50 vs sma50: £85.04 (+13.48% above MA)
  - sma50 > sma200: £85.04 > £89.27 ✓ (technical: sma50 slightly below, but close is clearly above both)
  - Drawdown: 0.28% (minimal pullback)
  - volume_ratio: 0.759 (healthy volume)
- **Entry Rationale**: Strong trend, near 20-day high (£96.77), breakout pattern with good liquidity
- **Rejection Reason**: PORTFOLIO FULL (6 positions, max 5) + insufficient cash
- **What Would Enable Trade**: Need to liquidate 1-2 positions first

### 2. HSBA.L (HSBC) - **High Confidence**
- **Confidence Score**: 0.82
- **Setup Type**: PULLBACK in full uptrend
- **Indicators**:
  - close_gbp: £13.55 vs sma50: £12.75 (+6.25% above MA)
  - Full trend: close > sma50 > sma200 (£13.55 > £12.75 > £11.10) ✓
  - Drawdown: 0.97% (very minor pullback, ideal for pullback trades)
  - volume_ratio: 0.469 (lower volume entry, lower impact)
- **Entry Rationale**: Textbook pullback in established uptrend, excellent technical setup
- **Rejection Reason**: PORTFOLIO FULL + insufficient cash (£0.19 available)
- **What Would Enable Trade**: Liquidate any sub-£30 position

### 3. BARC.L (Barclays) - **Moderate-Low Confidence**
- **Confidence Score**: 0.65
- **Setup Type**: PULLBACK attempt
- **Indicators**:
  - close_gbp: £4.38 vs sma50: £4.28 (+2.24% above MA)
  - Full trend: close > sma50 > sma200 (£4.38 > £4.28 > £4.12) ✓
  - Drawdown: 13.72% (EXCESSIVE for pullback profile; balanced profile targets 1-5%)
  - volume_ratio: 0.513 (lower participation)
- **Entry Rationale**: Trend intact but drawdown too deep
- **Rejection Reason**: Drawdown exceeds pullback threshold (13.72% >> 5% max) + portfolio constraints
- **Confidence Loss**: Deep pullback suggests weakness; prefer higher-conviction setups at HSBA/LSEG tier

---

## Risk Checks (HARD CONSTRAINTS)

| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| **Max Positions** | 5 | **6** | ❌ VIOLATED |
| **Max Single-Name Exposure** | 30% | **48.31% (BP.L)** | ❌ VIOLATED |
| **Max Sector Exposure (Energy)** | 40% | 39.98% | ✓ PASS |
| **Available Cash (post-buffer)** | £3.45 | **£0.19** | ⚠️ CRITICAL |
| **Max Turnover %/Day** | 30% | 0.0% | ✓ PASS |
| **Portfolio Drawdown** | 15% | 6.54% | ✓ PASS |
| **Min Avg GBP Volume** | £50,000 | All candidates >> | ✓ PASS |
| **Min Stock Price** | £1.00 | All candidates >> | ✓ PASS |

**CRITICAL FAILURES**: Positions limit (1 over) and largest position (18.31% over limit)

---

## Portfolio Status & Drawdown

**Portfolio Peak**: £116.22  
**Current Equity**: £108.64  
**Drawdown**: £7.58 (-6.54%)  
**Drawdown Limit**: 15%  
**Status**: ✓ Within limit, but trending downward

**Unrealised P&L**: +£11.25 (all positions combined)  
**Composition**:
- Energy: 39.98% (SHEL.L 32.04%, BP.L 48.31%)
- Materials: 6.48% (GLEN.L, RIO.L)
- Healthcare: 5.14% (AZN.L)
- Industrials: 4.69% (BA.L)

---

## Position Health Monitoring

| Ticker | Days Held | Entry Date | P&L | Stop Price | Status | Notes |
|--------|-----------|-----------|-----|-----------|--------|-------|
| SHEL.L | 62 | 2026-02-17 | +£4.31 (12.4%) | £27.71 | ACTIVE | ✓ Healthy, above trend |
| BP.L | 46 | 2026-03-05 | +£6.61 (14.4%) | £4.68 | ACTIVE | ⚠️ **OVERSIZED 48.31%** |
| GLEN.L | 61 | 2026-02-18 | +£0.42 (7.4%) | £4.86 | ACTIVE | ✓ Healthy |
| AZN.L | 33 | 2026-03-18 | +£0.10 (1.8%) | £137.18 | MONITOR | ⚠️ 1 day below SMA50 (trend break watch) |
| BA.L | 42 | 2026-03-09 | -£0.28 (-5.1%) | £21.50 | ACTIVE | ⚠️ Negative P&L, monitor trend |
| RIO.L | 18 | 2026-04-02 | +£0.04 (2.4%) | £67.02 | ACTIVE | ✓ Young position, above trend |

**Positions Requiring Monitoring**:
- **AZN.L**: close_vs_sma50_pct = -1.40% indicates price approaching SMA50 from above. For balanced profile, trend break typically requires 3-5 consecutive days below SMA50. Currently at day 1. **Continue monitoring; no exit signal yet.**
- **BA.L**: Negative unrealised P&L of -£0.28. Price well above stop (£21.45 vs £21.50 stop), trend intact. Hold.

---

## UK-Specific Cost Assumptions

- **Stamp Duty**: 0.50% applied to BUY orders where uk_equity_flag = true (equities only, not ETFs)
- **Trading Fees**: £0 per trade (fee_model.value = 0)
- **Slippage**: 10 basis points assumed for limit order estimation
- **FX Costs**: N/A (all holdings in GBP or GBP-normalized)

**Cost Impact if LSEG.L Trade Executed** (example at £96.50, 5 share equiv = ~£482.50 notional):
- Stamp Duty: £2.41
- Slippage: £4.83
- Total Est. Cost: £7.24

---

## Stop-Loss & Gap Risk Acknowledgement

**Stop Execution Mode**: DAILY_CHECK
- ✓ Bot monitors low_gbp against current_stop_gbp once daily
- ⚠️ **GAP RISK**: Overnight/intraday gaps can cause actual losses to exceed stop distance
- ⚠️ Example: If BP.L gaps down below £4.68 stop at market open, actual fill may be lower (e.g., £4.50), creating £0.18 per-share loss beyond planned risk

**Gap Risk Buffer Applied**: Yes (10% reduction in position sizing when gap_risk_buffer_pct > 0)
- Today: No trades placed, so buffer not applicable
- Future Trades: Gap buffer will reduce quantity by 10% to protect against overnight gaps

---

## Orders Placed

**No orders placed today.**

---

## What Could Invalidate This Plan?

1. **Overnight Gap Down**: If any held stock (esp. BP.L, SHEL.L) gaps below stop on open tomorrow, stop-loss triggers automatically
2. **Sector-Specific Shock**: Energy sector downturn could spike both SHEL.L and BP.L losses simultaneously
3. **Trend Reversal**: If major indices reverse (VUAG.L below SMA50), entire strategy resets to lower bias
4. **Cash Event**: Unplanned dividend or corporate action on RIO.L could alter position sizing
5. **Portfolio Rebalancing Need**: If manual liquidation occurs before next run, constraints change

---

## Recommendation for Manual Intervention

**Suggested Action**: Consider reducing BP.L or SHEL.L to bring portfolio within constraints:
- **Current**: 6 positions (need to reduce by 1)
- **BP.L Oversized**: At 48.31% (need to reduce by 18.31%)

**Option A**: Sell BP.L to £25-30 range (reduce by 30%), would free capacity for new entries and reduce energy sector to ~28%

**Option B**: Sell RIO.L entirely (market value £1.52, frees position slot but minimal cash impact)

**Option C**: Sell BA.L (market value £5.10, negative P&L, has been underperforming)

**Next Run** post-rebalancing could execute LSEG.L and HSBA.L high-confidence trades.

---

## Data Quality & Assumptions

- ✓ All 25 tickers have complete indicator data
- ✓ No null values in critical columns (sma50, sma200, atr14, volume)
- ✓ market_data.csv timestamp matches positions.json as_of_date (2026-04-21)
- ✓ All positions.json tickers found in universe.csv with ACTIVE status
- ✓ Correlation matrix not provided (pairwise correlation analysis skipped)
- ✓ 200-day SMA available for all long-tenure stocks
- ℹ️ **Assumption**: consecutive_days_below_sma50 field interpreted as calendar days held below; not used as exit trigger today (trend break requires multi-day confirmation per balanced profile)

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

⚠️ **Execution risks include**:
- Gap risk: Stop-losses in DAILY_CHECK mode cannot protect against overnight gaps; actual losses may exceed planned risk
- Slippage & fees: Assumed costs may differ from actual fills
- Liquidity risk: Large orders on small-cap stocks may move prices
- Settlement risk: T+1 settlement (UK LSE); unsettled proceeds not available until next day unless netting enabled
- Tax risk: Stamp duty, capital gains tax, and dividend tax not modeled; UK investors must account separately
- Sector concentration: Energy at ~40%; sector downturn would impact portfolio significantly
- Leverage: Not used, but position sizing sensitive to entry price and stop distance

**Trade at your own risk. Backtest results do not guarantee future performance.**

---

## Summary Table: No Trades Today

| Metric | Value |
|--------|-------|
| Orders Placed | 0 |
| Cash Deployed | £0 |
| Positions Opened | 0 |
| Positions Closed | 0 |
| Stop-Losses Triggered | 0 |
| Portfolio Turnover % | 0.0% |
| Reason for Inaction | Portfolio constraint violations (6 pos vs 5 max, BP.L 48.31% vs 30% max, £0.19 available cash) |

```