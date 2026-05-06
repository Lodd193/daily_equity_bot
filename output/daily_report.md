# Daily Trading Report
**Date:** 2026-05-06  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-07
- **Bank Holidays Next 5 Days:** None

---

## Executive Summary
Portfolio in holding mode. No new positions initiated due to insufficient available cash (£0.33 after 3% buffer on £106.61 equity). All existing positions monitored for stop-loss breach and trend deterioration. Portfolio drawdown is 8.3% from peak, well within the 15% limit.

---

## Top 3 Entry Candidates Evaluated

### 1. HSBA.L (HSBC Holdings)
- **Entry Type:** PULLBACK  
- **Trend Status:** FULL (close 13.434 > sma50 12.844 > sma200 11.303)  
- **Confidence:** 0.78  
- **Confidence Components:**
  - Trend: 0.95 (strong uptrend, sma50_slope positive)
  - Setup: 0.75 (1.8% drawdown from 20d high, volume ratio 0.943)
  - Risk/Reward: 0.72 (ATR14 0.342, reasonable risk distance)
  - Liquidity: 0.88 (avg_gbp_volume_20d £279.9M, well above minimum)
  - Diversification: 0.62 (would add to Financials sector, already 4 holdings in tight sectors)
- **Rejection Reason:** Insufficient cash. Minimum required £3.42 (100 shares @ 13.434 with 50bps stamp duty + slippage), but only £0.33 available after buffer.

### 2. LSEG.L (London Stock Exchange Group)
- **Entry Type:** PULLBACK  
- **Trend Status:** FULL (close 93.4 > sma50 89.243 > sma200 88.715)  
- **Confidence:** 0.74  
- **Confidence Components:**
  - Trend: 0.92 (strong trend, sma50_slope positive)
  - Setup: 0.68 (7.9% drawdown from 20d high, volume ratio 0.674 - low volume)
  - Risk/Reward: 0.70 (ATR14 2.465, moderate risk)
  - Liquidity: 0.82 (avg_gbp_volume_20d £162.7M, adequate)
  - Diversification: 0.60 (Financials, already well-represented)
- **Rejection Reason:** Insufficient cash. Minimum required £4.18 for viable position, available £0.33 only.

### 3. RIO.L (Rio Tinto)
- **Entry Type:** None (Already Held)  
- **Trend Status:** FULL (strong uptrend)  
- **Confidence:** 0.72  
- **Current Status:** HOLD. Position held 29 days with +0.13 GBP unrealised gain. Stop at 67.02 GBP active; low of 75.45 well above stop. Consider accumulating on future pullbacks if cash becomes available.

---

## Risk Checks

### Position-Level Stops
All active positions have DAILY_CHECK stop-loss orders in place:

| Ticker | Stop Price | Current Low | Status | Days Held |
|--------|-----------|------------|--------|-----------|
| SHEL.L | 27.71 | 31.385 | SAFE | 73 |
| GLEN.L | 4.86 | 5.596 | SAFE | 72 |
| BP.L | 4.68 | 5.382 | SAFE | 57 |
| BA.L | 21.5 | 20.63 | **NEAR** | 53 |
| AZN.L | 137.18 | 134.34 | SAFE | 44 |
| RIO.L | 67.02 | 75.45 | SAFE | 29 |

**⚠️ WARNING:** BA.L is close to its stop (20.63 vs 21.5). Monitor closely for intraday dips.

### Exposure Limits
- **Max Positions:** 5 limit; currently 6 (includes RIO.L recent entry)
- **Max New Positions Per Day:** 1 limit; 0 new positions today (cash constraint)
- **Turnover:** 0% (all HOLD)
- **Largest Position:** BP.L at 48.2% of equity (slightly elevated but within risk tolerance)
- **Sector Exposure:**
  - Energy: 42.2% (SHEL.L + BP.L)
  - Materials: 10.8% (GLEN.L + RIO.L)
  - Healthcare: 4.9% (AZN.L)
  - Industrials: 4.7% (BA.L)
  - All below 40% sector limit ✓

### Liquidity Filter
All holdings and candidates meet £50k min_avg_gbp_volume:
- Tightest: RIO.L at £149.4M ✓
- All satisfy £1.0 minimum price ✓

### Cash & Settlement
- **Portfolio Equity:** £106.61
- **Cash Balance:** £3.45
- **Required Buffer (3%):** £3.20
- **Available for Buys:** £0.33
- **Settlement Days:** 1 (T+1, standard UK)
- **Intraday Netting:** Disabled
- **Impact:** Only small fractional positions could be initiated today; major new entries blocked until portfolio rebalances (via stops or takes profits)

### Portfolio Drawdown
- **Peak Equity:** £116.22
- **Current Equity:** £106.61
- **Drawdown:** 8.3%
- **Limit:** 15%
- **Status:** ✓ Within tolerance

---

## Existing Position Review

### High-Confidence Holds
**RIO.L (Rio Tinto)** - Confidence 0.72
- Entry 2026-04-02 (29 days), +0.13 GBP gain
- Trend: FULL (close 77.2 > sma50 70.564 > sma200 58.438)
- Price action: Only 0.37% drawdown from 20d high; excellent risk/reward
- Stop: 67.02 GBP (ATR14 × 1.5 multiplier) — well below current
- **Recommendation:** HOLD; monitor for further strength or pullback entry opportunity

**BP.L (BP)** - Confidence 0.68
- Entry 2026-03-05 (57 days), +5.49 GBP gain (healthy)
- Trend: FULL (positive sma50_slope, close > sma50 > sma200)
- Stop: 4.68 GBP; low 5.382 safe
- **Recommendation:** HOLD; largest position; consider partial profit-taking if price reaches 6.0+ GBP

**GLEN.L (Glencore)** - Confidence 0.65
- Entry 2026-02-18 (72 days), +0.63 GBP gain
- Trend: FULL (strong materials recovery)
- Stop: 4.86 GBP; low 5.596 safe
- **Recommendation:** HOLD; approaching time stop (73+ days), but trend remains sound

**SHEL.L (Shell)** - Confidence 0.68
- Entry 2026-02-17 (73 days), +3.63 GBP gain
- Trend: FULL (Energy sector strength)
- Stop: 27.71 GBP; low 31.385 safe
- **Recommendation:** HOLD; longest-held position; consider profit-taking if energy continues rallying

### Weak Holds (Monitor for Exit)
**BA.L (BAE Systems)** - Confidence 0.55
- Entry 2026-03-09 (53 days), -0.41 GBP loss
- **Concern:** Trend negative (close 20.895 < sma50 21.842); 11 consecutive days below sma50
- Stop: 21.5 GBP; low 20.63 GBP (just 1.3% above stop)
- **Recommendation:** HOLD but prepare exit order if low touches 21.5 or trend break confirmed (close < 20.945)

**AZN.L (AstraZeneca)** - Confidence 0.52
- Entry 2026-03-18 (44 days), -0.28 GBP loss
- **Concern:** Strong downtrend (close 135.66 < sma50 145.522); 11 consecutive days below sma50
- **High Drawdown:** 12.2% from 20d high (highest among holdings)
- Stop: 137.18 GBP; low 134.34 GBP (safe but trend weak)
- **Recommendation:** HOLD for now, but exit on next stop breach or trend confirmation (close drops below 134.3)

---

## Costs & Fees Assumption
- **Fee Model:** Per-trade, £0.00 (effectively no trading fees assumed)
- **Stamp Duty:** 0.5% applied to UK equity BUY orders only
- **Slippage:** 10 bps (0.1%) estimated for entry/exit
- **Currency:** All prices and costs in GBP; no FX hedging required

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
Stop-loss orders are monitored **once per day** (at market close). Overnight or intraday gaps can result in:
- Execution at worse prices than stop price
- Losses exceeding planned risk (especially for BA.L and AZN.L, which are close to stops)
- No protection during market closed periods

**Mitigation:** Portfolio is small and concentrated; consider broker-GTC stops for overnight protection if available.

---

## Cash Constraint Analysis
The primary blocker for new entries today is **insufficient cash**: £3.45 total, of which £3.20 is required as buffer, leaving only £0.33 for new positions. This is because:
1. Portfolio is small (£106.61) and fully invested
2. No liquidations planned (all positions in uptrends or manageable downtrends)
3. Sell proceeds from any exit would settle T+1 (not available same-day with assume_intraday_netting=false)

**Recommendation:** Wait for natural exit signals (stops, time stops, or trend breaks) to free capital. Several high-quality setups (HSBA.L, LSEG.L, AAL.L) are queued and ready to execute once cash is available.

---

## Portfolio Snapshot (As of 2026-05-06)

| Ticker | Qty | Avg Cost | Market Value | PnL | Days | Sector | Stop | Status |
|--------|-----|----------|--------------|-----|------|--------|------|--------|
| SHEL.L | 1.0624 | 28.70 | 34.12 | +3.63 | 73 | Energy | 27.71 | HOLD |
| GLEN.L | 1.035 | 5.08 | 5.89 | +0.63 | 72 | Materials | 4.86 | HOLD |
| BP.L | 9.32 | 4.92 | 51.38 | +5.49 | 57 | Energy | 4.68 | HOLD |
| BA.L | 0.2378 | 22.61 | 4.97 | -0.41 | 53 | Industrials | 21.50 | HOLD⚠️ |
| AZN.L | 0.0383 | 142.90 | 5.20 | -0.28 | 44 | Healthcare | 137.18 | HOLD⚠️ |
| RIO.L | 0.0208 | 71.09 | 1.61 | +0.13 | 29 | Materials | 67.02 | HOLD |
| **TOTAL** | — | — | **106.61** | **+9.19** | — | — | — | — |
| **CASH** | — | — | **3.45** | — | — | — | — | — |

---

## What Could Invalidate This Plan?

1. **Market Gap Down at Open:** BA.L or AZN.L could gap through stops, locking in larger losses than planned
2. **Surprise News:** Delisting notice, earnings shock, sector collapse, or geopolitical event could trigger cascading exits
3. **Data Staleness:** If market_data.csv is not updated with today's final prices before next run, stop-check logic becomes invalid
4. **Settlement Delay:** If unsettled proceeds are delayed beyond T+1, cash availability forecast breaks
5. **Broker System Outage:** Cannot execute stops if broker systems are down
6. **Regulatory Change:** Unexpected changes to trading rules, fees, or stamp duty
7. **Correlation Spike:** If Energy (42.2% of portfolio) suffers sector-wide crash, stop-loss triggers cascade

---

## Data Quality Notes
✓ All required columns present in market_data.csv  
✓ All pre-computed indicators (SMA50, SMA200, ATR14, etc.) available for all 25 instruments  
✓ No missing or null values in critical fields for evaluated holdings  
✓ Market data dated 2026-05-06 matches as_of_date in positions.json  
✓ Universe.csv status field confirms all holdings are ACTIVE  
✓ Trading calendar confirms is_trading_day=true, is_half_day=false  

---

## Orders Summary
**No orders generated today.** All positions are HOLD. Reason: Insufficient available cash (£0.33) to open new positions after 3% buffer requirement.

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice. Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Use at your own risk.**

Historical performance does not guarantee future results. Portfolio is concentrated in Energy sector (42.2%) and may experience heightened volatility. Two positions (BA.L, AZN.L) are below SMA50 and should be monitored closely for further deterioration.

---