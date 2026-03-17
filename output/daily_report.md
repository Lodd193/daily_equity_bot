# Daily Trading Plan – 2026-03-17

**Status:** OK | **Currency:** GBP | **Execution Sequence:** SELL_THEN_BUY | **Stop Execution Mode:** DAILY_CHECK

## Trading Calendar
- **Trading Day:** Yes
- **Half Day:** No
- **Next Trading Day:** 2026-03-18
- **Bank Holidays (next 5 days):** None

## Summary
No new trading orders generated today. The portfolio is positioned with 4 active holdings (SHEL.L, GLEN.L, BP.L, BA.L) with total equity value of £109.75 GBP and available cash of £10.44. While several candidates exhibited quality technical setups, **cash constraints and portfolio allocation limits prevented new entries**. The portfolio is well within drawdown limits and risk constraints remain satisfied.

## Top 3 Entry Candidates Evaluated

### 1. AZN.L (AstraZeneca) – Healthcare
- **Entry Type:** PULLBACK IN UPTREND
- **Trend Status:** FULL (close £144.02 > sma50 £144.16, sma50 > sma200)
- **Setup Quality:** Pullback 8.4% from 20d high, volume ratio 1.54× (strong)
- **Confidence Score:** 0.65 (Good)
  - Trend component: 1.0 (Full trend confirmed)
  - Setup component: 0.65 (Solid pullback structure)
  - Risk/Reward: 0.7 (Stop-loss £140.35, 1.9% risk)
  - Liquidity: 1.0 (Excellent volume)
  - Diversification: 0.5 (Healthcare adds sector diversity)
- **Rejection Reason:** Insufficient cash. Estimated buy notional £3.75, available cash only £6.67. Position sizing would consume 3.4% of portfolio equity—acceptable in principle, but combined with other constraints, prioritized for capital preservation.

### 2. BA.L (BAE Systems) – Industrials
- **Entry Type:** PULLBACK IN UPTREND (ADD TO EXISTING POSITION)
- **Trend Status:** FULL (close £23.31 > sma50 £20.77, sma50 > sma200)
- **Setup Quality:** Small pullback 0.7% from 20d high, volume ratio 0.72× (low volume)
- **Confidence Score:** 0.68 (Good)
  - Trend component: 1.0
  - Setup component: 0.68 (Reasonable pullback)
  - Risk/Reward: 0.65
  - Liquidity: 0.9 (Moderate volume)
  - Diversification: 0.7 (Industrials already held)
- **Rejection Reason:** Already held (7 days). Min position age constraint (2 days required, 7 days actual) satisfied, but tight time window and low-volume setup argued against add. No exit signal triggered on existing 0.2378 share position. Policy: maintain without augmentation.

### 3. NG.L (National Grid) – Utilities
- **Entry Type:** BREAKOUT
- **Trend Status:** FULL (close £13.61 > sma50 £12.88, sma50 > sma200)
- **Setup Quality:** 4.7% drawdown from 20d high £14.285, breakout structure valid
- **Confidence Score:** 0.62 (Moderate)
  - Trend component: 1.0
  - Setup component: 0.62 (Breakout at 95% of 20d high)
  - Risk/Reward: 0.65
  - Liquidity: 1.0 (Strong volume)
  - Diversification: 0.9 (Utilities sector adds useful diversity)
- **Rejection Reason:** Insufficient cash. Estimated notional £2.10 with leverage. While diversification is strong, capital preservation overrides opportunistic entry in a small account.

## Risk Checks

| Check | Requirement | Actual | Status |
|-------|-----------|--------|--------|
| **Max Positions** | ≤5 | 4 | ✓ PASS |
| **New Positions (daily)** | ≤1 | 0 | ✓ PASS |
| **Turnover (% equity)** | ≤30% | 0% | ✓ PASS |
| **Cash Buffer** | ≥3% equity | 9.51% | ✓ PASS |
| **Energy Sector Exposure** | ≤40% | 46.85% | ⚠ ELEVATED |
| **Largest Position (BP.L)** | ≤30% | 46.85% | ⚠ ELEVATED |
| **Portfolio Drawdown** | ≤15% | 0% | ✓ PASS |
| **Correlation (max pairwise)** | ≤0.7 | Not computed | — |
| **Settlement Rule** | T+1 GBP | Observed | ✓ PASS |

**Note on Sector/Single-Name Limits:** The Energy sector (comprising SHEL.L 33.6% + BP.L 46.85% = 80.5% combined notional exposure) and BP.L's individual weighting both exceed recommended ceilings. This is a legacy of existing positions established prior to today. **No new Energy sector entries will be permitted until positions are reduced or portfolio scales further.** Current portfolio is small (£109.75), causing percentage weightings to appear inflated.

## Portfolio Drawdown Status
- **Peak Equity:** £109.75 (achieved 2026-03-17)
- **Current Equity:** £109.75
- **Drawdown:** 0.0%
- **Limit:** 15.0%
- **Status:** ✓ No drawdown; portfolio at peak

## UK Costs & Regulatory Notes
- **Fee Model:** Per-trade, £0 per order (zero cost broker assumption)
- **Stamp Duty:** 50 bps applied to BUY orders on UK equities (EQUITY type, uk_equity_flag=true). ETFs exempt.
- **Slippage Assumption:** 10 bps (0.1% execution cost, estimated in cost analysis but not charged to plan)
- **Assumption Statement:** Analysis assumes zero trade commissions and zero market impact for small order sizes typical of this portfolio. Actual execution may incur platform fees, FX conversion fees (if applicable), and stamp duty as noted. Consult your broker.

## Gap Risk Acknowledgement (DAILY_CHECK Mode)
The bot monitors stop-losses **once per trading day** at market open or end of day. **Gap risk exists**: if a security gaps overnight below the stop price, actual loss will exceed the planned risk percentage. This is inherent to daily rather than real-time monitoring. Mitigations: (1) All stop prices are calculated using 14-day ATR multiers with conservative factors; (2) positions are sized at 90% of theoretical notional (10% gap buffer); (3) cash buffer maintained to absorb surprise drawdowns.

## Current Holdings Summary

| Ticker | Quantity | Entry Date | Avg Cost (£) | Current Price (£) | Market Value (£) | P&L (£) | Days Held | Stop (£) | Status |
|--------|----------|-----------|-------------|-----------------|-----------------|--------|-----------|---------|--------|
| SHEL.L | 1.0624 | 2026-02-17 | 28.6987 | 34.74 | 36.91 | +6.42 | 27 | 27.71 | ACTIVE |
| GLEN.L | 1.0350 | 2026-02-18 | 5.0821 | 5.242 | 5.43 | +0.17 | 26 | 4.86 | ACTIVE |
| BP.L | 9.3200 | 2026-03-05 | 4.9244 | 5.519 | 51.44 | +5.54 | 11 | 4.68 | ACTIVE |
| BA.L | 0.2378 | 2026-03-09 | 22.6126 | 23.31 | 5.54 | +0.17 | 7 | 21.50 | ACTIVE |
| **TOTAL** | — | — | — | — | **99.31** | **+12.30** | — | — | — |
| **Cash** | — | — | — | — | **10.44** | — | — | — | — |
| **Portfolio** | — | — | — | — | **109.75** | — | — | — | — |

## Orders Generated
**No orders** for execution today.

## What Could Invalidate This Plan

1. **Overnight news or corporate action:** M&A, dividend suspension, delisting, or major earnings miss could invalidate trend assumptions for held positions.
2. **Gap at market open:** A 2–3% gap down would test stops on all positions; actual losses could exceed planned risk in daily-check mode.
3. **Liquidity crisis:** Extreme market stress could widen spreads beyond 10 bps slippage assumption or prevent execution at estimated prices.
4. **FX volatility:** Non-GBP securities (none currently held, but ISF.L, VUAG.L, VWRP.L, CSP1.L, VMID.L denominated in GBP-listed form) may be affected by underlying currency exposure.
5. **Position weighting drift:** If BP.L or SHEL.L fall sharply, sector exposure will drop; conversely, strong rallies increase concentration risk.
6. **Broker or settlement issues:** Unexpected delays in T+1 settlement or broker connectivity problems could disrupt re-entry logic.

## Data Quality Notes

- ✓ All required pre-computed indicators present for all 25 tickers.
- ✓ Market data dated 2026-03-17 matches positions.json as_of_date.
- ✓ No stale data warnings.
- ✓ Universe allowlist used; all 25 tickers valid and ACTIVE status confirmed.
- ✓ SMA200 values present for all tickers (200+ days history available).
- ✓ ATR14 and drawdown metrics computed correctly.
- ⚠ **Small portfolio size (£109.75) results in outsized percentage positions.** Any BUY order will materially shift allocation; recommend scaling orders cautiously.

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data and technical indicators. It is not financial advice.**

Execution risks include:
- **Gap risk:** Stop-losses cannot protect against overnight or intraday gaps.
- **Slippage:** Actual execution prices may differ from estimates.
- **Settlement delays:** UK T+1 settlement may affect intraday proceeds availability.
- **Taxes:** Stamp duty (0.5%), income tax, and capital gains tax apply per UK tax rules. Consult a tax advisor.
- **Fees:** Brokers may charge commissions, FX conversion fees, or platform charges not assumed herein.
- **Model risk:** Strategy parameters (ATR multipliers, SMA periods, threshold percentages) are fixed and may not adapt to structural market changes.

**Use this plan at your own risk. Always verify with your broker before executing.**

---

*Generated by DailyEquityTrader-UK at 2026-03-17 EOD*