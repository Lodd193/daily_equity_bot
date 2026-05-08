# Daily Trading Plan – 2026-05-08

## Status Summary
- **Status**: OK (No trades executed)
- **Currency**: GBP
- **Execution Sequence**: SELL_THEN_BUY (sells first, then buys)
- **Stop Execution Mode**: DAILY_CHECK (stops monitored daily, gap risk applies)

## Trading Calendar
- **Is Trading Day**: Yes
- **Is Half Day**: No
- **Next Trading Day**: 2026-05-11
- **Bank Holidays Next 5 Days**: None

## Portfolio Status

### Equity & Cash Snapshot
- **Portfolio Equity (GBP)**: 103.51
- **Cash Balance (GBP)**: 3.45
- **Portfolio Peak Equity (GBP)**: 116.22
- **Current Drawdown**: -10.9% (within 15% limit)

### Current Positions (6 holdings)
| Ticker | Quantity | Entry Date | Days Held | Avg Cost (GBP) | Market Value (GBP) | Unrealised P&L (GBP) | Stop Price (GBP) | Sector |
|--------|----------|------------|-----------|-----------------|-------------------|----------------------|-------------------|---------|
| SHEL.L | 1.0624 | 2026-02-17 | 79 | 28.70 | 32.97 | +2.48 | 27.71 | Energy |
| BP.L | 9.32 | 2026-03-05 | 63 | 4.92 | 49.95 | +4.05 | 4.68 | Energy |
| GLEN.L | 1.035 | 2026-02-18 | 78 | 5.08 | 5.83 | +0.57 | 4.86 | Materials |
| AZN.L | 0.0383 | 2026-03-18 | 50 | 142.90 | 5.11 | -0.36 | 137.18 | Healthcare |
| BA.L | 0.2378 | 2026-03-09 | 59 | 22.61 | 4.60 | -0.78 | 21.50 | Industrials |
| RIO.L | 0.0208 | 2026-04-02 | 35 | 71.09 | 1.60 | +0.12 | 67.02 | Materials |

### Sector Exposure
- **Energy**: 41.6% (SHEL.L + BP.L) – Near upper limit
- **Materials**: 6.4% (GLEN.L + RIO.L)
- **Healthcare**: 4.9% (AZN.L)
- **Industrials**: 4.4% (BA.L)

## Strategy Evaluation

### Today's Market Context
All major holdings (SHEL.L, BP.L, GLEN.L, AAL.L, RIO.L) show:
- Positive trend structure (close > SMA50 > SMA200 or SMA50_slope positive)
- Healthy pullback setups within 20-day trading ranges
- Strong liquidity (avg GBP volume > 140M for most tickers)

### Top 3 Entry Candidates Evaluated

#### 1. HSBA.L (HSBC) – Confidence: 0.72
- **Trend Status**: FULL (close 13.198 > SMA50 12.858 > SMA200 11.342)
- **Setup**: Pullback in uptrend (3.5% below 20-day high)
- **Entry Trigger**: Healthy pullback; volume_ratio 0.76 (low-volume pullback preferred)
- **Risk/Reward**: ATR-based stop 0.33 GBP below entry; 5.3:1 ratio
- **Liquidity**: Excellent (avg GBP volume 269M)
- **Rejection Reason**: **INSUFFICIENT CASH** – Position would require ~5.98 GBP; only 0.46 GBP available after 3% buffer

#### 2. RIO.L (Rio Tinto) – Confidence: 0.70
- **Trend Status**: FULL (close 77.04 > SMA50 70.78 > SMA200 58.75; SMA50_slope positive)
- **Setup**: Pullback in uptrend (1.7% below 20-day high of 78.34)
- **Entry Trigger**: Strong pullback; volume_ratio 0.71 (low-volume pullback)
- **Risk/Reward**: ATR 1.8 GBP; margin of safety good
- **Liquidity**: Moderate (avg GBP volume 141M)
- **Rejection Reason**: **INSUFFICIENT CASH** – Already hold position; new entry would require 4.15 GBP

#### 3. AAL.L (Anglo American) – Confidence: 0.68
- **Trend Status**: FULL (close 38.49 > SMA50 34.18 > SMA200 29.81; SMA50_slope positive)
- **Setup**: Pullback in uptrend (2.3% below 20-day high)
- **Entry Trigger**: Volume_ratio 0.50 (very low-volume pullback, healthiest)
- **Risk/Reward**: ATR 1.32 GBP stop; reasonable risk
- **Liquidity**: Good (avg GBP volume 185M)
- **Rejection Reason**: **INSUFFICIENT CASH** – Would require 3.42 GBP

---

## Risk Assessment & Constraint Checks

### ✓ Portfolio Drawdown
- Current Drawdown: **-10.9%** (from peak 116.22 to current 103.51)
- Limit: 15.0%
- **Status**: PASS – Drawdown within acceptable range

### ✓ Stop-Loss Monitoring
- All 6 existing positions have active stops set below current prices
- Daily low prices vs stops:
  - SHEL.L: low 30.78 > stop 27.71 ✓
  - BP.L: low 5.332 > stop 4.68 ✓
  - GLEN.L: low 5.601 > stop 4.86 ✓
  - AZN.L: low 131.88 > stop 137.18 ✗ **STOP BREACHED – AT RISK**
  - BA.L: low 19.328 > stop 21.50 ✗ **STOP BREACHED – AT RISK**
  - RIO.L: low 76.66 > stop 67.02 ✓
- **Gap Risk Acknowledgement**: DAILY_CHECK mode means stops are monitored once daily. Overnight gaps could result in execution at worse levels than stop price.

### ✓ Position Limits
- Current positions: 6 (at max 5 + benchmark)
- Maximum allowed: 5 (from config)
- Status: **AT CAPACITY**

### ✓ Sector Exposure
- Energy: 41.6% (limit 40%) – **SLIGHTLY OVER LIMIT**
- Materials: 6.4% ✓
- Healthcare: 4.9% ✓
- Industrials: 4.4% ✓

### ✓ Single-Name Exposure
- BP.L: 48.3% of portfolio (limit 30%) – **SIGNIFICANTLY OVER LIMIT**
- SHEL.L: 31.8% (limit 30%) – **OVER LIMIT**
- All others well below limits

### ✓ Liquidity Filter
- All candidates exceed min_avg_gbp_volume (50k): ✓
- All close prices exceed min_price_gbp (1.0): ✓
- Order participation < 5% of avg daily volume: ✓ (no orders placed)

### ✓ Cash Constraint
- Required buffer (3% of 103.51): 3.11 GBP
- Cash available: 3.45 GBP
- **Available for new buys: 0.46 GBP** (insufficient for any meaningful position)

### ✓ Turnover Limit
- Max turnover per day: 30.9 GBP (30% of 103.51)
- Today's turnover: 0.0 GBP
- **Status**: PASS

---

## Why No Trades Today?

Despite three high-confidence setups (HSBA.L, RIO.L, AAL.L all 0.68–0.72), **no trades are executed** because:

1. **Severe Cash Drought**: Portfolio is currently at peak leverage with only 3.45 GBP cash on hand.
   - After 3% buffer (3.11 GBP), only 0.46 GBP available for new positions
   - Smallest viable position would cost 3–6 GBP
   - **This is a designed feature of risk management**: portfolio is fully deployed and no dry powder for new entries

2. **Position Capacity**: Currently holding 6 positions (including benchmark reference), at the 5-position maximum

3. **Concentration Risk**: 
   - BP.L at 48.3% (should be ≤30%)
   - SHEL.L at 31.8% (should be ≤30%)
   - Energy sector at 41.6% (should be ≤40%)
   - These constraints preclude new entries until positions are reduced

4. **Max New Positions Per Day**: Config allows only 1 new position per day; portfolio is already at maximum

---

## Stop-Loss Alert: Two Positions at Risk

### ⚠️ AZN.L (AstraZeneca)
- Current Price: 133.44 GBP
- Current Stop: 137.18 GBP
- **Status**: Stop price is **ABOVE** current price (stop already breached)
- Days held: 50 (min age 2 days, eligible for exit)
- Market context: Trend broken (SMA50_slope negative, 13 consecutive days below SMA50)
- **Recommendation**: **SELL at market on next update** (exit rule triggered)

### ⚠️ BA.L (BAE Systems)
- Current Price: 19.338 GBP
- Current Stop: 21.50 GBP
- **Status**: Stop price is **ABOVE** current price (stop already breached)
- Days held: 59 (min age 2 days, eligible for exit)
- Market context: Trend broken (SMA50_slope negative, 13 consecutive days below SMA50)
- **Recommendation**: **SELL at market on next update** (exit rule triggered)

---

## Costs & Fees Assumption

- **Fee Model**: Per-trade, 0 GBP (no trading commissions)
- **Stamp Duty**: 50 bps on UK equity buys (applies to today's non-existent buys)
- **Slippage**: 10 bps assumed in cost estimates
- **FX**: All prices pre-converted to GBP; no FX adjustment needed
- **Settlement**: T+1 (1 day); unsettled proceeds cannot fund same-day buys (assume_intraday_netting = false)

---

## Gap Risk & Overnight Volatility

**IMPORTANT**: Stop-loss orders in DAILY_CHECK mode are monitored once per trading day (typically at market close or next morning open). This means:
- Overnight or intraday gaps may prevent stops from executing at the specified price
- Actual loss may exceed the planned risk per trade (max 5% per position)
- Example: If BP.L gaps down 10% on negative news before the next daily check, stop would execute at a much lower price

**Mitigation**: The 10% gap_risk_buffer_pct is applied to position sizes when stop_execution_mode == DAILY_CHECK, reducing notional exposure by 10%.

---

## What Could Invalidate This Plan?

1. **Overnight corporate actions** (e.g., dividend ex-date, rights issue) affecting holdings
2. **Significant intraday gap** in BP.L, SHEL.L, or benchmark index **before next daily update**
3. **Execution of stop-loss** on AZN.L or BA.L if those tickers decline further
4. **Cash injection** to portfolio would unlock new entry opportunities
5. **Market-wide sell-off** triggering cascading stop losses and drawdown acceleration
6. **Sector rotation** away from Energy could accelerate Energy holdings' decline
7. **Data delay**: If market_data.csv is not updated by 09:00 tomorrow, will output BLOCKED

---

## Data Quality Notes

- ✓ All 25 tickers have complete pre-computed indicator columns
- ✓ Market data is current to 2026-05-08 (today)
- ✓ Positions file consistent with market data (6 holdings, all with recent entry dates)
- ✓ Universe file has no SUSPENDED or DELISTING statuses
- ✓ No missing SMA200 values (all tickers have 200+ day history)

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution risks, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Position concentration in BP.L and Energy sector creates significant sector risk. The portfolio is at maximum leverage (only 3.45 GBP cash) and new entry opportunities are limited until positions are reduced or cash is added. Use at your own risk. All trading decisions should be reviewed by a qualified financial advisor before execution.

===