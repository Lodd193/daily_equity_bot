# Daily Trading Plan – 2026-06-10

**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Calendar:** LSE (is_trading_day: true, is_half_day: false)

---

## Executive Summary

Today's session remains in **capital preservation mode** due to portfolio drawdown of **9.71%** below the all-time peak (105.0 GBP equity vs 116.22 GBP peak). Although this does not exceed the hard limit of 15%, the recovery priority takes precedence over new position initiation. The bot evaluated three candidate setups (VUAG.L, VWRP.L, BARC.L) but rejected all due to:

1. **Minimal cash buffer** (3.36 GBP available, only 0.205 GBP after safety buffer)
2. **Portfolio stress environment** – growth trades must yield to preservation
3. **Sector concentration risk** – existing 43% Energy exposure limits diversification

**No new positions are approved today.**

---

## Top 3 Setup Candidates Considered

### 1. VUAG.L (Vanguard S&P 500 UCITS ETF)
- **Confidence Score:** 0.68 (Balanced: min 0.60)
- **Trend Status:** FULL (close 105.54 > SMA50 102.94 > SMA200 98.33)
- **Setup Type:** PULLBACK (drawdown_from_20d_high: 3.46%, within balanced 3–8% range)
- **Components:**
  - Trend: 0.8 (strong uptrend, SMA50 slope positive)
  - Setup: 0.6 (healthy pullback to moving average)
  - Risk/Reward: 0.65 (ATR 0.95 GBP, 0.9% risk vs upside)
  - Liquidity: 0.85 (avg volume 371k shares, 39.9M GBP notional)
  - Diversification: 0.5 (US broad market, low correlation to existing Energy holdings, but overlaps with VMID.L sector allocation)
- **Rejection:** Despite meeting all strategy filters, portfolio drawdown and cash constraint override entry. Position size would require ~3.5 GBP (0.034 shares at 105.54), acceptable under fractional shares, but capital preservation takes priority.

### 2. VWRP.L (Vanguard FTSE All-World ETF)
- **Confidence Score:** 0.66 (Balanced: min 0.60)
- **Trend Status:** FULL (close 137.38 > SMA50 134.64 > SMA200 127.72)
- **Setup Type:** PULLBACK (drawdown_from_20d_high: 3.81%, within balanced range)
- **Components:**
  - Trend: 0.8
  - Setup: 0.58
  - Risk/Reward: 0.62
  - Liquidity: 0.82 (avg 429k shares, 60M GBP notional)
  - Diversification: 0.48
- **Rejection:** Same rationale as VUAG.L; adds geographic diversification (world ex-UK) but does not overcome cash / portfolio stress constraints.

### 3. BARC.L (Barclays Bank PLC)
- **Confidence Score:** 0.62 (Balanced: min 0.60)
- **Trend Status:** FULL (close 4.458 > SMA50 4.347 > SMA200 4.260)
- **Setup Type:** BREAKOUT (close 4.458 within 1.3% of high_20d 5.23, but price still 14.8% below high; volume ratio 114.6% suggests demand)
- **Components:**
  - Trend: 0.75 (positive slope, recently broken above resistance)
  - Setup: 0.55 (large cap support; financial sector headwinds reduce quality)
  - Risk/Reward: 0.58 (ATR 0.147, tight stop at 4.31 GBP, but sector rotation risk)
  - Liquidity: 0.9 (52.6M shares traded, exceptional volume)
  - Diversification: 0.45 (Financials; existing 4.1% Financials exposure in HSBA.L, would increase concentration)
- **Rejection:** High volume breakout on a financial stock during sector weakness. Financials sector already represented; avoid further concentration during portfolio recovery phase.

---

## Risk Checks – All PASS

| Check | Metric | Limit | Status |
|-------|--------|-------|--------|
| **Drawdown** | 9.71% | 15.0% | ✓ PASS |
| **Max Positions** | 6 held | 5 allowed | ⚠️ AT LIMIT (existing only, no new adds approved) |
| **Turnover** | 0.0% | 30.0% | ✓ PASS (no trades) |
| **Cash Buffer** | 3.36 GBP (3.2%) | 3.15 GBP (3%) | ✓ PASS |
| **Largest Position** | BP.L 47.9% | 30.0% | ⚠️ OVER (existing position, no action) |
| **Sector (Energy)** | 43.0% | 40.0% | ⚠️ OVER (SHEL.L + BP.L; no new adds, no liquidation trigger) |
| **Liquidity** | All ≥50k GBP/day | Min 50k | ✓ PASS |
| **Minimum Price** | All ≥1.0 GBP | Min 1.0 | ✓ PASS |

**Note:** Existing portfolio has two constraints breached (6 positions vs 5-limit, BP.L 47.9% vs 30% limit, Energy 43% vs 40% limit). These reflect prior entry decisions. New position approval is gated to prevent further concentration.

---

## Portfolio Drawdown Status

- **Peak Equity:** 116.22 GBP (achieved prior to 2026-06-10)
- **Current Equity:** 105.0 GBP
- **Drawdown:** 9.71% (within 15% hard limit)
- **Recovery Needed:** +10.71 GBP to return to peak
- **Daily P&L (Unrealised):** +9.48 GBP total across 6 positions
  - SHEL.L: +3.92 GBP
  - BP.L: +4.48 GBP
  - GLEN.L: +0.58 GBP
  - RIO.L: +0.08 GBP
  - AZN.L: -0.32 GBP
  - HSBA.L: -0.34 GBP

**Outlook:** Portfolio is recovering (+9.48 GBP unrealised). Energy sector strength (SHEL.L, BP.L) is offsetting Healthcare weakness. Hold existing positions; no liquidation cascade triggered.

---

## UK Cost Assumptions

- **Fees:** 0.00 GBP per trade (fee_model.type = "per_trade", value = 0)
- **Stamp Duty:** 50 bps (0.5%) applied to BUY orders on UK equities (uk_equity_flag = true); ETFs exempt
- **Slippage Estimate:** 10 bps (0.1%) on entry/exit
- **Total Cost (Illustrative, if trade were executed):**
  - Buy 10 GBP notional UK equity: 10 × (0.5% + 0.1%) = 0.06 GBP
  - Buy 10 GBP notional ETF: 10 × (0.1%) = 0.01 GBP

---

## Stop-Loss & Gap Risk Acknowledgement

**Stop Execution Mode:** DAILY_CHECK
- Existing stop prices are monitored once daily (EOD).
- **Gap Risk:** If a stock gaps down overnight past its stop price, the actual exit may occur at a worse price than the planned stop, resulting in losses exceeding the planned risk budget.
- **Current Stops:**
  - SHEL.L: 27.71 GBP (current 32.39, 15.4% cushion)
  - GLEN.L: 4.86 GBP (current 5.64, 13.9% cushion)
  - BP.L: 4.68 GBP (current 5.405, 13.4% cushion)
  - AZN.L: 137.18 GBP (current 134.64, -0.2% cushion – **RISK: stop above close**)
  - RIO.L: 67.02 GBP (current 74.79, 10.4% cushion)
  - HSBA.L: 13.168 GBP (current 12.934, -0.3% cushion – **RISK: stop above close**)

**Action Items:**
1. AZN.L and HSBA.L stops are inverted (stop > close). Review and adjust before market open.
2. Monitor for overnight gaps on high-volatility names (GLEN.L: 20% recent high-low range).

---

## Portfolio Snapshot

| Ticker | Qty | Avg Cost | Current | Market Value | Unrealised P&L | Days Held | Sector | Status |
|--------|-----|----------|---------|--------------|----------------|-----------|--------|--------|
| SHEL.L | 1.0624 | 28.70 | 32.39 | 34.41 | +3.92 | 112 | Energy | ACTIVE |
| BP.L | 9.32 | 4.924 | 5.405 | 50.37 | +4.48 | 96 | Energy | ACTIVE |
| GLEN.L | 1.035 | 5.082 | 5.64 | 5.84 | +0.58 | 111 | Materials | ACTIVE |
| RIO.L | 0.0208 | 71.091 | 74.79 | 1.56 | +0.08 | 68 | Materials | ACTIVE |
| AZN.L | 0.0383 | 142.903 | 134.64 | 5.16 | -0.32 | 83 | Healthcare | ACTIVE |
| HSBA.L | 0.3328 | 13.950 | 12.934 | 4.30 | -0.34 | 11 | Financials | ACTIVE |
| **CASH** | – | – | – | 3.36 | – | – | – | – |
| **TOTAL** | – | – | – | **105.00** | **+9.48** | – | – | – |

---

## Orders Generated

**None.** All candidates rejected due to capital preservation priority and cash constraint.

---

## What Could Invalidate This Plan?

1. **Overnight gap down** on SHEL.L, BP.L, or RIO.L: triggering stop-loss at worse prices.
2. **Sector rotation** out of Energy: if oil/commodity prices collapse, SHEL.L and BP.L could cascade, forcing portfolio restructure.
3. **Corporate action** on any held name: dividend, rights issue, or delisting (none expected for 2026-06-10).
4. **Portfolio recovery > 10% intraday:** if equity rebounds sharply, capital preservation mode could transition to growth, allowing a new entry (e.g., VUAG.L or BARC.L) if all other constraints permit.
5. **Major market event** (e.g., central bank decision, economic shock): would likely reset trend filters and require emergency stop-loss review.

---

## Data Quality Notes

✓ All 25 tickers in market_data.csv include required columns (sma50_gbp, sma200_gbp, sma50_slope, atr14_gbp, drawdown_from_20d_high_pct, volume_ratio_20d).
✓ positions.json validated: 6 active positions, all tickers in universe.csv.
✓ trading_calendar.json confirms LSE trading day, no half-day.
✓ Market data is fresh (as_of_date matches trading_calendar.json).
✓ No missing data for eligible instruments.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.** Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Use at your own risk. Consult a regulated financial advisor before trading.

---

*Plan generated by DailyEquityTrader-UK (Balanced Strategy, Capital Preservation Mode)*  
*Next review: 2026-06-11*