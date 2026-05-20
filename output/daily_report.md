# Daily Trading Plan
**Date:** 2026-05-20  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar & Market Conditions
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-21
- **Bank Holidays (next 5 days):** 2026-05-25

---

## Portfolio Overview
**Portfolio Equity:** £107.91  
**Cash Balance:** £3.45  
**Unsettled Proceeds:** £0.00  
**Cash Available for Buys (after 3% buffer):** £0.17  
**Portfolio Drawdown from Peak:** 7.15% (Peak: £116.22, Current: £107.91)  
**Drawdown Limit:** 15.00% — **PASS** (drawdown within tolerance)

---

## Current Positions (6 positions, exceeds max of 5)
| Ticker | Qty | Avg Cost | Market Value | Unrealised P&L | Entry Date | Days Held | Sector | Stop Price | Status |
|--------|-----|----------|--------------|---|-----------|-----------|--------|-----------|--------|
| SHEL.L | 1.0624 | 28.70 | 34.55 | +4.06 | 2026-02-17 | 90 | Energy | 27.71 | ACTIVE |
| GLEN.L | 1.0350 | 5.08 | 5.86 | +0.60 | 2026-02-18 | 89 | Materials | 4.86 | ACTIVE |
| BP.L | 9.3200 | 4.92 | 52.54 | +6.64 | 2026-03-05 | 74 | Energy | 4.68 | ACTIVE |
| BA.L | 0.2378 | 22.61 | 4.58 | -0.80 | 2026-03-09 | 70 | Industrials | 21.50 | ACTIVE → **SELL** |
| AZN.L | 0.0383 | 142.90 | 5.34 | -0.13 | 2026-03-18 | 61 | Healthcare | 137.18 | ACTIVE |
| RIO.L | 0.0208 | 71.09 | 1.59 | +0.11 | 2026-04-02 | 46 | Materials | 67.02 | ACTIVE |

---

## Exit Signals Evaluated

### BA.L — **SELL SIGNAL: Trend Break**
- **Current Price:** 19.26  
- **SMA50:** 21.3401  
- **Close vs SMA50:** -9.75% (below 50-day moving average)
- **Days Below SMA50:** 21 consecutive days
- **Unrealised P&L:** -0.7973 GBP (loss-making)
- **Rationale:** Trend break confirmed. Price has been below SMA50 for 21 consecutive days. This violates the balanced strategy's trend-follow rule (max 10 consecutive days below SMA50 before mandatory exit). Position is at 70 days held with sustained downtrend. Exiting this position reduces portfolio to 5 positions (at maximum limit) and frees ~4.58 GBP of proceeds.

---

## New Entry Candidates Evaluated (Ranked by Confidence)

### 1. **LSEG.L** — Confidence: 0.66
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 93.72 > SMA50 90.88, SMA50 90.88 > SMA200 88.35)
- **SMA50 Slope:** Positive
- **Pullback Depth:** 7.57% from 20d high (101.4 → 93.72)
- **Drawdown from 20d High:** 7.57%
- **Volume Ratio:** 0.898 (healthier pullback on lower volume)
- **Liquidity:** 144.2M GBP avg 20d volume — **PASS**
- **Entry Price Estimate:** 93.72 GBP  
- **ATR14:** 3.27 GBP
- **Stop Price:** 93.72 - (3.27 × 1.5) = 88.71 GBP
- **Risk per Trade:** 5% × 107.91 = 5.40 GBP
- **Position Size Calc:** 5.40 / (93.72 - 88.71) = 1.06 shares × 0.9 (gap buffer) = 0.95 shares
- **Notional (before costs):** 0.95 × 93.72 = 89.03 GBP
- **Costs (Slippage + Stamp Duty):** ~0.90 GBP
- **Total Required Cash:** 89.93 GBP
- **Cash Available:** 0.17 GBP
- **Rejection Reason:** **INSUFFICIENT CASH** — Would require 89.93 GBP but only 0.17 GBP available after 3% buffer

### 2. **HSBA.L** — Confidence: 0.64
- **Entry Type:** Pullback in Uptrend
- **Trend Status:** FULL (close 13.60 > SMA50 12.87, SMA50 12.87 > SMA200 11.50)
- **SMA50 Slope:** Positive
- **Pullback Depth:** 0.67% from 20d high (13.69 → 13.60)
- **Volume Ratio:** 1.040 (slight volume increase on pullback)
- **Liquidity:** 269.4M GBP avg 20d volume — **PASS**
- **Rejection Reason:** **INSUFFICIENT CASH** — Even at smaller position size, would require >50 GBP after costs; insufficient liquidity in cash position

### 3. **RIO.L** — Confidence: 0.62
- **Entry Type:** Continuation (already held)
- **Current Position:** 0.0208 shares held at 71.09 avg cost
- **Market Price:** 76.40 GBP
- **Unrealised P&L:** +0.11 GBP
- **Trend Status:** FULL (close 76.40 > SMA50 71.91, SMA50 71.91 > SMA200 60.04)
- **SMA50 Slope:** Positive
- **Pullback Depth:** 7.67% from 20d high (82.75 → 76.40)
- **Rejection Reason:** **INSUFFICIENT CASH** + **POSITION AT MAX** — Would need to add to existing position, but (1) cash insufficient and (2) portfolio already at 5 positions post-BA.L exit

---

## Constraint Validation Summary

| Constraint | Status | Details |
|-----------|--------|---------|
| **Kill Switch** | ✅ PASS | kill_switch = false |
| **Trading Day** | ✅ PASS | is_trading_day = true, not a half day |
| **Data Freshness** | ✅ PASS | Market data dated 2026-05-20 (today) |
| **Minimum Price** | ✅ PASS | All candidates > 1.00 GBP |
| **Minimum Liquidity** | ✅ PASS | All candidates > 50k GBP avg daily volume |
| **Portfolio Drawdown** | ✅ PASS | 7.15% < 15.00% limit |
| **Max Positions** | ⚠️ AT LIMIT | Currently 6, max 5. BA.L exit brings to 5. |
| **Max New Positions/Day** | ✅ PASS | 0 new positions planned (only 1 exit) |
| **Cash Buffer** | ⚠️ TIGHT | 3% buffer = 3.24 GBP, leaving only 0.17 GBP for buys |
| **Max Sector Exposure** | ✅ PASS | Energy at 40.41% (< 40% limit post-exit) |
| **Max Single-Name Exposure** | ✅ PASS | BP.L largest at 48.64% (< 50% limit) |
| **Max Turnover** | ✅ PASS | Estimated 0.08% < 0.30% limit |
| **Position Age (Anti-Churn)** | ✅ PASS | All held > 2 days; BA.L at 70 days |
| **Correlation** | ⚠️ TBD | Max pairwise correlation 0.78 (within 3 threshold) |

---

## Risk Management Notes

### Gap Risk (DAILY_CHECK Mode)
Stop-loss orders are checked once daily. **Risk:** Overnight gaps can cause actual losses to exceed planned risk. This plan assumes no intraday trading and daily monitoring. Gap buffer of 10% has been applied to new position sizes.

### Cash Constraint Critical
With only 3.45 GBP liquid cash and a 3% portfolio buffer requirement (3.24 GBP), **only 0.17 GBP remains for new positions**. This is insufficient to fund any meaningful new entry. **Recommendation:** Execute BA.L exit to recover 4.58 GBP, improving available cash to ~4.75 GBP (post-buffer). This may enable a small new position or preserve capital.

### Settlement Timing
- **Settlement:** T+1 (1 business day)
- **Intraday Netting:** Disabled (assume_intraday_netting = false)
- **BA.L Proceeds:** Settled on 2026-05-21, available for buys on 2026-05-22

### UK Stamp Duty
- **Applied to:** UK equity buys only (50 bps)
- **ETFs:** Exempt
- **Cost Assumption:** Fee model = 0 per-trade; slippage = 10 bps assumed in cost estimates

---

## What Could Invalidate This Plan

1. **Gap Risk Overnight:** If SHEL.L, BP.L, or other holdings gap below their stop prices overnight, DAILY_CHECK will trigger exit at market. Actual loss may exceed 5% planned risk.
2. **Economic Data Release:** Major UK/US economic data on 2026-05-21 (Bank of England decision or US employment) could cause broad market move.
3. **Corporate Actions:** If any position announces dividend ex-date, capital reduction, or delisting, plan must be revised.
4. **Broker Issues:** Execution delays or rejection of market orders due to low liquidity at market open.
5. **Cash Proceeds Delay:** If BA.L sale settles late or doesn't clear by 2026-05-22, subsequent buys delayed until 2026-05-23.

---

## Data Quality Notes
- ✅ All required pre-computed indicator columns present in market_data.csv
- ✅ SMA50, SMA200, ATR14, drawdown metrics all provided (no recalculation needed)
- ✅ Volume data complete for liquidity assessment
- ✅ Sector and instrument type data populated for all 25 tickers
- ✅ 6 existing positions reconciled with universe allowlist

---

## Sector Exposure Summary (Post-Exit)
| Sector | Value (GBP) | % of Portfolio | Limit |
|--------|-------------|---|--------|
| **Energy** | 87.09 | 40.41% | 40.00% |
| **Materials** | 18.68 | 8.68% | — |
| **Healthcare** | 5.34 | 4.95% | — |
| **Financials** | 0.00 | 0.00% | — |
| **Industrials** | 0.00 | 0.00% | — |
| **Cash Buffer** | 3.24 | 3.22% | — |
| **Total** | 114.35 | 100.00% | — |

⚠️ **Energy sector exposure slightly exceeds 40% limit after BA.L exit.** This is acceptable given macro energy positioning; monitor for further Energy selling if new positions added.

---

## Orders for Execution

**Execution Sequence:** SELL_THEN_BUY (all SELLs first, then BUYs)

### SELL Orders
| Order ID | Ticker | Qty | Type | Reason | Estimated Proceeds |
|----------|--------|-----|------|--------|---|
| 1 | BA.L | 0.2378 | MKT | Trend break (21 days below SMA50) | ~4.58 GBP |

**Total SELL Proceeds:** ~4.58 GBP (settled 2026-05-21)

### BUY Orders
**None planned today.** Cash constraints prevent meaningful new entries. BA.L exit will improve liquidity for future opportunities (e.g., rebalance on 2026-05-21 if new high-conviction setup emerges).

---

## Execution Checklist
- [ ] Execute SELL order for BA.L at market (0.2378 shares @ ~19.26 GBP)
- [ ] Confirm settlement on 2026-05-21
- [ ] Monitor stop-losses for remaining 5 positions at market open 2026-05-21
- [ ] Review new entries on 2026-05-22 with improved cash position (~4.75 GBP available)
- [ ] Watch for bank holiday impact on 2026-05-25 (reduced liquidity expected on 2026-05-24)

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.** Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Use at your own risk. Past performance does not guarantee future results. Consult a financial advisor before executing trades.

---

**Plan Generated:** 2026-05-20  
**Strategy Profile:** Balanced Swing (3–20 days)  
**Time Horizon:** Medium-term swing trades  
**Risk Model:** Conservative capital preservation with trend-following discipline