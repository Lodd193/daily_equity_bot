# Daily Trading Plan Report
**Date:** 2026-02-26 | **Status:** NO_TRADES | **Currency:** GBP | **Execution Sequence:** SELL_THEN_BUY | **Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-02-27
- **Bank Holidays (Next 5 Days):** None

---

## Summary
No trades executed today. The portfolio is heavily constrained by insufficient available cash. With a cash balance of GBP 3.50 and a required cash buffer of GBP 2.99 (3% of equity), only GBP 0.51 remains available for new buys. Several high-confidence technical setups were identified but rejected due to capital insufficiency.

**Strategy:** Balanced swing (3–20 day horizon)  
**Profile Settings:** Balanced (confidence threshold 0.70, ATR multiplier 2.5, pullback range 2–6%)

---

## Top 3 Setup Candidates Considered

### 1. **RIO.L (Rio Tinto)** — BREAKOUT in Full Uptrend
- **Confidence Score:** 0.78
  - Trend (0.95): close_gbp 72.82 > sma50_gbp 65.74 > sma200_gbp 52.32
  - Setup (0.75): volume_ratio_20d 0.83, within 4.4% of 20d high 75.57
  - Risk/Reward (0.68): Stop at 70.01 (ATR 2.90×2.5), R:R ≈ 1.0
  - Liquidity (0.85): avg_gbp_volume_20d GBP 248M, volume ratio healthy
  - Diversification (0.65): Materials, low existing exposure (5.46%)
- **Rejection Reason:** Insufficient capital. Planned quantity 0.6 shares requires GBP 40.75; available GBP 0.51.
- **Rationale:** Strong breakout setup with positive momentum; would have diversified away from Healthcare concentration (58.61%).

### 2. **ULVR.L (Unilever)** — PULLBACK in Full Uptrend
- **Confidence Score:** 0.76
  - Trend (0.92): close_gbp 53.61 > sma50_gbp 49.98 > sma200_gbp 48.99
  - Setup (0.72): drawdown_from_20d_high_pct 2.98%, volume_ratio_20d 0.79 (low-vol pullback)
  - Risk/Reward (0.72): Stop at 51.26 (ATR 0.96×2.5), R:R ≈ 1.0
  - Liquidity (0.88): avg_gbp_volume_20d GBP 237M
  - Diversification (0.68): Consumer Staples, unique sector
- **Rejection Reason:** Insufficient capital. Planned quantity 0.72 shares requires GBP 38.80; available GBP 0.51.
- **Rationale:** Healthy pullback in established uptrend; conservative entry with low volume conditions.

### 3. **GSK.L (GSK)** — PULLBACK in Full Uptrend
- **Confidence Score:** 0.74
  - Trend (0.90): close_gbp 21.67 > sma50_gbp 19.59 > sma200_gbp 16.52
  - Setup (0.70): drawdown_from_20d_high_pct 5.03%, approaching support at sma50
  - Risk/Reward (0.68): Stop at 20.65 (ATR 0.48×2.5), potential for 4–6% move
  - Liquidity (0.82): avg_gbp_volume_20d GBP 261M
  - Diversification (0.72): Healthcare, but portfolio already 58.61% Healthcare (would exceed 60% sector limit)
- **Rejection Reason:** Insufficient capital; also sector concentration limit would be breached.
- **Rationale:** Quality pullback signal, but secondary constraint reinforces capital constraint as primary blocker.

---

## Risk Checks

| Check | Status | Details |
|-------|--------|---------|
| **Cash Buffer Rule** | ✓ PASS | Required GBP 2.99 (3% of equity), have GBP 3.50, surplus GBP 0.51 |
| **Max Positions** | ✓ PASS | Current 3/5 positions |
| **Max New Positions/Day** | ✓ PASS | Planned 0, limit 1 |
| **Portfolio Drawdown** | ✓ PASS | Current –0.51%, limit –15% |
| **Single-Name Exposure** | ⚠️ HIGH RISK | AZN.L = 58.61% of portfolio; limit 30% |
| **Sector Concentration** | ⚠️ HIGH RISK | Healthcare = 58.61%; limit 40% (BREACHED by existing position) |
| **Turnover** | ✓ PASS | Planned turnover 0%, limit 30% |
| **Settlement Constraint** | ✓ PASS | No unsettled proceeds; assume_intraday_netting = false |

**PORTFOLIO CONCENTRATION WARNING:** The existing AZN.L position (58.61%) is significantly above both the single-name limit (30%) and contributes to sector concentration (Healthcare 58.61% vs. limit 40%). This portfolio is poorly diversified and constrained. Consider SELL decision for AZN.L to rebalance.

---

## Portfolio Drawdown Status
- **Peak Equity:** GBP 100.19
- **Current Equity:** GBP 99.68
- **Drawdown:** –0.51% (0.51% below peak)
- **Drawdown Limit:** –15%
- **Status:** ✓ Within limit; no liquidation trigger

---

## UK Costs Assumption
- **Stamp Duty:** 0.50% applied to BUY orders on UK equities (status: no GBP values in orders to cost)
- **Trading Fees:** GBP 0.00 per trade (per fee_model configuration)
- **Slippage Assumption:** 10 bps assumed for execution (paper trade; no real slippage)
- **Gap Risk:** DAILY_CHECK stop-loss mode means stops are evaluated once daily at market open. Overnight gaps can result in losses exceeding planned risk. Gap risk buffer of 10% applied to position sizes (quantity reduced by 10% for DAILY_CHECK trades).

---

## Existing Positions Snapshot

| Ticker | Qty | Entry Date | Days Held | Entry Price | Curr Price | Market Value | Unrealised P&L | Stop Price | Status |
|--------|-----|-----------|-----------|------------|------------|--------------|----------------|-----------|--------|
| AZN.L | 0.3879 | 2026-02-17 | 8 | GBP 155.38 | GBP 151.10 | GBP 58.61 | –GBP 1.66 | GBP 151.25 | ACTIVE |
| SHEL.L | 1.0624 | 2026-02-17 | 8 | GBP 28.70 | GBP 30.24 | GBP 32.13 | +GBP 1.64 | GBP 27.71 | ACTIVE |
| GLEN.L | 1.035 | 2026-02-18 | 7 | GBP 5.08 | GBP 5.26 | GBP 5.44 | +GBP 0.18 | GBP 4.86 | ACTIVE |

**Portfolio Summary:**
- **Total Equity:** GBP 99.68
- **Cash:** GBP 3.50
- **Total P&L (Realised + Unrealised):** +GBP 0.16 (small gain)
- **Days Since Last Trade:** 7–8 days (min_position_age_days = 2, all positions eligible for sale if warranted)

---

## Existing Position Exit Checks

### STOP-LOSS REVIEW (DAILY_CHECK mode)
All current stops are above today's low prices. No stop breaches detected.
- **AZN.L:** Stop 151.25 > low 150.00 ✓
- **SHEL.L:** Stop 27.71 > low 29.75 ✓
- **GLEN.L:** Stop 4.86 > low 5.19 ✓

### TREND BREAK CHECK
All positions remain above 50-day SMA; no trend break signals.
- **AZN.L:** 151.10 > 141.45 (SMA50) ✓
- **SHEL.L:** 30.24 > 27.74 (SMA50) ✓
- **GLEN.L:** 5.26 > 4.65 (SMA50) ✓

### TIME STOP CHECK (pos held > X days with P&L ≤ 0)
- **AZN.L:** 8 days held, –GBP 1.66 P&L; time_stop_days = 20 (balanced profile). Not triggered.
- **SHEL.L:** 8 days held, +GBP 1.64 P&L (positive). Not triggered.
- **GLEN.L:** 7 days held, +GBP 0.18 P&L (positive). Not triggered.

**Conclusion:** No exits warranted at current market levels.

---

## Orders Table
*No orders generated today.*

---

## Capital Constraint: Why No Trades?

Available cash for buys = Cash Balance – Required Buffer = GBP 3.50 – GBP 2.99 = **GBP 0.51**

Minimum position size given current market prices and risk sizing:
- **Balanced Profile:** max_risk_per_trade_pct = 5% of equity = GBP 4.98 per trade
- **ATR Stop:** Typical stop distance GBP 0.50–3.00 depending on ticker
- **Position Sizing Formula:** qty = (GBP 4.98 / stop_distance) × (1 – 10% gap_buffer)
- **Minimum Notional for Entry:** Typically GBP 30–50 for a 1–5% portfolio position

**Conclusion:** The GBP 0.51 cash surplus is insufficient to fund a single balanced-risk trade. Capital allocation strategy requires portfolio rebalancing (e.g., reduce AZN.L concentration or take profits on SHEL.L) to free capital.

---

## What Could Invalidate This Plan?

1. **Intraday Cash Event:** Unexpected dividend payment or corporate action adding GBP 10+ would enable new entries.
2. **Stop-Loss Hit:** If AZN.L drops to 151.25 or below, the triggered SELL would free ~GBP 60 for reinvestment.
3. **Gap Up at Open:** If any position gaps up 3–5%, unrealised gains could push cash management differently.
4. **Urgent Rebalancing Signal:** If portfolio drawdown hits –5%, automated rebalancing may be triggered by external PM processes.
5. **Sector Rotation:** If Financials or Utilities see strong bullish signals, repositioning away from Healthcare would require sells first.

---

## Data Quality Notes

✓ **market_data.csv:** Fresh (as of 2026-02-26), all required columns present.
- All 25 tickers have complete SMA50, SMA200, ATR14, volume, and drawdown fields.
- No null values in critical pre-computed indicators.
- 20+ trading days of history confirmed for all tickers (no short-history exclusions).

✓ **positions.json:** Valid. All active positions confirmed in universe.csv with ACTIVE status.

✓ **universe.csv:** 25 instruments (20 equities, 5 ETFs), all ACTIVE.

✓ **trading_calendar.json:** Today is a valid trading day; no half-day or holiday impediments.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is NOT financial advice. Execution risk, gaps, slippage, FX effects, settlement timing, taxes, and fees apply.**

**Key Risks:**
- **Stop-Loss Gap Risk:** In DAILY_CHECK mode, stops are evaluated once daily at market open. Overnight gaps or pre-open moves can cause actual losses to exceed planned risk by 10–50% or more.
- **Liquidity Risk:** Actual execution prices may differ significantly from close prices due to bid–ask spreads, especially for lower-volume names.
- **Settlement Risk:** Under UK T+1 settlement, proceeds from sales are not available for same-day reinvestment unless assume_intraday_netting is true (currently false).
- **Concentration Risk:** Existing AZN.L position (58.61%) is well above the 30% single-name limit. Portfolio is vulnerable to single-stock moves.
- **Capital Constraint:** The GBP 3.50 cash balance limits flexibility for opportunistic entries. Rebalancing is advisable.

**Use this plan at your own risk. Consult a qualified financial adviser before committing capital.**

---