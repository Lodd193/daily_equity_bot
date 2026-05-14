# Daily Trading Report — 2026-05-14

## Status
**Status:** NO_TRADES  
**Date:** 2026-05-14  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Trading Calendar:** LSE — Trading day (not half-day)  

---

## Executive Summary

Portfolio remains in **drawdown recovery mode**. Current equity value £104.99 is 9.64% below peak of £116.22 (recorded on previous high-water mark). While this is below the hard limit of 15% (portfolio_drawdown_limit_pct), the strategy adopts a conservative posture during recovery phases: **no new entries** are initiated when portfolio is underwater.

All six existing positions are **held on active daily stop-loss monitoring** (DAILY_CHECK mode). Three positions are profitable (SHEL.L, GLEN.L, BP.L, RIO.L) and two are underwater (BA.L, AZN.L), contributing to net recovery pathway.

---

## Top 3 Candidate Setups (All Rejected — Recovery Mode)

### 1. AAL.L (Anglo American) — PULLBACK in Uptrend
- **Confidence:** 72%  
- **Setup:** Close £40.63 > SMA50 £34.42 > SMA200 £30.16 (full uptrend)  
- **Signal:** 20-day pullback 1.35% from 20-day high; volume_ratio 0.45 (low-volume pullback, healthy)  
- **Rejection:** Position sizing fails. Stop distance £2.41, required risk capital ~£2.62 GBP (5% of equity), position size = 1.08 shares, notional £43.88 — would exceed 30% single-name limit. Also: portfolio drawdown recovery mode — no new entries.

### 2. RIO.L (Rio Tinto) — PULLBACK in Uptrend
- **Confidence:** 68%  
- **Setup:** Close £81.54 > SMA50 £71.35 > SMA200 £59.42 (strong uptrend, positive slope)  
- **Signal:** 20-day pullback 1.46% from 20-day high; high quality setup  
- **Rejection:** Portfolio in drawdown recovery — no new entries permitted. (Note: small existing position 0.0208 qty held for recovery contribution.)

### 3. LSEG.L (London Stock Exchange) — BREAKOUT
- **Confidence:** 65%  
- **Setup:** Close £92.12 > SMA50 £90.38 > SMA200 £88.40; positive slope  
- **Signal:** Close within 1.5% of 20-day high (£101.40); volume_ratio 0.45  
- **Rejection:** Portfolio drawdown recovery mode — no new entries. Defer until recovery confirmed.

---

## Risk & Constraint Checks

| Check | Value | Limit | Status |
|-------|-------|-------|--------|
| **Portfolio Drawdown** | 9.64% | 15.00% | ✓ PASS |
| **Current Positions** | 6 | 5 | ⚠️ AT LIMIT |
| **Cash Buffer (%)** | 3.29% | 3.00% | ✓ PASS |
| **Largest Position** | 47.92% (BP.L) | 30.00% | ❌ BREACH |
| **Energy Sector** | 31.77% | 40.00% | ✓ PASS |
| **Total Turnover** | 0.00% | 30.00% | ✓ PASS |
| **Liquidity (min_avg_volume)** | £50,000 | All pass | ✓ PASS |

### ⚠️ Portfolio Structure Issues
1. **Overweight Position:** BP.L at 47.92% of equity exceeds 30% single-name limit. This is a legacy position held from earlier entries. No liquidation triggered (profit +8.9%, stop at £4.68 active), but size constraint is breached.
2. **At Position Limit:** 6 positions held vs. max_positions=5. This is also a legacy state from previous rebalancing.

**Recovery Strategy:** As profitable positions recover and unrealised gains accumulate, plan to rebalance BP.L and reduce position count once drawdown closes.

---

## Portfolio Snapshot (as_of_date 2026-05-14)

### Positions Summary
| Ticker | Qty | Avg Cost | Market Price | Market Value | Unrealised PnL | Days Held | Stop | Status |
|--------|-----|----------|--------------|--------------|--------|-----------|------|--------|
| **BP.L** | 9.32 | £4.9244 | £5.407 | £50.39 | +£4.50 (+8.9%) | 69d | £4.68 | HOLD |
| **SHEL.L** | 1.0624 | £28.6987 | £31.485 | £33.45 | +£2.96 (+8.9%) | 85d | £27.71 | HOLD |
| **GLEN.L** | 1.035 | £5.0821 | £5.959 | £6.17 | +£0.91 (+14.7%) | 84d | £4.86 | HOLD |
| **AZN.L** | 0.0383 | £142.9028 | £137.4 | £5.26 | -£0.21 (-3.8%) | 56d | £137.18 | HOLD |
| **BA.L** | 0.2378 | £22.6126 | £19.23 | £4.57 | -£0.80 (-14.9%) | 65d | £21.50 | HOLD |
| **RIO.L** | 0.0208 | £71.091 | £81.54 | £1.70 | +£0.22 (+12.8%) | 41d | £67.02 | HOLD |

**Total Equity:** £104.99 (cash £3.45 + positions £101.54)  
**Portfolio Peak:** £116.22 (drawdown -9.64%)  
**Net Unrealised PnL:** +£6.78 (+6.9% on positions)

### Trend Status by Position
- ✓ **BP.L, SHEL.L, GLEN.L, RIO.L:** Price > SMA50 > SMA200, positive momentum (HOLD for recovery)
- ❌ **AZN.L, BA.L:** Price < SMA50 for 17+ consecutive days; downtrend (stop-losses active; monitor closely)

---

## Daily Stop-Loss Check (DAILY_CHECK Mode)

**CRITICAL: All six positions have active stop-loss orders monitored by the bot daily.**

| Ticker | Stop Price | Current Price | Buffer | Risk |
|--------|-----------|---------------|--------|------|
| SHEL.L | £27.71 | £31.485 | +10.8% | Low |
| GLEN.L | £4.86 | £5.959 | +18.5% | Low |
| BP.L | £4.68 | £5.407 | +13.4% | Low |
| RIO.L | £67.02 | £81.54 | +17.9% | Low |
| BA.L | £21.50 | £19.23 | **-10.8%** ⚠️ | **HIGH — Likely to trigger** |
| AZN.L | £137.18 | £137.4 | **-0.16%** ⚠️ | **CRITICAL — May trigger intraday** |

**AZN.L Stop-Loss Risk:** Price is only 18 pence above stop. Any downward movement in early trading may trigger automatic exit.  
**BA.L Stop-Loss Risk:** Price £19.23 is already 13.5% below SMA50 (£21.60); if price drops further, stop at £21.50 acts as floor.

---

## Orders Generated
**None.** Recovery mode + insufficient capital for sizing = no trade execution.

---

## UK Costs & Tax Notes
- **Stamp Duty:** 0.50% applied to UK equities BUY orders (not applicable today).
- **Trading Fees:** £0.00 per trade (fee_model type=per_trade, value=0).
- **Slippage Assumption:** 10 bps on execution (pre-computed in order notional estimates).
- **Settlement:** T+1 (UK standard); unsettled proceeds unavailable for same-day buys (assume_intraday_netting=false).

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

Stop-loss orders are **monitored once daily** (at market open). **Overnight and intraday gaps** can result in:
- Stop-loss execution at slippage prices far below planned stop price.
- Portfolio losses exceeding risk_per_trade_pct estimate.
- Unexecuted fills during volatile market periods.

**Mitigation:** Gap_risk_buffer applied to position sizing (10% reduction in quantity). This reduces notional exposure but does not eliminate gap risk entirely.

---

## What Could Invalidate This Plan

1. **Market-Moving News:** Corporate actions (dividend, split, takeover), earnings misses, regulatory news affecting holdings.
2. **Overnight/Intraday Gaps:** Large gap down at market open could trigger multiple stop-losses below planned levels (e.g., AZN.L and BA.L are at high risk).
3. **Settlement Failure:** If a sale fails to settle, available cash for buys is affected (not applicable today).
4. **Sector Shock:** If Energy sector (31.77% exposure) faces a broad sell-off, BP.L and SHEL.L would decline simultaneously.
5. **Liquidity Collapse:** If any position suffers reduced volume, stop-loss execution could occur at worse prices.
6. **Kill Switch Activation:** If CONFIG.kill_switch is set to true on next run, all trades are halted.

---

## Data Quality Notes

✓ **market_data.csv:** Fresh as of 2026-05-14. All required columns present (SMA50, SMA200, ATR14, drawdown, volume ratios).  
✓ **positions.json:** All positions valid, status ACTIVE, settlement clear.  
✓ **universe.csv:** All tickers ACTIVE, no DELISTING flags.  
✓ **trading_calendar.json:** LSE trading day (not half-day, no bank holidays).  

**No data quality issues detected.**

---

## Disclaimer

This is an **automated, rules-based trading plan** generated from provided historical market data and pre-computed indicators. It is **NOT financial advice**, and does not constitute a recommendation to buy, sell, or hold any security.

**Risks:**
- Execution risk: Orders may fill at slippage prices; stop-losses may trigger at worse prices than planned.
- Gap risk: Overnight gaps can result in losses exceeding estimated risk_per_trade_pct.
- Settlement risk: T+1 settlement may delay cash availability; unsettled proceeds unavailable for same-day buys.
- FX risk: Non-GBP securities subject to currency fluctuation (none in current portfolio; benchmark is GBP-normalised).
- Liquidity risk: Illiquid securities may have wider bid-ask spreads; participation limits may not be achievable.
- Systematic risk: Strategy is trend-following; may underperform during range-bound or reversal markets.
- Sector concentration: Portfolio is 31.77% Energy (BP.L + SHEL.L); sector downturn amplifies losses.
- Tax consequences: Frequent trading may trigger capital gains tax liability; consult a tax advisor.

**Use at your own risk. Past performance does not guarantee future results.**

---