# Daily Trading Plan – 2026-03-16

**Status:** NO_TRADES

**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (daily monitoring required)

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Bank Holidays (Next 5 Days):** None

---

## Summary

No new trades are being initiated today. The portfolio is in a **severely cash-constrained state** with only **10.44 GBP in cash** and an equity value of **107.94 GBP**. After accounting for the mandatory **3% cash buffer (3.24 GBP)**, only **7.20 GBP** remains available for new position entry.

The strategy profile (balanced) requires a minimum risk allocation of **5% of portfolio equity (5.40 GBP)** per trade. However, once slippage (10 bps), stamp duty (50 bps for UK equities), and fees are factored in, a single new position would consume approximately **0.18–0.25 GBP** in costs, leaving insufficient capital to adequately size a position to the required 5.40 GBP risk target.

**Existing positions are all ACTIVE with no exit signals triggered today.** No stop-loss breaches, trend breaks, or corporate actions require immediate action.

---

## Top 3 Opportunities Evaluated (Not Executed)

### 1. **BA.L (BAE Systems)** – Confidence: 68%
- **Trend Status:** FULL (close > SMA50 > SMA200)
- **Setup Type:** N/A (existing position)
- **Rejection:** Position already held (days_held=3), meeting min_position_age_days=2. Anti-churn rule prevents re-entry within 2 days of acquisition.
- **Market Context:** Strong uptrend (close=23.22, SMA50=20.68, SMA200=18.93), but position is only 3 days old. Fundamentals and positioning remain sound.

### 2. **NG.L (National Grid)** – Confidence: 72%
- **Trend Status:** FULL (close > SMA50 > SMA200)
- **Setup Type:** PULLBACK (drawdown_from_20d_high=5.1%, volume_ratio=1.18)
- **Entry Price:** 13.56 GBP (current close)
- **Stop Loss:** 13.22 GBP (close – 0.34*ATR14 = 13.56 – 0.34*1.0 ≈ 13.22)
- **Risk per Trade:** 5.40 GBP → requires ~40 shares at 13.56 GBP = ~542 GBP notional
- **Rejection:** **Insufficient cash.** Available after buffer = 7.20 GBP. Position would cost ~542 GBP + ~2.71 GBP (slippage + stamp duty) = ~544.71 GBP. Capital shortfall of ~537.51 GBP.

### 3. **TSCO.L (Tesco)** – Confidence: 70%
- **Trend Status:** FULL (close > SMA50 > SMA200)
- **Setup Type:** PULLBACK (drawdown_from_20d_high=3.5%, volume_ratio=0.42)
- **Entry Price:** 4.906 GBP
- **Stop Loss:** 4.79 GBP
- **Risk per Trade:** 5.40 GBP → requires ~1,100 shares at 4.906 GBP = ~5,397 GBP notional
- **Rejection:** **Insufficient cash.** Capital shortfall exceeds available funds by orders of magnitude.

---

## Risk Checks

| Constraint | Value | Limit | Status |
|-----------|-------|-------|--------|
| **Portfolio Drawdown** | 0.0% | 15.0% | ✓ PASS |
| **Current Positions** | 4 | 5 | ✓ PASS |
| **Cash Buffer (% of Equity)** | 3.0% | 3.0% | ✓ PASS |
| **Max Sector Exposure (Energy)** | 45.4% | 40.0% | ✗ BREACH |
| **Max Single-Name Exposure (BP.L)** | 46.6% | 30.0% | ✗ BREACH |
| **Turnover (Today)** | 0.0% | 30.0% | ✓ PASS |
| **Trading Day Valid** | Yes | – | ✓ YES |
| **Kill Switch** | OFF | – | ✓ OK |

---

## Sector & Position Exposure Analysis

### Current Holdings (4 positions)
| Ticker | Sector | Market Value (GBP) | % of Equity | Days Held | Status | Current Stop (GBP) |
|--------|--------|-------------------|------------|-----------|--------|-------------------|
| **SHEL.L** | Energy | 36.28 | 33.6% | 23 | ACTIVE | 27.71 |
| **BP.L** | Energy | 50.36 | 46.6% | 7 | ACTIVE | 4.68 |
| **GLEN.L** | Materials | 5.34 | 4.95% | 22 | ACTIVE | 4.86 |
| **BA.L** | Industrials | 5.52 | 5.12% | 3 | ACTIVE | 21.50 |

### Sector Exposure Totals
- **Energy:** 80.0% (BREACH – limit 40%)
  - SHEL.L: 33.6%
  - BP.L: 46.6%
- **Materials:** 4.95%
- **Industrials:** 5.12%
- **Cash:** 9.68%

**⚠️ WARNING: Energy sector is heavily overweight at 80.0% of equity. This violates the max_sector_exposure_pct constraint (40.0%). Consider rebalancing via targeted sells of either SHEL.L or BP.L once market conditions permit.**

---

## Portfolio Drawdown Status

- **Current Equity:** 107.94 GBP
- **Peak Equity (All-Time):** 107.94 GBP
- **Drawdown:** 0.0%
- **Drawdown Limit:** 15.0%
- **Status:** ✓ No drawdown; at portfolio peak.

---

## Cash & Liquidity Analysis

| Item | Amount (GBP) |
|------|--------------|
| Cash Balance | 10.44 |
| Unsettled Proceeds | 0.00 |
| Required Buffer (3%) | 3.24 |
| Available for Buys | 7.20 |
| Max Risk per Single Trade (5% of equity) | 5.40 |
| Estimated Costs per Trade (slippage + stamp duty) | 0.18–0.25 |

**Bottleneck:** Available cash (7.20 GBP) is insufficient to:
1. Satisfy the 5% risk allocation (5.40 GBP minimum)
2. Cover typical transaction costs (0.18–0.25 GBP)
3. Maintain a safety buffer for slippage or gaps

**Recommendation:** No new positions should be opened until:
- Existing positions generate profits and increase cash reserves, OR
- Market conditions create a high-conviction breakout (confidence > 0.85) in a micro-cap that requires only 1–2 shares.

---

## UK Costs & Assumptions

- **Fee Model:** Per-trade fixed fee of **0 GBP** (no commission)
- **Stamp Duty:** **50 bps (0.5%)** on BUY orders for UK equities (applied in position sizing)
- **Slippage Assumption:** **10 bps (0.1%)** market impact on order entry
- **Total Cost Estimate per Trade:** ~0.2% of notional value

No trades were executed, so costs are not charged today.

---

## Stop-Loss Monitoring (DAILY_CHECK Mode)

In DAILY_CHECK mode, the bot checks once daily whether the low price (low_gbp) breaches any position's current stop price. If breached, a market sell order is generated.

**Today's Stop Check:**

| Ticker | Current Stop (GBP) | Today's Low (GBP) | Breach? | Action |
|--------|-------------------|------------------|--------|--------|
| SHEL.L | 27.71 | 33.73 | ✓ NO | HOLD |
| GLEN.L | 4.86 | 5.13 | ✓ NO | HOLD |
| BP.L | 4.68 | 5.33 | ✓ NO | HOLD |
| BA.L | 21.50 | 22.96 | ✓ NO | HOLD |

**No stop-loss exits triggered today.**

### Gap Risk Acknowledgement
In DAILY_CHECK mode, stop-losses are checked once per day (at close). **If overnight gaps occur (e.g., news-driven or forex-driven), actual execution may occur at a significantly worse price than the target stop, resulting in losses exceeding the planned risk allocation.** This is an inherent limitation of daily monitoring. Consider using broker GTC (good-till-cancelled) orders for stricter risk management if available.

---

## Portfolio Snapshot (End of Day)

| Metric | Value |
|--------|-------|
| **Total Equity** | 107.94 GBP |
| **Cash Balance** | 10.44 GBP |
| **Total Positions** | 4 |
| **Unrealised P&L** | +10.50 GBP |
| **Portfolio Return** | +9.74% |
| **Largest Position** | BP.L (46.6%) |
| **Sector Concentration** | Energy 80.0% (OVERWEIGHT) |

### Position Snapshot
| Ticker | Qty | Entry Price (GBP) | Current Price (GBP) | Market Value (GBP) | Unrealised P&L (GBP) | Current Stop (GBP) |
|--------|-----|------------------|-------------------|------|---------|------------------|
| SHEL.L | 1.0624 | 28.70 | 34.15 | 36.28 | +5.79 | 27.71 |
| GLEN.L | 1.0350 | 5.08 | 5.16 | 5.34 | +0.08 | 4.86 |
| BP.L | 9.3200 | 4.92 | 5.40 | 50.36 | +4.46 | 4.68 |
| BA.L | 0.2378 | 22.61 | 23.22 | 5.52 | +0.14 | 21.50 |

---

## Today's Orders

**No orders generated.**

**Execution Sequence:** SELL_THEN_BUY (not applicable today).

---

## What Could Invalidate This Plan?

1. **Market Gap:** Overnight geopolitical event, earnings announcement, or macro news causing a gap open below current stop prices. Check pre-market data at next session open.
2. **Liquidity Crisis:** If avg_gbp_volume drops significantly, position exits may be constrained.
3. **Corporate Actions:** Spin-offs, mergers, or delisting of SHEL.L, BP.L, GLEN.L, or BA.L would trigger forced exits.
4. **Momentum Reversal:** If Energy sector weakens and both SHEL.L and BP.L breach SMA50, dual energy exposure creates concentrated exit risk.
5. **Cash Infusion:** Receipt of dividends or cash deposits would unlock new entry opportunities.
6. **Stop Breach:** If any position closes below its stop price, a market sell is triggered at next day's open or intraday if monitoring is intraday.

---

## Data Quality Notes

✓ All required columns present in market_data.csv  
✓ All tickers in universe.csv have ACTIVE status  
✓ Market data is fresh (date = 2026-03-16, matches as_of_date)  
✓ No stale sma200_gbp values; all tickers have > 200 days history  
✓ Trading day confirmed (is_trading_day = true)  
✓ No half-day risk (is_half_day = false)  
✓ No pending corporate actions or delistings  
✓ Positions.json reconciles: 36.28 + 5.34 + 50.36 + 5.52 + 10.44 = 107.94 GBP ✓

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice and does not constitute a recommendation to buy, sell, or hold any security.**

**Key Risks:**
- Execution risk: Orders may fill at worse prices due to market impact, slippage, or widened spreads.
- Gap risk: Overnight gaps or market halts may cause stop-losses to execute at significantly worse prices.
- Settlement risk: T+1 settlement in the UK means cash from sells is not immediately available for reinvestment (assume_intraday_netting=false).
- FX risk: Although all prices are in GBP, international ETFs (VUAG.L, VWRP.L, CSP1.L) carry underlying currency exposure.
- Concentration risk: Current portfolio is 80% Energy sector, exceeding constraint limits. Rebalancing is needed.
- Liquidity risk: Small portfolio (107.94 GBP) and micro-position sizes (some < 1 share) may incur slippage or rounding errors.
- Tax and fees: Stamp duty, capital gains tax, and other jurisdictional costs are not modeled.

**Use at your own risk. Consult a qualified financial advisor before making investment decisions.**

---

## Next Steps

1. Monitor SHEL.L, GLEN.L, BP.L, BA.L for stop-loss breaches at next trading session.
2. Consider rebalancing Energy exposure (currently 80%, limit 40%) via a targeted SELL of either SHEL.L or BP.L.
3. If any position is closed, reinvest proceeds in a diversified sector (Healthcare, Financials, or Utilities).
4. Await cash inflow (dividend, deposit) to unlock new entry opportunities.

---

*Generated by DailyEquityTrader-UK at 2026-03-16. Next run: 2026-03-17 (if trading day).*