```markdown
# Daily Trade Plan – 2026-03-06

**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  
**Strategy Profile:** Balanced  

---

## Trading Calendar
- **Trading Day:** Yes  
- **Half Day:** No  
- **LSE Open:** Normal hours  

---

## Executive Summary

No trades executed today. Portfolio is significantly **cash-constrained**, preventing entry into high-quality swing opportunities identified by the strategy.

**Key Metric:** Only 12.82 GBP available for buys (after 3% cash buffer), while all identified high-confidence entry candidates require 65–127 GBP notional.

---

## Opportunity Analysis

### Top 3 Setups Considered

#### 1. **RIO.L (Rio Tinto)** – Confidence: 0.87 ⭐
- **Setup:** Pullback in full uptrend  
- **Entry Price:** 67.49 GBP  
- **Stop:** 62.77 GBP (1.5× ATR below entry)  
- **Risk/Reward:** ~1:1.8  
- **Pullback Depth:** 10.7% from 20d high (within 5–15% balanced zone)  
- **Volume Signal:** vol_ratio = 0.75 (healthy pullback, not panic selling)  
- **Liquidity:** 230M GBP avg 20d volume ✓  
- **Trend Confirmation:** close (67.49) > sma50 (67.23) > sma200 (53.04) ✓  
- **Rejection:** **Cash constraint** – requires 65.23 GBP total (notional 64.84 + stamp duty 0.32 + slippage 0.07), available only 12.82 GBP.

#### 2. **AZN.L (AstraZeneca)** – Confidence: 0.85
- **Setup:** Pullback in full uptrend  
- **Entry Price:** 145.0 GBP  
- **Stop:** 139.75 GBP (1.5× ATR below entry)  
- **Risk/Reward:** ~1:2.2  
- **Pullback Depth:** 7.8% from 20d high (solid, within zone)  
- **Volume Signal:** vol_ratio = 0.52 (very healthy pullback)  
- **Liquidity:** 508M GBP avg 20d volume ✓  
- **Trend:** close > sma50 > sma200 ✓  
- **Rejection:** **Cash constraint** – requires 127.15 GBP total, available only 12.82 GBP.

#### 3. **GSK.L (GlaxoSmithKline)** – Confidence: 0.82
- **Setup:** Pullback in full uptrend  
- **Entry Price:** 20.38 GBP  
- **Pullback Depth:** 10.7%  
- **Liquidity:** 240M GBP avg 20d volume ✓  
- **Rejection:** **Cash constraint + sector concentration** – healthcare overlap with AZN; lower confidence.

---

## Current Portfolio Status

### Positions (as of 2026-03-06)

| Ticker | Qty | Entry Date | Days Held | Entry Price | Current Price | Market Value | P&L | Stop | Status |
|--------|-----|----------|-----------|-----------|--------------|-------------|-------|------|--------|
| **SHEL.L** | 1.0624 | 2026-02-17 | 16 | 28.70 | 31.33 | 33.29 | +2.80 | 27.71 | ACTIVE ✓ |
| **GLEN.L** | 1.0350 | 2026-02-18 | 15 | 5.08 | 5.028 | 5.20 | −0.06 | 4.86 | ACTIVE ✓ |
| **BP.L** | 9.3200 | 2026-03-05 | 0 | 4.92 | 4.989 | 46.50 | +0.60 | 4.68 | ACTIVE ✓ |

### Portfolio Metrics

| Metric | Value |
|--------|-------|
| **Total Equity** | 100.83 GBP |
| **Cash Balance** | 15.84 GBP |
| **Peak Equity** | 101.97 GBP |
| **Current Drawdown** | 1.12% |
| **Required Buffer (3%)** | 3.03 GBP |
| **Available for Buys** | 12.82 GBP |
| **Number of Positions** | 3 |
| **Max Allowed Positions** | 5 |
| **Max New Positions/Day** | 1 |
| **Sector Concentration** | Energy: 79.1%, Materials: 5.2% |

---

## Exit Monitoring

### Stop-Loss Check (DAILY_CHECK Mode)

All positions remain **above their stop prices.** No stop-loss exits triggered.

| Ticker | Close | Low | Stop | Status |
|--------|-------|-----|------|--------|
| SHEL.L | 31.33 | 30.96 | 27.71 | Safe (low > stop by 3.25) |
| GLEN.L | 5.028 | 4.8692 | 4.8573 | Safe (low > stop by 0.0119) |
| BP.L | 4.989 | 4.907 | 4.6827 | Safe (low > stop by 0.224) |

### Trend Break Check

All positions remain in **positive uptrends:**
- SHEL.L: close > sma50 ✓, sma50 > sma200 ✓
- GLEN.L: close > sma50 ✓, sma50 > sma200 ✓
- BP.L: close > sma50 ✓, sma50 > sma200 ✓

No trend-based exits.

### Anti-Churn Compliance

- SHEL.L: 16 days held ✓ (> 2 days min)
- GLEN.L: 15 days held ✓
- BP.L: 0 days held (entered yesterday) – cannot exit for non-stop reasons until day 2

---

## Risk & Constraint Analysis

### ✓ Data Integrity
- Market data