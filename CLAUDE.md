# Daily Equity Trader

## Overview

An LLM-powered daily equity trading bot for UK FTSE 100 blue chips.
Paper trading mode with £100 starting capital. Runs daily via GitHub Actions after LSE close.

## Architecture

Python pipeline computes all technical indicators from Yahoo Finance data.
Claude API (Haiku) acts as the decision engine — applies V2 strategy rules,
enforces constraints, and outputs structured trading decisions.
Python post-processing applies paper trades and persists state.

```
bot.py              Main orchestrator (run / --status / --dry-run)
data_pipeline.py    Yahoo Finance fetch + indicator computation
decision_engine.py  Claude API wrapper + output parsing
portfolio.py        Paper portfolio management
trading_calendar.py LSE trading calendar
config.json         All configuration and strategy thresholds
universe.csv        ~25 FTSE 100 tickers + ETFs
system_prompt.txt   V2 system prompt for Claude API
positions.json      Portfolio state (committed to git for persistence)
```

## Commands

```bash
python bot.py              # Run daily trading cycle
python bot.py --status     # Print portfolio summary
python bot.py --dry-run    # Pipeline + Claude but don't apply trades
```

## Key Design Decisions

- **Paper trading mode** — simulates trades with fractional shares. Switch to live later.
- **Claude Haiku for decisions** — ~$0.002/run, ~$0.05/month. Configurable in config.json.
- **Pre-computed indicators** — Python computes all SMA/ATR/volume indicators. Claude only applies strategy logic.
- **GitHub Actions scheduling** — daily cron at 17:30 UTC (after LSE close). No need for PC to be on.
- **positions.json committed to git** — persistence mechanism for GitHub Actions (same pattern as Kraken bot).
- **market_data.csv NOT committed** — re-fetched each run from Yahoo Finance.

## Strategy (V2 System Prompt)

Conservative swing strategy with 4 layers:
1. **Trend filter** — SMA50 > SMA200 (or SMA50 slope positive if < 200 days)
2. **Entry triggers** — Pullback in uptrend OR breakout with volume
3. **Risk sizing** — ATR-based stops, 5% risk per trade on £100 account
4. **Exit rules** — Stop-loss, trend break, time stop, portfolio drawdown

## Configuration

Edit `config.json` to adjust:
- `strategy_profile`: "conservative" / "balanced" / "aggressive"
- `max_risk_per_trade_pct`: risk per trade (0.05 = 5%)
- `max_positions`: max simultaneous positions (5)
- `kill_switch`: true to halt all trading
- `claude_model`: which Claude model to use

## Dependencies

yfinance, anthropic, python-dotenv, pandas (see requirements.txt)

## Setup

1. `pip install -r requirements.txt`
2. Set `ANTHROPIC_API_KEY` in `.env`
3. `python bot.py --dry-run` to test

## Trading Calendar

Update `trading_calendar.py` annually with UK bank holidays.
Consider switching to `exchange_calendars` package for automatic LSE calendar.
