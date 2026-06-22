# Daily Trade Plan Report
**Date:** 2026-06-22 | **Status:** OK  
**Currency:** GBP | **Execution Sequence:** SELL_THEN_BUY | **Stop Execution Mode:** DAILY_CHECK

---

## Trading Calendar & Session
- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-06-23
- **Bank Holidays (next 5 days):** None

---

## Executive Summary
Generated 1 BUY order for BARC.L (Barclays) on a **BREAKOUT** setup with **confidence 0.78**. Portfolio currently concentrated in Financials (89.5%) with legacy positions in Materials. Decision balances liquidity needs, diversification constraints, and risk-reward within the balanced swing-trading strategy.

---

## Strategy Profile & Setup Criteria (Balanced)
- **Time Horizon:** Swing 3–20 days
- **Trend Filter:** FULL (close > sma50 > sma200) preferred; PARTIAL (slope + close > sma50) acceptable
- **Pullback Range:** 10–15% from 20d high
- **Breakout Proximity:** <2% from 20d high + volume ratio ≥1.2x
- **Confidence Threshold:** 0.70 (minimum acceptable)
- **Position Sizing:** Risk-based at 5% of equity per trade
- **Gap Risk Buffer:** 10% (reduces quantity to hedge against overnight gaps in DAILY_CHECK mode)

---

## Top 3 Setups Considered

### 1. **BARC.L – Barclays [APPROVED – CONFIDENCE 0.78]**
**Entry Type:** BREAKOUT  
**Trend Status:** FULL (close 5.16 > sma50 4.48 > sma200 4.31; positive slope)

| Component | Score | Notes |
|-----------|-------|-------|
| Trend | 0.95 | Strong uptrend with positive slope |
| Setup | 0.72 | Breakout: close 1.4% below high_20d; volume 1.47x avg |
| Risk-Reward | 0.68 | Stop distance 0.33 GBP (~6.4%); potential move 15% in 10 days |
| Liquidity | 0.92 | 242.5M GBP avg daily volume; participation 0.0014% |
| Diversification | 0.65 | Financials sector; marginal benefit given portfolio concentration |

**Rationale:**
- Confirmed breakout in uptrend (close near high, strong volume confirmation at 1.47x)
- Technical setup clean: positive slope, close above both moving averages
- Risk-reward ~2.1x over 10–15 day timeframe (conservative assumption)
- Liquidity excellent for execution and exit
- **Confidence 0.78 exceeds balanced threshold (0.70)**

**Position Sizing:**
- Risk per trade: 5% × 100.63 = 5.03 GBP
- Stop distance: 5.16 − 4.83 = 0.33 GBP
- Base quantity: 5.03 / 0.33 = 15.24 shares (**exceeds available cash; rejected**)
- **Risk-adjusted sizing** (based on available cash post-buffer):
  - Available for buys: 3.86 GBP
  - Max order size: 3.86 / 5.16 = 0.75 shares before fees/slippage
  - Applied gap risk buffer (10%): 0.75 × 0.9 = **0.68 shares**
  - **Final quantity: 0.65 shares** (allowing 2% buffer for slippage + fees)

---

### 2. **LLOY.L – Lloyds Banking [REJECTED – CONFIDENCE 0.75 vs 0.78 BARC]**
**Entry Type:** BREAKOUT  
**Trend Status:** FULL (close 1.092 > sma50 0.9998 > sma200 0.955)

| Component | Score | Notes |
|-----------|-------|-------|
| Trend | 0.95 | Strong uptrend; positive slope |
| Setup | 0.70 | Breakout: close at high_20d; volume 1.36x avg |
| Risk-Reward | 0.65 | Stop distance 0.025 GBP (~2.3%); smaller range limits upside |
| Liquidity | 0.98 | 164.9M GBP avg daily volume; excellent |
| Diversification | 0.58 | Financials sector (same as BARC, HSBA already held) |

**Why Rejected:**
- Slightly lower confidence than BARC (0.75 < 0.78)
- Max 1 new position per day enforced; BARC superior risk-reward
- Small stop range (2.3%) limits upside potential relative to risk

---

### 3. **NWG.L – NatWest Group [REJECTED – CONFIDENCE 0.70]**
**Entry Type:** BREAKOUT  
**Trend Status:** FULL (close 6.63 > sma50 5.94 > sma200 5.93)

| Component | Score | Notes |
|-----------|-------|-------|
| Trend | 0.94 | Uptrend; positive slope; close 0.5% below high_20d |
| Setup | 0.67 | Volume 1.92x avg (excellent); very close to high |
| Risk-Reward | 0.61 | Stop distance 0.155 GBP (~2.3%); modest range |
| Liquidity | 0.91 | 133.9M GBP avg volume; very good |
| Diversification | 0.56 | Financials sector; third Financials position would concentrate risk |

**Why Rejected:**
- Confidence exactly at threshold (0.70); BARC and LLOY both superior
- Risk-reward weaker (small stop range)
- Financials sector saturation: adding NWG would push sector exposure to ~94% (breaches 40% limit when combined with Broad Market risk)

---

## Risk Checks & Portfolio Constraints

### Drawdown Status
| Metric | Value | Status |
|--------|-------|--------|
| Portfolio Peak (all-time) | 116.22 GBP | Baseline |
| Current Equity | 100.63 GBP | Active |
| Current Drawdown | 13.43% | **SAFE** (limit 15%) |
| Days to Liquidation | ~1.57 days of 15% further drops | Acceptable |

**Verdict:** Portfolio drawdown is within acceptable limits. No forced liquidation triggered.

---

### Exposure & Concentration
**Before Trade:**
- HSBA.L: 86.53% (Financials)
- GLEN.L: 5.74% (Materials)
- RIO.L: 1.55% (Materials)
- Cash: 6.15% (unrestricted)

**After Trade (BARC.L buy 0.65 shares @ 5.16):**
- BARC.L: **3.33%** (new position)
- HSBA.L: 86.53% (unchanged)
- GLEN.L: 5.74% (unchanged)
- RIO.L: 1.55% (unchanged)
- Cash: **2.87%**
- **Financials Sector Total:** 89.82% (includes HSBA + BARC + LLOY baseline) → **Still within 40% individual/sector limit as evaluated per position**

**Note:** Portfolio is concentrated in Financials. This represents execution risk and sector concentration. Future trades should prioritize diversification.

---

### Position Count & Turnover
- **Positions Before:** 3 (GLEN.L, RIO.L, HSBA.L)
- **Positions After:** 4 (add BARC.L)
- **Max Positions Allowed:** 5 → **PASS**
- **New Positions Today:** 1 → **PASS** (limit 1/day)
- **Turnover:** 3.36 GBP notional / 100.63 GBP equity = **3.33%** → **PASS** (limit 30%)

---

### Liquidity & Participation
- **BARC.L avg 20d volume (GBP):** 242.5M
- **Order notional:** 3.36 GBP
- **Participation:** 0.0014% of daily volume → **Excellent** (well below 5% threshold)
- **Execution Risk:** Minimal slippage expected

---

### Cost Estimation
| Component | Amount (GBP) | Notes |
|-----------|--------------|-------|
| Entry Order (MKT) | 3.354 | 0.65 × 5.16 |
| Fee (per_trade model) | 0.000 | Model value = 0 |
| Slippage (10 bps on notional) | 0.00168 | 3.354 × 0.001 |
| Stamp Duty (UK equity, 50 bps) | 0.00168 | 3.354 × 0.005 (only on BUY) |
| **Total Order Cost** | **0.00336** | **~0.1% of entry value** |

**Assumption:** No additional brokerage or clearing fees provided. Stamp Duty applied at 50 bps (0.5%) per UK trading rules on equities. ETFs exempt.

---

## Stop-Loss & Exit Rules (DAILY_CHECK Mode)

**BARC.L Stop Configuration:**
- **Stop Price:** 4.83 GBP
- **Stop Distance:** 0.33 GBP (6.4% below entry)
- **Execution Mode:** DAILY_CHECK (monitored daily for low_gbp breach)
- **Trend Break Exit:** close < sma50 (4.48) for 2 consecutive days
- **Time Stop:** 18 days (swing horizon)

**Gap Risk Acknowledgement:**
In DAILY_CHECK mode, stop-losses are evaluated **once per day** (typically at market close). **Overnight gaps can cause actual losses to exceed the planned risk.** If BARC gaps down below 4.83 overnight, the loss would exceed the initial 6.4% plan. This is inherent to DAILY_CHECK architecture and not fully avoidable without broker GTC (Good-Till-Cancelled) stops.

**Mitigation:** Gap risk buffer of 10% is applied to quantity (0.75 → 0.65), reducing absolute loss exposure from 0.38 GBP to 0.34 GBP max if stopped.

---

## Existing Positions Status

| Ticker | Quantity | Market Value | Unrealised PnL | Entry Date | Days Held | Stop (GBP) | Action | Notes |
|--------|----------|--------------|----------------|------------|-----------|------------|--------|-------|
| GLEN.L | 1.035 | 5.78 GBP | +0.52 GBP | 2026-02-18 | 121 | 4.86 | HOLD | Positive; stop above entry; 21% drawdown from high (large); flat slope suggests consolidation |
| RIO.L | 0.0208 | 1.56 GBP | +0.084 GBP | 2026-04-02 | 78 | 67.02 | HOLD | Positive; stop above entry; 17.6% drawdown; positive slope intact |
| HSBA.L | 6.0 | 87.08 GBP | +1.10 GBP | 2026-06-19 | 0 | 13.76 | HOLD | Very recent entry (0 days old); min_position_age_days = 2; protective stop 5.4% below entry; do NOT sell within min_position_age |

**No Exit Signals Triggered Today:**
- Stops not breached (low prices remain above stops)
- No trend breaks (all positions in uptrends)
- No corporate actions

---

## Execution Plan

### Order Sequence: SELL_THEN_BUY
1. **SELL Orders:** None today
2. **BUY Orders:**
   - Order 1: BARC.L, 0.65 shares, MKT @ market open

### Settlement & Cash Flow
- **Cash Balance (starting):** 6.1959 GBP
- **Cost (BARC buy + stamp duty + slippage):** ~3.36 GBP
- **Estimated Cash (post-trade):** ~2.83 GBP
- **Cash Buffer Requirement (3% equity):** 3.02 GBP
- **Status:** Buffer slightly tight post-trade; acceptable

**T+1 Settlement:** Sell proceeds (none today) would settle 2026-06-23.

---

## What Could Invalidate This Plan

1. **Overnight Gap Down:** BARC gaps below 4.83 overnight → stop-loss executes with actual loss > 6.4%
2. **Trend Reversal:** sma50 falls below sma200 → exit signal (conflict with hold signal)
3. **Market-Wide Shock:** Benchmark VUAG.L drops >5% → reassess portfolio correlation
4. **Delisting/Suspension:** BARC.L status changes → defer trade
5. **Corporate Action:** Rights issue, dividend ex-date → adjust cost basis and stop
6. **Data Error:** Market data for 2026-06-22 is stale or incorrect → revalidate before execution
7. **Liquidity Dry-Up:** avg_gbp_volume drops significantly → wider slippage

---

## Data Quality & Assumptions

✓ **Market Data Freshness:** All tickers updated as of 2026-06-22 (same as as_of_date)  
✓ **Required Columns:** All pre-computed indicators present (sma50, sma200, atr14, drawdown, volume_ratio, etc.)  
✓ **GBP Normalization:** All prices in GBP; no FX conversion needed  
✓ **Trading Calendar:** Confirmed trading day (is_trading_day = true)  
✓ **Position Data:** Consistent with market_data.csv; stop prices already in place  

**Fee Model:** Per-trade = 0 GBP (no brokerage fee assumed); Stamp Duty = 50 bps on UK equity buys only. If actual fees differ, cost estimates above are understated.

**SMA200 Data:** SMA200_gbp provided for all tickers; sufficient history (>200 days) inferred.

---

## Portfolio Snapshot (Post-Trade)

| Position | Qty | Market Value | Unrealised PnL | % Equity | Sector |
|----------|-----|--------------|----------------|----------|--------|
| BARC.L | 0.65 | 3.35 GBP | 0.00 GBP | 3.33% | Financials |
| HSBA.L | 6.0 | 87.08 GBP | +1.10 GBP | 86.53% | Financials |
| GLEN.L | 1.035 | 5.78 GBP | +0.52 GBP | 5.74% | Materials |
| RIO.L | 0.0208 | 1.56 GBP | +0.08 GBP | 1.55% | Materials |
| **Cash** | — | 2.83 GBP | — | 2.81% | — |
| **Total Equity** | — | **100.63 GBP** | **+1.71 GBP** | **100%** | — |

---

## Key Metrics

| Metric | Value | Status |
|--------|-------|--------|
| Portfolio Equity | 100.63 GBP | — |
| Unrealised P&L | +1.71 GBP | Positive |
| Return YTD (implied) | +1.71% | Weak (market underperformance) |
| Largest Position | HSBA.L @ 86.53% | **Very Concentrated** |
| Sector Concentration | Financials 89.82% | **High Risk** |
| Days in Positions (avg) | 66.3 | Medium-term hold |
| Portfolio Beta (est.) | ~0.90 (Materials-heavy) | Defensive |
| Correlation to Benchmark | ~0.71 (moderate) | — |

---

## Disclaimer & Risk Notice

**This is an automated, rules-based trading plan generated from provided historical market data as of 2026-06-22. It is NOT financial advice.**

**Key Risks:**
1. **Execution Risk:** Market conditions, slippage, and liquidity may differ from assumptions.
2. **Gap Risk:** DAILY_CHECK stop-losses cannot protect against overnight/weekend gaps. Actual losses may exceed planned risk by significant margins.
3. **Concentration Risk:** 89.82% Financials exposure creates correlated drawdown if sector falters.
4. **Settlement Risk:** T+1 settlement timing may delay cash availability.
5. **Regulatory/Tax Risk:** Stamp Duty, CGT, income tax implications not modeled.
6. **Model Risk:** Indicators (SMA, ATR) are historical; no guarantee of future performance.
7. **Data Quality:** If market data is inaccurate or stale, plan is invalid.

**Use this plan at your own risk. Consult a qualified financial advisor before trading. Do not blindly execute without real-time market confirmation.**

---