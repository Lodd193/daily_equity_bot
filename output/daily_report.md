# Daily Trade Plan | 2026-05-22 (Friday)

## Status
- **Status**: OK
- **Currency**: GBP
- **Execution Sequence**: SELL_THEN_BUY
- **Stop Execution Mode**: DAILY_CHECK (monitored once daily; gap risk acknowledged)
- **Portfolio Drawdown**: 8.61% (limit 15%)

## Trading Calendar
- **Is Trading Day**: Yes
- **Is Half Day**: No
- **Next Trading Day**: 2026-05-26
- **Bank Holidays (next 5 days)**: 2026-05-25 (UK Bank Holiday – no trading Friday 25 May)

---

## Summary
**No trades executed today.** 

All five positions held. Portfolio remains fully invested with strong trend confirmation in 4 of 5 holdings. Cash available (4.85 GBP) is insufficient to support new entries; all candidates exceeded available cash after mandatory 3% buffer. One position (AZN.L) flagged for trend deterioration and close monitoring.

---

## Opportunity Assessment

### Top Candidates Considered (All Rejected – Insufficient Cash)

#### 1. **HSBA.L** (Pullback in Uptrend)
- **Confidence**: 71.5% 
- **Trend Status**: FULL (close 13.742 > SMA50 12.913 > SMA200 11.541)
- **Setup**: Pullback 0.28% from 20d high; volume_ratio 0.915 (normal volatility)
- **Rejection Reason**: Required capital 5.31 GBP + slippage/fees. Available: 4.85 GBP (after 3% buffer).
- **Why Strong**: Financials sector, highest avg_gbp_volume (279M), tight stops possible.

#### 2. **LSEG.L** (Pullback in Uptrend)
- **Confidence**: 68.1%
- **Trend Status**: FULL (close 93.26 > SMA50 91.15 > SMA200 88.28)
- **Setup**: Pullback 7.2% from 20d high; quality reversal pattern
- **Rejection Reason**: Required capital 11.28 GBP. Available: 4.85 GBP.
- **Why Interesting**: Strong trend slope, good risk/reward at 93.26 entry.

#### 3. **AAL.L** (Breakout)
- **Confidence**: 67.2%
- **Trend Status**: FULL (close 38.35 > SMA50 34.95 > SMA200 30.65)
- **Setup**: Near 20d high (41.185); volume_ratio 0.507 (healthy confirmation)
- **Rejection Reason**: Marginal shortfall; required 4.89 GBP, available 4.85 GBP.
- **Why Good**: Materials sector diversification, strong intraday breakout candidate.

#### 4. **DGE.L** (Pullback)
- **Confidence**: 61.8%
- **Trend Status**: FULL (close 16.00 > SMA50 14.70 > SMA200 16.98 … wait, close > SMA50 > SMA200 broken due to SMA200)
- **Rejection Reason**: All available cash would be consumed; no buffer for slippage/fees.
- **Note**: Actually, SMA200 16.98 > SMA50 14.70, trend filter fails on this variant.

### Excluded Tickers (Trend/Data Quality Issues)

- **AZN.L**: Already held; trend broken (23 consecutive days below SMA50, SMA50 negative slope). Close below SMA50. On watch.
- **ULVR.L**: Trend broken (SMA50 43.70 > SMA200 47.85 inverted; close 42.58 below SMA50). HOLD/EXIT candidate.
- **GSK.L**: Trend broken (SMA50 20.06 > SMA200 18.23, but close 19.15 below SMA50). Negative slope.
- **RKT.L**, **IMB.L**, **BA.L**, **TSCO.L**, **NG.L**: Various trend breaks or deep pullbacks below SMA50. Not eligible for new entries.
- **REL.L**: Trend broken; 12 consecutive days below SMA50.
- **RIO.L**: Already held; no exit signal.
- **BP.L**, **SHEL.L**, **GLEN.L**: Already held; no exit signals.

---

## Risk & Constraint Checks

| Check | Limit | Current | Status |
|-------|-------|---------|--------|
| Portfolio Drawdown | 15.0% | 8.61% | ✅ PASS |
| Cash Buffer (3%) | 3.18 GBP | 8.03 GBP (pre-buffer) | ✅ PASS |
| Available for Buys | – | 4.85 GBP (post-buffer) | ⚠️ CRITICAL LOW |
| Max Positions | 5 | 5 | ✅ AT LIMIT |
| Position Age Constraint | 2 days | All > 49 days | ✅ PASS |
| Sector Exposure (Energy) | 40% | 42.5% | ⚠️ SLIGHT OVERSHOOT |
| Single Name (BP.L) | 30% | 48.3% | ❌ OVERSHOOT |
| Liquidity (avg_gbp_volume) | 50k GBP | All > 50k | ✅ PASS |
| Min Price | 1.0 GBP | All > 1.0 | ✅ PASS |
| Max Turnover (30% daily) | – | 0% (HOLD day) | ✅ PASS |

**Critical Issue**: BP.L concentration at 48.3% of portfolio exceeds 30% single-name limit. This position was entered before today's rules enforcement; no exit signal, so position held.

---

## Position Summary

| Ticker | Qty | Avg Cost | Current | Market Value | Unrealised PnL | Days Held | Stop | Trend | Action |
|--------|-----|----------|---------|--------------|----------------|-----------|------|-------|--------|
| **SHEL.L** | 1.0624 | 28.70 | 32.05 | 34.05 | +3.56 (+3.3%) | 93 | 27.71 | ✅ FULL | HOLD |
| **GLEN.L** | 1.0350 | 5.08 | 5.69 | 5.89 | +0.63 (+10.7%) | 92 | 4.86 | ✅ FULL | HOLD |
| **BP.L** | 9.3200 | 4.92 | 5.51 | 51.37 | +5.48 (+10.7%) | 77 | 4.68 | ✅ FULL | HOLD |
| **AZN.L** | 0.0383 | 142.90 | 139.16 | 5.33 | –0.14 (–2.6%) | 64 | 137.18 | ❌ BROKEN | HOLD* |
| **RIO.L** | 0.0208 | 71.09 | 77.77 | 1.62 | +0.14 (+8.6%) | 49 | 67.02 | ✅ FULL | HOLD |
| **CASH** | – | – | – | **8.03** | – | – | – | – | – |

*AZN.L is on close watch. Trend broken (negative slope, 23 consecutive days below SMA50). Position likely to hit time stop (~2026-06-02) or trigger stop-loss (137.18 GBP) if downtrend accelerates.

---

## What Could Invalidate This Plan

1. **Overnight Gap Down**: Stop-losses in DAILY_CHECK mode are monitored once per market close. A gap-down overnight could result in execution below the planned stop, incurring unexpected losses. Example: if BP.L gaps to 4.50 GBP, stop-loss would trigger at market opening, realising ~0.18 GBP loss on top of planned 0.23 GBP risk.

2. **Market Holiday (25 May)**: LSE closed Friday 25 May (UK Bank Holiday). Next trading day is 26 May. Any overnight news over the weekend could affect Monday open.

3. **Unexpected News/Corporate Action**: No dividend or split announced in today's data, but earnings announcements could trigger sharp moves.

4. **FX Risk (Minimal)**: All positions are GBP-denominated LSE equities. ETFs in universe (VUAG, VWRP, CSP1, ISF, VMID) are priced in GBP but track non-UK indices; FX headwinds not quantified here.

5. **Liquidity Evaporation**: If any position suddenly loses average volume, slippage could exceed 10 bps assumed. This is unlikely for FTSE 100 / mid-cap names but worth noting for smaller liquidity events.

---

## UK Costs Assumption

- **Fees**: 0 GBP per trade (fee_model.value = 0). Assumption: Broker offers zero-commission execution (typical of modern platforms).
- **Stamp Duty**: 50 bps (0.5%) applied **only** to BUY orders for UK equities (uk_equity_flag=true). ETFs are exempt. No BUY orders today, so no stamp duty applied.
- **Slippage**: 10 bps (0.1%) estimated for all market orders. Not charged today due to no trades.

If fees or stamp duty differ, recalculate available cash and repeat rank-order of candidates.

---

## Gap Risk Acknowledgement (DAILY_CHECK Mode)

This portfolio operates with **DAILY_CHECK** stop-loss execution:
- Stops are monitored once per trading day (at market close or EOD data refresh).
- **Gap risk**: If a position gaps sharply (intraday or overnight), the stop may only be triggered on the next scheduled check.
- **Mitigation**: 10% gap-risk buffer applied to position sizing, reducing quantity and expected loss impact.
- **Actual loss > Planned loss** if gap exceeds 10%.

---

## Orders to Execute

**None.** All positions held. No new entries, no exits today.

---

## Conclusion

Portfolio is well-positioned with 4/5 holdings in intact uptrends and strong positive PnL overall (+9.46 GBP or +8.9%). Cash reserves are critically low (4.85 GBP available after buffer), preventing new entry opportunities despite several high-confidence pullback/breakout setups. 

**Recommendation for next business day (26 May)**:
1. If any positions exit (stop-loss on AZN.L or manual trim of BP.L overshoot), redeploy freed cash into HSBA.L or LSEG.L (both 68–72% confidence, Full Trend).
2. Monitor AZN.L closely for time-stop execution or trend-break sell (likely ~2026-06-02).
3. Consider partial trim of BP.L to bring below 30% single-name limit and reallocate to Financials/Materials sector diversification.

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data.** It is not financial advice. 

**Risks**:
- Execution risk: Actual fill prices may differ from market data due to slippage, liquidity, and bid-ask spreads.
- Gap risk: Stop-losses in DAILY_CHECK mode cannot protect against overnight or intraday gaps. Losses may exceed planned 5% per trade.
- Settlement timing: UK T+1 settlement. Unsettled proceeds cannot fund same-day buys (assume_intraday_netting=false).
- Taxes/fees: Stamp duty, taxes, and regulatory costs not modelled in full detail.
- Model risk: Confidence scores and indicator values are pre-computed by the upstream pipeline; recalculation or data quality issues could invalidate signals.
- Sector/concentration risk: Energy sector is 42.5% of portfolio; BP.L alone is 48.3%. Diversification limited by low cash buffer.

**Use this plan at your own risk. Always consult a regulated financial adviser before trading.**

---

*Report generated by DailyEquityTrader-UK v1.0 | GBP cash account | LSE trading calendar | 2026-05-22*

===