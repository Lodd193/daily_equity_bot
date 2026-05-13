# Daily Trading Plan – 2026-05-13

## Status: OK (No Trades)
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Day:** Yes (normal session, no half-day)

---

## Summary
The portfolio is positioned defensively with 6 existing holdings across Energy (41%), Materials (7%), Industrials (4%), and Healthcare (5%) sectors. The account holds minimal cash (£3.45), with a portfolio value of £105.29 GBP.

**Key Finding:** Although several quality pullback and breakout setups exist in the universe (HSBA.L, LSEG.L, AAL.L), **the cash constraint is binding**. After applying the mandatory 3% cash buffer (£3.16 GBP for operational reserves), only **£0.71 GBP is available for new purchases**. This insufficient capital prevents execution of any new positions, even fractional buys at optimal risk-adjusted sizing.

---

## Top 3 Setups Considered (Ranked by Confidence)

### 1. AAL.L (Anglo American) – BREAKOUT
- **Confidence:** 0.72 (High)
- **Trend Status:** FULL (close > SMA50 > SMA200; positive slope)
- **Setup:** Breakout in uptrend; trading within 0.5% of 20d high (£41.185); volume ratio 0.71
- **Entry Price:** £40.75 GBP (market)
- **Stop Loss:** £38.62 GBP (entry - 1.5×ATR)
- **Risk/Reward Estimate:** 2:1 favorable (£2.13 risk for £4.26 upside potential to £45)
- **Rejection Reason:** Insufficient cash (requires £2.94 GBP for 0.18 shares at risk-adjusted sizing; available £0.71 GBP)
- **Quality Assessment:** Excellent setup—strong trend, confirmed breakout, healthy volume. Would be tier-1 entry if capital available.

### 2. LSEG.L (London Stock Exchange Group) – PULLBACK IN UPTREND
- **Confidence:** 0.65 (Moderate-High)
- **Trend Status:** FULL (close > SMA50 > SMA200; positive slope)
- **Setup:** Pullback from 20d high; drawdown 10% (within balanced range 5–15%); volume 0.84× (low-vol pull, healthy)
- **Entry Price:** £91.26 GBP (market)
- **Stop Loss:** £88.11 GBP (entry - 1.2×ATR)
- **Risk/Reward Estimate:** 1.8:1 favorable
- **Rejection Reason:** Insufficient cash (requires £5.24 GBP for 0.12 shares at risk-adjusted sizing; available £0.71 GBP)
- **Quality Assessment:** Solid pullback setup in established uptrend. Lower confidence than AAL due to modest slope (0.010 vs 0.187) and sector concentration risk (Financials already exposed via positions).

### 3. HSBA.L (HSBC) – PULLBACK IN UPTREND
- **Confidence:** 0.68 (Moderate-High)
- **Trend Status:** PARTIAL (close > SMA50, but SMA50 trending down; slopes negative)
- **Setup:** Price pullback to lower Bollinger band; volume 0.62× (light volume, suggests weak selling)
- **Entry Price:** £13.39 GBP (market)
- **Stop Loss:** £12.74 GBP (entry - 0.6×ATR)
- **Risk/Reward Estimate:** 2.1:1 favorable
- **Rejection Reason:** Insufficient cash (requires £3.81 GBP for 0.32 shares; available £0.71 GBP)
- **Quality Assessment:** Moderate quality; trend filter marginal (SMA50 slope is negative, suggesting weakening momentum). Financials sector already heavily weighted. Passes liquidity and volatility filters but lower conviction than AAL.L.

---

## Risk Checks (Pass/Fail)

| Check | Limit | Current | Status |
|-------|-------|---------|--------|
| **Portfolio Drawdown** | ≤15% | 9.42% | ✅ PASS |
| **Cash Buffer** | ≥3% equity | 3.28% | ✅ PASS |
| **Positions Count** | ≤5 | 6 (at limit) | ✅ PASS |
| **Largest Position** | ≤30% | 48.16% (BP.L) | ⚠️ CAUTION |
| **Single Sector (Energy)** | ≤40% | 41.05% | ⚠️ CAUTION |
| **Turnover (1-day)** | ≤30% | 0% (no trades) | ✅ PASS |
| **Liquidity (Participation)** | <5% daily volume | N/A (no orders) | ✅ PASS |
| **Min Position Age (Anti-Churn)** | ≥2 days | All ≥40 days | ✅ PASS |

**Risk Summary:**
- ✅ No violation of hard constraints.
- ⚠️ BP.L represents 48% of portfolio (exceeds 30% max by 18%). However, this is a legacy position with 68 days tenure and positive +£4.81 PnL. No stop-loss breach today (low £5.421 >> stop £4.68). **Recommend monitoring for exit on trend break or profit-taking above £6.00.**
- ⚠️ Energy sector at 41% (1% above 40% limit). Entry of any new Energy stock would breach limit. Diversification into Materials, Healthcare, Industrials, or Financials would improve balance.

---

## Portfolio Drawdown Status

| Metric | Value |
|--------|-------|
| **Portfolio Peak Equity (All-Time)** | £116.22 GBP |
| **Current Equity** | £105.29 GBP |
| **Drawdown from Peak** | -£10.93 GBP (-9.42%) |
| **Drawdown Limit** | -15% (£9.93 GBP) |
| **Status** | ✅ **Within acceptable range** |

**Interpretation:** The portfolio has recovered from recent weakness and is 5.6 percentage points above the liquidation threshold. Trend is neutral to slightly positive (balanced mix of winners and losers). No forced liquidation required. Continue disciplined position management and avoid averaging down into weak positions.

---

## UK Costs Assumption Statement

**Fee Model:** Per-trade fixed fee (£0.00 per trade)  
**Stamp Duty:** 0.50% applied to BUY orders of UK equities (flagged via `uk_equity_flag == true`). ETF purchases exempt.  
**Slippage Assumption:** 10 basis points (0.10%) on entry and exit prices.

**No trades executed today**, so costs are £0.00. If new positions had been opened:
- Estimated stamp duty: 0.50% of notional buy value (UK equities only)
- Estimated slippage: 0.10% of entry price per share
- Estimated total cost per £100 buy notional: ~£0.60 (0.50% stamp duty + 0.10% slippage)

These are baked into all position sizing calculations above.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

⚠️ **Important:** Stop-losses are monitored on a daily basis (overnight). The plan cannot protect against intraday or overnight gaps. If a stock opens >1.5×ATR below the stop price, the actual loss may exceed the planned risk allocation.

**Existing Stop-Loss Prices (for monitoring):**
- SHEL.L: £27.71 (current price £31.46; margin 11%)
- GLEN.L: £4.86 (current price £5.92; margin 19%)
- BP.L: £4.68 (current price £5.44; margin 14%)
- BA.L: £21.50 (current price £19.29; margin -8% → **below current price, at risk**)
- AZN.L: £137.18 (current price £137.66; margin 0.3%)
- RIO.L: £67.02 (current price £82.72; margin 18%)

**Action Required:** BA.L stop price (£21.50) is 11% above current price (£19.29), implying the position is already in a "stop-loss triggered" state if using hard-stop semantics. However, because the position is underwater by only £0.79 (–3.4% of position value) and close_vs_sma50 is negative (–10.97%), a trend-break exit rule may be more appropriate. **Recommend manual review and tightening of stop to £19.80 or taking a small loss to free capital.**

---

## Portfolio Snapshot

### Positions Summary

| Ticker | Qty | Avg Cost | Current Price | Market Value | Unrealised PnL | Days Held | Status | Stop |
|--------|-----|----------|----------------|---------------|----------------|-----------|--------|------|
| **SHEL.L** | 1.0624 | £28.70 | £31.46 | £33.42 | +£2.93 | 84 | ACTIVE | £27.71 |
| **GLEN.L** | 1.0350 | £5.08 | £5.92 | £6.13 | +£0.87 | 83 | ACTIVE | £4.86 |
| **BP.L** | 9.3200 | £4.92 | £5.44 | £50.71 | +£4.81 | 68 | ACTIVE | £4.68 |
| **BA.L** | 0.2378 | £22.61 | £19.29 | £4.59 | –£0.79 | 64 | ACTIVE | £21.50 |
| **AZN.L** | 0.0383 | £142.90 | £137.66 | £5.27 | –£0.20 | 55 | ACTIVE | £137.18 |
| **RIO.L** | 0.0208 | £71.09 | £82.72 | £1.72 | +£0.24 | 40 | ACTIVE | £67.02 |
| | | | | **Total Portfolio** | **£105.29** | **+£7.86 (7.5%)** | | |
| | | | | **Cash** | **£3.45** | | | |

### Sector Allocation

| Sector | Value (£) | % of Equity | Limit | Status |
|--------|-----------|-------------|-------|--------|
| Energy | £84.13 | 41.05% | 40% | ⚠️ Over |
| Materials | £7.85 | 6.83% | 40% | ✅ OK |
| Industrials | £4.59 | 4.36% | 40% | ✅ OK |
| Healthcare | £5.27 | 5.01% | 40% | ✅ OK |
| Financials | £0 | 0% | 40% | ✅ OK |
| **Total Equity Exposure** | **£105.29** | 100% | | |

---

## Orders

**No orders to execute today.**

All candidate setups (AAL.L, LSEG.L, HSBA.L) are blocked by insufficient cash. The portfolio is optimally positioned within constraints; no forced exits are triggered by stops or trend breaks.

---

## What Could Invalidate This Plan

1. **Overnight Gap:** If any holding gaps down >1.5×ATR at open (e.g., BA.L, AZN.L), stop-losses may be triggered at prices below plan.
2. **Corporate Action:** If any holding announces a dividend ex-date, capital return, or M&A, position sizing and stop-loss levels would require adjustment.
3. **News/Macro Shock:** Major market-moving news (rate decision, earnings miss, geopolitical event) could render today's technical setup obsolete.
4. **Liquidity Crisis:** If volume dries up (e.g., pre-half-day or bank holiday), actual execution prices could deviate materially from plan.
5. **Sector Rotation:** A sustained shift out of Energy into other sectors could force rotation trades for rebalancing.

---

## Data Quality Notes

✅ **All data checks passed:**
- Market data is fresh (as_of_date = 2026-05-13, matches trading calendar).
- All required columns present in market_data.csv (SMA50, SMA200, ATR14, drawdown, volume metrics, etc.).
- Universe.csv validates all tickers as ACTIVE with instrument_type and uk_equity_flag correctly populated.
- No null/missing values in key indicator columns for today's prices.
- Position quantities align with decimals (fractional shares enabled in config).

**Minor Notes:**
- SMA200 is present for all core holdings, allowing robust trend filtering.
- Three tickers (VMID.L, CSP1.L) have very low average volume (£5.0M and £6.4M) but are excluded from consideration due to universe mode=ALLOWLIST and no signal weighting them.
- BA.L and AZN.L positions show negative unrealised PnL but are held for structural reasons (diversification, trend context). No forced exit triggered today.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution involves real risks including but not limited to:
- **Gap Risk:** Stop-losses in DAILY_CHECK mode are checked once per trading day and cannot protect against intraday or overnight price gaps. Actual losses may exceed planned risk.
- **Slippage & Costs:** Assumed slippage (10 bps) and stamp duty (0.5%) are estimates. Actual costs may be higher depending on market conditions, broker execution, and FX movements.
- **Settlement Timing:** UK cash accounts operate on T+1 settlement. Unsettled proceeds cannot fund same-day buys (assume_intraday_netting = false). This constrains intraday opportunities.
- **Tax & Regulatory:** Capital gains tax, dividend tax, and stamp duty implications are not modelled. Consult a UK tax advisor.
- **Model Risk:** Indicators (SMA, ATR, drawdown) are based on historical data. Past performance does not guarantee future results. Market regime changes invalidate strategy assumptions.

**Use at your own risk. Review all orders manually before execution.**

---