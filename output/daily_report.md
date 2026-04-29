```markdown
# Daily Trading Plan Report
**Date:** 2026-04-29 (Wednesday)  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY (sells before buys)  
**Stop Execution Mode:** DAILY_CHECK (daily monitoring of stop levels)  

---

## Trading Calendar
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-04-30
- **Bank Holidays (next 5 days):** 2026-05-04

---

## Portfolio Summary

### Before Today's Trades
| Metric | Value |
|--------|-------|
| Total Equity (GBP) | 109.20 |
| Cash Balance (GBP) | 3.45 |
| Portfolio Peak Equity (GBP) | 116.22 |
| Current Drawdown (%) | 6.03% |
| Drawdown Limit (%) | 15.0% |
| Positions Held | 6 |
| Max Positions | 5 |

### Positions
| Ticker | Qty | Entry Date | Days Held | Entry Price | Current Price | Market Value | PnL | Stop | Status |
|--------|-----|------------|-----------|-------------|---------------|--------------|-----|------|--------|
| SHEL.L | 1.0624 | 2026-02-17 | 70 | 28.70 | 32.80 | 34.85 | +4.36 | 27.71 | ACTIVE |
| GLEN.L | 1.0350 | 2026-02-18 | 69 | 5.08 | 5.53 | 5.73 | +0.47 | 4.86 | ACTIVE |
| BP.L | 9.3200 | 2026-03-05 | 54 | 4.92 | 5.76 | 53.67 | +7.78 | 4.68 | ACTIVE |
| BA.L | 0.2378 | 2026-03-09 | 50 | 22.61 | 20.01 | 4.76 | -0.62 | 21.50 | **SELL** |
| AZN.L | 0.0383 | 2026-03-18 | 41 | 142.90 | 136.92 | 5.24 | -0.23 | 137.18 | **SELL** |
| RIO.L | 0.0208 | 2026-04-02 | 26 | 71.09 | 72.25 | 1.50 | +0.02 | 67.02 | ACTIVE |

---

## EXIT ANALYSIS

### BA.L – BAE Systems (Industrials) – **SELL**
**Reason:** Trend Break  
**Trigger:** 7 consecutive days of close < SMA50; current close (20.01) < SMA50 (21.89)

| Metric | Value |
|--------|-------|
| Entry Date | 2026-03-09 |
| Days Held | 50 |
| Entry Price | 22.61 GBP |
| Current Price | 20.01 GBP |
| Current PnL | -0.62 GBP (-2.7%) |
| Market Value | 4.76 GBP |

**Rationale:**  
The strategy requires a hard exit when an uptrend breaks (close < SMA50 for 7+ consecutive days). BA.L breached this level 7 days ago, and the close remains ~8% below the SMA50. While the position has been held 50 days and is only in a small loss, the uptrend has decisively broken and the risk of further downside has increased. Exiting preserves remaining capital and reduces sector concentration (Energy/Industrials).

---

### AZN.L – AstraZeneca (Healthcare) – **SELL**
**Reason:** Trend Break  
**Trigger:** 7 consecutive days of close < SMA50; current close (136.92) < SMA50 (146.98)

| Metric | Value |
|--------|-------|
| Entry Date | 2026-03-18 |
| Days Held | 41 |
| Entry Price | 142.90 GBP |
| Current Price | 136.92 GBP |
| Current PnL | -0.23 GBP (-0.16%) |
| Market Value | 5.24 GBP |

**Rationale:**  
AZN.L has similarly breached its SMA50 for 7 consecutive days (close is ~7% below SMA50). This is a mandatory trend-break exit per strategy rules. The position has lost ground and the uptrend supporting the entry is no longer valid.

---

## NEW ENTRY ANALYSIS

### Top Candidate: LSEG.L (London Stock Exchange Group, Financials)
**Confidence Score:** 0.70 (Above 0.60 threshold, but rejected due to cash constraint)

| Metric | Value |
|--------|-------|
| Entry Type | PULLBACK |
| Trend Status | PARTIAL (close > SMA50, SMA50 slope positive, but SMA50 < SMA200) |
| Current Price | 96.48 GBP |
| SMA 50 | 87.83 GBP |
| SMA 200 | 88.97 GBP |
| 20d High | 101.40 GBP |
| Drawdown from 20d High | 4.85% (within balanced profile target: 3–8%) |
| Volume Ratio (20d) | 0.8771 (healthy, <1.0) |
| Avg GBP Volume (20d) | 163.06M GBP (excellent) |

**Setup Evaluation:**
- ✅ Positive SMA50 slope → uptrend momentum
- ✅ Close > SMA50 → price above intermediate trend
- ⚠️ SMA50 < SMA200 → longer-term trend is flat/declining (partial trend only)
- ✅ Pullback magnitude (4.85%) is ideal for balanced profile
- ✅ Volume ratio <1.0 suggests a healthy, low-panic pullback
- ✅ Liquidity