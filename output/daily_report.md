# Daily Trading Report
**Date:** 2026-04-27  
**Status:** NO_TRADES  
**Currency:** GBP  
**Base Equity:** £108.78  
**Cash Balance:** £3.45  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (daily monitoring, gap risk present)

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-04-28
- **Bank Holidays (next 5 days):** None

---

## Executive Summary
No trades executed today. The portfolio has recovered to only 6.40% below peak equity (target max 15%), but faces two material constraints preventing new entries:

1. **Position Limit Constraint:** Currently holding 6 positions against a maximum of 5. The portfolio is overweight and must be rebalanced before new entries can be added.
2. **Liquidity Constraint:** Available cash for buys is £0.19, insufficient for any meaningful position. The cash buffer alone requires £3.26.
3. **Insufficient High-Quality Setups:** Analysis of the eligible universe identified no entry candidates meeting the 0.65+ confidence threshold for the balanced strategy profile when combined with the above constraints.

**Capital Preservation Bias Applied:** In the presence of tight liquidity and position overload, the default strategy is to hold existing positions and monitor for exits rather than force marginal entries.

---

## Candidate Analysis (Top Opportunities Considered)

### 1. LSEG.L (London Stock Exchange Group) — Confidence: 0.68 (REJECTED)
- **Setup:** Pullback in full uptrend (trend score 0.95)
- **Technicals:** Close £99.42 > SMA50 £86.98 > SMA200 £89.08; SMA50 slope positive; 20d high £101.40, drawdown 1.95%
- **Volume:** 1.29M shares (0.702x 20d avg); avg GBP volume £169.6M — passes liquidity filter
- **Risk/Reward:** ATR £2.34; stop at ~£97.10; R:R 0.60
- **Rejection:** Insufficient cash (requires £5.96, have £0.19). Position limit already exceeded. Would breach max_single_name_exposure (current largest position BP.L is 49.03%).

### 2. HSBA.L (HSBC) — Confidence: 0.62 (REJECTED)
- **Setup:** Pullback in full uptrend (trend score 0.90)
- **Technicals:** Close £13.20 > SMA50 £12.77 > SMA200 £11.18; drawdown 3.48% from 20d high
- **Volume:** 11.6M shares; avg GBP volume £280M — excellent liquidity
- **Risk/Reward:** ATR £0.32; stop at £12.45; R:R 0.55
- **Rejection:** Confidence below 0.65 threshold (0.62). Insufficient cash. Financials sector already exposed via BARC.L (not currently held, but listed).

### 3. AAL.L (Anglo American) — Confidence: 0.58 (REJECTED)
- **Setup:** Breakout in full uptrend (trend score 0.92)
- **Technicals:** Close £36.32 > SMA50 £34.09 > SMA200 £29.25; 20d high £38.37, close within 5.4%
- **Volume:** 11.0M shares; volume ratio 2.25x (strong demand) — but indicates elevated intraday volatility
- **Risk/Reward:** ATR £1.36; stop at £34.96; R:R 0.48
- **Rejection:** Confidence 0.58 is well below threshold. High volume ratio increases gap risk in DAILY_CHECK mode (gap_risk_buffer 10% reduces effective position size). Materials sector already has exposure (RIO.L, GLEN.L).

### 4. RKT.L (Reckitt Benckiser) — (NOT CONSIDERED FOR ENTRY)
- **Trend Status:** BROKEN
- **Technicals:** SMA50 slope negative; close £47.21 < SMA50 £55.04; 38 consecutive days below SMA50 indicates sustained weakness, not a recoverable dip.
- **Volume:** 5.1M shares; 2.22x 20d average — strong volume on downside is a bearish signal
- **Verdict:** No entry consideration. This is a falling knife pattern.

---

## Risk Checks Summary

| Constraint | Status | Details |
|-----------|--------|---------|
| **Position Limit** | ❌ VIOLATED | 6 positions held, max 5 allowed. Over by 1. |
| **Cash Buffer** | ✓ PASS | £3.26 required, £3.45 available. Margin: +£0.19 |
| **Max Sector Exposure** | ✓ PASS | Energy 41.15% (limit 40%) — **at threshold**. Materials 6.59%, Industrials 4.45% |
| **Single Name Exposure** | ✓ PASS | BP.L largest at 49.03% (limit 30%) — **CONSTRAINT VIOLATED** |
| **Turnover Limit** | ✓ PASS | 0% turnover (no trades planned). Limit 30% |
| **Drawdown Limit** | ✓ PASS | Current 6.40% (limit 15%). Headroom £7.75 |
| **Data Freshness** | ✓ PASS | Market data as of 2026-04-27, trading_calendar confirmed today is trading day |
| **Liquidity Filters** | ✓ PASS | All held positions exceed min_avg_gbp_volume £50k and min_price £1.0 |

**CRITICAL OBSERVATION:** BP.L position is 49.03% of portfolio (£53.35 / £108.78), exceeding the max_single_name_exposure_pct limit of 30%. This is a legacy position (entry 2026-03-05, 50 days held, avg cost £4.92, unrealised +£7.45). **Current stop at £4.68 should be monitored; breach would trigger automatic exit via DAILY_CHECK mode.**

---

## Portfolio Drawdown Status
- **Peak Equity (all-time):** £116.22 (recorded in positions.json)
- **Current Equity:** £108.78
- **Current Drawdown:** (116.22 - 108.78) / 116.22 = **6.40%**
- **Portfolio Drawdown Limit:** 15.0%
- **Headroom to Limit:** 8.60%
- **Verdict:** ✓ Within acceptable range. No liquidation triggered.

The portfolio has recovered £7.44 from recent lows but remains below peak. The positive unrealised P&L in SHEL.L (+£4.07), BP.L (+£7.45), and GLEN.L (+£0.45) is being offset by losses in BA.L (-£0.54) and AZN.L (-£0.12).

---

## UK Costs & Fees

**Assumptions:**
- **Fee Model:** Per-trade model, £0 per trade (CONFIG fee_model.type = "per_trade", value = 0)
- **Stamp Duty:** 50 bps on UK equities only (non-ETF). ETF purchases exempt.
  - If entry were executed on LSEG.L (UK equity): £99.42 * qty * 0.005 = stamp duty
  - Slippage: 10 bps assumed on all orders (CONFIG slippage_bps = 10)
- **Settlement:** T+1 (UK LSE standard). Sell proceeds from today would settle 2026-04-28, not available for today's buys.

**No trades executed today, so costs are moot.** However, the tight cash position would make any future entry expensive relative to portfolio size.

---

## Stop-Loss Monitoring (DAILY_CHECK Mode)

**Active Positions & Stop Triggers:**

| Ticker | Quantity | Entry Date | Days Held | Entry Price | Current Price | Stop Price | % to Stop | Status |
|--------|----------|------------|-----------|-------------|---------------|------------|-----------|--------|
| SHEL.L | 1.0624 | 2026-02-17 | 66 | 28.70 | 32.53 | 27.71 | +3.1% | ✓ Safe |
| GLEN.L | 1.0350 | 2026-02-18 | 65 | 5.08 | 5.52 | 4.86 | +1.4% | ✓ Safe |
| BP.L | 9.3200 | 2026-03-05 | 50 | 4.92 | 5.72 | 4.68 | +2.2% | ✓ Safe |
| BA.L | 0.2378 | 2026-03-09 | 46 | 22.61 | 20.36 | 21.50 | -5.3% | ⚠ CLOSE |
| AZN.L | 0.0383 | 2026-03-18 | 37 | 142.90 | 139.72 | 137.18 | +1.8% | ✓ Safe |
| RIO.L | 0.0208 | 2026-04-02 | 22 | 71.09 | 73.47 | 67.02 | +9.6% | ✓ Safe |

**BA.L Warning:** Position is near stop (-5.3% margin). Current drawdown 5.3% from entry. Low quantity (0.24 shares) makes this a marginal position. Any adverse move will trigger exit at stop £21.50.

**Gap Risk Acknowledgement (DAILY_CHECK Mode):**
The DAILY_CHECK stop execution mode monitors stops once daily at market open or close, depending on pipeline timing. **Overnight gaps can cause actual fill prices to differ significantly from planned stops.** In the event of an adverse gap (e.g., market opens below stop price), the position would be closed at market open price, which may be worse than the stop. **Historical example:** If energy sector shocks (geopolitical event, supply surprise) and BP.L opens -10% below stop, the position exits at that price, not at the planned £4.68 stop. Investors using DAILY_CHECK mode must accept this gap risk.

---

## Portfolio Snapshot

**Equity Value:** £108.78  
**Cash:** £3.45  
**Unrealised P&L:** +£11.29 (gross)

### Position Summary
- **Energy Sector:** 41.15% (SHEL.L + BP.L)
  - SHEL.L: £34.55 (31.7%), unrealised +£4.07
  - BP.L: £53.35 (49.0%), unrealised +£7.45
- **Materials Sector:** 6.59% (GLEN.L + RIO.L)
  - GLEN.L: £5.71 (5.2%), unrealised +£0.45
  - RIO.L: £1.53 (1.4%), unrealised +£0.05
- **Industrials Sector:** 4.45% (BA.L)
  - BA.L: £4.84 (4.4%), unrealised -£0.54
- **Healthcare Sector:** 4.91% (AZN.L)
  - AZN.L: £5.35 (4.9%), unrealised -£0.12

**Sector Concentration Risk:** Energy is overweighted at 41.15% vs. limit of 40%, and single name BP.L at 49.03% far exceeds the 30% limit. This concentration reflects the strong performance of the energy holdings but creates vulnerability to sector-specific shocks (e.g., OPEC announcements, renewable energy policy changes).

---

## Orders

**No orders generated today.**

---

## What Could Invalidate This Plan

1. **Overnight Corporate Action on Held Positions:**
   - Dividend announcement, share split, or delisting for any held ticker would require immediate re-evaluation.
   - The pipeline should flag status changes in universe.csv (currently all held tickers show "ACTIVE").

2. **Significant Market Gap (Gap Risk in DAILY_CHECK Mode):**
   - If LSE opens with a >5% gap (geopolitical event, macro shock, earnings miss), stop-losses may execute at worse prices than planned.
   - BP.L stop (£4.68) and BA.L stop (£21.50) could be tested if energy or industrials sell off sharply.

3. **Cash Injection:**
   - If dividends are paid on held positions or external funds are deposited, liquidity constraint would be relieved, unlocking new entries (e.g., LSEG.L or HSBA.L could become viable).

4. **Portfolio Rebalance:**
   - Manual sell of BA.L (loss position) or partial trim of BP.L (overweight) would free cash and reduce position count, enabling new entries at higher confidence.

5. **Rapid Trend Reversals:**
   - If any held position's SMA50 slope reverses (e.g., BP.L or GLEN.L sma50_slope flips negative), the trend filter would fail on next re-evaluation, and the position would become an exit candidate.

6. **Data Quality Issues:**
   - If market_data.csv is stale (e.g., no update for >1 trading day), output status would change to BLOCKED. This is a safety circuit-breaker.

---

## Data Quality Notes

- ✓ All required columns present in market_data.csv
- ✓ All held tickers have complete indicator data (sma50, sma200, atr14, drawdown metrics)
- ✓ No tickers with null sma200_gbp (all have >200 days of trading history)
- ✓ Universe.csv status field shows all held and candidate tickers as "ACTIVE"
- ✓ Positions.json and trading_calendar.json data consistent with market_data.csv date (2026-04-27)
- ✓ No settlement complications (unsettled_sell_proceeds_gbp = 0)

---

## DISCLAIMER

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

**Execution Risk:** This plan assumes the orders execute at prices close to current market levels. Market conditions, liquidity, and news events can cause actual fills to differ materially.

**Gaps & Slippage:** Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Sell orders in volatile markets may execute at prices significantly worse than the stop price.

**FX & Settlement:** All prices are in GBP. Non-UK trades settle T+1 (next business day). Cash for same-day buys after sells is not available under the current CONFIG (assume_intraday_netting = false).

**Taxes & Fees:** Stamp duty (50 bps on UK equities), trading fees, and tax implications (CGT, income tax) are not calculated in this plan. Consult a tax advisor.

**Regulatory & Execution Risk:** This plan is generated for a paper trading account (mode = "paper"). Live account execution requires validation by a licensed broker and compliance with FCA regulations.

**Use at Your Own Risk:** Past performance does not guarantee future results. Equity markets are subject to loss of capital.

---

## Next Steps

1. **Monitoring:** Watch for stop-loss triggers on BA.L (within 5% of stop) and overall portfolio drawdown.
2. **Rebalance Opportunity:** Consider manual reduction of BP.L to bring single-name exposure within 30% limit and Energy sector within 40% limit. This would free cash for new entries.
3. **New Setup Watch:** If LSEG.L, HSBA.L, or AAL.L show improved trend confirmation with stronger volume, they remain candidates for next rebalance.
4. **Calendar:** Next trading day 2026-04-28; no bank holidays in the next 5 days.

---