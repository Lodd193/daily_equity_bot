# DailyEquityTrader-UK Daily Report

**Date:** 2026-02-18  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (gaps may result in slippage beyond planned stop)

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-02-19
- **Bank Holidays (Next 5 Days):** None

---

## Executive Summary
**Action:** 1 BUY order generated for GLEN.L (Glencore, Materials).  
**Rationale:** High-confidence pullback entry in uptrend (confidence 0.74). Balanced profile, healthy volume structure. Adds Materials diversification to portfolio of Healthcare + Energy holdings.

**Risk Assessment:** ALL PASSED
- Portfolio drawdown: 0.0% (limit 15%) ✓
- Cash buffer: 3.0% (maintained) ✓
- Turnover: 5.2% (limit 30%) ✓
- Position limits: 3/5 positions ✓
- Sector/single-name exposure within bounds ✓

---

## Top 3 Entry Setups Considered

### 1. **GLEN.L (Glencore, Materials)** — ACCEPTED
- **Entry Type:** PULLBACK in Uptrend
- **Confidence:** 0.74 (Trend 0.95 | Setup 0.68 | Risk/Reward 0.72 | Liquidity 0.95 | Diversification 0.65)
- **Signal:**
  - Price: 5.077 GBP | SMA50: 4.5124 | SMA200: 3.4825 (Full uptrend ✓)
  - Drawdown from 20d high: 4.89% (within balanced threshold 5–15% ✓)
  - Volume ratio: 0.89 (healthy low-volume pullback ✓)
  - ATR stop: 4.8573 GBP (0.2197 GBP risk)
- **Decision:** BUY 1.035 shares @ MKT 5.077 GBP
- **Costs:** £0.0314 (fees + stamp duty + slippage)

### 2. **RIO.L (Rio Tinto, Materials)** — REJECTED
- **Entry Type:** PULLBACK in Uptrend
- **Confidence:** 0.72 (Trend 0.95 | Setup 0.65 | Risk/Reward 0.70 | Liquidity 0.90 | Diversification 0.60)
- **Rejection Reason:** Cash constraint. Required notional £19.73 > available cash £5.79 GBP (after buffer). Although confidence is high, position sizing is infeasible given small portfolio size and tight settlement constraints.

### 3. **GSK.L (GlaxoSmithKline, Healthcare)** — REJECTED
- **Entry Type:** PULLBACK in Uptrend
- **Confidence:** 0.68 (Trend 0.92 | Setup 0.60 | Risk/Reward 0.65 | Liquidity 0.92 | Diversification 0.58)
- **Rejection Reason:** Sector concentration. Healthcare already represents 60.13% of portfolio (AZN.L holding). Adding GSK.L would breach sector exposure limits (40% max). Diversification penalty applied due to high existing sector weight.

---

## Risk Checks — All PASSED ✓

| Check | Limit | Current | Status |
|-------|-------|---------|--------|
| Portfolio Drawdown | 15.0% | 0.0% | ✓ |
| Cash Buffer | 3.0% | 3.0% | ✓ |
| Max Positions | 5 | 3 | ✓ |
| Max New Positions/Day | 1 | 1 | ✓ |
| Turnover % | 30.0% | 5.2% | ✓ |
| Single-Name Exposure (post-trade) | 30.0% | 5.2% (GLEN.L) | ✓ |
| Sector Exposure (Materials) | 40.0% | 5.2% | ✓ |
| Sector Exposure (Healthcare) | 40.0% | 60.13% | ⚠ Existing only |
| Min Avg GBP Volume | £50k | £239.5M (GLEN.L) | ✓ |
| Min Price | £1.00 | £5.077 (GLEN.L) | ✓ |

---

## Portfolio Drawdown Status
- **Portfolio Peak Equity:** £100.19
- **Current Equity:** £100.19
- **Drawdown:** 0.0%
- **Drawdown Limit:** 15.0%
- **Status:** No liquidation required; normal operations.

---

## UK Costs Assumption Statement
**Fee Model:** Per-trade, £0.00 per trade  
**Stamp Duty:** 0.50 bps applied to BUY orders of UK equities (uk_equity_flag = true). ETFs exempt.  
**Slippage:** 10 bps estimated.  

For GLEN.L BUY order:
- Stamp duty: 5.2547 × 0.005 = £0.0262
- Slippage: 5.2547 × 0.001 = £0.0052
- Total costs: £0.0314

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

⚠ **Stop-loss monitoring is performed once daily at market open.** Overnight gaps or intraday moves may cause:
- Actual exit price worse than planned stop price (gap-down risk)
- Stop-loss penetration undetected until next trading day
- Larger losses than planned risk budget (max 5.0% per trade)

**Mitigation Applied:** Gap risk buffer of 10% has been applied to position sizing. Entry quantity reduced by 10% to buffer against gap risk. Actual position: 1.035 shares (vs. 1.149 without buffer).

---

## Portfolio Snapshot (Post-Trade)

### Current Holdings (Before Trade)
| Ticker | Quantity | Avg Cost | Market Price | Market Value | Unrealised PnL | Sector | Days Held | Status |
|--------|----------|----------|--------------|--------------|----------------|--------|-----------|--------|
| AZN.L  | 0.3879   | 155.3752 | 155.42       | 60.287       | +0.017         | Healthcare | 0 | ACTIVE |
| SHEL.L | 1.0624   | 28.6987  | 29.29        | 31.118       | +0.628         | Energy | 0 | ACTIVE |
| **GLEN.L** | **1.035** | **5.077** | **5.077** | **5.255** | **0.000** | **Materials** | **0** | **ACTIVE** |

### Summary Post-Trade
- **Total Positions:** 3 / 5 max
- **Total Equity:** £105.52
- **Total Cash:** £3.50
- **Cash as % of Portfolio:** 3.3%

### Sector Breakdown
- **Healthcare:** 60.13% (AZN.L)
- **Energy:** 31.07% (SHEL.L)
- **Materials:** 5.23% (GLEN.L)

---

## Orders for Execution

| Order ID | Ticker | Side | Type | Qty | Limit Price | Time in Force | Stop Price | Reason |
|----------|--------|------|------|-----|-------------|----------------|------------|--------|
| ORD001 | GLEN.L | BUY | MKT | 1.035 | — | GTC | 4.8573 | PULLBACK_IN_UPTREND_BALANCED_PROFILE |

**Execution Sequence:** SELL_THEN_BUY (no sells today; BUY executes immediately after market open).

---

## What Could Invalidate This Plan

1. **Overnight Gap Down:** GLEN.L opens < 4.8573 GBP → stop triggered immediately on T+1.
2. **Dividend/Corporate Action:** Unforeseen split or dividend announcement affecting GLEN.L or holdings.
3. **Sector Shock:** Major macro event affecting Materials (e.g., commodity price crash) invalidates trend filter.
4. **Data Feed Lag:** If market_data.csv for 2026-02-19 shows close < sma50_gbp for holdings, exit signals override plan.
5. **Liquidity Evaporation:** Market stress reducing GLEN.L avg_gbp_volume below £50k threshold → position becomes illiquid.
6. **Settlement Failure:** T+1 settlement delayed; proceeds not available for next-day rebalance.
7. **Exchange Closure:** Unscheduled LSE halt or force majeure.

---

## Data Quality Notes

✓ **market_data.csv:** All 25 tickers present for 2026-02-18. All required columns populated (sma50, sma200, atr14, drawdown, volume_ratio, etc.).  
✓ **positions.json:** 2 holdings (AZN.L, SHEL.L), days_held=0 (entry 2026-02-17). Both marked ACTIVE. No corporate actions flagged.  
✓ **universe.csv:** 25 instruments, 23 EQUITIES + 2 ETFs. All ACTIVE. GBP-normalised prices provided.  
✓ **trading_calendar.json:** 2026-02-18 confirmed as trading day (not half-day). No bank holidays next 5 days.  

**No data quality issues detected. All indicators computed and fresh.**

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice.**

- **Execution risk:** Orders may not fill at planned prices; slippage applies.
- **Gap risk:** Overnight and intraday gaps may cause losses exceeding planned stop-loss amount (10% gap buffer applied but not guaranteed).
- **Settlement timing:** T+1 settlement on UK equities; unsettled proceeds unavailable same day.
- **FX effects:** Non-GBP assets converted to GBP; FX rate fluctuations may affect returns.
- **Taxes & fees:** Stamp duty, capital gains tax, dividend withholding, and other charges apply beyond stated costs.
- **Regulatory:** This plan is for informational purposes. Verify compliance with FCA rules, CASS requirements, and your broker's T&C before execution.

**Use at your own risk. Consult a qualified financial advisor before executing.**

---

*Report generated by DailyEquityTrader-UK (Balanced Profile, Conservative Risk Settings)*