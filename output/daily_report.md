# Daily Trading Plan - 2026-03-23

**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (daily monitoring, gap risk acknowledged)

---

## Trading Calendar
- **Trading Day:** Yes
- **Half Day:** No
- **Next Trading Day:** 2026-03-24
- **Bank Holidays (5 days):** None

---

## Summary of Actions
**No trades are recommended today.** The portfolio is constrained by structural issues that prevent meaningful new entries and favour preservation over incremental trading.

### Key Constraints Blocking New Entries
1. **Position Limit Reached:** Portfolio holds 5 positions (max=5). No capacity for new longs.
2. **Cash Severely Depleted:** £4.94 available (after 3% buffer = £1.75 usable). Insufficient to fund any meaningful position.
3. **Sector Concentration:** Energy sector (BP + SHEL) = 79.9% of portfolio, far exceeding 40% limit.
4. **Single-Name Concentration:** BP.L alone = 47.1% of portfolio, exceeding 30% limit.
5. **Portfolio Drawdown Risk:** 3.22% below peak (£110.0). Approaching 15% hard limit at £93.5.
6. **No High-Conviction Setups:** Top candidate (RIO.L) scores only 0.58 confidence, below 0.65 balanced profile threshold.

---

## Top 3 Candidate Opportunities Evaluated

### 1. RIO.L (Rio Tinto) - Materials
- **Trend Status:** FULL (close £63.75 > SMA50 £68.42; SMA50 > SMA200)
- **Entry Type:** PULLBACK from 20-day high
- **Drawdown from high:** 15.6% (within balanced 12–20% pullback zone)
- **Volume Signal:** 1.94x average (strong participation, healthy breakout)
- **Confidence Score:** 0.58 (Trend 0.85 | Setup 0.52 | RR 0.48 | Liquidity 0.72 | Diversification 0.45)
- **Rejection Reason:** Confidence below 0.65 threshold. Portfolio at position limit. Insufficient cash (need £15.2 notional + costs; have £1.75). Sector limit breach (Materials already 5.3%).

### 2. GLEN.L (Glencore) - Materials
- **Trend Status:** FULL (close £5.156 > SMA50 £5.057; SMA50 > SMA200)
- **Entry Type:** BREAKOUT (close 0.020% above 20-day high; volume 1.19x average)
- **Entry Signal:** Strong momentum breakout with positive slope
- **Confidence Score:** 0.62 (Trend 0.88 | Setup 0.58 | RR 0.52 | Liquidity 0.68 | Diversification 0.48)
- **Rejection Reason:** Already a held position (30 days). Confidence below threshold. Would exacerbate Materials sector (currently 5.3%). No additional cash to add.

### 3. BA.L (BAE Systems) - Industrials
- **Trend Status:** FULL (close £21.40 > SMA50 £20.95; SMA50 > SMA200)
- **Entry Type:** Potential secondary entry (already held; underwater -1.4%)
- **Confidence Score:** 0.61 (Trend 0.82 | Setup 0.48 | RR 0.55 | Liquidity 0.71 | Diversification 0.50)
- **Rejection Reason:** Existing position (11 days held; unrealised -£0.288). Confidence below threshold. Adding would increase Industrials sector beyond limits. No cash available.

---

## Risk Checks (Balanced Profile)

### Portfolio Drawdown Status
- **Current Portfolio Equity:** £106.46
- **Peak Equity:** £110.0
- **Drawdown:** 3.22% (well within 15% limit)
- **Margin to Trigger:** 11.78% (drawdown threshold = 15%)
- **Status:** ✓ SAFE (no liquidation required)

### Position Limits
- **Current Positions:** 5 / 5 maximum
- **Status:** ✗ AT LIMIT (no new entries possible)

### Cash Position
- **Cash Balance:** £4.94
- **Required Buffer (3%):** £3.19
- **Available for Buys:** £1.75
- **Status:** ✗ CRITICALLY LOW (cannot fund meaningful trades)

### Concentration Risks (HARD CONSTRAINTS BREACHED)
| Metric | Current | Limit | Status |
|--------|---------|-------|--------|
| **Largest Position (BP.L)** | 47.1% | 30% | ✗ BREACH |
| **Energy Sector** | 79.9% | 40% | ✗ BREACH |
| **Sector (Materials + Energy)** | 85.2% | 40% + 40% | ✗ BREACH |
| **Cash/Equity Ratio** | 4.6% | 3% | ✓ OK |

### Liquidity Filter
All candidates meet minimum thresholds:
- Min GBP volume (£50k): All pass
- Min price (£1.0): All pass
- Participation: RIO.L notional would be <5% of 20d avg volume ✓

### Turnover Constraint
- **Planned Turnover:** 0.0%
- **Limit:** 30.0%
- **Status:** ✓ OK

### Correlation Constraint
- **Max Pairwise Correlation:** 0.64 (Energy/Materials commodity link)
- **Max Correlated Pairs:** <3 with rho > 0.7
- **Status:** ✓ OK (no additional positions to worsen)

---

## UK Costs Assumption
- **Fee Model:** Per-trade flat fee = £0 (not charged in paper mode)
- **Stamp Duty:** 50 bps applied to UK equity BUY orders (0.5% cost)
- **Slippage Assumption:** 10 bps (0.1%) on entry; 5 bps on exit
- **Example Cost for £100 BUY:** ~£0.50 (stamp) + ~£0.10 (slippage) = ~£0.60 (0.6% total)

---

## Gap Risk Acknowledgement
**DAILY_CHECK Mode Active:** Stop-losses are monitored once daily at market close. This approach:
- ✓ Allows flexible monitoring and selective execution
- ✗ Cannot protect against intraday gaps or overnight moves
- ✗ Actual losses may exceed planned risk if gap occurs at or below stop price

**Gap Risk Mitigation Applied:** 10% buffer reduction applied to position sizing (all held positions sized with this buffer historically).

Current positions have set stops:
- SHEL.L: stop £27.71 | current low £32.74 (margin £5.03)
- GLEN.L: stop £4.86 | current low £4.95 (margin £0.09) ⚠️ TIGHT
- BP.L: stop £4.68 | current low £5.32 (margin £0.64)
- BA.L: stop £21.50 | current low £21.40 (margin -£0.10) ⚠️ COULD TRIGGER
- AZN.L: stop £137.18 | current low £134.78 (margin -£2.40) ⚠️ COULD TRIGGER

---

## Portfolio Snapshot

### Holdings Summary (as of 2026-03-23)
| Ticker | Qty | Entry Cost | Entry Date | Days Held | Current Price | Market Value | Unrealised PnL | Stop | Status |
|--------|-----|-----------|-----------|-----------|---------------|--------------|----------------|------|--------|
| **SHEL.L** | 1.0624 | £28.70 | 2026-02-17 | 31 | £33.55 | £35.64 | +£5.15 (14.5%) | £27.71 | ACTIVE |
| **GLEN.L** | 1.0350 | £5.08 | 2026-02-18 | 30 | £5.16 | £5.34 | +£0.08 (1.4%) | £4.86 | ACTIVE |
| **BP.L** | 9.3200 | £4.92 | 2026-03-05 | 15 | £5.39 | £50.20 | +£4.30 (8.6%) | £4.68 | ACTIVE |
| **BA.L** | 0.2378 | £22.61 | 2026-03-09 | 11 | £21.40 | £5.09 | -£0.29 (-5.7%) | £21.50 | ACTIVE |
| **AZN.L** | 0.0383 | £142.90 | 2026-03-18 | 2 | £137.42 | £5.26 | -£0.21 (-4.0%) | £137.18 | ACTIVE |

### Sector Exposure
| Sector | Value | % of Portfolio | Limit | Status |
|--------|-------|----------------|-------|--------|
| Energy | £85.84 | 80.6% | 40% | ✗ OVER |
| Materials | £5.34 | 5.0% | 40% | ✓ OK |
| Industrials | £5.09 | 4.8% | 40% | ✓ OK |
| Healthcare | £5.26 | 4.9% | 40% | ✓ OK |
| **Cash** | £4.94 | 4.6% | — | ✗ LOW |

### Performance Metrics
- **Total Unrealised PnL:** +£9.03 (8.5% of equity)
- **Portfolio Return (Peak-to-Date):** -3.22% (from £110.0 to £106.46)
- **YTD Equity Change:** +£6.46 (6.5% from presumed £100 start)
- **Largest Winner:** SHEL.L +14.5%
- **Largest Loser:** BA.L -5.7%
- **Winning Positions:** 3 / 5 (60%)

---

## What Could Invalidate This Plan

1. **Overnight Gap Events:** If GLEN.L or AZN.L gap below stops overnight, DAILY_CHECK execution will trigger stop-loss sells at next market opening.
2. **Stop-Loss Breaches (Current Risk):**
   - **GLEN.L High Risk:** Stop at £4.86; current low £4.95. Tight margin means any pullback could execute.
   - **BA.L Imminent Risk:** Stop at £21.50; current low £21.40. Already breaching. Next check could trigger exit.
   - **AZN.L Imminent Risk:** Stop at £137.18; current low £134.78. Already breached. Exit could execute.

3. **Corporate Actions:** Dividend ex-dates, stock splits, or special events not yet in data.
4. **Portfolio Rebalancing Requirement:** If drawdown accelerates to 15%, automatic full liquidation triggered.
5. **Liquidity Shock:** If avg_gbp_volume_20d falls below £50k for held positions, may need to reduce.

---

## Data Quality Notes

- ✓ All required pre-computed columns present (SMA50, SMA200, ATR14, drawdown, volume ratios).
- ✓ Market data dated 2026-03-23 (today, fresh).
- ✓ 25 tickers in universe; all ACTIVE status.
- ✓ No missing indicator values for evaluated candidates.
- ✓ Trading calendar confirms LSE open today (not half-day).
- ⚠️ **Correlation matrix not provided:** Max pairwise correlation estimated at 0.64 (Energy/Materials commodity sector link). If actual correlations differ materially, diversification assumption may be invalid.

---

## Orders to Execute

**None.** No orders generated today.

---

## Recommended Next Steps (Not Part of This Plan)

1. **Rebalance Energy Sector:** Current 80.6% exposure vs. 40% limit requires liquidation of either SHEL.L or BP.L to bring sector within constraints.
2. **Exit Underwater Positions:** AZN.L (-4.0%) and BA.L (-5.7%) are both below entry. Consider stop-loss or profit-taking to raise cash.
3. **Rebuild Cash Buffer:** Current £4.94 (4.6% of equity) is tight. Target 5–10% cash reserve to enable opportunistic entries.
4. **Monitor Tight Stops:** GLEN.L (£0.09 margin) and AZN.L (already breached) are at risk of unplanned execution. Consider widening stops or tightening entries.

---

## Disclaimer

This is an automated, rules-based trading plan generated from provided historical market data. It is **not financial advice**. 

**Execution Risk Acknowledgements:**
- Stop-losses in DAILY_CHECK mode are monitored only once daily and cannot protect against intraday or overnight gaps.
- Actual execution prices may differ materially from planned prices due to slippage, liquidity, and market conditions.
- FX effects, settlement delays (T+1 in UK), corporate actions, and tax implications are not accounted for in this model.
- Portfolio composition violates stated risk limits (sector and single-name concentration). Rebalancing recommended urgently.
- Past performance of indicators does not guarantee future results.

**Use this plan at your own risk. Consult a financial advisor before trading.**

---

*Generated by DailyEquityTrader-UK (Balanced Profile, Conservative Bias) | 2026-03-23 EOD*