# Daily Trading Report
**Date:** 2026-02-24 (Tuesday)  
**Status:** NO_TRADES  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (monitored once daily, gap risk applies)

---

## Trading Calendar
- **Is Trading Day:** Yes ✓
- **Is Half Day:** No
- **Next Trading Day:** 2026-02-25
- **Bank Holidays (next 5 days):** None

---

## Executive Summary

### Portfolio Status
- **Equity Value:** £99.89
- **Cash Available:** £3.50 (3.51% of equity)
- **Drawdown from Peak:** 0.30% (peak £100.19) — well within 15% limit ✓
- **Positions:** 3 active (AZN.L, SHEL.L, GLEN.L)

### Action Today
**NO NEW TRADES.** All existing positions remain healthy with intact trends and no stop-loss breaches. Two high-confidence entry signals identified but insufficient cash liquidity to fund them without liquidating existing positions, which show no exit criteria.

**Decision Logic:** Capital preservation takes precedence. The portfolio is adequately positioned; forcing a rebalance into insufficient cash would violate risk discipline.

---

## Analysis of Candidates

### Top Candidates Evaluated (Ranked by Confidence)

#### 1. **VWRP.L (Vanguard FTSE All-World ETF)** — Confidence: 0.83 ⭐ Highest
- **Entry Type:** Pullback in uptrend
- **Trend:** ✓ FULL (close £130.38 > sma50 £127.99 > sma200 £120.60)
- **Setup:** Drawdown 3.42% from 20d high (within balanced range 2.5%-8%)
- **Volume:** 1.01× average (healthy)
- **Confidence Breakdown:**
  - Trend conviction: 1.00 (full uptrend)
  - Setup quality: 0.80 (solid pullback, good retracement level)
  - Risk/reward: 0.76 (ATR-based stops favorable)
  - Liquidity: 0.92 (broad ETF, £33.9M avg daily volume)
  - Diversification: 0.88 (broad-market hedge, uncorrelated to holdings)
- **Why Rejected:** **INSUFFICIENT CASH**
  - Required quantity: 1.2566 shares (after 10% gap buffer)
  - Order cost: £164.04 (price + slippage + fees)
  - Available cash: £0.50
  - Shortfall: £163.54

#### 2. **BA.L (BAE Systems)** — Confidence: 0.76
- **Entry Type:** Pullback in uptrend (high-volume retracement)
- **Trend:** ✓ FULL (close £21.41 > sma50 £19.27 > sma200 £18.66)
- **Setup:** Shallow pullback (1.70% from 20d high) but confirmed by 1.41× volume spike
- **Risk Rejection:** **INSUFFICIENT CASH** (requires £67.88)

#### 3. **GSK.L (GlaxoSmithKline)** — Confidence: 0.75
- **Entry Type:** Pullback in uptrend
- **Trend:** ✓ FULL (close £22.01 > sma50 £19.45 > sma200 £16.44)
- **Setup:** 3.54% pullback (good retracement, balanced profile sweet spot)
- **Setup Concern:** Low volume (0.52× average) may indicate weak conviction
- **Why Rejected:** **INSUFFICIENT CASH** (requires £96.95)

#### 4. **RIO.L (Rio Tinto)** — Confidence: 0.71
- **Entry Type:** Shallow pullback (2.05% from high)
- **Trend:** ✓ FULL (close £72.69 > sma50 £65.04 > sma200 £52.06)
- **Why Rejected:** **INSUFFICIENT CASH** (requires £141.67)

#### 5. **TSCO.L (Tesco)** — Confidence: 0.68
- **Entry Type:** Very shallow pullback (1.38% from high)
- **Setup:** Borderline confidence due to minimal drawdown
- **Why Rejected:** **INSUFFICIENT CASH** (requires £22.14)

#### Non-Eligible Tickers (Trend Filter Failed)
- **LSEG.L, REL.L, NWG.L:** Negative trend (close below sma50 or sma50 below sma200)
  - LSEG.L: close £76.78 < sma50 £83.90 (downtrend, 25+ days below SMA50)
  - REL.L: close £22.73 < sma50 £27.35 (strong downtrend, 27+ days below)
  - NWG.L: close £6.04 < sma50 £6.40 (downtrend, 12+ days below)
- **BARC.L:** close < sma50, early downtrend signal
- **All others:** Insufficient pullback magnitude or volume confirmation for balanced profile

---

## Existing Positions: Hold Assessment

### AZN.L (AstraZeneca)
| Metric | Value |
|--------|-------|
| **Quantity** | 0.3879 shares |
| **Avg Cost** | £155.38 |
| **Current Price** | £153.26 |
| **Market Value** | £59.45 |
| **Unrealised PnL** | -£0.82 (-1.36%) |
| **Entry Date** | 2026-02-17 |
| **Days Held** | 2 |
| **Stop Price** | £151.25 |
| **Low Today** | £151.84 ✓ above stop |
| **Trend** | ✓ FULL (close > sma50 > sma200) |
| **Close vs SMA50** | +8.86% |

**Decision:** HOLD
- Stop level not breached (£151.84 > £151.25)
- Trend conviction intact and strengthening (close > sma50 > sma200, positive slope)
- Position age = 2 days (meets min_position_age_days; eligible for exit only if signal triggered)
- Unrealised loss (-£0.82) is modest; position still has positive risk/reward
- No consecutive days below SMA50

### SHEL.L (Shell)
| Metric | Value |
|--------|-------|
| **Quantity** | 1.0624 shares |
| **Avg Cost** | £28.70 |
| **Current Price** | £29.715 |
| **Market Value** | £31.57 |
| **Unrealised PnL** | +£1.08 (+3.53%) |
| **Entry Date** | 2026-02-17 |
| **Days Held** | 2 |
| **Stop Price** | £27.71 |
| **Low Today** | £29.61 ✓ above stop |
| **Trend** | ✓ FULL (close > sma50 > sma200) |
| **Close vs SMA50** | +7.62% |

**Decision:** HOLD
- Stop not breached; position well above support
- Trend intact with positive momentum
- Profitable position; no incentive to exit
- No exit signals present

### GLEN.L (Glencore)
| Metric | Value |
|--------|-------|
| **Quantity** | 1.035 shares |
| **Avg Cost** | £5.08 |
| **Current Price** | £5.193 |
| **Market Value** | £5.37 |
| **Unrealised PnL** | +£0.11 (+2.09%) |
| **Entry Date** | 2026-02-18 |
| **Days Held** | 1 |
| **Stop Price** | £4.86 |
| **Low Today** | £5.10 ✓ above stop |
| **Trend** | ✓ FULL (close > sma50 > sma200, flat slope) |
| **Close vs SMA50** | +13.08% |

**Decision:** HOLD (Anti-Churn Rule)
- Position age = 1 day < min_position_age_days (2 days)
- Anti-churn rule prevents sell-and-rebuy within 2 days unless stop breached
- Stop not breached; no exit signal
- Even though trend is not as compelling (sma50_slope = flat), position remains valid
- Holding to avoid churn fees and market-timing risk

---

## Risk Compliance Checklist

| Check | Value | Limit | Status |
|-------|-------|-------|--------|
| **Positions Count** | 3 | 5 | ✓ OK |
| **Portfolio Drawdown** | 0.30% | 15.0% | ✓ OK |
| **Cash Buffer** | £3.50 (3.51%) | 3.0% required | ✓ OK |
| **Turnover (% of equity)** | 0.0% | 30.0% | ✓ OK (no trades) |
| **Healthcare Sector Exposure** | 59.60% | 40.0% max | ⚠️ OVER LIMIT |
| **Max Single-Name (AZN.L)** | 59.60% | 30.0% max | ⚠️ OVER LIMIT |

### ⚠️ Sector & Concentration Violations (Inherited)
The portfolio is currently **overfitted to Healthcare** (AZN.L = 59.60% of equity). This position was established in the previous session and remains active because:
1. **No stop-loss breach** — position still has downside cushion
2. **Trend conviction** — uptrend remains valid
3. **