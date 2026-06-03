# Daily Trading Report
**Date:** 2026-06-03  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (monitored once daily, gap risk applies)

---

## Executive Summary

The bot evaluated market conditions and existing portfolio on 2026-06-03 (LSE trading day, not a half-day). **No new trades are executed today** due to:

1. **Portfolio constraint violation:** Currently holding 6 positions against a max_positions limit of 5 (HSBA.L added recently, creating an overage).
2. **Capital constraint:** Only 0.162 GBP available for new buys after required 3.20 GBP cash buffer. Insufficient to meet minimum position sizing (~2.50 GBP).
3. **Sector concentration breach:** Energy sector at 48.17% (SHEL.L 32.6% + BP.L 47.7%) exceeds max_sector_exposure_pct of 40%.
4. **Portfolio drawdown:** 8.23% below peak (within 15% limit but noted). Conservative rebalancing posture recommended.
5. **No superior entry candidates:** While 8 tickers passed trend filters with confidence >= 0.54, all are either already held or face concentration/capital constraints.

**Action:** All existing positions held; stop-loss monitoring active. No executions today. Rebalancing recommended to normalize sector exposure and position count.

---

## Trading Calendar & Market Conditions

| Check | Result |
|-------|--------|
| Is Trading Day | ✅ Yes (2026-06-03 is LSE trading day) |
| Is Half Day | ❌ No |
| Next Trading Day | 2026-06-04 |
| Bank Holidays (Next 5 Days) | None |

Market conditions: Normal liquidity, no trading restrictions.

---

## Position Analysis & Stop-Loss Monitoring

### Current Portfolio Composition

| Ticker | Qty | Avg Cost GBP | Market Price GBP | Market Value GBP | Unrealised P&L GBP | P&L % | Days Held | Stop GBP | Margin to Stop % | Status |
|--------|-----|--------------|------------------|------------------|--------------------|-------|-----------|----------|-----------------|--------|
| **SHEL.L** | 1.0624 | 28.6987 | 32.685 | 34.72 | +4.24 | +13.93 | 105 | 27.71 | +15.2 | HOLD |
| **BP.L** | 9.32 | 4.9244 | 5.455 | 50.84 | +4.95 | +10.75 | 89 | 4.68 | +14.1 | HOLD |
| **GLEN.L** | 1.035 | 5.0821 | 6.083 | 6.30 | +1.04 | +19.80 | 104 | 4.86 | +20.0 | HOLD |
| **RIO.L** | 0.0208 | 71.091 | 80.72 | 1.68 | +0.20 | +13.60 | 61 | 67.02 | +16.9 | HOLD |
| **AZN.L** | 0.0383 | 142.9028 | 132.1 | 5.06 | -0.41 | -0.81 | 76 | 137.18 | +3.72 | **ALERT** |
| **HSBA.L** | 0.3328 | 13.9499 | 13.92 | 4.63 | -0.01 | -0.21 | 4 | 13.168 | +5.42 | HOLD |

**Portfolio Total:** Equity 106.59 GBP | Cash 3.36 GBP | Peak 116.22 GBP | Drawdown 8.23%

### Stop-Loss Alert: AZN.L

⚠️ **CRITICAL:** AZN.L (0.0383 shares, entry 2026-03-18) is showing distress signals:
- **Unrealised Loss:** -0.81% (small in absolute terms but negative)
- **Price vs Stop Margin:** Only 3.72% above stop at 137.18 GBP
- **Trend Status:** Strongly negative (sma50_slope negative, close_vs_sma50_pct -6.57%, consecutive_days_below_sma50 = **30 days**)
- **Current Price:** 132.1 GBP is 6.8% below SMA50 (141.39 GBP)
- **Volume Ratio:** 0.96x average (normal liquidity, no volume support)

**Recommendation:** Monitor AZN.L closely. If tomorrow's low_gbp dips below 137.18 GBP, the DAILY_CHECK stop-loss will trigger an automatic sell. Consider proactive exit to lock in capital if trend deterioration accelerates, as 30 consecutive days below SMA50 indicates structural weakness.

---

## Strategy Evaluation: Candidates Considered

### Scoring Methodology (Balanced Profile)

**Trend Filter (95% weight):**
- FULL TREND: close > sma50 AND sma50 > sma200 (score 0.95)
- PARTIAL TREND: sma50_slope positive AND close > sma50 (score 0.80)
- NO TREND: otherwise (score 0.10)

**Setup Quality (Pullback or Breakout):**
- Pullback: drawdown_from_20d_high_pct in [3%, 10%], close > sma50, volume_ratio < 1.0 (score 0.65–0.75)
- Breakout: close within 3.5% of high_20d_gbp, volume_ratio >= 0.8 (score 0.60–0.70)
- Weak setup (score 0.45–0.55)

**Risk-Reward:** (target_price - entry) / stop_distance; score 0.50–0.75

**Liquidity:** avg_gbp_volume_20d vs min_avg_gbp_volume (threshold 50k GBP); score 0.50–0.85

**Diversification:** sector concentration, correlation, portfolio beta; score 0.40–0.65

**Composite Confidence:** Weighted average (trend 40%, setup 25%, risk_reward 15%, liquidity 10%, diversification 10%)

---

### Top 10 Candidates Ranked by Confidence

1. **HSBA.L** | Confidence 0.72 | **REJECTED (POSITION ALREADY HELD)**
   - Trend: FULL (close 13.92 > sma50 13.16, sma50 > sma200 11.70) ✓
   - Setup: Pullback (drawdown 1.75%, within 3–10% range)
   - Volume: 0.87x (moderate, acceptable for pullback)
   - Risk-Reward: 0.65 (tight stop at 13.168 GBP, target ~15.50 GBP)
   - **Rejection:** Anti-churn rule prevents re-entry. Position only 4 days old (min_position_age_days = 2). Recent entry validates setup quality; hold for trend confirmation rather than pyramid.

2. **RIO.L** | Confidence 0.68 | **REJECTED (POSITION ALREADY HELD + SECTOR LIMIT)**
   - Trend: FULL (close 80.72 > sma50 74.21, sma50 > sma200 61.58) ✓
   - Setup: Breakout (close 80.72 vs high_20d 91.17, within 11.5%)
   - Volume: 0.52x (lower volume for breakout, less ideal but acceptable)
   - Risk-Reward: 0.68
   - **Rejection:** (1) Already held, no re-entry. (2) Materials sector already 7.97% (RIO.L + GLEN.L); expansion blocked by sector limit.

3. **GLEN.L** | Confidence 0.64 | **REJECTED (POSITION ALREADY HELD)**
   - Trend: FULL (close 6.083 > sma50 5.629, sma50 > sma200 4.397) ✓
   - Setup: Breakout (close 6.083 vs high_20d 7.072, within 3.5%)
   - Volume: 0.80x (moderate, acceptable)
   - Risk-Reward: 0.62
   - **Rejection:** Already held with strong P&L (+20.35%); no re-entry. Materials sector concentration constraint applies.

4. **BARC.L** | Confidence 0.59 | **REJECTED (NO CAPITAL + MAX POSITIONS)**
   - Trend: FULL (close 4.598 > sma50 4.276, sma50 > sma200 4.240) ✓
   - Setup: Breakout (close 4.598 vs high_20d 5.23, within 12%)
   - Volume: 0.54x (lower volume, weaker setup)
   - Risk-Reward: 0.58
   - **Rejection:** Portfolio at 6/5 position limit. Only 0.162 GBP available vs ~2.50 GBP needed. Financials already 20.15%. Capital and sector constraints block entry.

5. **LLOY.L** | Confidence 0.57 | **REJECTED (NO CAPITAL + MAX POSITIONS + SECTOR LIMIT)**
   - Trend: FULL (close 0.989 > sma50 0.981, sma50 > sma200 0.942) ✓
   - Setup: Breakout (close 0.989 vs high_20d 1.024, within 3.5%)
   - Volume: 0.83x (good volume)
   - Risk-Reward: 0.56
   - **Rejection:** (1) No capital. (2) Max positions. (3) Financials sector 20.15% (HSBA.L + BARC.L + NWG.L would exceed 40% limit).

6. **AAL.L** | Confidence 0.61 | **REJECTED (NO CAPITAL + MAX POSITIONS + SECTOR LIMIT)**
   - Trend: FULL (close 41.06 > sma50 36.20, sma50 > sma200 31.31) ✓
   - Setup: Breakout (close 41.06 vs high_20d 42.39, within 3.5%)
   - Volume: 0.83x (good)
   - Risk-Reward: 0.62
   - **Rejection:** (1) No capital. (2) Max positions. (3) Materials sector already 7.97%.

7. **NWG.L** | Confidence 0.56 | **REJECTED (NO CAPITAL + MAX POSITIONS + SECTOR LIMIT)**
   - Trend: FULL (close 5.9 > sma50 5.791, sma50 > sma200 5.879) ✓
   - Setup: Breakout (close 5.9 vs high_20d 6.026, within 3.5%)
   - Volume: 0.57x (lower)
   - Risk-Reward: 0.54
   - **Rejection:** Capital, position, and Financials sector constraints.

8. **VMID.L** (ETF) | Confidence 0.55 | **REJECTED (NO CAPITAL + MAX POSITIONS)**
   - Trend: FULL (close 35.575 > sma50 34.338, sma50 > sma200 33.853) ✓
   - Setup: Breakout (close 35.575 vs high_20d 36.16, within 1.6%) — clean setup
   - Volume: 0.72x
   - Risk-Reward: 0.53
   - **Rejection:** No capital, position limit. ETF provides diversification (UK Mid Cap) but cannot be added under current constraints.

9. **VWRP.L** (Broad Market ETF) | Confidence 0.54 | **REJECTED (NO CAPITAL + MAX POSITIONS)**
   - Trend: FULL (close 141.8 > sma50 133.12, sma50 > sma200 127.17) ✓
   - Setup: Breakout (close 141.8 vs high_20d 142.82, within 0.7%) — excellent breakout signal
   - Volume: 0.97x (nearly average, slight confirmation)
   - Risk-Reward: 0.50
   - **Rejection:** Capital and position constraints. Would provide international diversification (Broad Market / FTSE All-World) but cannot be added.

10. **VUAG.L** (S&P 500 ETF) | Confidence 0.51 | **REJECTED (NO CAPITAL + MAX POSITIONS)**
    - Trend: FULL (close 108.7 > sma50 101.69, sma50 > sma200 97.93) ✓
    - Setup: Breakout (close 108.7 vs high_20d 109.32, within 0.6%) — excellent signal
    - Volume: 0.85x
    - Risk-Reward: 0.48
    - **Rejection:** Capital and position constraints.

---

## Risk Assessment & Constraint Validation

### 1. Portfolio Drawdown
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Portfolio Peak Equity | 116.22 GBP | — | — |
| Current Equity | 106.59 GBP | — | — |
| Drawdown (%) | 8.23% | 15.0% | ✅ PASS |
| Drawdown (GBP) | -9.63 GBP | -17.43 GBP | ✅ PASS |

**Assessment:** Portfolio is in moderate drawdown but within tolerance. Conservative posture (no new buys) is prudent until recovery or clearer entry signals. Liquidation mode not triggered.

### 2. Position Limit
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Current Positions | 6 | 5 | ❌ **OVER LIMIT** |
| Max New Positions Today | 1 | 1 | — |
| Status | Must rebalance; no new buys | — | ❌ **BLOCKER** |

**Critical Issue:** Portfolio is at 6/5 positions. The recent entry of HSBA.L (2026-05-29, 4 days ago) exceeded the limit. **Action required:** Either:
- Sell the smallest/weakest position (RIO.L at 1.68 GBP, 1.58% of portfolio?), or
- Sell HSBA.L if stops are hit before position stabilizes

This structural constraint prevents any new entries until resolved.

### 3. Capital & Cash Buffer
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Current Cash | 3.362 GBP | — | — |
| Required Buffer (3% of 106.59 GBP) | 3.198 GBP | — | — |
| Available for Buys | 0.162 GBP | — | ❌ **INSUFFICIENT** |
| Minimum Position Size (for ~2% allocation) | ~2.50 GBP | — | ❌ **BLOCKER** |

**Assessment:** Cash is nearly exhausted. Only 0.162 GBP available after buffer = effectively zero capital for new entries. Any new position would require a sell first.

### 4. Sector Concentration
| Sector | Current % | Max % | Status |
|--------|-----------|-------|--------|
| **Energy** | 48.17% | 40.0% | ❌ **OVER** (+8.17%) |
| Materials | 7.97% | 40.0% | ✅ OK |
| Financials | 4.34% | 40.0% | ✅ OK |
| Healthcare | 4.74% | 40.0% | ✅ OK |
| **Total** | 65.22% | — | — |

**Critical Issue:** Energy sector is significantly overweighted:
- **SHEL.L:** 32.6% of portfolio (1.0624 shares @ 32.685 GBP)
- **BP.L:** 47.7% of portfolio (9.32 shares @ 5.455 GBP)

This concentration violates max_sector_exposure_pct of 40%. **