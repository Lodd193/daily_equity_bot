# Daily Trading Report
**Date:** 2026-02-19  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-02-20
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary

**NO TRADES are being generated today due to a critical liquidity and risk management issue.**

The portfolio is in a precarious financial state:
- **Portfolio Value:** £99.31 (down 0.88% from peak of £100.19)
- **Cash Balance:** £3.50
- **Required Cash Buffer (3%):** £2.98
- **Available for Trading:** £0.52

This situation creates three blocking constraints:

1. **Insufficient Liquidity for Position Sizing:** Even the most attractive opportunities (e.g., RIO.L with 0.72 confidence) require position costs exceeding £250 once stamp duty and slippage are factored in. Available cash of £0.52 is entirely inadequate.

2. **Existing Positions at Extreme Risk:** All three current positions are tightly bunched around their stop-loss prices with minimal downside margin:
   - **SHEL.L:** Stop 27.71, Low 20-day 26.66 (only 1.05 pence gap)
   - **GLEN.L:** Stop 4.86, Low 20-day 4.56 (only 0.30 pence gap) — CRITICAL
   - **AZN.L:** Stop 151.25, still viable but underwater

3. **Turnover and Position Limit Constraints:** Any new entry combined with potential stop-loss sales would violate max_turnover_pct_per_day (30%) and max_new_positions_per_day (1).

---

## Top 3 Setups Considered

### 1. RIO.L — Rio Tinto (Materials)
- **Setup Type:** PULLBACK in uptrend
- **Confidence Score:** 0.72 (composite)
  - Trend component: 1.0 (close > SMA50 > SMA200)
  - Setup component: 0.65 (drawdown_from_20d_high 4.08%, pullback timing favorable)
  - Risk/reward: 0.7 (stop distance 2.27 pence)
  - Liquidity: 0.92 (avg GBP volume £253M, excellent)
  - Diversification: 0.6 (Materials, but portfolio already 5.27% Materials)
- **Price Data:** Close 71.18, High 20-day 74.21, ATR14 2.27
- **Rejection Reason:** Insufficient cash. Position sizing requires ~£251.67 total outlay (notional ~£157 + stamp duty £78.65 + slippage £15.73). Available: £0.52. **BLOCKED.**

### 2. AZN.L — AstraZeneca (Healthcare)
- **Setup Type:** None (existing position)
- **Confidence Score:** 0.68
  - Trend component: 1.0 (close > SMA50 > SMA200)
  - Setup component: 0.6 (modest pullback: 2.8% from 20-day high)
  - Risk/reward: 0.65
  - Liquidity: 0.93 (avg GBP volume £338M)
  - Diversification: 0.4 (Healthcare already 59.75% of portfolio)
- **Price Data:** Close 152.90, Entry 155.38, Stop 151.25 (only 1.65 pence below current)
- **Rejection Reason:** Existing position with days_held=1 (min_position_age_days=2). Anti-churn rule prevents immediate re-entry. Additionally, position is underwater (-£0.96 unrealised) and stop is extremely tight.

### 3. SHEL.L — Shell (Energy)
- **Setup Type:** None (existing position)
- **Confidence Score:** Not re-evaluated (already held)
- **Price Data:** Close 29.44, Entry 28.70, Stop 27.71, High 20-day 29.625
- **Rejection Reason:** Already held with days_held=1. Only minor profit (+£0.79 unrealised) but critical stop placement: 20-day low is 26.66, creating only 1.05 pence gap above stop. High gap risk in DAILY_CHECK mode.

---

## Risk Constraint Checks

### Liquidity & Cash
| Check | Required | Current | Status |
|-------|----------|---------|--------|
| Cash buffer (3% of £99.31) | £2.98 | £3.50 | ✓ PASS (marginal) |
| Available for new trades | £0.52+ | £0.52 | **✗ FAIL** |
| Min GBP volume filter | £50k/day | All pass | ✓ PASS |
| Min price filter (£1.00) | All > £1.00 | All pass | ✓ PASS |

### Position & Exposure Limits
| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| Max positions | 5 | 3 | ✓ PASS |
| Max new positions/day | 1 | 0 planned | ✓ PASS |
| Single name (AZN.L) | 30% | 59.75% | **✗ FAIL** |
| Sector (Healthcare) | 40% | 59.75% | **✗ FAIL** |
| Sector (Energy) | 40% | 31.52% | ✓ PASS |
| Sector (Materials) | 40% | 5.27% | ✓ PASS |

**Note:** Portfolio concentration is dangerously high. AZN.L alone is 59.75% of portfolio, well above the 30% single-name limit. Healthcare sector is 59.75%, exceeding the 40% sector limit. This imbalance, combined with AZN.L being underwater and positioned close to its stop, creates additional risk.

### Turnover
- Planned turnover: 0% (no new trades)
- Max allowed: 30% of £99.31 = £29.79
- **Status:** ✓ PASS (but irrelevant given no trades)

### Stop-Loss Monitoring (DAILY_CHECK Mode)
| Ticker | Current | Stop | Distance | 20-day Low | Gap Risk | Status |
|--------|---------|------|----------|-----------|----------|--------|
| SHEL.L | 29.44 | 27.71 | +1.73p | 26.66 | HIGH | MONITOR |
| AZN.L | 152.90 | 151.25 | +1.65p | 133.25 | MODERATE | MONITOR |
| GLEN.L | 5.05 | 4.86 | +0.19p | 4.56 | **CRITICAL** | MONITOR |

**Critical Alert:** GLEN.L has a 20-day low of 4.56 pence, only 0.30 pence below its stop of 4.86. This is an extremely tight margin. Any weakness that revisits the 20-day low will trigger the stop-loss. The position was entered yesterday (days_held=0) and is already underwater (entry 5.08, current 5.05). **Recommend immediate review.**

### Portfolio Drawdown
- **Current Drawdown:** 0.88% [(£100.19 - £99.31) / £100.19]
- **Limit:** 15%
- **Status:** ✓ PASS (well within limit)
- **Note:** Drawdown is minimal in percentage terms but portfolio is operationally insolvent due to cash constraints, not mark-to-market loss.

---

## Portfolio Snapshot

### Current Positions
| Ticker | Quantity | Avg Cost (GBP) | Current Price (GBP) | Market Value (GBP) | Unrealised P&L (GBP) | Entry Date | Days Held | Stop (GBP) | Status |
|--------|----------|----------------|-------------------|------------------|------------------|-----------|-----------|-----------|--------|
| AZN.L | 0.3879 | 155.38 | 152.90 | 59.31 | -0.96 | 2026-02-17 | 1 | 151.25 | ACTIVE |
| SHEL.L | 1.0624 | 28.70 | 29.44 | 31.28 | +0.79 | 2026-02-17 | 1 | 27.71 | ACTIVE |
| GLEN.L | 1.0350 | 5.08 | 5.05 | 5.23 | -0.03 | 2026-02-18 | 0 | 4.86 | ACTIVE |

**Portfolio Composition:**
- Healthcare: 59.75% (OVER LIMIT)
- Energy: 31.52%
- Materials: 5.27%
- Utilities/Other: 3.46% (cash)

**Total Equity Value:** £99.31  
**Total Cash:** £3.50  
**Net Liquid Assets:** £102.81

---

## Cost Assumptions

**Fee Model:** Per-trade, £0 per transaction  
**Stamp Duty:** 0.5% on UK equity purchases only (ETFs exempt)  
**Slippage Assumption:** 10 basis points (0.1%) on entry/exit notional  
**Settlement:** T+1 (1 day), assume_intraday_netting = false (today's sell proceeds NOT available for today's buys)

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

**Critical:** The bot monitors stop-losses once daily. Overnight gaps, opening gaps, or intraday moves can bypass stops entirely. Examples from today's positions:

- **SHEL.L:** If market opens below 27.71 (20-day low is 26.66), stop would be executed at market price, potentially 0–1.05 pence lower than stop price.
- **GLEN.L:** Gap risk is CRITICAL. 20-day low 4.56 is 0.30 pence below stop 4.86. Any overnight weakness risks execution at or below 4.60, triggering a loss on top of the existing -£0.03 unrealised loss.

**Mitigation:** Use broker GTC (Good-Till-Cancelled) stops if available, or accept that worst-case execution in a gap scenario may be at the 20-day low.

---

## What Could Invalidate This Plan?

1. **Gap up in AZN.L or SHEL.L:** If either stock rallies sharply at open, reducing stop-loss risk and freeing up mental capital for new entries.
2. **Sudden cash injection:** Dividend, corporate action, or external deposit would relax liquidity constraints.
3. **Stop-loss execution(s):** If GLEN.L stops out at market, would free ~£5 and allow a modest new position entry (though turnover constraints would still apply).
4. **Market-wide reversal:** If LSE 100 weakens significantly, all three holdings could approach stops simultaneously, forcing rapid liquidation at disadvantageous prices.
5. **Data quality issue:** If today's market data proves stale (older than 2026-02-19), the plan would be invalidated and re-run.

---

## Data Quality Notes

- ✓ Market data is fresh (as_of_date = 2026-02-19 = today)
- ✓ All required pre-computed indicator columns present
- ✓ No DELISTING or SUSPENDED statuses in universe
- ✓ No missing or null values in key fields (SMA50, SMA200, ATR14 all provided)
- ✓ Trading calendar confirms LSE is open today
- ⚠ WARNING: Very high concentration in AZN.L (59.75%) violates max_single_name_exposure_pct (30%). This is a pre-existing portfolio state, not a new-trade issue, but represents elevated idiosyncratic risk.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

Execution risks, overnight gaps, slippage, FX effects (if any), settlement timing, taxes, and fees all apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight price gaps. Actual execution prices may differ materially from planned prices. Use this plan at your own risk and always consult a qualified financial advisor before trading.

The portfolio's tight stop placements and critical cash shortage mean that a single adverse market move could trigger cascading liquidations. Risk management should be reviewed immediately.

---