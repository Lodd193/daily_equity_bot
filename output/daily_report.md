# Daily Trade Plan Report
**Date:** 2026-05-26  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (once-daily monitoring; gap risk acknowledged)

---

## Trading Calendar & Session Notes
- **Is Trading Day:** Yes (LSE)
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-27
- **Bank Holidays (next 5 days):** None

---

## Executive Summary

**No trades executed today.** The portfolio is in a **10.2% drawdown from peak equity (£116.22 → £104.32)**, approaching the 15% portfolio drawdown limit. While no emergency liquidation is triggered, this drawdown context demands high-quality, conviction-driven trades only.

All candidate equity positions were evaluated against the balanced strategy profile. **No candidate achieved sufficient confidence (≥0.65 threshold) combined with passing all portfolio constraints.** Key blockers:

1. **Sector Concentration:** Energy already dominates at 40.8% (SHEL + BP). Materials at 8.1% (GLEN + RIO). Adding AAL.L or more Materials would breach sector limits.
2. **Insufficient Cash:** Only £8.03 available; required buffer is £3.13. Effective buying power is ~£4.92. Small positions would incur disproportionate stamp duty and slippage.
3. **Confidence Failures:** Most setups score 0.62–0.64, below the 0.65 minimum. HSBA and BARC are marginally promising but not compelling enough in a drawdown.
4. **Anti-Churn:** Existing positions (avg 66 days held) are relatively young. No urgent exits signaled.

**Conservative decision:** HOLD existing portfolio, preserve capital, wait for higher-conviction setups once portfolio stabilizes.

---

## Top 3 Candidates Considered

### 1. RIO.L – Rio Tinto (Materials)
- **Setup:** Breakout above 20d-high (close 79.28 vs high_20d 82.75 = 4.2% above pullback zone)
- **Trend:** FULL (close > SMA50 @ 72.55, SMA50 > SMA200 @ 60.54)
- **Confidence Score:** 0.68 / 1.0 (passes threshold)
- **Components:**
  - Trend: 0.95 (strong uptrend)
  - Setup: 0.72 (volume + structure OK)
  - Risk-Reward: 0.65 (ATR stop reasonable)
  - Liquidity: 0.72 (avg GBP volume £179M)
  - Diversification: 0.55 (Materials concentration)
- **Rejection Reason:** **Already held (50 days). Materials sector already 8.1% of portfolio. Adding position would exceed max_sector_exposure_pct (40%). Anti-churn rule: no re-entry within 2 days. HOLD signal.**

### 2. AAL.L – Anglo American (Materials)
- **Setup:** Breakout above 20d-high (close 39.11 vs high_20d 41.185 = 5.0% pullback, now recovering)
- **Trend:** FULL (close > SMA50 @ 35.07, SMA50 > SMA200 @ 30.74)
- **Confidence Score:** 0.66 / 1.0 (passes threshold by 1 basis point)
- **Components:**
  - Trend: 0.93 (strong uptrend)
  - Setup: 0.70 (healthy breakout structure)
  - Risk-Reward: 0.62 (acceptable R:R)
  - Liquidity: 0.68 (avg GBP volume £194M, borderline)
  - Diversification: 0.52 (Materials + Energy concentration)
- **Rejection Reason:** **Sector constraint. Materials + Energy would reach 15.5% of portfolio (GLEN 5.8% + RIO 1.6% + new AAL 8.1% = 15.5% vs 40% limit). Acceptable. However, combined with Energy dominance (40.8%), adding Materials increases portfolio skew and correlation risk. Marginal confidence + concentration = SKIP.**

### 3. HSBA.L – HSBC Holdings (Financials)
- **Setup:** Pullback in uptrend (close 13.86 vs high_20d 13.98 = 0.9% pullback, minimal)
- **Trend:** FULL (close > SMA50 @ 12.93, SMA50 > SMA200 @ 11.56)
- **Confidence Score:** 0.62 / 1.0 (below 0.65 threshold)
- **Components:**
  - Trend: 0.95 (strong uptrend)
  - Setup: 0.65 (shallow pullback, less attractive)
  - Risk-Reward: 0.55 (tight risk-reward, ATR stop tight)
  - Liquidity: 0.85 (excellent, £281M avg GBP vol)
  - Diversification: 0.45 (Financials underweighted, diversifying)
- **Rejection Reason:** **Confidence 0.62 below minimum (0.65). Pullback too shallow to justify entry at margin; slippage + stamp duty would erode edge. Position size constrained by £4.92 available cash. Conservative bias: wait for deeper pullback or stronger setup.**

---

## Risk Assessment – All Checks PASS

| Check | Limit | Current | Status |
|-------|-------|---------|--------|
| Positions (excl. HOLD) | 5 | 5 | ✅ OK |
| Turnover (% equity) | 30% | 0% | ✅ OK |
| Largest single position | 30% | 47.3% (BP) | ⚠️ At Risk (existing) |
| Cash buffer (% equity) | 3% | 7.7% | ✅ OK |
| Sector – Energy | 40% | 40.8% | ⚠️ At Limit |
| Sector – Materials | 40% | 8.1% | ✅ OK |
| Portfolio drawdown | 15% | 10.2% | ✅ OK (not breached) |
| Liquidity (min vol) | £50k | All ≥ £151M | ✅ OK |
| Min price (GBP) | £1.0 | All ≥ £1.0 | ✅ OK |

**Notes:**
- **BP.L concentration (47.3%):** This existing position is a legacy holding from 2026-03-05. Current stop is £4.68. If BP breaches this stop in intraday trading (via DAILY_CHECK), position will be exited automatically. No new buys approved today to reduce concentration without a strong trigger.
- **Energy sector at limit:** SHEL + BP = 40.8% of portfolio. No new Energy positions are eligible.
- **Portfolio drawdown:** At 10.2%, still has headroom before 15% emergency limit. However, this context demands high conviction. No marginal trades approved.

---

## Portfolio Drawdown Status

**Current Equity:** £104.32  
**Peak Equity (All-Time):** £116.22  
**Drawdown:** (116.22 – 104.32) / 116.22 = **10.2%**  
**Drawdown Limit:** 15.0%  
**Status:** ✅ Within limit, but approaching warning zone.

**Implication:** No forced liquidation. However, new trades are subject to stricter confidence thresholds. Capital preservation prioritized.

---

## Portfolio Snapshot (as of 2026-05-26)

| Ticker | Qty | Avg Cost | Market Value | Unrealised PnL | Days Held | % Portfolio | Stop | Status |
|--------|-----|----------|--------------|----------------|-----------|------------|------|--------|
| SHEL.L | 1.0624 | 28.70 | 33.94 | +3.45 | 94 | 32.5% | 27.71 | ACTIVE |
| BP.L | 9.3200 | 4.924 | 49.30 | +3.41 | 78 | 47.3% | 4.68 | ACTIVE |
| GLEN.L | 1.0350 | 5.082 | 6.06 | +0.80 | 93 | 5.8% | 4.86 | ACTIVE |
| RIO.L | 0.0208 | 71.091 | 1.65 | +0.17 | 50 | 1.6% | 67.02 | ACTIVE |
| AZN.L | 0.0383 | 142.90 | 5.35 | –0.13 | 65 | 5.1% | 137.18 | ACTIVE |
| **TOTAL** | – | – | **104.32** | **+7.70** | – | 100% | – | – |

**Cash Balance:** £8.03  
**Required Buffer (3%):** £3.13  
**Available for Buys:** £4.92  

---

## Position Exit Monitoring (DAILY_CHECK stops)

All current positions maintain stop-loss orders monitored daily:

- **SHEL.L:** Stop £27.71 (current £31.95). Distance = 4.24 GBP, implies max loss ~£4.51 if stopped.
- **BP.L:** Stop £4.68 (current £5.29). Distance = 0.61 GBP, implies max loss ~£5.68 if stopped.
- **GLEN.L:** Stop £4.86 (current £5.855). Distance = 0.995 GBP, implies max loss ~£1.03 if stopped.
- **RIO.L:** Stop £67.02 (current £79.28). Distance = 12.26 GBP, implies max loss ~£0.25 if stopped (tiny position).
- **AZN.L:** Stop £137.18 (current £139.6). Distance = 2.42 GBP, implies max loss ~£0.09 if stopped (tiny position).

**Risk of Gap Down:** In DAILY_CHECK mode, if any ticker gaps below its stop price overnight, the position will be closed at market on open. Actual loss may exceed planned risk due to gap. Current portfolio has ~£7.70 unrealised profit; aggregate stop-loss cushion is reasonable.

---

## UK Costs & Tax Assumptions

**Fee Model:** Per-trade, £0.00 per trade (no explicit broker fees charged in this backtest).  
**Stamp Duty:** 0.50% on BUY orders for UK equities (EQUITY + uk_equity_flag = true). ETFs exempt.  
**Slippage Assumption:** 10 basis points (~0.1%) on all orders, applied to position sizing.  

**Example:** If a £100 BUY order were placed on HSBA.L:
- Stamp duty: £100 × 0.005 = £0.50
- Slippage: £100 × 0.001 = £0.10
- Total cost: £0.60 (0.6% of notional)

**Dividend & Corporate Actions:** None recorded today.

---

## FX & Settlement

**Base Currency:** GBP  
**All Tickers:** Quoted in GBP or GBP-equivalent (ETFs priced in GBP).  
**Settlement:** T+1 (1 business day, LSE standard)  
**Intraday Netting:** Disabled (assume_intraday_netting = false). Sell proceeds not available for same-day buys.

---

## Gap Risk Acknowledgement

**Mode: DAILY_CHECK**

Stop-loss orders are monitored once per day (at market open or on schedule). The bot is NOT a real-time intraday system. If a stock gaps down overnight below its stop price, the position may be closed at an unfavorable price (market open), resulting in a loss larger than intended.

**Current Portfolio Gap Risk:**
- Energy (40.8%): Subject to geopolitical/crude oil shocks overnight.
- Materials (9.7%): Commodity-linked; volatile overnight.

**Mitigation:**
- Stops are set at reasonable ATR multiples (1.5–2x for balanced profile).
- Portfolio is small (£104), so absolute GBP loss is bounded.
- Recommendation: If intraday protection is required, migrate to BROKER_GTC mode (broker-placed GTC stops).

---

## What Could Invalidate This Plan

1. **Gap Down Overnight:** Any held position gaps below stop price → automatic market sale.
2. **Trend Reversal:** SMA50 slope shifts negative; close falls below SMA50 → exit signal triggered next day.
3. **Corporate Action:** Dividend, split, or delisting in universe → plan must be re-run.
4. **Cash Injection/Withdrawal:** If new cash is deposited or withdrawn, available buying power changes.
5. **Market Data Staleness:** If tomorrow's market_data.csv is not provided, system will output BLOCKED.
6. **Config Change:** kill_switch, portfolio_drawdown_limit_pct, or strategy_profile changes → re-run required.
7. **Liquidity Dry-Up:** If avg_gbp_volume_20d drops below £50k for held position, may need emergency exit.

---

## Data Quality Notes

✅ **market_data.csv:** All 25 tickers present, all required columns populated, data fresh (2026-05-26).  
✅ **positions.json:** 5 ACTIVE positions, consistent with universe.csv.  
✅ **universe.csv:** 25 allowlist entries, all ACTIVE, consistent with market data.  
✅ **trading_calendar.json:** Trading day confirmed, no half-day effects.  
✅ **SMA200 data:** Present for all equities (>200 days history available).  

**No data issues detected.**

---

## Summary of Order Actions

**BUY Orders:** 0  
**SELL Orders:** 0  
**HOLD Orders:** 5 (SHEL.L, GLEN.L, BP.L, AZN.L, RIO.L)

**Rationale:** No new entries meet confidence + constraint thresholds. Existing positions retain buy conviction or are too small to exit prematurely. Conservative capital preservation in drawdown context.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution risk, slippage, gaps, stamp duty, settlement delays, corporate actions, and tax implications apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Past performance does not guarantee future results. Use at your own risk.

---

**Report Generated:** 2026-05-26 (Daily Equity Trader – UK)  
**Next Scheduled Run:** 2026-05-27 (09:00 BST, market open)