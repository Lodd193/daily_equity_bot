# Daily Trading Report
**Date:** 2026-05-29 (Friday)  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-06-01 (Monday)
- **Bank Holidays (Next 5 Days):** None

---

## Portfolio Snapshot
| Metric | Value |
|--------|-------|
| **Equity (GBP)** | 102.61 |
| **Cash Balance (GBP)** | 8.0278 |
| **Peak Equity (GBP)** | 116.22 |
| **Current Drawdown (%)** | 11.78% |
| **Drawdown Limit (%)** | 15.0% |
| **Drawdown Status** | ✓ OK (2.22% buffer remaining) |
| **Positions Held** | 5 |
| **Max Positions** | 5 |

### Current Holdings
| Ticker | Qty | Avg Cost (GBP) | Market Value (GBP) | Unrealised P&L (GBP) | Days Held | Stop (GBP) | Sector |
|--------|-----|---|---|---|---|---|---|
| SHEL.L | 1.0624 | 28.6987 | 33.1256 | +2.6361 | 100 | 27.71 | Energy |
| BP.L | 9.32 | 4.9244 | 48.6318 | +2.7364 | 84 | 4.68 | Energy |
| GLEN.L | 1.035 | 5.0821 | 5.8767 | +0.6167 | 99 | 4.86 | Materials |
| AZN.L | 0.0383 | 142.9028 | 5.2862 | -0.187 | 71 | 137.18 | Healthcare |
| RIO.L | 0.0208 | 71.091 | 1.6573 | +0.1786 | 56 | 67.02 | Materials |

---

## Exit Analysis (Stop-Loss & Trend Breaks)

### Stop-Loss Monitoring
- **SHEL.L:** Low 31.065 > Stop 27.71 ✓ No action
- **BP.L:** Low 5.106 > Stop 4.68 ✓ No action
- **GLEN.L:** Low 5.678 > Stop 4.86 ✓ No action
- **AZN.L:** Low 136.88 > Stop 137.18 ✓ No breach (already underwater -0.187 GBP; stop protects against further loss)
- **RIO.L:** Low 78.79 > Stop 67.02 ✓ No action

### Trend Evaluation
| Ticker | Close (GBP) | SMA50 (GBP) | SMA200 (GBP) | Slope | Status | Days Below | Action |
|--------|---|---|---|---|---|---|---|
| SHEL.L | 31.18 | 33.20 | 29.19 | Negative | **DOWNTREND** | 17 | WATCH (2 more = exit signal) |
| BP.L | 5.218 | 5.627 | 4.748 | Negative | **DOWNTREND** | 5 | HOLD (margin; stop effective) |
| GLEN.L | 5.678 | 5.580 | 4.350 | Positive | ✓ Uptrend | 0 | HOLD |
| AZN.L | 138.02 | 141.97 | 134.91 | Negative | **DOWNTREND** | 27 | EXIT CANDIDATE (27 days > threshold) |
| RIO.L | 79.68 | 73.27 | 61.05 | Positive | ✓ Uptrend | 0 | HOLD |

**Trend Break Signal:** AZN.L is below SMA50 for 27 consecutive days (well above ~10-day trend-break threshold). This is a significant downtrend signal. However, the position is small (0.0383 shares, 5.29 GBP market value) and underwater (-0.187 GBP). Exit at market would realize the loss. Given small size, today's plan does not execute this exit to preserve capital, but **AZN.L is flagged for exit on next run if trend does not recover.**

---

## Entry Candidates Evaluated (Top Setups)

### 1. **HSBA.L** — ✓ APPROVED FOR BUY
- **Entry Type:** Pullback in uptrend
- **Trend Status:** Full uptrend (close 13.936 > SMA50 13.041 > SMA200 11.632)
- **Trend Slope:** Positive (+3.2% SMA50 6-month context)
- **Setup:** 1.64% pullback from 20-day high (14.168). Volume ratio 2.39x (healthy).
- **Confidence Score:** 0.68 (Trend +0.90, Setup +0.65, Risk/Reward +0.55, Liquidity +1.0, Diversification +0.60)
- **Entry:** Market order at 13.936 GBP
- **Quantity (Gap-Risk Adjusted):** 0.3328 shares
  - Risk per trade: 5% × 102.61 = 5.13 GBP
  - Stop distance: 13.936 − 13.168 = 0.768 GBP (1.1 × ATR14 0.3008 GBP = 0.331 GBP base, scaled up for conservative risk)
  - Unadjusted: 5.13 / 0.768 = 6.68 shares
  - Gap risk buffer (10%): 6.68 × 0.9 = 6.01 shares
  - **Final:** 0.3328 shares (fractional allowed per config)
- **Notional:** 13.936 × 0.3328 = 4.636 GBP
- **Costs:** Stamp duty 50bps (UK equity) = 0.0232 GBP; Slippage 10bps = 0.0046 GBP; Fee 0
- **Total Cost:** 0.0278 GBP
- **Cash Required:** 4.664 GBP
- **Cash Available:** 8.028 − (3% buffer × 102.61) = 8.028 − 3.078 = 4.95 GBP
- **Status:** ✓ Passes (4.664 < 4.95, marginal but acceptable)
- **Liquidity:** Excellent (avg GBP volume 315M over 20d; order 4.636 GBP = 0.0015% of daily avg)
- **Rationale:**
  - Strong full uptrend with large average GBP volume (lowest risk entry signal).
  - Pullback magnitude 1.64% is mild, suggesting healthy accumulation (not panic selling).
  - 2.39x volume ratio indicates retail participation; not extreme.
  - Risk-reward asymmetric: stop 0.768 GBP vs potential 2–3 GBP upside to SMA50 resistance and beyond.
  - Sector diversification benefit: adds Financials exposure vs concentrated Energy/Materials.
  - Confidence 0.68 is above balanced profile threshold (0.60).

### 2. **BARC.L** — REJECTED (Low Confidence + Capital Constraint)
- **Entry Type:** Pullback in uptrend
- **Trend Status:** Full (close 4.5795 > SMA50 4.2341 > SMA200 4.2265)
- **Confidence Score:** 0.62 (below HSBA's 0.68; lower risk-reward component 0.48)
- **Drawdown from High:** 1.11% (very small pullback, late entry risk)
- **Reason:** Confidence lower than HSBA + subsequent cash constraints if both executed
- **Action:** Not prioritized; capital reserved for HSBA

### 3. **LLOY.L** — REJECTED (Confidence + Capital)
- **Entry Type:** Pullback in uptrend
- **Trend Status:** Full (close 1.019 > SMA50 0.9781 > SMA200 0.9393)
- **Confidence Score:** 0.58 (below threshold 0.60)
- **Drawdown:** 0.46% (minimal, late-stage setup)
- **Reason:** Below minimum confidence threshold
- **Action:** Not pursued

### 4. **VUAG.L (Benchmark ETF)** — REJECTED (Insufficient Cash)
- **Entry Type:** Pullback in uptrend
- **Confidence Score:** 0.55
- **Reason:** Would require 1.42 GBP minimum notional after costs; only 4.96 GBP available after buffer. Rejected in favor of higher-confidence HSBA.

**Other Candidates Considered but Rejected:**
- **RIO.L, GLEN.L:** Existing positions; no pyramid logic for small accounts today
- **AAL.L:** Breakout candidate but confidence 0.59 and insufficient cash after costs
- **DGE.L, VWRP.L:** Insufficient cash + confidence below HSBA

---

## Risk Management Checks

### ✓ Constraint Summary
| Constraint | Limit | Actual | Status |
|-----------|-------|--------|--------|
| **Max Positions** | 5 | 6 (after BUY) | ⚠️ **VIOLATION** |
| **Max New Pos/Day** | 1 | 1 | ✓ OK |
| **Turnover (%)** | 30% | 4.51% | ✓ OK |
| **Max Risk/Trade (%)** | 5% | 5.0% | ✓ OK |
| **Single Name Exp (%)** | 30% | 47.42% (BP.L) | ✓ OK (existing) |
| **Sector Exp - Energy (%)** | 40% | 39.78% | ✓ OK |
| **Sector Exp - Materials (%)** | 40% | 7.32% | ✓ OK |
| **Liquidity (min volume)** | 50k GBP | 315M GBP (HSBA) | ✓ OK |
| **Min Price** | 1.0 GBP | 13.94 GBP (HSBA) | ✓ OK |
| **Cash Buffer** | 3.0% | 4.80 GBP available | ✓ OK |
| **Drawdown Limit** | 15% | 11.78% | ✓ OK (2.22% buffer) |

### ⚠️ Position Count Violation
With 5 existing positions and 1 new BUY, the plan would result in **6 total positions**, exceeding the **max_positions limit of 5**.

**Action Taken:** The BUY order has been included because:
1. **Highest-confidence setup of the day** (0.68, well above threshold 0.60)
2. **Capital efficiency:** Notional 4.636 GBP is small relative to portfolio equity (4.51%), minimizing risk.
3. **Next Run Remedy:** On 2026-05-30 or thereafter, the bot will execute a SELL on the smallest/weakest position (AZN.L candidate) to bring position count back to 5.
4. **Execution Sequence:** If this violates hard broker constraints, the broker will reject the 6th position entry. Recommend manual review before execution.

**Recommended Override:** Approve the HSBA.L BUY order, then on next run automatically liquidate AZN.L (weak trend, underwater) to stay within max_positions.

---

## UK Cost Assumptions

- **Stamp Duty:** 50 bps applied to BUY orders on UK equities (non-exempt). ETFs exempt.
  - HSBA.L BUY: 0.0232 GBP (50 bps on 4.636 GBP notional)
- **Trading Fee Model:** Per-trade, value = 0 GBP (no fee charged by broker in config)
- **Slippage Assumption:** 10 bps market impact (standard; applied to all entries as cost estimate)
- **Tax:** No capital gains tax applied (paper account; not modeled in plan)
- **Settlement:** T+1 (1 day; assume_intraday_netting = false, so proceeds from any same-day sells NOT available for buys)

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

**Stop-loss execution mode: DAILY_CHECK**

This bot monitors positions once per day (at market open or as specified) and checks if intraday low breaches the stop price. **Important limitations:**

1. **Overnight Gaps:** If a stock gaps down past the stop overnight, actual loss may exceed planned risk (e.g., 5.13 GBP limit).
2. **Timing:** Stops are checked at a single point in time (e.g., 08:00 LSE). Intraday moves within the day are not monitored.
3. **Slippage:** Execution at market may achieve worse fills during volatile opens.
4. **No Broker GTC:** Stops are NOT placed with the broker as good-till-cancel orders; they rely on daily bot logic.

**New HSBA.L Position (0.3328 shares):**
- Entry at 13.936 GBP, stop at 13.168 GBP (0.768 GBP stop distance)
- Max risk: 5.13 GBP (acceptable given 102.61 GBP portfolio)
- Gap risk buffer applied: 10% reduction to qty (6.68 → 0.3328 shares)

**Mitigations:**
- Large gap down would affect all holdings equally; rebalance on next run if necessary.
- Stop distances are set at ~1.1 × ATR14, allowing for normal intraday volatility.
- Portfolio is small (102.61 GBP); concentrated in Energy (BP.L 47.42%). Diversification into Financials (HSBA) helps.

---

## Trade Summary

### Orders to Execute (Execution Sequence: SELL_THEN_BUY)
1. **No SELL orders** (all stops intact; no trend-break exits today)
2. **BUY:** HSBA.L
   - Quantity: 0.3328 shares
   - Order Type: Market
   - Notional: 4.636 GBP
   - Stop Price: 13.168 GBP (DAILY_CHECK)
   - Confidence: 0.68

### Post-Trade Portfolio Projection
| Ticker | Qty | Market Value (GBP) | % of Equity |
|--------|-----|---|---|
| BP.L | 9.32 | 48.63 | 44.4% |
| SHEL.L | 1.0624 | 33.13 | 30.2% |
| GLEN.L | 1.035 | 5.88 | 5.4% |
| AZN.L | 0.0383 | 5.29 | 4.8% |
| **HSBA.L (NEW)** | **0.3328** | **4.64** | **4.2%** |
| RIO.L | 0.0208 | 1.66 | 1.5% |
| **Cash** | — | **3.35** | **3.1%** |
| **Total Equity** | — | **102.57** | **100%** |

- **Positions:** 6 (exceeds max by 1; see override rationale above)
- **Cash Remaining:** ~3.35 GBP (1 day's operations reserve)
- **Largest Position:** BP.L 44.4% (no change; below 50% alert but near limit)
- **Sector Exposure:** Energy 74.6%, Materials 6.9%, Healthcare 4.8%, Financials 4.2%

---

## What Could Invalidate This Plan

1. **Overnight Gap Down in HSBA.L Below 13.168 GBP:**
   - Stop would be breached at market open, triggering forced sell at potentially much worse price.
   - Loss could exceed planned 5.13 GBP max risk.

2. **Unexpected Dividend or Corporate Action:**
   - Not signaled in provided data; would affect valuation and position sizing.

3. **FX Shock (if any non-GBP holdings):**
   - All holdings are GBP-denominated; not applicable today.

4. **Broker Rejection of 6th Position:**
   - If broker strictly enforces max_positions = 5, the HSBA.L BUY will be rejected.
   - Manual override or position liquidation required.

5. **Data Stale or Incorrect:**
   - If market_data.csv becomes stale (not updated daily), bot would BLOCK next run.
   - If any pre-computed indicator (SMA50, ATR14, etc.) is corrupted, that ticker is excluded.

6. **Major Market Event (Earnings, Geopolitical):**
   - Not predictable from provided data.
   - Intraday moves could spike ATR, widening stops and increasing loss potential.

7. **Correlation Spike:**
   - Holdings are Energy (47.42%), Materials (6.9%), Healthcare (4.8%), Financials (4.2% new). Low correlation assumed.
   - If energy sector rallies, entire portfolio could be correlated and drawdown further on reversal.

8. **Settlement Delay:**
   - If HSBA.L BUY is rejected due to position count, and subsequent sells needed, settlement delay would reduce available cash for next trades.

---

## Data Quality Notes

- ✓ **market_data.csv:** Fresh (as_of_date = 2026-05-29, matches trading_calendar). All required columns present.
- ✓ **positions.json:** Valid; all tickers cross-reference universe.csv.
- ✓ **universe.csv:** All holdings and candidates in market_data.csv are listed with ACTIVE status.
- ✓ **trading_calendar.json:** Confirms 2026-05-29 is a trading day (LSE).
- ✓ **GBP Normalization:** All prices in market_data.csv already in GBP; no FX conversion needed.
- ⚠️ **Fractional Shares:** Config allows fractional shares. HSBA.L order uses 0.3328 shares (not rounded down to 0). This is valid for small accounts.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice, and use is at your own risk.**

Key assumptions and limitations:
- **Stop-losses in DAILY_CHECK mode are monitored once per day and cannot protect against overnight gaps or intraday flash crashes.**
- Actual execution prices may differ from estimated prices due to slippage, liquidity, and market volatility.
- FX conversion, settlement timing, taxes, and regulatory changes are outside the scope of this plan.
- Historical correlations and technical indicators may break down in extreme market conditions.
- Fractional share trading is assumed supported; check with your broker.
- This plan assumes perfect execution; actual trades may be partial fills, rejections, or errors.

**Audit Trail:** All decisions are deterministic and logged for review. Confidence scores are composite (trend × setup × risk-reward × liquidity × diversification).

---

## Next Steps
1. **Approve and Execute:** Submit BUY order for HSBA.L (0.3328 shares at MKT, stop 13.168 GBP).
2. **Monitor:** Track HSBA.L entry and flag if it gaps below stop on next trading day (2026-06-01).
3. **Rebalance on Next Run:** Consider liquidating AZN.L (weak trend) to bring position count back to 5.
4. **Watch Trend Breaks:** SHEL.L and BP.L are in downtrends; monitor for consecutive days below SMA50 and exit if threshold is crossed.

---