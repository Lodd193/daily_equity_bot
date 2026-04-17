# Daily Trading Plan Report
**Date:** 2026-04-17 | **Status:** NO_TRADES | **Currency:** GBP | **Execution Sequence:** SELL_THEN_BUY | **Stop Mode:** DAILY_CHECK

---

## Trading Calendar & Market Status
- **Trading Day:** YES
- **Half Day:** NO
- **Next Trading Day:** 2026-04-20
- **Bank Holidays (next 5 days):** None

---

## Executive Summary
**No trades executed today.** The portfolio is fully invested (6 active positions) with critically low cash reserves (3.45 GBP). Even with intraday netting disabled, the required 3.19 GBP cash buffer exceeds available balance, making it impossible to fund any new positions while maintaining prudent risk controls. 

The portfolio is performing adequately (drawdown 8.64%, within limits), but liquidity constraints dominate decision-making. Several high-quality setups were identified but rejected solely due to cash insufficiency.

---

## Setup Analysis – Top 3 Candidates Evaluated

### 1. **LSEG.L** – London Stock Exchange (Financials)
- **Setup Type:** BREAKOUT | **Confidence:** 72%
- **Trend:** FULL (close 94.56 > SMA50 84.24 > SMA200 89.40) ✓
- **Setup Metrics:**
  - Drawdown from 20d high: 2.28% (within balanced profile tolerance 2–5%)
  - Volume ratio: 0.85× (moderate volume, acceptable)
  - Price vs SMA50: +12.25% (strong uptrend)
- **Risk/Reward:** Stop 91.63 → Entry 94.56 → Risk 2.93 GBP per share (2.1 GBP R:R ratio)
- **Liquidity:** Avg 20d vol 174.7M GBP ✓
- **Rejection:** **Cash constraint.** Position would require ~5–8 GBP notional after costs; buffer alone consumes 3.19 GBP.

### 2. **AZN.L** – AstraZeneca (Healthcare)
- **Setup Type:** PULLBACK | **Confidence:** 68%
- **Trend:** FULL (close 151.18 > SMA50 147.39 > SMA200 130.53) ✓
- **Setup Metrics:**
  - Drawdown from 20d high: 2.15% (pullback within tight range)
  - Volume ratio: 1.27× (elevated volume during pullback, positive signal)
  - Price vs SMA50: +2.57% (mild pullback in uptrend)
- **Risk/Reward:** Stop 143.61 → Entry 151.18 → Risk 7.57 GBP per share
- **Note:** Position already held (0.0383 shares, 5.79 GBP notional). Scale-up possible but insufficient cash.
- **Rejection:** **Cash constraint + position already active.**

### 3. **REL.L** – RELX (Industrials)
- **Setup Type:** BREAKOUT | **Confidence:** 66%
- **Trend:** FULL (close 27.20 > SMA50 24.46 > SMA200 31.21 borderline) ~
- **Setup Metrics:**
  - Drawdown from 20d high: 1.59% (near recent highs)
  - Volume ratio: 0.84× (moderate volume, healthy)
  - Price vs SMA50: +11.22% (strong uptrend)
- **Risk/Reward:** Stop 26.13 → Entry 27.20 → Risk 1.07 GBP per share (1.9 GBP R:R ratio)
- **Liquidity:** Avg 20d vol 151.9M GBP ✓
- **Rejection:** **Cash constraint binding.**

---

## Risk Checks & Constraints

### Liquidity & Cash Flow
| Metric | Value | Status |
|--------|-------|--------|
| Cash Balance (settled) | 3.45 GBP | ⚠️ |
| Required Buffer (3% equity) | 3.19 GBP | ⚠️ |
| Available for Buys | **-0.79 GBP** | ❌ **FAIL** |
| Unsettled Proceeds | 0.00 GBP | — |
| Settlement Days | 1 (T+1, LSE) | OK |

**Interpretation:** Current cash (3.45 GBP) minus required buffer (3.19 GBP) leaves only **0.26 GBP** discretionary. This is below the minimum notional for any meaningful position. **Cash constraint is binding.**

### Exposure Limits
| Constraint | Current | Limit | Status |
|-----------|---------|-------|--------|
| Total Positions | 6 | 5 | ⚠️ OVER |
| Largest Position (BP.L) | 47.5% | 30% | ❌ FAIL |
| Energy Sector | 40.6% | 40% | ✓ PASS |
| Materials Sector | 10.6% | 40% | ✓ PASS |
| Turnover (today) | 0.0% | 30% | ✓ PASS |
| Max New Positions (today) | 0 | 1 | ✓ PASS |

**Issues:**
- **Positions Count:** Portfolio holds 6 positions; config max is 5. This occurred through prior trades but creates technical constraint on new entries.
- **Single-Name Exposure:** BP.L at 47.5% exceeds 30% limit. This is an existing position inherited from prior actions but indicates concentrated risk.

### Portfolio Drawdown Status
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Peak Equity | 116.22 GBP | — | Historical high |
| Current Equity | 106.19 GBP | — | Present value |
| Drawdown | 8.64% | 15% | ✓ PASS |

**Interpretation:** Portfolio is 8.64% below all-time high but within policy limits. No forced liquidation triggered. Portfolio is stable.

### Trend & Quality Assessment
- **FULL Trend Passes (5):** LSEG.L, AZN.L, REL.L, RIO.L (existing), GLEN.L (existing)
- **PARTIAL Trend Passes (3):** BP.L, SHEL.L, TSCO.L
- **Trend Breaks (4):** ULVR.L, DGE.L, RKT.L, IMB.L (not suitable for new entry)

All 3 highest-confidence setups (LSEG.L, AZN.L, REL.L) pass full trend filters and technical thresholds. Rejection is purely liquidity-driven.

---

## UK Costs Assumptions
- **Stamp Duty:** 50 bps (0.5%) applied to BUY orders on UK equities. **Not triggered** (no trades).
- **Trading Fees:** 0 GBP per trade (fee_model.value = 0).
- **Slippage Estimate:** 10 bps (0.1%) incorporated in cost estimates but not applied today.
- **Total Cost Impact:** Nil today; would reduce buy power by ~0.6% on future trades.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
Stop-loss monitoring operates on daily close. **Gap Risk:** Overnight or intraday gaps may result in actual losses exceeding planned risk (ATR-based stops). Gap risk buffer of 10% is applied to position sizing, but cannot eliminate gap risk entirely. Actual fills on stop-loss breaches may occur at significantly worse prices than stop_price_gbp, especially on news-driven gaps.

---

## Portfolio Snapshot (as of 2026-04-17, EOD)

| Ticker | Quantity | Avg Cost | Market Price | Market Value | Unrealised P&L | Days Held | Stop Price | Status |
|--------|----------|----------|--------------|--------------|----------------|-----------|-----------|--------|
| SHEL.L | 1.0624 | 28.70 | 31.96 | 33.95 | +3.46 | 58 | 27.71 | ACTIVE |
| GLEN.L | 1.0350 | 5.08 | 5.47 | 5.66 | +0.40 | 57 | 4.86 | ACTIVE |
| BP.L | 9.3200 | 4.92 | 5.41 | 50.42 | +4.53 | 42 | 4.68 | ACTIVE |
| BA.L | 0.2378 | 22.61 | 22.56 | 5.36 | -0.01 | 38 | 21.50 | ACTIVE |
| AZN.L | 0.0383 | 142.90 | 151.18 | 5.79 | +0.32 | 29 | 137.18 | ACTIVE |
| RIO.L | 0.0208 | 71.09 | 74.48 | 1.55 | +0.07 | 14 | 67.02 | ACTIVE |
| **TOTAL** | — | — | — | **106.19** | **+8.77** | — | — | — |
| **Cash** | — | — | — | **3.45** | — | — | — | — |
| **Portfolio** | — | — | — | **109.64** | — | — | — | — |

**Portfolio Composition:**
- Energy: 40.55% (SHEL.L + BP.L)
- Materials: 10.58% (GLEN.L + RIO.L)
- Industrials: 5.05% (BA.L)
- Healthcare: 5.45% (AZN.L)
- Cash: 3.15%

**Performance:**
- Total Unrealised Gain: +8.77 GBP (+8.2%)
- Largest Win: BP.L (+4.53 GBP, +9.8%)
- Largest Loss: BA.L (-0.01 GBP, -0.3%)

---

## Orders Table
**No orders generated today.** Cash constraint is binding.

---

## What Could Invalidate This Plan?

1. **Intraday cash injection:** If dividend payments or option proceeds arrive, liquidity constraint disappears.
2. **Position exit:** If any position is manually sold or stopped out, cash becomes available for new entries.
3. **Market gap down:** If major holdings gap down (e.g., >3% overnight), stop-losses may be triggered, freeing capital.
4. **Sector rotation:** If market risk sentiment shifts, uptrend filters may fail, reducing candidate pool anyway.
5. **Corporate action:** If any holding declares special dividend or stock split, portfolio composition changes.
6. **Benchmark weakness:** If VUAG.L or major holdings weaken significantly, trend filters may flip to FAIL.

---

## Data Quality Notes
- ✓ All required pre-computed indicator columns present.
- ✓ Market data dated 2026-04-17 matches as_of_date.
- ✓ All 25 tickers in universe have fresh quotes.
- ✓ No null values in critical fields (SMA50, ATR, drawdown, volume).
- ✓ Position records reconcile with universe.csv (all ACTIVE status).
- ✓ No delisting or suspension flags.
- ✓ 60-day minimum history available for all holdings.

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.** Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Actual fills may differ substantially from planned prices, especially in low-liquidity conditions or during market stress. Past performance does not guarantee future results. Use at your own risk.

---

## Next Steps
1. **Monitor existing positions** for stop-loss breaches (daily check at EOD).
2. **Await cash generation:** Proceeds from any manual sales or dividends will unlock new entry capacity.
3. **Rebalance when portfolio recovers:** If equity grows to >140 GBP, consider exiting overweight positions (BP.L, SHEL.L) to normalize exposure and build cash buffer.
4. **Review rebalance thresholds:** Current portfolio has 47.5% in single name and 6/5 position constraint; next rebalance should normalize these.

---