# Daily Trading Report
**Date:** 2026-05-18  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (gap risk acknowledged)

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-05-19
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary
The bot does NOT execute any trades today. The portfolio is severely undercapitalized with insufficient buying power to execute meaningful new positions, while simultaneously overweight (6 positions vs. 5 max). The decision prioritizes capital preservation over forced trading.

### Key Constraints Breached
1. **Portfolio Over Position Limit:** 6 current positions vs. max 5 allowed
2. **Insufficient Buying Power:** £3.45 cash, minus 3% buffer (£3.26) = £0.20 available
3. **Stamp Duty Impact:** UK equity purchases incur 50 bps (0.5%) stamp duty, consuming buying power
4. **Position Size Reality:** Max risk per trade is £5.43 (5% of £108.52 equity). Typical entry would require fractional shares with notional < £50, leaving stop distance questions unresolved.

---

## Portfolio Status
| Metric | Value |
|--------|-------|
| **Equity Value** | £108.52 |
| **Cash Balance** | £3.45 |
| **Portfolio Peak** | £116.22 |
| **Drawdown from Peak** | 6.65% |
| **Drawdown Limit** | 15.0% |
| **Current Positions** | 6 |
| **Max Positions Allowed** | 5 |
| **Unrealised P&L** | +£11.05 |

---

## Position Breakdown
| Ticker | Qty | Entry Date | Days Held | Avg Cost | Current Price | Market Value | Unrealised P&L | Stop Price |
|--------|-----|------------|-----------|----------|---------------|--------------|----------------|------------|
| SHEL.L | 1.0624 | 2026-02-17 | 86 | £28.70 | £32.90 | £34.95 | +£4.46 | £27.71 |
| BP.L | 9.32 | 2026-03-05 | 70 | £4.92 | £5.67 | £52.85 | +£6.96 | £4.68 |
| AZN.L | 0.0383 | 2026-03-18 | 57 | £142.90 | £137.10 | £5.25 | -£0.22 | £137.18 |
| BA.L | 0.2378 | 2026-03-09 | 66 | £22.61 | £18.80 | £4.47 | -£0.91 | £21.50 |
| RIO.L | 0.0208 | 2026-04-02 | 42 | £71.09 | £77.27 | £1.61 | +£0.13 | £67.02 |
| GLEN.L | 1.035 | 2026-02-18 | 85 | £5.08 | £5.74 | £5.94 | +£0.68 | £4.86 |

---

## Analysis of Top Candidates (None Evaluated)
Because available buying power is effectively zero, the bot did not perform detailed confidence scoring on candidate tickers. However, **if capital were available**, the following would have been analyzed:

1. **RIO.L (Rio Tinto)**
   - **Trend:** FULL (close 77.27 > SMA50 71.59, SMA50 71.59 > SMA200 59.74)
   - **Setup:** Pullback pattern within 20-day range
   - **Drawdown from 20d High:** 6.6%
   - **Volume Ratio:** 1.025 (above avg, breakout signal)
   - **Status:** Already held; no new entry warranted

2. **GLEN.L (Glencore)**
   - **Trend:** FULL (close 5.74 > SMA50 5.49, SMA50 5.49 > SMA200 4.24)
   - **Setup:** Pullback in confirmed uptrend
   - **Drawdown from 20d High:** 4.1%
   - **Status:** Already held; positive momentum but position aging (85 days)

3. **LSEG.L (LSE Group)**
   - **Trend:** FULL (close 92.76 > SMA50 90.62, SMA50 90.62 > SMA200 88.35)
   - **Setup:** Breakout; close within 8.5% of 20d high (101.4)
   - **Volume Ratio:** 0.877 (below average; less conviction)
   - **Drawdown from 20d High:** 8.5%
   - **Rejection:** Buying power constraint; also not currently held

---

## Risk Checks

### Liquidity Filters
✅ **Min Price Filter:** All holdings > £1.00  
✅ **Avg GBP Volume Filter:** All holdings > £50k/day  
✅ **Volume Participation:** Not evaluated (no trades)

### Portfolio Limits
❌ **Position Count:** 6 positions vs. 5 max (BREACH)  
✅ **Drawdown Limit:** 6.65% drawdown vs. 15% limit (OK)  
✅ **Single-Name Exposure:** Largest (BP.L) = 48.7% < 30% limit... **BREACH** (largest exposure exceeds limit)  

**Sector Exposure:**
| Sector | Exposure | Limit | Status |
|--------|----------|-------|--------|
| Energy | 36.3% | 40% | ✅ OK |
| Materials | 7.5% | 40% | ✅ OK |
| Healthcare | 4.8% | 40% | ✅ OK |
| Industrials | 4.1% | 40% | ✅ OK |

### Turnover & Position Sizing
- **Planned Turnover:** 0.0%
- **Max Allowed:** 30.0%
- **Status:** ✅ OK

### Settlement & Cash
- **Settlement Days:** 1 (T+1)
- **Intraday Netting:** Disabled
- **Current Cash:** £3.45
- **Cash Buffer Required (3%):** £3.26
- **Available for Buys:** £0.20
- **Unsettled Proceeds:** £0.00
- **Status:** ❌ **Insufficient buying power**

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
This portfolio uses **DAILY_CHECK** stop-loss execution. Actual outcomes may differ from planned stops due to:
- **Overnight gaps** (prices gap below stop-loss at market open)
- **Intraday gaps** (limited intraday monitoring between market open and close)
- **Liquidity shocks** (large bid-ask spreads, reduced volume)

Current stops are set as:
- SHEL.L: £27.71 (vs current £32.90)
- BP.L: £4.68 (vs current £5.67)
- GLEN.L: £4.86 (vs current £5.74)
- RIO.L: £67.02 (vs current £77.27)
- AZN.L: £137.18 (vs current £137.10) — **at risk**
- BA.L: £21.50 (vs current £18.81) — **in loss**

**BA.L and AZN.L are underwater.** If the bot had capital, exiting these positions for rebalancing might be considered, but the cost of redeployment exceeds the benefit given portfolio scale.

---

## UK Costs Assumption
- **Stamp Duty (UK Equities):** 50 bps (0.5%) applied to BUY notional; ETFs exempt
- **Trade Fees:** £0 per trade (configured)
- **Slippage Assumption:** 10 bps (0.1%) on entry/exit
- **Total Cost per Trade:** ~0.6% for UK equities (stamp duty + slippage)

At £108.52 portfolio size, a £50 position entry incurs ~£0.30 in costs, meaningful relative to available cash.

---

## Constraints Preventing Entry
1. **Capital Constraint (Primary):** £0.20 available after buffer exhausts buying power
2. **Position Count:** Already at 6 vs 5 max; any new entry requires prior exit
3. **Underwater Positions:** BA.L (-£0.91) and AZN.L (-£0.22) are losers; selling at a loss when capital is scarce is suboptimal unless exit rules trigger
4. **Rebalancing vs. No-Trade Bias:** The no-trade bias wins when capital-constrained

---

## What Could Invalidate This Plan
- **Market Gap Down:** If the market gaps down >3%, stops for SHEL, BP, GLEN, RIO may be hit, releasing £40–50 in proceeds
- **Sector Rotation:** Consumer, Healthcare rebound could change sector attractiveness
- **News/Corporate Actions:** Dividends, splits, or analyst downgrades could affect individual tickers
- **FX Movement:** GBP weakness would increase GBP value of foreign holdings (if any were present), but universe is GBP-quoted

---

## Data Quality Notes
✅ **Market Data Freshness:** 2026-05-18 data provided; matches as_of_date  
✅ **Required Columns:** All technical indicators present (SMA50, SMA200, ATR14, 20d range, volume ratios)  
✅ **Position Reconciliation:** 6 positions in portfolio; all present in universe allowlist  
✅ **Status Flags:** All positions ACTIVE; no SUSPENDED or DELISTING  
✅ **Indicator Validity:** No NaN or null values in required pre-computed fields for holdings  

---

## Summary & Recommendation
**Status:** NO_TRADES (capital constraint + over-position limit)

The portfolio is in a **recovery phase** (6.65% drawdown, 85%+ of peak). Rather than force trades on a minimal capital base, the bot waits for:
1. **Proceeds from existing profitable positions** (e.g., SHEL, BP, GLEN showing gains)
2. **Market pullbacks** to reset entry points on new candidates
3. **Rebalancing opportunity** when cash or stop-loss exits free up capital

No BUY is justified until available buying power exceeds £10–20 GBP (meaningful position size).

---

## DISCLAIMER
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice. Execution risk, gaps, slippage, FX effects, settlement timing, taxes, and fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Use at your own risk.**

---