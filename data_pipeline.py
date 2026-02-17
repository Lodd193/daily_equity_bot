"""Data pipeline — fetch Yahoo Finance data and compute all technical indicators.

Fetches daily OHLCV for the universe, computes SMA, ATR, rolling highs/lows,
volume metrics, and drawdowns. Outputs market_data.csv with one row per ticker
containing all pre-computed fields the V2 system prompt expects.
"""

import csv
import logging
import time
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

log = logging.getLogger(__name__)


def load_universe(universe_path):
    """Load universe.csv and return list of ticker dicts."""
    tickers = []
    with open(universe_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("status", "ACTIVE") == "ACTIVE":
                tickers.append(row)
    log.info("Loaded %d active tickers from universe", len(tickers))
    return tickers


def fetch_ohlcv(tickers, period="1y"):
    """Fetch daily OHLCV from Yahoo Finance for all tickers.

    Returns dict mapping ticker -> pd.DataFrame with columns:
    Open, High, Low, Close, Volume (raw, may be GBX for LSE equities).
    """
    ticker_symbols = [t["ticker"] for t in tickers]
    log.info("Fetching OHLCV for %d tickers...", len(ticker_symbols))

    results = {}

    # Batch download
    try:
        data = yf.download(
            ticker_symbols,
            period=period,
            group_by="ticker",
            auto_adjust=True,
            progress=False,
            threads=True,
        )

        if data.empty:
            log.warning("Batch download returned empty data, trying individual")
        else:
            for sym in ticker_symbols:
                try:
                    if len(ticker_symbols) == 1:
                        df = data.copy()
                    else:
                        df = data[sym].copy()
                    df = df.dropna(subset=["Close"])
                    if not df.empty:
                        results[sym] = df
                        log.info("  %s: %d rows", sym, len(df))
                    else:
                        log.warning("  %s: no data after dropna", sym)
                except (KeyError, TypeError):
                    log.warning("  %s: not in batch result", sym)
    except Exception as e:
        log.warning("Batch download failed: %s — falling back to individual", e)

    # Individual fallback for missing tickers
    missing = [s for s in ticker_symbols if s not in results]
    for sym in missing:
        try:
            log.info("  Fetching %s individually...", sym)
            ticker = yf.Ticker(sym)
            df = ticker.history(period=period, auto_adjust=True)
            df = df.dropna(subset=["Close"])
            if not df.empty:
                results[sym] = df
                log.info("  %s: %d rows", sym, len(df))
            else:
                log.warning("  %s: no data", sym)
            time.sleep(0.5)  # Rate limit
        except Exception as e:
            log.warning("  %s: failed — %s", sym, e)

    log.info("Fetched data for %d/%d tickers", len(results), len(ticker_symbols))
    return results


def normalize_to_gbp(df, ticker_info):
    """Convert GBX (pence) to GBP if needed.

    yfinance returns prices in GBX for most LSE equities.
    Heuristic: if currency is GBp (pence), divide by 100.
    Also checks via yfinance ticker info if available.

    Returns DataFrame with _gbp suffixed price columns.
    """
    df = df.copy()

    # Try to detect currency from yfinance
    try:
        info = yf.Ticker(ticker_info["ticker"]).info
        currency = info.get("currency", "GBP")
    except Exception:
        currency = "GBP"

    divisor = 100.0 if currency == "GBp" else 1.0

    if divisor != 1.0:
        log.info("  %s: converting from GBX to GBP (÷100)", ticker_info["ticker"])

    df["close_gbp"] = df["Close"] / divisor
    df["high_gbp"] = df["High"] / divisor
    df["low_gbp"] = df["Low"] / divisor
    df["open_gbp"] = df["Open"] / divisor
    df["volume"] = df["Volume"]

    return df


def compute_indicators(df, ticker_sym):
    """Compute all V2-required indicators for a single ticker.

    Expects DataFrame with close_gbp, high_gbp, low_gbp, open_gbp, volume columns.
    Returns a dict with the latest row's indicator values, or None if insufficient data.
    """
    if len(df) < 20:
        log.warning("  %s: only %d rows, need 20+ for indicators", ticker_sym, len(df))
        return None

    df = df.copy()
    df = df.sort_index()

    # SMA50
    df["sma50_gbp"] = df["close_gbp"].rolling(window=50, min_periods=50).mean()

    # SMA200 (may be NaN if < 200 days)
    df["sma200_gbp"] = df["close_gbp"].rolling(window=200, min_periods=200).mean()

    # SMA50 slope over last 5 days
    sma50_slope = _compute_sma_slope(df["sma50_gbp"])

    # ATR14
    df["atr14_gbp"] = _compute_atr(df["high_gbp"], df["low_gbp"], df["close_gbp"], 14)

    # 20-day rolling high and low
    df["high_20d_gbp"] = df["high_gbp"].rolling(window=20, min_periods=20).max()
    df["low_20d_gbp"] = df["low_gbp"].rolling(window=20, min_periods=20).min()

    # Volume averages
    df["avg_volume_20d"] = df["volume"].rolling(window=20, min_periods=20).mean()
    df["avg_gbp_volume_20d"] = (df["close_gbp"] * df["volume"]).rolling(
        window=20, min_periods=20
    ).mean()

    # Drawdown from 20D high
    df["drawdown_from_20d_high_pct"] = (
        (df["high_20d_gbp"] - df["close_gbp"]) / df["high_20d_gbp"]
    )

    # Volume ratio
    df["volume_ratio_20d"] = df["volume"] / df["avg_volume_20d"]

    # Close vs SMA50
    df["close_vs_sma50_pct"] = (df["close_gbp"] - df["sma50_gbp"]) / df["sma50_gbp"]

    # Consecutive days below SMA50
    consecutive_below = _consecutive_days_below_sma50(df)

    # Get latest row
    latest = df.iloc[-1]

    # Check we have the minimum required fields
    if pd.isna(latest.get("sma50_gbp")) or pd.isna(latest.get("atr14_gbp")):
        if pd.isna(latest.get("close_gbp")):
            log.warning("  %s: missing close_gbp in latest row", ticker_sym)
            return None
        if pd.isna(latest.get("atr14_gbp")) and len(df) >= 14:
            log.warning("  %s: ATR14 is NaN despite %d rows", ticker_sym, len(df))

    result = {
        "date": latest.name.strftime("%Y-%m-%d") if hasattr(latest.name, "strftime") else str(latest.name),
        "ticker": ticker_sym,
        "close_gbp": _round(latest.get("close_gbp")),
        "high_gbp": _round(latest.get("high_gbp")),
        "low_gbp": _round(latest.get("low_gbp")),
        "open_gbp": _round(latest.get("open_gbp")),
        "volume": int(latest.get("volume", 0)),
        "sma50_gbp": _round(latest.get("sma50_gbp")),
        "sma200_gbp": _round(latest.get("sma200_gbp")),
        "sma50_slope": sma50_slope,
        "atr14_gbp": _round(latest.get("atr14_gbp")),
        "high_20d_gbp": _round(latest.get("high_20d_gbp")),
        "low_20d_gbp": _round(latest.get("low_20d_gbp")),
        "avg_volume_20d": _round(latest.get("avg_volume_20d")),
        "avg_gbp_volume_20d": _round(latest.get("avg_gbp_volume_20d")),
        "drawdown_from_20d_high_pct": _round(latest.get("drawdown_from_20d_high_pct"), 6),
        "volume_ratio_20d": _round(latest.get("volume_ratio_20d"), 4),
        "close_vs_sma50_pct": _round(latest.get("close_vs_sma50_pct"), 6),
        "consecutive_days_below_sma50": consecutive_below,
    }

    return result


def _compute_atr(high, low, close, period=14):
    """Compute Average True Range."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return true_range.rolling(window=period, min_periods=period).mean()


def _compute_sma_slope(sma_series, lookback=5):
    """Determine SMA slope direction over last N days.

    Returns 'positive', 'negative', or 'flat'.
    """
    recent = sma_series.dropna().tail(lookback)
    if len(recent) < 2:
        return "flat"

    first = recent.iloc[0]
    last = recent.iloc[-1]

    if first == 0:
        return "flat"

    change_pct = (last - first) / first
    if change_pct > 0.001:
        return "positive"
    elif change_pct < -0.001:
        return "negative"
    return "flat"


def _consecutive_days_below_sma50(df):
    """Count consecutive most-recent days where close < SMA50."""
    if "sma50_gbp" not in df.columns:
        return 0

    below = df["close_gbp"] < df["sma50_gbp"]
    below = below.dropna()

    if below.empty or not below.iloc[-1]:
        return 0

    count = 0
    for val in reversed(below.values):
        if val:
            count += 1
        else:
            break
    return count


def _round(value, decimals=4):
    """Round a value, returning None for NaN."""
    if pd.isna(value):
        return None
    return round(float(value), decimals)


def build_market_data(universe_path, output_path):
    """Main entry point. Fetch data, compute indicators, write market_data.csv.

    Returns True if at least one ticker has valid data.
    """
    universe = load_universe(universe_path)
    raw_data = fetch_ohlcv(universe)

    if not raw_data:
        log.error("No data fetched for any ticker")
        return False

    # Build universe lookup by ticker symbol
    universe_lookup = {t["ticker"]: t for t in universe}

    rows = []
    for ticker_info in universe:
        sym = ticker_info["ticker"]
        if sym not in raw_data:
            log.warning("  %s: skipped (no data)", sym)
            continue

        df = raw_data[sym]

        # Normalize to GBP
        df = normalize_to_gbp(df, ticker_info)

        # Compute indicators
        indicators = compute_indicators(df, sym)
        if indicators is None:
            log.warning("  %s: skipped (insufficient data for indicators)", sym)
            continue

        # Add universe metadata
        indicators["sector"] = ticker_info.get("sector", "")
        indicators["instrument_type"] = ticker_info.get("instrument_type", "EQUITY")
        indicators["uk_equity_flag"] = ticker_info.get("uk_equity_flag", "true")

        rows.append(indicators)

    if not rows:
        log.error("No tickers produced valid indicator data")
        return False

    # Write CSV
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "date", "ticker", "close_gbp", "high_gbp", "low_gbp", "open_gbp", "volume",
        "sma50_gbp", "sma200_gbp", "sma50_slope", "atr14_gbp",
        "high_20d_gbp", "low_20d_gbp",
        "avg_volume_20d", "avg_gbp_volume_20d",
        "drawdown_from_20d_high_pct", "volume_ratio_20d", "close_vs_sma50_pct",
        "consecutive_days_below_sma50",
        "sector", "instrument_type", "uk_equity_flag",
    ]

    with open(output, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    log.info("Wrote market_data.csv: %d tickers", len(rows))
    return True


def load_market_data(csv_path):
    """Load market_data.csv into a dict keyed by ticker.

    Returns dict of ticker -> row dict.
    """
    result = {}
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields
            for key in row:
                if key in ("ticker", "date", "sma50_slope", "sector",
                           "instrument_type", "uk_equity_flag"):
                    continue
                try:
                    if row[key] == "" or row[key] is None:
                        row[key] = None
                    else:
                        row[key] = float(row[key])
                except (ValueError, TypeError):
                    pass
            result[row["ticker"]] = row
    return result
