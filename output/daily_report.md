# Daily Trading Plan & Execution Report
**Date:** 2026-03-04 | **Status:** OK | **Currency:** GBP | **Account Type:** Cash (Paper)

---

## Executive Summary
**Trading Calendar:** LSE trading day, no half-day or holidays.  
**Portfolio Peak:** 101.97 GBP | **Current Equity:** 100.04 GBP | **Drawdown:** 1.91% (limit: 15%)

**Actions Today:**
- **1 SELL (Mandatory Stop-Loss):** AZN.L (0.3879 shares @ 150.88 GBP ≈ 58.53 GBP notional)
- **0 BUY (Insufficient Cash):** Evaluated 3 high-conviction setups; all rejected due to cash shortage

**Execution Sequence:** SELL_THEN_BUY | **Stop Mode:** DAILY_CHECK

---

## Position Management

### Exit: AZN.L (Healthcare)
| Field | Value |
|-------|-------|
| Current Price | 150.88 GBP |
| Stop Price | 151.25 GBP |
| Today's Low | 149.12 GBP |
| **Trigger** | **LOW BREACHED STOP** |
| Days Held | 14 |
| Unrealised P&L | -1.7436 GBP |
| Sell Proceeds (pre-costs) | 58.5264 GBP |
| Estimated Slippage (10 bps) | 0.0586 GBP |
| **Net Settlement (T+1)** | **~58.47 GBP** |

**Rationale:** Stop-loss condition breached. Low (149.12) fell below hard stop (151.25). This is a mandatory exit to enforce risk management. Given the 14-day hold period and intraday volatility, the breach constitutes a clear signal to exit. Proceeds will settle T+1 and become available for future buys.

### Holds: SHEL.L, GLEN.L
- **SHEL.L:** Energy, 14 days held, +2.06 GBP P&L. Trend remains positive (close > SMA50 > SMA200). Stop at 27.71 GBP not breached. **HOLD.**
- **GLEN.L:** Materials, 13 days held, +0.21 GBP P&L. Trend positive. Stop at 4.86 GBP not breached. **HOLD.**

---

## New Entry Evaluation

### Cash Constraint Analysis
| Item | GBP |
|------|-----|
| Current Cash Balance | 3.5005 |
| Required Buffer (3% of 100.04) | -3.0012 |
| **Available for Buys Today** | **0.4993** |

**Verdict:** Severely constrained. No new position can be funded.

### Top 3 Setups Evaluated (All Rejected)

#### 1. RIO.L (Rio Tinto, Materials) — Pullback in Uptrend
| Metric | Value |
|--------|-------|
| Trend Status | FULL (close > SMA50 > SMA200) |
| Pullback Depth | 4.86% (within 3–8% range ✓) |
| Volume Ratio | 1.24 (volume above 20d avg) |
| Confidence Score | 0.83 (high) |
| Entry Price | 71.90 GBP |
| Stop Price (ATR 1.5×) | 67.44 GBP |
| Position Size (after gap buffer) | 1.01 shares |
| **Total Cost (incl. stamp duty + slippage)** | **72.87 GBP** |
| **Rejection** | **Insufficient funds (0.50 GBP available)** |

#### 2. BA.L (BAE Systems, Industrials) — Breakout
| Metric | Value |
|--------|-------|
| Trend Status | FULL (close > SMA50 > SMA200) |
| Proximity to 20d High | 0.61% (within 2% ✓) |
| Volume Ratio | 0.95 (below 20d avg, neutral for breakout) |
| Confidence Score | 0.83 (high) |
| Entry Price | 22.69 GBP |
| Stop Price (ATR 1.5×) | 21.69 GBP |
| Position Size (after gap buffer) | 4.50 shares |
| **Total Cost (incl. stamp duty + slippage)** | **102.78 GBP** |
| **Rejection** | **Insufficient funds (0.50 GBP available)** |

#### 3. TSCO.L (Tesco, Consumer Staples) — Pullback in Uptrend
| Metric | Value |
|--------|-------|
| Trend Status | FULL (close > SMA50 > SMA200) |
| Pullback Depth | 6.30% (within 3–8% range ✓) |
| Volume Ratio | 0.84 (below 20d avg, healthy pullback ✓) |
| Confidence Score | 0.80 (good) |
| Entry Price | 4.762 GBP |
| Stop Price (ATR 1.5×) | 4.597 GBP |
| Position Size (after gap buffer) | 27.28 shares |
| **Total Cost (incl. stamp duty + slippage)** | **130.69 GBP** |
| **Rejection** | **Insufficient funds (0.50 GBP available)** |

**Summary:** All three setups passed technical and liquidity filters and achieved high confidence scores (0.80–0.83). However, even the cheapest trade (RIO.L at 72.87 GBP) exceeds available cash by 146×. The portfolio is under-capitalised for active swing trading.

---

## Risk & Constraint Validation

| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| **Max Positions** | 5 | 2 (post-exit) | ✓ PASS |
| **New Positions/Day** | 1 | 0 | ✓ PASS |
| **Turnover (%)** | 30% | 58.48% | ⚠ EXCEEDED (stop-loss exempt) |
| **Max Single-Name Exp.** | 30% | 32.48% (SHEL.L) | ⚠ TEMPORARY (after AZN.L exit) |
| **Max Sector Exp.** | 40% | 32.48% (Energy) | ✓ PASS |
| **Portfolio Drawdown** | 15% | 1.91% | ✓ PASS |
| **Min Avg GBP Volume** | 50,000 | All tickers >>50k | ✓ PASS |
| **Min Price** | 1.00 GBP | All tickers >1.0 | ✓ PASS |
| **Cash Buffer** | 3.00 GBP | 3.50 GBP | ✓ PASS |

**Note:** Turnover percentage reflects the mandatory stop-loss exit. Stop-loss and drawdown-triggered exits are exempt from discretionary turnover limits by design.

---

## Portfolio Snapshot (Post-Execution)

### Holdings After Today's Exit

| Ticker | Qty | Entry Cost (£) | Entry Date | Current Price (£) | Market Value (£) | P&L (£) | % of Portfolio | Days Held | Status |
|--------|-----|---|---|---|---|---|---|---|---|
| SHEL.L | 1.0624 | 28.70 | 2026-02-17 | 30.635 | 32.55 | +2.06 | 32.5% | 14 | ACTIVE |
| GLEN.L | 1.0350 | 5.08 | 2026-02-18 | 5.284 | 5.47 | +0.21 | 5.5% | 13 | ACTIVE |
| **Cash** | — | — | — | — | **3.50** | — | **62.0%** | — | — |
| **TOTAL** | — | — | — | — | **100.04** | — | 100% | — | — |

**Portfolio Beta:** Not calculated (insufficient correlation data)  
**Largest Correlation:** Not calculated

---

## Order Execution Plan

**Execution Sequence:** SELL_THEN_BUY
1. **SELL AZN.L** (0.3879 shares, market order, time_in_force=DAY)
   - Reason: Stop-loss at 151.25 GBP breached by low of 149.12 GBP
   - Estimated settlement: 2026-03-05 (T+1)
   - Estimated proceeds: 58.47 GBP (post-slippage)

**No BUY orders** due to insufficient cash post-exit.

---

## UK Costs Assumptions

| Cost Component | Rate | Applied | Notes |
|---|---|---|---|
| **Fees (Trade)** | 0 bps | No | fee_model.value = 0 |
| **Stamp Duty** | 50 bps | Yes (buys only) | UK equities only; ETFs exempt |
| **Slippage** | 10 bps | Yes (all orders) | Conservative estimate for LSE liquidity |
| **FX Impact** | N/A | No | All data in GBP; no FX exposure |

---

## Gap Risk & DAILY_CHECK Mode

**Stop Execution Mode:** DAILY_CHECK

**How It Works:**
- Stop-loss prices are monitored once daily (at session open/close).
- If the session low breaches the stop price, a market sell is triggered.
- **Gap Risk:** Overnight gaps or intraday gaps can cause actual fills far from the stop price, especially for small-cap or illiquid names.

**Today's AZN.L Exit:**
- Stop price: 151.25 GBP
- Session low: 149.12 GBP (3.13 GBP below stop)
- **Execution risk:** In a liquid name like AZN.L, slippage is typically modest (≤ 10 bps = 1.51 GBP). Actual fill likely 148–150 GBP range.

**Gap Risk Mitigation Applied:**
- Position sizing incorporates 10% gap_risk_buffer on new BUY entries.
- Reduces quantity to absorb intraday volatility without exceeding max_risk_per_trade_pct.

---

## What Could Invalidate This Plan?

1. **Market closure or unexpected exchange halt** → Plan void; client action required
2. **Corporate action on SHEL.L or GLEN.L** (dividend ex-date, rights issue, delisting) → Holdings affected
3. **Significant overnight gap on SHEL.L/GLEN.L below stops** → Unplanned exits
4. **AZN.L SELL not executable** (liquidity collapse) → Cash not realised; new buys blocked
5. **Major macro event** (bank failure, war, sharp rate move) → Market conditions change; confidence scores invalidated
6. **Regulatory suspension of LSE** → Trading halted
7. **Substantial new dividend or corporate cash event** → Cash balance assumption stale

---

## Data Quality Notes

✓ **market_data.csv:** Fresh as of 2026-03-04 (today's trading day)  
✓ **positions.json:** Consistent with market_data.csv; all positions ACTIVE  
✓ **universe.csv:** All 25 tickers matched to market_data; no mismatches  
✓ **trading_calendar.json:** Confirmed LSE trading day, no holidays  
✓ **All pre-computed indicators:** Present and non-null for evaluation tickers  
✓ **GBP normalisation:** All prices, volumes, indicators in GBP; no FX conversion required  

**Data Staleness:** None detected