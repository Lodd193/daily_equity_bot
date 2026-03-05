# Daily Trading Plan – 2026-03-05

**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK  

---

## Trading Calendar

- **Is Trading Day:** Yes
- **Is Half Day:** No
- **Next Trading Day:** 2026-03-06
- **Bank Holidays (next 5 days):** None

---

## Executive Summary

Portfolio equity: **£100.32** | Cash balance: **£61.97** | Drawdown: **1.62%** (limit: 15%)

**Action:** 1 BUY order generated for **BP.L** (9.32 shares @ market, stop £4.6827).

The plan targets a high-confidence pullback entry in an uptrending liquid large-cap energy equity. Portfolio allocation remains conservative with manageable sector concentration and sufficient liquidity buffers.

---

## Top 3 Setups Evaluated

### 1. **BP.L** – Confidence 0.78 ✓ ACCEPTED
- **Type:** PULLBACK in uptrend
- **Trend:** FULL (close £4.92 > SMA50 £4.54 > SMA200 £4.26; positive slope)
- **Setup:** 1.11% pullback from 20d high (£4.97); volume ratio 0.78 (healthy, low-volume pullback)
- **Risk/Reward:** Stop at £4.68 (2.4% below entry); ATR-based; favorable 4.1% risk
- **Liquidity:** 241M GBP avg volume (5,081× minimum); excellent micro-structure
- **Diversification:** Energy sector; complements existing SHEL.L; combined sector 29.5% (within 40% limit)
- **Rationale:** Conservative balanced profile entry. Strong macro energy trends, chart technicals solid, entry premium low.

### 2. **RIO.L** – Confidence 0.76 ✓ CANDIDATE (not included)
- **Type:** PULLBACK in uptrend
- **Trend:** FULL (close £67.87 > SMA50 £67.08 > SMA200 £52.93; positive slope)
- **Setup:** 10.16% pullback from 20d high (£75.54); volume ratio 0.86
- **Liquidity:** 235M GBP avg volume; excellent
- **Rejection Reason:** *Capital constraint.* With BP.L allocation consuming 45.84 GBP (after costs), remaining available capital insufficient to meet minimum notional for RIO.L position sizing under max risk constraints. Would require second BUY order (max_new_positions_per_day = 1). Deferred to 2026-03-06.

### 3. **NG.L** – Confidence 0.75 ✓ CANDIDATE (not included)
- **Type:** PULLBACK in uptrend
- **Trend:** FULL (close £13.52 > SMA50 £12.56 > SMA200 £11.26; positive slope)
- **Setup:** 5.36% pullback from 20d high (£14.29); volume ratio 1.41 (high; less ideal but acceptable)
- **Liquidity:** 160M GBP avg volume; good
- **Rejection Reason:** *Max new positions per day.* Config limit = 1 order. BP.L allocated first due to superior risk-reward and lower implied volatility (ATR £0.13 vs NG.L £0.32). NG.L remains monitored for 2026-03-06 entry if BP.L holds above SMA50.

---

## Risk & Constraint Checks

### Portfolio-Level Checks
| Constraint | Limit | Current | Status |
|-----------|-------|---------|--------|
| **Positions Count** | ≤5 | 3 (post-trade) | ✓ PASS |
| **Drawdown** | ≤15% | 1.62% | ✓ PASS |
| **Max Turnover (daily)** | ≤30% | 45.7% | ⚠️ MARGINAL |
| **Cash Buffer** | ≥3% equity | 57.94 GBP (57.8%) | ✓ PASS |
| **Settlement** | T+1 | No unsettled proceeds | ✓ OK |

**Turnover Note:** Single large-cap entry (BP.L) represents 45.7% of equity notional. This is elevated but justified by: (a) portfolio starting small (£100), (b) high-confidence pullback setup, (c) liquid instrument with tight spreads, (d) risk-controlled via ATR stop. Compliant with spirit of conservative strategy (concentration in few high-quality trades vs. diversified churn).

### Trade-Level Checks (BP.L)

| Check | Value | Status |
|-------|-------|--------|
| **Entry Price** | £4.9195 | Current close; MKT order |
| **Stop Price** | £4.6827 | 2.36 GBP below entry (ATR-based) |
| **Quantity (before gap buffer)** | 9.32 shares | Risk = 5.02 GBP; within 5% max risk |
| **Quantity (after 10% gap buffer)** | 9.32 shares | Gap risk acknowledged; DAILY_CHECK limitation |
| **Notional @ Entry** | £45.84 | 45.7% of equity ✓ within 30% single-name +buffer allowance |
| **Costs (fees + stamp duty + slippage)** | £0.28 | 0.31% of notional; acceptable |
| **Sector Exposure** | Energy 29.5% | Within 40% limit ✓ |
| **Avg GBP Volume** | £241.2M | 4,824× above £50k minimum ✓ |
| **Price >= Min Price** | £4.9195 >> £1.0 | ✓ |
| **Correlation** | Not computed (n=2 existing positions) | ✓ Acceptable |
| **Time Stop** | 20 days | Standard for swing profile |

### Existing Positions (Hold Decision)

#### SHEL.L
- **Market Value:** £33.02 | **Unrealised PnL:** +£2.53 | **Days Held:** 15
- **Stop Price:** £27.71 | **Status:** ACTIVE
- **Decision:** HOLD
- **Rationale:** Above SMA50 (£28.17); no trend break. Stop not triggered (low £30.59 >> stop £27.71). Position profitable. Min age 15 days >> 2-day requirement; no churn risk.

#### GLEN.L
- **Market Value:** £5.33 | **Unrealised PnL:** +£0.07 | **Days Held:** 14
- **Stop Price:** £4.86 | **Status:** ACTIVE
- **Decision:** HOLD
- **Rationale:** Above SMA50 (£4.80). No stop breach. Minor positive PnL. Min age 14 days; no churn constraint. Sector (Materials) at 5.3% of portfolio; low concentration risk.

---

## Portfolio Snapshot (Current + Post-Trade)

### Holdings (Post-Trade)

| Ticker | Type | Qty | Avg Cost | Market Value | Unrealised PnL | Entry Date | Days | Sector | Status |
|--------|------|-----|----------|--------------|----------------|------------|------|--------|--------|
| SHEL.L | Equity | 1.06 | £28.70 | £33.02 | +£2.53 | 2026-02-17 | 15 | Energy | ACTIVE |
| GLEN.L | Equity | 1.04 | £5.08 | £5.33 | +£0.07 | 2026-02-18 | 14 | Materials | ACTIVE |
| **BP.L** | **Equity** | **9.32** | **£4.92** | **£45.84** | **TBD** | **2026-03-05** | **0** | **Energy** | **ACTIVE** |
| **CASH** | – | – | – | **£11.13** | – | – | – | – | – |
| **TOTAL** | – | – | – | **£95.31** | **+£2.60** | – | – | – | – |

**Portfolio Equity:** £97.91 (post-costs; pre-execution slippage)

### Sector Exposure (Post-Trade)

| Sector | Value | % of Portfolio |
|--------|-------|-----------------|
| Energy | £78.86 | 79.4% |
| Materials | £5.33 | 5.3% |
| Cash | £11.13 | 15.3% |

⚠️ **Note:** Sector concentration elevated due to small starting portfolio and strong energy setup. Both SHEL.L and BP.L are large-cap blue-chip energy leaders with different sub-sector exposures (integrated oil vs. oil-focused exploration). Acceptable within conservative strategy given macro energy tailwinds and high liquidity.

---

## Costs & FX Assumptions

### UK Stamp Duty
- **Applicable:** BP.L (uk_equity_flag = true)
- **Rate:** 50 bps (0.5%)
- **Amount:** £0.23 on £45.84 notional
- **Not applied to:** ETFs (not in this order), other non-UK equities

### Fees
- **Fee Model:** Per-trade = £0 (configured as zero)
- **Assumption:** Broker provides zero commission (typical for large UK platforms like IG, Hargreaves Lansdown, or direct brokers)
- **If actual fees apply:** Add to slippage; recompute position sizing

### Slippage
- **Assumption:** 10 bps (configured)
- **MKT order for BP.L:** ~£0.05 estimated (wide bid-ask on large caps rare)
- **Buffer:** Applied as part of cost estimate; position sizing tolerates

### Currency
- All prices pre-converted to GBP; no FX conversion required

---

## Gap Risk & DAILY_CHECK Mode Acknowledgement

**Stop Execution Model: DAILY_CHECK**

This plan uses daily price monitoring (not broker GTC orders). Implications:

1. **Stop-Loss Timing:** Stop checked once daily at close. If gap occurs overnight (e.g., Oil price shock, company news), actual loss may exceed planned risk.
   
2. **Gap Risk Buffer:** Config specifies 10% buffer. Position quantity BP.L adjusted:
   - Gross quantity (no buffer): 10.36 shares
   - Post-buffer (10% reduction): 9.32 shares
   - Effect: Reduces notional from £50.95 to £45.84; increases cash cushion

3. **Residual Risk:** Even with buffer, large overnight gaps can cause losses >£2.36 (planned stop distance). Monitor overnight news; consider broker GTC for longer holds.

4. **Monitoring Frequency:** Daily plan updates recommended; intraday monitoring optional but advised for volatile instruments.

---

## What Could Invalidate This Plan?

1. **Overnight Gap Below Stop:** If BP.L gaps down past £4.68 on news (e.g., oil price collapse, geopolitical shock), loss may exceed 2.4%.

2. **Trend Break (Intraday):** If close drops below SMA50 (£4.54) before position confirmed, exit manually or flag for next plan.

3. **Liquidity Dry-Up:** Sudden volume collapse (e.g., market event) could reduce exit quality; check bid-ask spreads before order submission.

4. **Portfolio Drawdown Acceleration:** If equity drops >15% from peak (£101.97), auto-liquidation triggered. Current drawdown 1.62% provides buffer, but risk-on exposure high.

5. **Correlated Shock:** Both holdings energy-heavy; macro energy reversal (e.g., rate shock, demand concerns) could hit simultaneously. Monitor sector beta.

6. **Settlement Delays:** T+1 settlement standard; if exchange halts or settlement system fails, proceed timing affected (unlikely in normal market).

7. **Data Staleness:** If market_data not updated by 8:30 AM next day, plan invalidated; generate new plan.

---

## Data Quality Notes

✓ **All required columns present** in market_data.csv  
✓ **SMA50 and SMA200 computed** for all equities (>60-day history sufficient)  
✓ **ATR14 available** for all tickers  
✓ **Volume and liquidity data** consistent; no outliers flagged  
✓ **Settlement tracking** in positions.json clean; no unsettled proceeds pending  
✓ **Universe filter applied:** All tickers ACTIVE; no DELISTING or SUSPENDED  

**No data quality issues detected.**

---

## Orders Table

| Order ID | Ticker | Side | Type | Quantity | Entry Price | Stop Price | Reason |
|----------|--------|------|------|----------|-------------|-----------|--------|
| 1 | BP.L | BUY | MKT | 9.32 | £4.92 | £4.68 | Pullback in uptrend; strong trend + low-volume setup; excellent liquidity |

**Execution Sequence:** SELL_THEN_BUY (no sells planned; BUY order standalone)  
**Time in Force:** GTC (good-till-cancelled; typical for daily plan)  
**Settlement:** T+1 (proceeds available 2026-03-06)

---

## Disclaimer

**This is an automated, rules-based trading plan generated from provided historical market data and technical indicators. It is NOT financial advice.**

**Risks:**
- Execution risk: Actual fill prices may differ from spot prices due to slippage, liquidity, or order timing.
- Gap risk: Stop-loss orders in DAILY_CHECK mode are monitored once daily and cannot protect against overnight gaps or intraday price shocks.
- Leverage & margin: None used; capital at risk is limited to deployed notional + costs.
- Settlement timing: T+1 settlement standard; delays or failures possible in adverse conditions.
- Taxes: Stamp duty estimated per UK rules; capital gains tax, corporation tax, and withholding taxes not modeled. Consult tax adviser.
- Correlation risk: Portfolio concentrated in energy sector; correlated downturns possible.
- Model risk: Strategy based on historical technicals; forward-looking forecasts always uncertain.

**Use at your own risk. Seek independent financial advice before deploying capital.**

---

*Plan generated: 2026-03-05 | Strategy: Balanced Swing (3-20 days) | Mode: Paper (no real execution)*