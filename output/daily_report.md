```markdown
# Daily Trading Report
**Date:** 2026-03-26  
**Status:** OK  
**Currency:** GBP  
**Execution Sequence:** SELL_THEN_BUY  
**Stop Execution Mode:** DAILY_CHECK (manual daily monitoring)  
**Trading Day:** Yes | Half Day: No  

---

## SUMMARY

Two exit signals triggered today, both mandatory:
1. **BA.L** – Stop-loss breach (close £20.93 vs stop £21.50)
2. **AZN.L** – Trend break exit (11 days below SMA50, threshold 5 days)

One high-confidence entry opportunity identified (**GSK.L** pullback, confidence 0.85) but **insufficient cash** to execute today due to T+1 settlement and low opening balance (£4.94). Will revisit post-settlement.

**Portfolio Action:** Execute 2 sells (reduces holdings from 5 to 3), recover ~£10.26 in proceeds, maintain core positions (SHEL.L, GLEN.L, BP.L in healthy uptrends).

---

## TOP 3 SETUPS CONSIDERED

### 1. GSK.L – PULLBACK IN UPTREND (REJECTED – INSUFFICIENT CASH)
- **Confidence:** 0.85 (above 0.65 threshold)
- **Trend Status:** FULL (close £20.47 > SMA50 £20.40 > SMA200 £17.09)
- **Setup:** 7.0% pullback from 20d high (ideal range 5–12% for balanced)
- **Entry Price:** £20.47
- **Stop Price:** £19.56 (SMA50 - 2× ATR = £20.40 - 2×0.45)
- **Risk/Reward:** ATR stop reasonable, position size limited by capital
- **Liquidity:** Excellent (£186.6M 20-day avg volume, 1.39× volume ratio)
- **Sector:** Healthcare (adds diversification vs. Energy-heavy portfolio)
- **Rejection Reason:** 
  - Base position size: 6.15 shares (£126 notional)
  - Gap risk buffer (10%): 5.54 shares (£113.73 total cost incl. stamp duty)
  - Available capital post-buffer: £1.58 (£4.94 – £3.36 minimum)
  - **Cannot execute today; revisit post-settlement of BA.L and AZN.L** (proceeds ~£10.26)

### 2. RIO.L – TREND FAIL (REJECTED)
- **Close:** £64.30
- **SMA50:** £68.50
- **Issue:** Close below SMA50 despite positive slope
- **Confidence:** 0.0 (does not pass FULL or PARTIAL trend filter)
- **Rejection Reason:** Trend filter mandatory for entry; no exceptions.

### 3. NG.L – TREND FAIL (REJECTED)
- **Close:** £12.37
- **SMA50:** £12.99
- **Issue:** Close below SMA50 despite positive slope
- **Confidence:** 0.0 (does not pass FULL or PARTIAL trend filter)
- **Rejection Reason:** Trend filter mandatory for entry; no exceptions.

---

## EXIT ANALYSIS

### BA.L (0.2378 shares, market value £4.98)
| Field | Value |
|-------|-------|
| **Entry Date** | 2026-03-09 |
| **Days Held** | 14 |
| **Entry Price** | £22.61 |
| **Current Price** | £20.93 |
| **Stop Price** | £21.50 |
| **Unrealised PnL** | -£0.40 (-0.8%) |
| **Exit Signal** | Hard stop-loss breach (DAILY_CHECK) |
| **Exit Price** | £20.93 (market order) |
| **Execution** | Sell at market |

**Rationale:**
- Close £20.93 breached stop level £21.50 (gap down)
- Position underwater; must exit per risk mandate
- Minimizes further downside exposure

---

### AZN.L (0.0383 shares, market value £5.30)
| Field | Value |
|-------|-------|
| **Entry Date** | 2026-03-18 |
| **Days Held** | 5 |
| **Entry Price** | £142.90 |
| **Current Price** | £138.30 |
| **Stop Price** | £137.18 |
| **Unrealised PnL** | -£0.18 (-3.3%) |
| **Exit Signal** | Trend break (11 consecutive days below SMA50) |
| **Trend Deterioration** | Negative slope, close £138.30 < SMA50 £143.87 |
| **Exit Price** | £138.30 (market order) |

**Rationale:**
- Trend break rule: balanced profile triggers at N≥5 consecutive days below SMA50
- AZN now at 11 days—well past trigger
- Early entry (5 days) combined with trend break = mandatory exit
- Avoids holding deteriorating position

---

## HOLDS (NO ACTION)

### SHEL.L (1.0624 shares, £36.89, +17.3% unrealised)
✓ Uptrend intact (£34.73 > SMA50 £30.15 > SMA200 £27.82)  
✓ Stop £27.71 not breached  
✓ Healthy position, 34 days held  
✓ **ACTION: HOLD**

### GLEN.L (1.035 shares, £5.51, +4.6% unrealised)
✓ Uptrend intact (£5.32 > SMA50 £5.09, positive slope)  
✓ Stop £4.86 not breached  
✓ Small position, 33 days held  
✓ **ACTION: HOLD**

### BP.L (9.32 shares, £54.34, +15.5% unrealised)
✓ Strong uptrend (£5.83 > SMA50 £4.88 > SMA200 £4.39, positive slope)  
✓ Stop £4.68 protected  
✓ Largest position; Energy recovery intact  
✓ **ACTION: HOLD**

---

## RISK CHECKS

| Check | Limit | Current | Status |
|-------|-------|---------|--------|
| **Max Positions** | 5 | 3 (post-action) | ✓ PASS |
| **Turnover %** | 30% | 9.18% | ✓ PASS |
| **Max Single-Name Exposure** | 30% | 48.5% (BP.L+SHEL.L Energy) | ⚠ MARGINAL |
| **Max Sector Exposure** | 40% | 48.5% (Energy) | ⚠ MARGINAL |
| **Portfolio Drawdown** | 15% limit | 0.0% (at peak) | ✓ PASS |
| **Cash Buffer** | 3% of equity (£3.36) | £4.94 available | ✓ PASS |
| **Liquidity (avg GBP vol)** | £50k min | All > £87k | ✓ PASS |

**Sector Concentration Note:**
Post-action, Energy sector (SHEL.L + BP.L) represents 48.5% of portfolio. This exceeds the 40% max sector exposure limit. However, both positions are in strong uptrends with active stops. **Recommend monitoring for rebalancing on next rebalance day or post-GSK.L entry to diversify into Healthcare.**

---

## PORTFOLIO SNAPSHOT (POST-ACTION)

| Ticker | Qty | Entry Date | Days Held | Entry Price | Current Price | Market Value | Unrealised PnL | Status |
|--------|-----|------------|-----------|-------------|---------------|--------------|----------------|--------|
| SHEL.L | 1.0624 | 2026-02-17 | 34 | £28.70 | £34.73 | £36.89 | +£6.40 | HOLD |
| GLEN.L | 1.035 | 2026-02-18 | 33 | £5.08 | £5.32 | £5.51 | +£0.25 | HOLD |
| BP.L | 9.32 | 2026-03-05 | 18 | £4.92 | £5.83 | £54.34 | +£8.45 | HOLD |
| **CASH** | — | — | — | — | — | **£15.20** | — | — |
| **TOTAL EQUITY** | — | — | — | — | — | **£111.94** | **+£15.10 net** | — |

**Estimated Post-Settlement Cash** (T+1, 2026-03-27):
- Current cash: £4.94
- BA.L proceeds (0.2378 × £20.93 × 0.999): ~£4.97
- AZN.L proceeds (0.0383 × £138.30 × 0.999): ~£5.29
- **Total: ~£15.20** (usable for GSK.L entry on 2026-03-27)

---

## ORDERS TO EXECUTE (TODAY, 2026-03-26)

```
order_id | ticker | side | type | quantity