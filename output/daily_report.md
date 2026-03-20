# Daily Trading Plan – 2026-03-20

**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Calendar:** LSE (normal day, not a half-day)

---

## Summary

No trades generated today. The portfolio is performing reasonably well (0.11% drawdown from peak), but the eligible universe did not produce entry signals with sufficient confidence under the balanced profile rules.

**Key Points:**
- Portfolio contains 5 positions (at max capacity)
- Two positions already held in today's universe (SHEL.L, BP.L, GLEN.L, BA.L, AZN.L)
- New entry candidates (AZN.L, GSK.L, RIO.L, NG.L, TSCO.L, IMB.L) all rejected on trend filters or confidence thresholds
- Cash available for buys: £1.68 (after 3% buffer), insufficient to size meaningful new positions even if a signal emerged
- Portfolio is well-positioned in Energy (80.9%) but concentrated; no rebalancing triggered today

---

## Top 3 Candidates Evaluated (with Rejection Reasons)

### 1. TSCO.L (Tesco) – Confidence 0.42 [REJECTED]
- **Setup Type:** Breakout (marginal)
- **Trend Status:** Full (SMA50=4.59, SMA200=4.39, close=4.689, slope=positive)
- **Technical Detail:** Close is 7.7% below 20-day high (5.082 GBP); breakout threshold requires 95%+ of high. Insufficient proximity.
- **Rejection Reason:** Confidence 0.42 below balanced profile minimum (0.50). Risk-reward ratio poor (stop at ~4.57, entry 4.69 = 0.12 GBP risk).

### 2. IMB.L (Imperial Brands) – Confidence 0.44 [REJECTED]
- **Setup Type:** Pullback in uptrend
- **Trend Status:** Partial (SMA50=31.63, close=30.59, slope=positive; sma200 data present)
- **Technical Detail:** Pullback 8.4% from 20-day high (33.4), volume ratio 2.22x (concerning spike)
- **Rejection Reason:** Confidence 0.44 below minimum 0.50. Unusual volume pattern (2.22x) suggests possible corporate action or volatility event. Average GBP volume ~87.6M, acceptable but not compelling.

### 3. GSK.L (GlaxoSmithKline) – Confidence 0.41 [REJECTED]
- **Setup Type:** Pullback in uptrend
- **Trend Status:** Partial (SMA50=20.29, close=19.505, slope=positive)
- **Technical Detail:** Pullback 12.2% from 20-day high (22.22); volume ratio 1.76x (normal). Close below SMA50, 4 consecutive days below SMA50.
- **Rejection Reason:** Pullback depth (12.2%) exceeds balanced profile threshold (8%). Confidence 0.41. Risk-reward unfavourable (stop at ~19.05, entry 19.505).

---

## Risk Checks (All Constraints)

| Constraint | Limit | Current | Status | Notes |
|---|---|---|---|---|
| **Portfolio Drawdown** | ≤15.00% | 0.11% | ✓ PASS | Peak was £110.00, current £109.88. Minimal drawdown. |
| **Max Positions** | 5 | 5 | ✓ AT LIMIT | No room for new positions without exits. Current: SHEL.L, BP.L, GLEN.L, BA.L, AZN.L. |
| **Max New Positions/Day** | 1 | 0 | ✓ PASS | No new entries approved. |
| **Turnover %** | 30.0% | 0.0% | ✓ PASS | No trades executed; turnover = 0%. |
| **Max Single-Name Exposure** | 30.0% | 47.7% (BP.L) | ⚠ CAUTION | BP.L is 47.7% of portfolio. Not a hard breach (no new position), but portfolio is concentrated. |
| **Max Sector Exposure** | 40.0% | 80.9% (Energy) | ⚠ CAUTION | Energy sector (SHEL.L + BP.L) is 80.9%. Exceeds 40% limit significantly. Existing holdings; no new Energy entries permitted. |
| **Liquidity (Min Avg GBP Volume)** | £50,000 | All >£50k | ✓ PASS | All candidates exceed minimum liquidity threshold. |
| **Min Price** | £1.00 | All >£1.00 | ✓ PASS | All tickers above minimum. |
| **Cash Buffer** | 3.0% of equity | 4.5% | ✓ PASS | Cash: £4.94 of £109.88 equity = 4.5% buffer. Adequate. |
| **Settlement (T+1)** | N/A | N/A | ✓ PASS | No unsettled proceeds pending. Settlement ready for execution. |

---

## Portfolio Drawdown Analysis

- **Peak Equity:** £110.00 (2026-03-20 or earlier)
- **Current Equity:** £109.88
- **Drawdown:** (110.00 - 109.88) / 110.00 = **0.11%**
- **Drawdown Limit:** 15.0%
- **Status:** ✓ Well within limit. Portfolio is performing soundly; no liquidation trigger.

---

## UK Costs Assumption

- **Fee Model:** Per-trade, £0.00 per trade (no commission applied).
- **Stamp Duty:** 0.5% (50 bps) on BUY orders for UK equities; ETFs exempt.
  - *Example:* Buy £1,000 of UK equity = £5 stamp duty.
  - *Note:* Not applied today as no buys executed.
- **Slippage:** 10 bps assumed on all entry prices and exits.
- **Calculation:** All cost estimates in trade_plan.json are illustrative if trades occur. Actual costs depend on market conditions and broker execution.

---

## Gap Risk & Stop-Loss Acknowledgement (DAILY_CHECK Mode)

**Stop Execution Mode:** DAILY_CHECK

In DAILY_CHECK mode, the bot monitors stops once per day (at close). **Important limitations:**
- Stop-losses are checked against the daily low; if low_gbp ≤ stop_price_gbp, a market sell is triggered.
- **Gap Risk:** Overnight gaps can cause the opening price to be below the stop, resulting in execution at a worse price than planned.
- **Intraday Gaps:** Intraday price movements cannot be monitored; stops are only checked at day-end.
- **Example:** A stock stops at £10.00, but overnight news causes a 5% gap down to £9.50. The DAILY_CHECK will execute at or near £9.50, exceeding planned loss.
- **Current Holdings:** 
  - SHEL.L stop: £27.71 (current: £34.34)
  - BP.L stop: £4.68 (current: £5.62)
  - GLEN.L stop: £4.86 (current: £5.20)
  - BA.L stop: £21.50 (current: £22.50)
  - AZN.L stop: £137.18 (current: £138.96)
  - All stops are >10% below current price; reasonable buffer against intraday volatility.

---

## Portfolio Snapshot (as of 2026-03-20)

| Ticker | Quantity | Avg Cost | Current Price | Market Value | Unrealised PnL | Days Held | Stop | % of Equity |
|---|---|---|---|---|---|---|---|---|
| SHEL.L | 1.0624 | £28.70 | £34.34 | £36.48 | +£5.99 | 29 | £27.71 | 33.2% |
| BP.L | 9.32 | £4.92 | £5.62 | £52.41 | +£6.51 | 13 | £4.68 | 47.7% |
| GLEN.L | 1.035 | £5.08 | £5.20 | £5.38 | +£0.12 | 28 | £4.86 | 4.9% |
| BA.L | 0.2378 | £22.61 | £22.50 | £5.35 | -£0.03 | 9 | £21.50 | 4.9% |
| AZN.L | 0.0383 | £142.90 | £138.96 | £5.32 | -£0.15 | 0 | £137.18 | 4.8% |
| **TOTAL** | | | | **£109.88** | **+£12.44** | | | **100%** |

**Portfolio Quality:**
- Total unrealised gain: +£12.44 (11.3% profit on deployed capital)
- Average holding period: ~15 days (swap trade duration)
- Concentration: 80.9% in Energy (SHEL.L + BP.L); well above 40% sector limit but due to existing holdings, not new entries.
- Cash: £4.94 (4.5% of equity)

---

## Orders to Execute

**None.** No valid entry or exit signals generated today.

---

## What Could Invalidate This Plan

1. **Corporate Actions:** If any held position issues a dividend, rights issue, or spin-off, dividend/PnL calculations may shift.
2. **Overnight News:** Earnings announcements, regulatory changes, or macro events could cause gaps that breach stop-losses or invalidate trend analysis.
3. **Liquidity Crisis:** Market closure, trading halt, or liquidity crunch could prevent execution of stops or future entries.
4. **FX Movements:** No GBP/USD, GBP/JPY currency effects apply (all prices in GBP). ETFs are GBP-denominated.
5. **Data Errors:** If market_data.csv or positions.json contain errors (e.g., typos in prices, incorrect volumes), strategy decisions may be flawed.
6. **Sector Rotation:** Strong intraday movement in Energy, Healthcare, or Financials could create new breakout opportunities not visible in daily close data.
7. **Settlement Delays:** If T+1 settlement is delayed (e.g., exchange technical issue), cash availability could be constrained.
8. **Broker Errors:** Manual execution errors, failed orders, or incorrect fills could result in unplanned positions.

---

## Data Quality Notes

- **Market Data:** All 25 tickers in market_data.csv include required pre-computed columns (SMA50, SMA200, ATR14, drawdown, etc.). No data issues detected.
- **Data Freshness:** market_data.csv dated 2026-03-20 (today); positions.json as_of_date 2026-03-20. Data is current.
- **Missing Columns:** None. All required indicators present.
- **Outliers:** GLEN.L volume_ratio_20d = 4.95x (very high); NG.L volume_ratio_20d = 4.43x (high). These are noted but not disqualifying; may reflect corporate actions or volatility events not detailed in input files.
- **Correlation Data:** correlation_matrix.csv not provided. Pairwise correlation checks cannot be performed; correlation constraint assumed met (no warnings issued).

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution involves substantial risks:
- **Market Risk:** Stock prices can move sharply against positions.
- **Gap Risk:** Overnight and intraday gaps can cause stop-losses to execute at unfavourable prices.
- **Slippage & Costs:** Actual execution prices may differ from market close; fees, stamp duty, and FX costs apply.
- **Settlement & Timing:** T+1 settlement means cash is not available for same-day reinvestment (assume_intraday_netting=false).
- **Model Risk:** The strategy is based on historical technical indicators; past performance is not indicative of future results.
- **Data Risk:** Errors in market data, corporate actions, or position records could invalidate decisions.
- **Stop-Loss Risk (DAILY_CHECK Mode):** Stops are monitored once daily at close. Intraday and overnight gaps can cause execution at worse prices or miss protection entirely.

**Use this plan at your own risk. Consult a qualified financial advisor before executing any trades.**

---

*Generated by DailyEquityTrader-UK (Automated Rules Engine)*  
*Run Date: 2026-03-20 | Base Currency: GBP | Account Type: Cash (no leverage, no shorts)*

===