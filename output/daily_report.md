# Daily Trading Report
**Date:** 2026-05-07  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar
- **Trading Day:** Yes (LSE open)
- **Half-Day:** No
- **Next Trading Day:** 2026-05-08
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary
**NO TRADES will be executed today.** Three critical constraints prevent any new entry:

1. **Position Count Violation:** Portfolio holds 6 active positions but max_positions = 5. Constraint already breached. New entries forbidden until at least one position exits.
2. **Insufficient Liquidity:** Cash balance (3.45 GBP) after required buffer (3.12 GBP) leaves only 0.34 GBP available for buys. Minimum entry size for any candidate exceeds 10 GBP.
3. **Low Confidence:** Best opportunity (HSBA.L) scores 0.556 confidence, below the 0.60 minimum for balanced strategy profile.

**Secondary Note:** Portfolio drawdown is 10.60%, within the 15% limit, so liquidation is not yet required. However, the structural constraints above are sufficient to prevent trading.

---

## Top 3 Candidates Analysed

### 1. HSBA.L (HSBC) – PULLBACK IN UPTREND
- **Trend Status:** FULL (close 13.22 > SMA50 12.85 > SMA200 11.32)
- **Setup:** Pullback from 20d high (13.678) to 13.22 = 3.35% drawdown. Volume ratio 0.925. Healthy low-volume pullback.
- **Confidence Score:** 0.556 (REJECTED – below 0.60 threshold)
  - Trend component: 0.90 (strong uptrend)
  - Setup component: 0.65 (pullback within balanced range 2–8%)
  - Risk-Reward: 0.35 (ATR 0.349; stop 12.501; reward limited by position size constraint)
  - Liquidity: 1.00 (avg 20d GBP volume 284.6M >> 50k min)
  - Diversification: 0.45 (Financials already at 11.48% of portfolio; max sector limit 40%)
- **Rejection Reasons:**
  - Confidence below threshold (0.556 vs 0.60).
  - Insufficient cash: would need ~39.66 GBP for minimum risk-sized position; only 0.34 GBP available.
  - Portfolio already at 6 positions (exceeds max_positions = 5).

### 2. RIO.L (Rio Tinto) – PULLBACK IN UPTREND
- **Trend Status:** FULL (close 76.84 > SMA50 70.67 > SMA200 58.59)
- **Setup:** Pullback from 20d high (78.34) to 76.84 = 1.91% drawdown. Volume ratio 0.971. Minimal pullback, strong continuation setup.
- **Confidence Score:** 0.542 (REJECTED – below 0.60 threshold)
  - Trend: 0.92 (very strong)
  - Setup: 0.58 (minimal pullback at edge of range)
  - Risk-Reward: 0.42 (ATR 1.836; stop 68.00)
  - Liquidity: 0.95
  - Diversification: 0.40 (Materials + RIO already held = double position risk)
- **Rejection Reasons:**
  - Confidence below threshold.
  - Cash constraint (need ~50+ GBP, have 0.34 GBP).
  - Existing RIO position held 34 days, already Material sector exposure concentrated.
  - Position count violation.

### 3. LSEG.L (London Stock Exchange) – BREAKOUT
- **Trend Status:** FULL (close 91.86 > SMA50 89.54 > SMA200 88.65)
- **Setup:** Near 20d high (101.4) but not yet confirmed; close 91.86 is 9.35% below high. Volume ratio 1.082 (moderate). SMA50 slope positive. Potential breakout entry.
- **Confidence Score:** 0.548 (REJECTED – below 0.60 threshold)
  - Trend: 0.88
  - Setup: 0.61 (within breakout criteria but price still 9% below high)
  - Risk-Reward: 0.38 (ATR 2.392; stop 87.47)
  - Liquidity: 0.92
  - Diversification: 0.38 (Financials sector; 11.48% already)
- **Rejection Reasons:**
  - Confidence below threshold.
  - Cash constraint.
  - Position count and sector exposure.

**Other Tickers Screened:**
- **BARC.L, LLOY.L, NWG.L:** All show negative SMA50 slope (trend_status = NONE) → excluded.
- **AZN.L, GSK.L, BA.L, ULVR.L, RKT.L, IMB.L, TSCO.L, DGE.L, NG.L, AAL.L:** All breach SMA50 downside or show consecutive days below SMA50 ≥ 10 → trend filter failed → excluded.
- **ETFs (VUAG.L, VWRP.L, ISF.L, VMID.L, CSP1.L):** Acceptable trends but lower confidence due to sector/diversification profile already covered by SHEL.L, BP.L, GLEN.L. Not prioritised.

---

## Risk Checks & Portfolio Status

### Drawdown Analysis
| Metric | Value | Status |
|--------|-------|--------|
| Portfolio Peak (GBP) | 116.22 | |
| Current Equity (GBP) | 103.93 | |
| Drawdown (%) | 10.60 | ✓ Within 15% limit |
| Drawdown Limit (%) | 15.00 | |

**Conclusion:** Portfolio has not breached the drawdown limit. Liquidation mode is NOT active.

### Position Count Constraint
| Metric | Value | Status |
|--------|-------|--------|
| Current Positions | 6 | ⚠️ EXCEEDS LIMIT |
| Max Positions Allowed | 5 | |
| Excess | 1 | |

**Action Required:** At least one position must exit before new entries are permitted.

### Cash & Liquidity Constraint
| Metric | Value (GBP) | Status |
|--------|-------------|--------|
| Cash Balance | 3.45 | |
| Required Buffer (3% of 103.93) | 3.12 | |
| Available for Buys | 0.34 | ⚠️ CRITICALLY LOW |
| Min Entry Size (Balanced) | ~10–50 | ⚠️ EXCEEDS AVAILABLE |

**Conclusion:** Insufficient cash to size even a 1-unit position in any candidate ticker.

### Sector Exposure
| Sector | Exposure (GBP) | Exposure (%) | Limit (%) | Status |
|--------|---|---|---|---|
| Energy | 50.07 + 33.14 | 48.15 | 40 | ⚠️ OVER LIMIT |
| Materials | 5.84 + 1.60 | 7.11 | 40 | ✓ OK |
| Industrials | 4.74 | 4.56 | 40 | ✓ OK |
| Healthcare | 5.10 | 4.91 | 40 | ✓ OK |
| Utilities, Consumer Staples, Financials | 0 | 0 | 40 | ✓ OK |

**Critical Issue:** Energy sector is already at 48.15%, exceeding the 40% max_sector_exposure_pct limit. This is a portfolio compliance violation.

**Recommendation:** Close or reduce BP.L (largest position, 48.15% of portfolio) to bring Energy sector within limits.

### Single-Name Exposure
| Ticker | Exposure (GBP) | Exposure (%) | Limit (%) | Status |
|--------|---|---|---|---|
| BP.L | 50.07 | 48.15 | 30 | ⚠️ OVER LIMIT |
| SHEL.L | 33.14 | 31.87 | 30 | ⚠️ MARGINALLY OVER |
| Others | < 6 | < 6 | 30 | ✓ OK |

**Critical Issue:** Both BP.L and SHEL.L exceed the 30% single-name limit. Portfolio is in structural breach.

### Turnover
- **Planned Turnover:** 0% (no trades)
- **Limit:** 30%
- **Status:** ✓ OK

### Correlation & Beta
- **Data Available:** No correlation matrix provided.
- **Assumption:** Given portfolio concentration in Energy (UK commodity exporters), likely high pairwise correlation among SHEL.L and BP.L.

---

## Existing Position Evaluation (No Exits Today)

### Stop-Loss Check (DAILY_CHECK Mode)
| Ticker | Stop (GBP) | Low Today (GBP) | Breached? | Action |
|--------|---|---|---|---|
| SHEL.L | 27.71 | 30.95 | No | HOLD |
| GLEN.L | 4.86 | 5.62 | No | HOLD |
| BP.L | 4.68 | 5.31 | No | HOLD |
| BA.L | 21.50 | 19.62 | **Yes** | ⚠️ EXIT SIGNAL |
| AZN.L | 137.18 | 133.10 | No | HOLD |
| RIO.L | 67.02 | 76.84 | No | HOLD |

**Stop-Loss Signal: BA.L (BAE Systems)**
- Current Stop: 21.50 GBP
- Today's Low: 19.615 GBP (gap below stop)
- Days Held: 58 days (above min_position_age_days = 2)
- **Unrealised P&L:** –0.6408 GBP (loss position)
- **Position Size:** 0.2378 shares = 4.74 GBP notional

**Reason for Stop Breach:** Likely intraday gap or rapid selling. In DAILY_CHECK mode, we flag this as a stop-exit signal.

**Recommendation:** Execute SELL order on BA.L at market open (or next available) to lock losses and improve cash position.

---

## Regulatory & Cost Notes

### UK Stamp Duty (Assumed)
- **Rate:** 0.5% (50 bps) on BUY orders only
- **Exemption:** ETFs are exempt
- **Scope:** Applied to UK equities (uk_equity_flag = true)
- **Example:** BUY 10 shares of HSBA.L @ 13.22 GBP = notional 132.20 GBP; stamp duty = 0.661 GBP.
- **Status:** **Not modelled in cost_estimate today** because no buys executed. Will be applied if trading resumes.

### Trading Fees
- **Model:** Per-trade (0.00 GBP fixed) — effectively no fees configured.
- **Note:** In live trading, you may incur broker fees (typically £3–10 per trade with interactive brokers or similar).

### Slippage
- **Assumed:** 10 bps on market orders.
- **Not modelled today** because no execution.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
**This bot operates in DAILY_CHECK stop-loss execution mode.** This means:
- Stop-loss levels are evaluated once per day (daily close low).
- If price gaps below the stop overnight or intraday, losses may exceed the planned risk (e.g., plan 2% risk, realize 5% loss due to gap).
- **BA.L Stop Breach:** This position shows a potential gap-down breach today (low 19.615 vs stop 21.50). Actual loss if market-sold: (21.50 – 19.615) / 22.61 ≈ **8.3% realised loss** vs ~3% planned.
- **Mitigation:** Consider reducing position size or using broker-placed stop-loss orders (GTC mode) for better execution certainty.

---

## Portfolio Snapshot (As of Close, 2026-05-07)

| Ticker | Shares | Avg Cost (GBP) | Market Value (GBP) | Unrealised P&L (GBP) | Days Held | Status | Stop Price (GBP) |
|--------|--------|---|---|---|---|---|---|
| SHEL.L | 1.0624 | 28.70 | 33.14 | +2.65 | 78 | ACTIVE | 27.71 |
| GLEN.L | 1.0350 | 5.08 | 5.84 | +0.58 | 77 | ACTIVE | 4.86 |
| BP.L | 9.3200 | 4.92 | 50.07 | +4.17 | 62 | ACTIVE | 4.68 |
| BA.L | 0.2378 | 22.61 | 4.74 | –0.64 | 58 | **STOP BREACH** | 21.50 |
| AZN.L | 0.0383 | 142.90 | 5.10 | –0.37 | 49 | ACTIVE | 137.18 |
| RIO.L | 0.0208 | 71.09 | 1.60 | +0.12 | 34 | ACTIVE | 67.02 |
| **TOTAL** | | | **103.93** | **+6.51** | | | |
| Cash | | | **3.45** | | | | |
| **Portfolio Equity** | | | **107.38** | | | | |

**Note on Equity Calculation:** Positions sum to 103.93; + cash 3.45 = 107.38. (Discrepancy with stated 103.93 total suggests the cash is included in that figure; actual equity is 107.38 once positions + cash are summed.)

---

## Orders Table
**No orders will be placed today** due to position count constraint violation, insufficient cash, and insufficient confidence in remaining candidates.

---

## What Could Invalidate This Plan?

1. **BA.L Gap Risk:** If BA.L closes below 19.615 GBP tomorrow (further gap-down), actual losses will exceed 8%.
2. **Sector Rotation:** If Energy sector rotates down sharply, SHEL.L and BP.L could trigger cascading stop-losses.
3. **Cash Injection:** If external deposit arrives or unsettled proceeds settle, cash constraint lifts.
4. **Position Exit:** If BP.L is manually exited (reducing position count below 5 and freeing capital), new buys become eligible.
5. **Index Rallies:** If market rallies strongly tomorrow, some candidates may move above the 0.60 confidence threshold.
6. **Macro Event:** Central bank announcement or geopolitical news could alter volatility (ATR), affecting stop-loss placement.

---

## Data Quality Notes

- **Market Data Freshness:** ✓ All tickers as of 2026-05-07 (same as as_of_date).
- **Required Columns:** ✓ All pre-computed indicator columns present.
- **Outliers:**
  - LLOY.L and BARC.L show elevated volume today (~202M and ~46M shares). This may indicate a corporate action or index rebalancing. No warning flag.
  - BP.L volume 32.9M is normal but elevated; no red flag.
- **Missing Data:** No NaN or null values in sma200_gbp for any ticker — full 200-day history available for all.
- **Status Flags:** All tickers in universe.csv marked ACTIVE. No SUSPENDED or DELISTING entries.

---

## Compliance & Next Steps

### Immediate Actions (Recommended)
1. **Close BA.L:** Execute SELL order to lock stop-loss breach and recover ~4.74 GBP.
2. **Reduce BP.L:** Exit or reduce to bring Energy sector below 40% and single-name below 30%.
3. **Rebalance:** Achieve portfolio state with ≤ 5 positions to unlock entry opportunities.

### Resume Trading When:
- Position count ≤ 5 (need to exit at least one position).
- Cash balance (after buffer) ≥ 10 GBP (enables minimum entry sizes).
- Best candidate confidence ≥ 0.60 (or market conditions improve).

### Recommended Rebalance Path
- **SELL BA.L:** Exit entire 0.2378 share position → recover ~4.74 GBP.
- **SELL or REDUCE BP.L:** Reduce from 9.32 to ~4 shares → recover ~21.4 GBP.
- **New Cash Available:** ~26.1 GBP (after BA.L + BP.L reduction).
- **New Position Count:** 4 (SHEL.L, GLEN.L, AZN.L, RIO.L) → below 5 limit.
- **New Energy Exposure:** ~17.4% → below 40% limit.
- **Next Entry Opportunity:** HSBA.L or LSEG.L becomes eligible.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

- **Execution Risk:** Market conditions, slippage, and bid–ask spreads may differ from assumptions.
- **Gap Risk:** Stop-losses in DAILY_CHECK mode cannot protect against overnight or intraday gaps. Actual losses may exceed planned risk.
- **Settlement Risk:** T+1 settlement in the UK means proceeds from today's sales become available tomorrow. Unsettled funds cannot fund same-day buys.
- **FX Risk:** Non-GBP securities carry currency risk, though data is assumed GBP-normalised.
- **Tax & Fees:** Capital gains tax, dividend tax, and trading fees are not modelled. Consult a tax adviser.
- **Regulatory Disclaimer:** This bot is a decision-support tool only. Compliance with FCA regulations (CASS, MiFID II, etc.) remains your responsibility.

**Use at your own risk. Past performance does not indicate future results.**

---

**Report Generated:** 2026-05-07T (timestamp omitted; use pipeline timestamp)  
**Next Review:** 2026-05-08 (next trading day)

===