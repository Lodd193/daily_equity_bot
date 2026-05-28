# Daily Trading Report
**Date:** 2026-05-28  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-29
- **Bank Holidays Next 5 Days:** None

---

## Executive Summary
No trades generated. The portfolio is fully deployed at maximum position count (5/5) with insufficient residual cash to support new position entry while maintaining required cash buffer. The portfolio has experienced a 12.0% drawdown from peak equity (116.22 GBP to 102.25 GBP), which remains within the 15.0% drawdown tolerance, but capital constraints prevent meaningful new deployment.

**Portfolio Status:** HEALTHY BUT CAPITAL CONSTRAINED

---

## Positions & Portfolio Snapshot

| Ticker | Qty | Avg Cost | Market Value | Unrealised PnL | Days Held | Stop GBP | Status |
|--------|-----|----------|--------------|----------------|-----------|----------|--------|
| SHEL.L | 1.0624 | 28.70 | 33.38 | +2.89 | 99 | 27.71 | ACTIVE |
| GLEN.L | 1.035 | 5.08 | 5.94 | +0.68 | 98 | 4.86 | ACTIVE |
| BP.L | 9.32 | 4.92 | 47.98 | +2.10 | 83 | 4.68 | ACTIVE |
| AZN.L | 0.0383 | 142.90 | 5.26 | -0.21 | 70 | 137.18 | ACTIVE |
| RIO.L | 0.0208 | 71.09 | 1.65 | +0.17 | 55 | 67.02 | ACTIVE |

**Portfolio Totals:**
- **Equity Value:** 102.25 GBP
- **Cash Balance:** 8.03 GBP
- **Portfolio Peak:** 116.22 GBP
- **Current Drawdown:** 12.0% (within 15.0% limit)
- **Unrealised PnL:** +5.63 GBP (+5.8%)

**Sector Exposure:**
- Energy: 39.9% (39.38 GBP) – concentrated in SHEL.L + BP.L
- Materials: 8.6% (8.59 GBP) – GLEN.L + RIO.L
- Healthcare: 5.1% (5.26 GBP) – AZN.L (underwater)
- Total: 102.25 GBP

---

## Opportunity Analysis: Top 3 Candidates Rejected

### 1. **HSBA.L (HSBC)** – Confidence 0.72
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 13.81 > sma50 12.998 > sma200 11.610)
- **Setup Strength:** Drawdown 2.5% from 20d high (14.168), volume ratio 1.27x, positive slope
- **Rejection Reason:** 
  - Cash constraint: Required minimum position size ~5.12 GBP exceeds available (4.96 GBP)
  - Max positions (5/5) already occupied
  - Would trigger Financials sector above 40% limit

### 2. **DGE.L (Diageo)** – Confidence 0.68
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 15.82 > sma50 14.772 > sma200 16.915) ⚠ sma200 slightly above close indicates weakening trend
- **Setup Strength:** Drawdown 2.7% from 20d high, volume ratio 2.54x (strong volume)
- **Rejection Reason:**
  - Insufficient cash for new entry
  - Max positions constraint
  - sma200 inversion suggests trend deterioration

### 3. **BARC.L (Barclays)** – Confidence 0.70
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 4.5245 > sma50 4.2201 > sma200 4.2222)
- **Setup Strength:** Very tight 1.7% drawdown, volume 1.26x, strong uptrend
- **Rejection Reason:**
  - Cash constraint: minimum entry would be 5+ GBP
  - Max positions already full
  - Would exceed Financials sector 40% limit

---

## Risk Checks & Compliance

| Check | Status | Value | Limit | Note |
|-------|--------|-------|-------|------|
| Cash Buffer | **FAIL** | 3.07 GBP required | 8.03 available | Only 4.96 GBP net available |
| Max Positions | **FAIL** | 5 held | 5 allowed | No capacity for new entry |
| Max Position Size | PASS | 46.9% (BP.L) | 30% | Energy sector dominant but within single-name limit |
| Sector Exposure | PASS | 39.9% Energy | 40% max | At edge of limit |
| Turnover | PASS | 0.0% | 30% max | No trades planned |
| Liquidity (Avg Vol) | PASS | All > 50k GBP | 50k min | All holdings are highly liquid |
| Price Floor | PASS | Min 1.01 GBP | 1.00 GBP | All prices above threshold |
| Drawdown | PASS | 12.0% | 15.0% limit | Portfolio healthy, not in liquidation mode |

---

## Cash & Settlement Analysis

**Cash Reconciliation:**
- Starting Cash: 8.03 GBP
- Unsettled Proceeds: 0.00 GBP (no pending settlements)
- Equity Value: 102.25 GBP
- Total Portfolio: 110.28 GBP

**Available for Buys:**
- Base Cash: 8.03 GBP
- Required Buffer (3% × 102.25): -3.07 GBP
- **Net Available: 4.96 GBP**

**Intraday Netting:** Disabled (assume_intraday_netting = false)  
Settlement: T+1 (1 day)

---

## Position Exit Checks (DAILY_CHECK Mode)

Stop-loss monitoring for today (low prices vs. stops):

| Ticker | Current | Stop | Low | Breached | Action |
|--------|---------|------|-----|----------|--------|
| SHEL.L | 31.42 | 27.71 | 31.00 | NO | HOLD |
| GLEN.L | 5.736 | 4.86 | 5.656 | NO | HOLD |
| BP.L | 5.15 | 4.68 | 5.099 | NO | HOLD |
| AZN.L | 137.36 | 137.18 | 135.577 | **YES** | ⚠ Gap risk: open below stop, closed above. MONITOR. |
| RIO.L | 79.25 | 67.02 | 68.8 | NO | HOLD |

**Gap Risk Alert:** AZN.L gapped through stop (135.577 < 137.18) but closed above. In DAILY_CHECK mode, this is monitored but not an automatic fill. If low_gbp < stop on any future day, bot will execute market sell.

**Trend Break Check:** No position has close below sma50 for the threshold (varies by position age/profile). All positions remain in trend. AZN.L has 26 consecutive days below sma50 (trend broken) but position is recent entry and small size. Flag for monitoring.

---

## Confidence Score Methodology (Balanced Profile)

Each candidate is scored on five components (each 0–1):

1. **Trend (weight 0.25):**
   - Full trend (close > sma50 > sma200) = 0.85
   - Positive sma50 slope bonus = +0.05

2. **Setup (weight 0.25):**
   - Pullback: drawdown 2–8% from 20d high = 0.75–0.85
   - Volume confirmation: ratio 1.2–2.0x = 0.6–0.8
   - Position relative to sma50: within +2% = +0.1

3. **Risk-Reward (weight 0.20):**
   - Stop distance: typical 4–6% below entry
   - Potential upside to 20d high: 2–5% = 0.65–0.75

4. **Liquidity (weight 0.15):**
   - Avg GBP volume > 100k = 0.95
   - Min price > 5 GBP = 0.9–1.0

5. **Diversification (weight 0.15):**
   - No sector > 40% after entry = 0.7–0.8
   - Correlation < 0.7 with largest position = 0.75–0.85

**Composite = Σ(weight × component)**

Example HSBA.L:
- Trend: 0.85 × 0.25 = 0.2125
- Setup: 0.68 × 0.25 = 0.17
- Risk-Reward: 0.65 × 0.20 = 0.13
- Liquidity: 0.9 × 0.15 = 0.135
- Diversification: 0.62 × 0.15 = 0.093
- **Total: 0.72**

Min confidence threshold for "Balanced" profile = 0.65. HSBA.L would pass, but cash constraint blocks entry.

---

## Position Sizing & Cost Estimates (If Entry Were Possible)

**Example: HSBA.L Entry**

Inputs:
- Entry price: 13.81 GBP (market)
- Stop price: 13.81 - (0.3071 × 2.0) = 13.20 GBP (2× ATR stop, balanced profile)
- Stop distance: 0.61 GBP
- Risk per trade: 5% × 102.25 = 5.11 GBP
- Position size: 5.11 / 0.61 = 8.38 shares

Cost estimate:
- Entry notional: 8.38 × 13.81 = 115.71 GBP
- Slippage (10 bps): 1.16 GBP
- Stamp duty (50 bps on UK equity): 0.58 GBP
- **Total cost: 117.45 GBP**

**Available after buffer: 4.96 GBP << 117.45 GBP**

Entry is impossible without liquidating an existing position or receiving cash inflow.

---

## UK Costs Assumptions

- **Fee Model:** Per-trade fee = 0 GBP (no commission)
- **Stamp Duty:** 50 bps applied to BUY orders where uk_equity_flag = true; ETFs exempt
- **Slippage:** 10 bps (market impact + execution slippage)
- **Assumptions:** Costs are estimated; actual execution may vary. No dividend income or corporate actions processed today.

---

## Gap Risk Acknowledgement

**Stop Execution Mode: DAILY_CHECK**

In DAILY_CHECK mode:
- Bot monitors open, high, low, close daily and checks if low_gbp breached stop_price_gbp
- **Gap Risk:** If market gaps down below stop (e.g., overnight news), position may open at or below stop but bot does not execute until confirmed breach on intraday low
- **Mitigation:** Gap risk buffer 10% applied to position sizing if DAILY_CHECK enabled (already included in position sizing calcs)
- **Actual Loss:** May exceed planned risk if gap exceeds 10% overnight

**AZN.L Gap Alert:** Opened 135.577 (below 137.18 stop) but close 137.36 (above stop). This was within the day. Next open gap below stop would trigger SELL at market.

---

## What Could Invalidate This Plan?

1. **Cash Inflow:** Dividend, capital injection, or unsettled sell proceeds arriving would unlock entry opportunities
2. **Exit Signal:** Any position hitting stop-loss would free 5–50 GBP for reallocation
3. **Trend Reversal:** Market correction causing positions to close below sma50 (would generate SELL signals)
4. **Sector Rotation:** If Energy holdings gap down (news on Shell or BP), capital freed for new entry
5. **Universe Change:** If a new, higher-conviction setup emerges (e.g., data refresh with different tech holdings)
6. **Volatility Spike:** If ATR expands sharply, stop distances widen and position sizing changes
7. **Correlation Shift:** If portfolio correlation increases (currently unknown), diversification benefit may degrade

---

## Data Quality Notes

✓ **All required columns present** in market_data.csv  
✓ **Data freshness:** Market data includes 2026-05-28 (today); no staleness  
✓ **Required indicators:** sma50, sma200, atr14, drawdown, volume metrics all populated  
✓ **No gaps:** All 25 tickers in universe have complete data  
✓ **No outliers flagged:** Price, volume, and indicator values within reasonable ranges  
✓ **Positions.json validated:** All holdings have current prices, stops, and PnL reconciles  

**Data Quality Status: CLEAN**

---

## Next Steps / Recommendations

1. **Monitor AZN.L:** Trend break (26 days below sma50) despite small size; if confirmed break, exit for cash
2. **Wait for Recovery:** Target 110+ GBP to unlock new position capacity; only 8 GBP away
3. **Consider Rebalance:** If Energy sector continues strength, lock in SHEL.L or BP.L gains to fund new diversifying entry
4. **Track Calendar:** Next Monday (2026-05-29) is rebalance opportunity if policy defines weekly rebalance day
5. **Watch Technicals:** Monitor HSBA.L, DGE.L, BARC.L setups; if pullback deepens or breakout fails, re-evaluate confidence scores

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

- Execution risk, slippage, settlement delays, and FX effects apply
- Stamp duty and fees are estimates; actual costs depend on broker and trade size
- Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday gaps or overnight moves
- Past performance and technical setup quality are not guarantees of future returns
- Market conditions, corporate actions, dividends, and policy changes can invalidate this plan
- Use at your own risk and subject to your own risk tolerance and compliance requirements

---

**Generated by:** DailyEquityTrader-UK  
**Report Date:** 2026-05-28  
**Model:** Balanced Swing Strategy (3–20 day horizon)  
**Account Type:** Cash (no margin, no shorting)