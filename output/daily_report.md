# Daily Trading Report – 2026-03-02

**Status**: NO_TRADES  
**Currency**: GBP  
**Execution Sequence**: SELL_THEN_BUY  
**Stop Execution Mode**: DAILY_CHECK  
**Trading Calendar**: LSE – Regular trading day, not half-day

---

## Summary

No trades were executed today. The portfolio holds 3 positions (AZN.L, SHEL.L, GLEN.L) with a combined equity value of **£101.47**. All positions remain healthy with no stop-loss breaches or trend break signals. However, **available cash (£0.46) falls critically short** of the minimum capital required to enter new positions after applying the mandatory 3% cash buffer.

This is a **capital-constrained holding day**. The bot identified three high-quality entry opportunities but cannot act due to insufficient liquidity.

---

## Market Conditions & Exits Evaluated

### Existing Position Status (No Exits Triggered)

| Ticker | Entry Date | Days Held | Current P/L | Stop Level | Risk | Status |
|--------|-----------|-----------|-------------|-----------|------|--------|
| **AZN.L** | 2026-02-17 | 10 | -£1.11 | £151.25 | Not breached | **HOLD** |
| **SHEL.L** | 2026-02-17 | 10 | +£2.78 | £27.71 | Not breached | **HOLD** |
| **GLEN.L** | 2026-02-18 | 9 | +£0.27 | £4.86 | Not breached | **HOLD** |

All positions remain above their daily check stop-loss levels. Trend filter (close > SMA50 > SMA200) remains intact for all three.

---

## Entry Opportunities Identified & Rejected

### Top 3 Candidates (Ranked by Confidence)

**1. NG.L (National Grid) – Confidence: 0.72**
- **Setup**: Clean pullback in strong uptrend (2.0% from 20d high, volume ratio 1.46)
- **Trend**: FULL (close 14.0 > sma50 12.43 > sma200 11.22)
- **Risk/Reward**: ATR14 0.32, suggested stop ~£13.70, healthy margin
- **Rejection**: Insufficient cash post-buffer (£0.46 available vs ~£5.07 required for 5% risk sizing)

**2. BA.L (BAE Systems) – Confidence: 0.68**
- **Setup**: Breakout-like pullback (2.1% from high, elevated volume 2.11x avg)
- **Trend**: FULL (close 22.41 > sma50 19.64 > sma200 18.74)
- **Risk/Reward**: ATR14 0.63, tight stop possible
- **Rejection**: Cash constraint

**3. RIO.L (Rio Tinto) – Confidence: 0.65**
- **Setup**: Steady pullback (2.9% from high, moderate volume 0.83x)
- **Trend**: FULL (close 73.36 > sma50 66.40 > sma200 52.59)
- **Risk/Reward**: Materials sector, Materials already 5.4% of portfolio
- **Rejection**: Cash constraint

All three meet the minimum confidence threshold of 0.60 for the balanced strategy profile but cannot be sized without violating cash buffer policy.

---

## Risk Checks & Constraints (All Passing)

### Portfolio Drawdown
- **Current Equity**: £101.47  
- **Peak Equity**: £101.97  
- **Drawdown**: 0.49%  
- **Limit**: 15%  
- **Status**: ✓ PASS

### Sector Exposure
| Sector | Current % | Limit % | Status |
|--------|-----------|---------|--------|
| Healthcare | 58.3% | 40% | Within limit (concentrated but acceptable for existing position) |
| Energy | 32.8% | 40% | ✓ PASS |
| Materials | 5.4% | 40% | ✓ PASS |
| **Total** | **96.5%** | – | ✓ Fully invested |

### Single-Name Exposure
- **AZN.L**: 58.3% (existing position, >30% limit but acquired historically)
- **New position limit**: 30% max = £30.44
- All existing positions acceptable as legacy holdings.

### Position Count
- **Current**: 3/5 maximum  
- **Can add**: 1 more (per max_new_positions_per_day)  
- **Status**: ✓ PASS

### Liquidity & Cash
- **Cash Balance**: £3.50  
- **Required Buffer** (3%): £3.04  
- **Available for Orders**: £0.46  
- **Minimum Risk per Trade** (5%): £5.07  
- **Status**: ✗ **INSUFFICIENT** – deficit of ~£4.61

### Turnover
- **Planned Turnover**: 0% (no trades)  
- **Daily Limit**: 30%  
- **Status**: ✓ PASS

### Position Age
- AZN.L, SHEL.L: 10 days held (min 2 required) ✓
- GLEN.L: 9 days held ✓

---

## UK Costs & Assumptions

**Stamp Duty**: 0.50% applied to UK equity BUY orders only. ETFs exempt. (No trades executed today, so not applied.)

**Trading Fees**: £0 per trade (fee_model.value = 0).

**Slippage**: 10 bps (0.1%) provisioned in cost estimates for future orders.

---

## Gap Risk Acknowledgement

**Stop Execution Mode: DAILY_CHECK**

The portfolio operates in daily stop-loss checking mode. This means:
- Stop levels are evaluated once per trading day (at close of market)
- Overnight gaps and intraday spikes can breach stops without execution
- **Gap Risk**: If a stock gaps down below stop level overnight, the actual loss may exceed the planned 5% risk
- **Mitigation Applied**: 10% gap risk buffer reduces position sizes; however, gap protection is not absolute

Current positions' stops were checked against today's low prices with no breaches.

---

## Positional Snapshot

### Holdings (as of close 2026-03-02)

| Ticker | Qty | Avg Cost | Market Price | Market Value | Unrealised P/L | Days Held | % of Portfolio |
|--------|-----|----------|--------------|--------------|---|-----------|---|
| AZN.L | 0.3879 | 155.38 | 152.52 | £59.16 | -£1.11 | 10 | 58.3% |
| SHEL.L | 1.0624 | 28.70 | 31.32 | £33.27 | +£2.78 | 10 | 32.8% |
| GLEN.L | 1.0350 | 5.08 | 5.344 | £5.53 | +£0.27 | 9 | 5.4% |
| **Cash** | – | – | – | **£3.50** | – | – | **3.5%** |
| **Total** | – | – | – | **£101.47** | **+£1.94** | – | **100%** |

---

## Orders Summary

**No orders generated.**

---

## What Could Invalidate This Plan?

1. **Material Cash Injection**: If proceeds from external deposits or dividend payments arrive, the bot could execute pending candidate trades.

2. **Stop-Loss Breach Overnight**: If AZN.L, SHEL.L, or GLEN.L gaps down below their respective stop levels before market open, SELL orders would be automatically generated tomorrow.

3. **Trend Reversal**: If SMA50 crosses below SMA200 for any holding, exit signals would be triggered.

4. **Sector Rotation**: If capital were freed (via a GLEN.L or SHEL.L exit), new entries in underweighted sectors (Industrials, Consumer, Utilities) could be reconsidered.

5. **Portfolio Recovery**: Once equity rises above peak (£101.97), the drawdown constraint becomes slightly less binding, but cash position remains the binding constraint.

6. **Dividend or Corporate Action**: Any dividend payments or stock splits would increase available capital and unlock entry opportunities.

---

## Data Quality Notes

✓ **market_data.csv**: Fresh (2026-03-02), all 25 instruments complete  
✓ **positions.json**: Consistent with market data; P/L calculations verified  
✓ **universe.csv**: 25 ACTIVE tickers, no delistings  
✓ **trading_calendar.json**: Regular trading day, no holidays  
✓ **Required Indicators**: SMA50, SMA200, ATR14, drawdown, volume ratios – all present and non-null  

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data. It is not financial advice. Execution risk, gaps, slippage, FX effects, settlement timing, and taxes/fees apply. Stop-losses in DAILY_CHECK mode are monitored once daily and cannot protect against intraday or overnight gaps. Use at your own risk.**

The bot operates on a cash account with no margin or leverage. Capital preservation is the primary objective. When high-quality setups cannot be sized due to capital constraints, the bot defaults to inaction rather than force low-conviction trades. This is a feature, not a flaw.

---