# Daily Trading Plan – 2026-02-17

## Status Summary
- **Status**: OK (no trades executed)
- **Trading Day**: Yes
- **Half-Day**: No
- **Currency**: GBP
- **Execution Sequence**: SELL_THEN_BUY
- **Stop Execution Mode**: DAILY_CHECK

## Calendar & Session Notes
- 2026-02-17 is a regular LSE trading day
- Next trading day: 2026-02-18
- No bank holidays in the next 5 days

## Portfolio Status
| Metric | Value |
|--------|-------|
| **Equity** | £99.46 |
| **Cash** | £8.79 |
| **Peak Equity** | £100.00 |
| **Drawdown** | -0.54% |
| **Available for Buys** | £0.57 |
| **Positions** | 2 active |

### Current Holdings
| Ticker | Quantity | Avg Cost | Market Value | Unrealised P&L | Days Held | Stop Price | Sector |
|--------|----------|----------|--------------|---|----------|----|----|
| AZN.L | 0.3879 | £155.38 | £60.21 | -£0.06 | 0 | £151.25 | Healthcare |
| SHEL.L | 1.0624 | £28.70 | £30.46 | -£0.03 | 0 | £27.71 | Energy |

**Position Concentration**: Healthcare 60.52%, Energy 30.65%

## Exit Review
No stop-loss triggers detected today. Both positions remain above their stop prices:
- AZN.L: Close £155.22 > Stop £151.25 ✓
- SHEL.L: Close £28.67 > Stop £27.71 ✓

No trend breaks (consecutive_days_below_sma50 = 0 for all holdings). Portfolio remains in acceptable health.

## Entry Candidates Evaluated

**Balanced Strategy Thresholds:**
- Pullback Entry: 3–12% drawdown from 20d high
- Breakout Entry: Within 1% of 20d high, volume_ratio ≥ 0.95
- Minimum Confidence: 0.65

### Top 3 Candidates (Rejected)

1. **RIO.L** (Rio Tinto) – PULLBACK, Confidence 0.78 ⭐⭐⭐
   - Trend: FULL (close £71.16 > SMA50 £63.39 > SMA200 £51.38)
   - Setup: 4.11% drawdown from 20d high, within pullback zone
   - Volume: 2,426,902 shares, ratio 0.61 (lower volume entry – healthier)
   - Liquidity: £273.53M avg daily volume ✓
   - **Rejection**: Insufficient cash. Required ~£71.16 minimum; available £0.57
   - Risk/Reward: Stop at £68.12 (ATR buffer), potential 4.5% risk

2. **GSK.L** (GlaxoSmithKline) – BREAKOUT, Confidence 0.74 ⭐⭐⭐
   - Trend: FULL (close £22.39 > SMA50 £19.03 > SMA200 £16.23)
   - Setup: Close within 0.9% of 20d high (£22.60), volume ratio 0.91
   - Liquidity: £205.04M avg daily volume ✓
   - **Rejection**: Insufficient cash. Required ~£22.39; available £0.57
   - Positive momentum: SMA50 slope positive, close 17.6% above SMA50

3. **NG.L** (National Grid) – BREAKOUT, Confidence 0.71 ⭐⭐⭐
   - Trend: FULL (close £13.77 > SMA50 £11.99 > SMA200 £11.08)
   - Setup: Close within 1.4% of 20d high (£13.99), strong volume ratio 1.76
   - Liquidity: £125.48M avg daily volume ✓
   - **Rejection**: Insufficient cash. Required ~£13.77; available £0.57
   - Momentum: Strong volume breakout signal, close 14.8% above SMA50

## Why No Trades Today?

**Critical Constraint**: Cash Position Severely Depleted
- Current cash balance: £8.79
- Required buffer (3%): £2.98
- Available for deployment: £0.57
- Minimum viable position size: £1–2 GBP (even with fractional shares)

The portfolio entered today with only £8.79 cash against £99.46 equity (8.8% cash ratio). After subtracting the required 3% buffer, less than £0.60 remains for new positions. While several high-confidence entry opportunities exist (RIO.L, GSK.L, NG.L all scoring 0.71–0.78), every candidate requires minimum notional orders exceeding available cash by 10–100×.

**Decision Logic**: 
- NO_BUY bias is active when cash is inadequate.
- Rather than reduce position sizes to <£0.50 (fractionation becomes impractical and slippage/fees consume all expected return), the system chooses NO_TRADES.
- Recommend: Monitor for cash generation (dividends, settlement events) or execute targeted sells to raise capital for higher-conviction setups.

## Risk Checks

| Risk Category | Limit | Current | Status |
|---------------|-------|---------|--------|
| **Max Positions** | 5 | 2 | ✓ OK |
| **Max New Per Day** | 1 | 0 | ✓ OK |
| **Turnover %** | 30% | 0% | ✓ OK |
| **Max Risk Per Trade** | 5% | N/A | N/A |
| **Largest Position** | 30% | 60.5% | ⚠️ CAUTION |
| **Sector Exposure** | 40% | Healthcare 60.5% | ⚠️ CAUTION |
| **Portfolio Drawdown** | -15.0% | -0.54% | ✓ OK |
| **Min Liquidity (£50k daily)** | £50,000 | All candidates > £125M | ✓ OK |
| **Min Price** | £1.00 | All > £1.00 | ✓ OK |

### Concentration Risk ⚠️
AZN.L (Healthcare) represents 60.5% of portfolio equity, significantly above the 30% single-name limit. This position was opened today (days_held = 0), suggesting a fresh entry that has already moved against the portfolio (-£0.06 unrealised loss). SHEL.L (Energy) adds another 30.7%, creating a two-name concentration.

**Recommendation**: Consider scaling back AZN.L on any strength to restore diversification and improve resilience to sector rotation.

## Data Quality & Assumptions

**Market Data**: Fresh as of 2026-02-17 ✓
**All Required Columns Present**: ✓
**FX Treatment**: All instruments priced in GBP, no FX adjustment needed ✓
**Fees & Costs**:
- Stamp duty: 50 bps applied to UK equity purchases only
- Trading fee: £0 per trade (per fee_model)
- Slippage assumption: 10 bps on entry/exit
- No corporate actions, dividend payments, or splits reported today

**Settlement Assumption**: T+1 (UK standard); unsettled proceeds = £0.

## Gap Risk Acknowledgement

**DAILY_CHECK Stop Execution Mode Active**:
- Stop-losses are evaluated once per trading day (at market close or by daily scan).
- **CRITICAL**: This method provides NO protection against overnight gaps, flash crashes, or intraday reversals beyond the daily check point.
- Example: If SHEL.L gaps down to £25.00 overnight, actual loss could be £3.67/share beyond the planned £0.66 stop distance.
- For active risk management, consider requesting broker GTC (Good-Till-Cancelled) stop-loss placement for real-time execution.

## What Could Invalidate This Plan?

1. **Cash Injection**: If dividends, settlements, or deposits add >£1, new setups become viable.
2. **Trend Reversals**: If SMA50 crosses below close on RIO.L, GSK.L, NG.L, entry signals reverse.
3. **Overnight Gaps**: AZN.L or SHEL.L gaps down through stops → unplanned stop losses.
4. **Volume Collapse**: If avg_gbp_volume drops below £50k daily, liquidity filter blocks trades.
5. **Corporate Actions**: Delisting, suspension, or splits in portfolio → forced liquidation.
6. **Sector Rotation**: Flight from Healthcare/Energy could accelerate AZN.L/SHEL.L declines.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice.**

Execution involves real risks:
- **Slippage & Fees**: Actual execution prices may differ from assumptions by 10+ bps.
- **Gap Risk**: DAILY_CHECK stop-losses cannot protect against overnight or intraday gaps. Losses may exceed planned risk.
- **Settlement Timing**: T+1 settlement delays cash availability; bridging costs apply if positions are resized before settlement.
- **FX Effects**: GBP volatility affects international ETF valuations (e.g., VUAG.L, CSP1.L).
- **Concentration Risk**: Current AZN.L position is 60.5% of equity—significantly above policy limits.
- **Regulatory & Tax**: UK stamp duty, capital gains tax, and tax-loss harvesting rules apply.
- **Market Liquidity**: During stress (halts, wide bid-ask), fills may be worse than modelled.

**Use at your own risk. Consult a qualified financial advisor before deploying capital.**

---

## Orders Execution

**No orders to execute today.**

---

*Plan generated 2026-02-17 by DailyEquityTrader-UK (Balanced Conservative, GBP Cash Account, LSE)*