# Daily Trading Plan – 2026-02-25

## Status & Execution Details
- **Status**: NO_TRADES
- **Currency**: GBP
- **Date**: 2026-02-25
- **Trading Calendar**: LSE (is_trading_day=true, is_half_day=false)
- **Execution Sequence**: SELL_THEN_BUY
- **Stop Execution Mode**: DAILY_CHECK
- **Strategy Profile**: Balanced (swing 3–20 days)

---

## Executive Summary
The portfolio equity stands at **GBP 100.05** with cash balance **GBP 3.50**. After applying the mandatory 3% cash buffer (GBP 3.00), only **GBP 0.50** remains available for new positions. This is insufficient to meet minimum position sizing requirements for any candidate in the balanced profile. No new trades can be executed today.

The three existing positions (**AZN.L**, **SHEL.L**, **GLEN.L**) remain ACTIVE with no stop-loss breaches or trend breaks detected at today's close.

---

## Market & Trading Environment
- **Trading Day**: Yes – LSE open and active
- **Half Day**: No – full trading hours
- **Bank Holidays (next 5 days)**: None
- **Data Freshness**: Market data includes 2026-02-25 close; all required indicator columns present

---

## Portfolio Snapshot
| Ticker | Quantity | Avg Cost (GBP) | Market Value (GBP) | Unrealised P&L (GBP) | Days Held | Stop Price (GBP) | Status |
|--------|----------|----------------|--------------------|----------------------|-----------|------------------|--------|
| AZN.L  | 0.3879   | 155.3752       | 59.0306            | -1.2394              | 7         | 151.25           | ACTIVE |
| SHEL.L | 1.0624   | 28.6987        | 31.9889            | +1.4994              | 7         | 27.7112          | ACTIVE |
| GLEN.L | 1.0350   | 5.0821         | 5.5321             | +0.2721              | 6         | 4.8573           | ACTIVE |
| **Total** | | | **96.5516** | **+0.5321** | | | |

**Portfolio Equity**: GBP 100.05  
**Cash Balance**: GBP 3.50  
**Portfolio Peak (all-time high)**: GBP 100.19  
**Current Drawdown**: (100.19 – 100.05) / 100.19 = **−0.1393 (13.93%)**

---

## Risk & Constraint Checks

### Liquidity & Capital Availability
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Cash buffer (3%) | GBP 3.00 | Required | ✓ Applied |
| Available for buys | GBP 0.50 | – | **CRITICAL** |
| Max positions | 3 of 5 | 5 allowed | ✓ OK |
| Max new per day | 0 of 1 | 1 allowed | ✓ OK |

### Exposure & Diversification
| Metric | Value | Limit | Status |
|--------|-------|-------|--------|
| Largest position (AZN.L) | 59.1% | 30% | ✗ **EXCEEDS** |
| Healthcare sector | 59.1% | 40% | ✗ **EXCEEDS** |
| Turnover today | 0% | 30% | ✓ OK |
| Portfolio drawdown | 13.93% | 15% | ✓ OK (not breached) |

**Note**: The portfolio concentration in Healthcare (59.1% in AZN.L) exceeds the single-name (30%) and sector (40%) exposure limits. However, since no new trades are being executed, these existing positions remain unchanged. The bot cannot and does not liquidate existing positions to correct concentration unless stop-loss is breached or portfolio drawdown limit is exceeded.

### Positional Status
- **AZN.L**: Close (152.18) > SMA50 (141.15), unrealised P&L −1.24. Stop at 151.25; current close above stop. No exit signal.
- **SHEL.L**: Close (30.11) > SMA50 (27.68), unrealised P&L +1.50. Stop at 27.71; current close above stop. No exit signal.
- **GLEN.L**: Close (5.345) > SMA50 (4.623), unrealised P&L +0.27. Stop at 4.857; current close above stop. No exit signal.

---

## Top Candidate Setups (NOT EXECUTED – Capital Constraint)

### Candidate 1: SHEL.L (Shell)
- **Setup**: Pullback in uptrend
- **Trend Status**: FULL (close > SMA50 > SMA200)
- **Confidence**: 0.76 (76%)
- **Confidence Components**:
  - Trend: 0.95 (strong positive slope)
  - Setup: 0.72 (pullback to 20d high = 0%, healthy low-volume condition)
  - Risk/Reward: 0.68 (ATR-based stop 0.537 GBP below entry)
  - Liquidity: 0.99 (avg GBP volume 399M, exceptional)
  - Diversification: 0.65 (Energy sector, already 32% of portfolio)
- **Entry Price**: GBP 30.11 (at close)
- **Stop Price**: 30.11 − (0.537 × 1.5) = GBP 29.29
- **Estimated Position Size**: (5% risk × 100.05) / (0.82 margin) = 6.1 shares (~GBP 184 notional)
- **Rejection Reason**: Required capital GBP 184 > available GBP 0.50

### Candidate 2: RIO.L (Rio Tinto)
- **Setup**: Pullback in uptrend
- **Trend Status**: FULL (close > SMA50 > SMA200)
- **Confidence**: 0.74 (74%)
- **Confidence Components**:
  - Trend: 0.94 (positive slope, materials cyclical)
  - Setup: 0.70 (1.3% pullback from 20d high)
  - Risk/Reward: 0.67 (ATR stop 2.89 GBP)
  - Liquidity: 0.98 (avg GBP volume 259M)
  - Diversification: 0.68 (Materials, distinct from current holdings)
- **Entry Price**: GBP 74.61
- **Stop Price**: 74.61 − (2.89 × 1.5) = GBP 70.27
- **Estimated Position Size**: (5% risk × 100.05) / (4.34) = 1.15 shares (~GBP 86 notional)
- **Rejection Reason**: Required capital GBP 86 > available GBP 0.50

### Candidate 3: GLEN.L (Glencore) – Existing Position
- **Setup**: Continuation/pyramid opportunity (already in position)
- **Trend Status**: FULL (close > SMA50 > SMA200)
- **Confidence**: 0.71 (71%)
- **Rejection Reason**: Anti-churn rule (min 2 days before re-entry). Current holding: 6 days old. Could pyramid if capital permitted, but available capital GBP 0.50 insufficient for meaningful position. Not executed.

---

## Gap Risk & Stop-Loss Considerations
The portfolio uses **DAILY_CHECK** stop-loss execution mode:
- Stop prices are monitored once per trading day against the low price.
- **Gap risk**: Overnight or intraday gaps may cause actual exit prices to differ materially from stop prices.
- **Risk acknowledgement**: Losses may exceed the planned ATR-based risk if a position gaps through its stop overnight.
- **Mitigation**: All stop-loss breaches are checked at market open. If breached, market sells are generated.

Current positions have no stop breaches as of 2026-02-25 close.

---

## Capital & Liquidity Summary
| Item | GBP |
|------|-----|
| Cash balance | 3.5005 |
| Less: 3% buffer (required) | −3.0015 |
| Available for buys | 0.4990 |
| Unsettled proceeds | 0.0000 |
| Settlement days | 1 (T+1) |

**Intraday netting**: Disabled (assume_intraday_netting=false). Sell proceeds from today cannot fund today's buys.

---

## UK Costs & Fees Assumption
- **Stamp duty**: 50 bps applies to UK equity BUY orders only. ETF purchases exempt.
- **Broker fee model**: Per-trade cost of GBP 0.00 (zero commission environment assumed).
- **Slippage**: 10 bps estimated (embedded in position sizing calculations).
- **Total cost impact**: Minimal in this scenario due to no trades executed.

---

## Portfolio Metrics & Monitoring
| Metric | Value | Notes |
|--------|-------|-------|
| Equity value | GBP 100.05 | Current |
| Peak equity | GBP 100.19 | All-time high (2026-02-25 or earlier) |
| Drawdown | 13.93% | Below 15% limit; no liquidation triggered |
| Cash ratio | 3.5% | Low; constrains new entry capacity |
| Sector concentration | Healthcare 59.1% | Above 40% limit |
| Position count | 3 of 5 | Room for 2 more, but capital-constrained |
| Turnover today | 0% | No executions |
| Risk per trade (max) | GBP 5.00 | 5% of equity; unused today |

---

## What Could Invalidate This Plan?
1. **Intraday gap or limit move**: Stop-loss orders in DAILY_CHECK mode are monitored at end-of-day. Intraday price shocks are not caught in real time.
2. **Overnight news**: Corporate actions, earnings surprises, regulatory changes, or macroeconomic events could render the plan obsolete before market open.
3. **Liquidity crisis**: If market depth collapses, execution prices may slippage significantly beyond 10 bps.
4. **Data error**: If market data for 2026-02-25 is later found to be incorrect, all decisions are invalidated.
5. **Settlement delay**: If T+1 settlement is delayed, cash availability assumptions are broken.
6. **Capital infusion or withdrawal**: If funds are added or withdrawn, all position sizing must be recalculated.

---

## Immediate Action Items (For Manual Review)
1. **Capital constraint**: Portfolio equity is very low relative to trading costs. Consider:
   - Depositing additional capital to enable meaningful position sizes.
   - Liquidating low-conviction or losing positions to raise cash for high-conviction setups.
   
2. **Concentration risk**: AZN.L represents 59% of portfolio. Consider reducing on strength if it rallies further, or use any new capital inflows to diversify into other sectors.

3. **Position reviews** (daily):
   - **AZN.L**: −1.24 GBP unrealised loss. Monitor trend; stay above 151.25 stop.
   - **SHEL.L**: +1.50 GBP unrealised gain. Trend remains bullish.
   - **GLEN.L**: +0.27 GBP unrealised gain. Trend remains bullish.

---

## Data Quality Notes
- All required market data columns present and non-null for all 25 tickers.
- Indicator freshness: All indicators computed for 2026-02-25; no staleness issues.
- 20-day rolling calculations: Sufficient history present.
- 50-day SMA: Present for all tickers.
- 200-day SMA: Present for all tickers with >200-day history.
- Universe: 25 tickers total (20 equities, 5 ETFs); all ACTIVE status.
- Position reconciliation: 3 open positions match universe.csv; all ACTIVE.

---

## Disclaimer
**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice and does not constitute an offer to buy or sell securities.**

**Risk disclosures**:
- Execution risk: Actual fills may differ from planned entry prices due to slippage, market impact, or broker execution delays.
- Gap risk: Stop-losses in DAILY_CHECK mode are monitored once per day. Overnight or intraday gaps may result in losses exceeding the planned risk per trade.
- Settlement risk: T+1 settlement delays may affect cash availability for subsequent trades.
- FX risk: Non-GBP denominated assets have been converted to GBP; FX fluctuations are not hedged.
- Concentration risk: Current portfolio is concentrated in Healthcare (59%) and single stock (AZN.L). Large adverse moves in AZN.L could materially impact portfolio value.
- Model risk: All decisions rely on pre-computed indicators and historical patterns. Market regime changes or data errors can invalidate the strategy.
- Tax, fees, and corporate actions: Dividends, stock splits, mergers, and tax implications are not modeled in this plan.

**Use this plan at your own risk. Backtest results and historical performance do not guarantee future returns.**

---

Generated: 2026-02-25 (automated plan)  
Next review: 2026-02-26 (market open)

===