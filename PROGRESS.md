# Daily Equity Trader — Progress Log

## Completed (2026-02-17)

### Core Bot (All 5 Phases)
- [x] Project skeleton — config.json, universe.csv, positions.json, trading_calendar.py
- [x] Data pipeline — Yahoo Finance fetch + 15 indicator columns (SMA50, SMA200, ATR14, etc.)
- [x] Decision engine — Claude Haiku API integration + output parsing
- [x] Portfolio manager — paper trades, fractional shares, settlement, stamp duty
- [x] Orchestrator (bot.py) — run / --status / --dry-run
- [x] GitHub Actions — daily cron at 17:30 UTC weekdays
- [x] First trades executed: AZN.L (breakout) + SHEL.L (pullback)

### Dashboard
- [x] Static HTML dashboard with Chart.js (dark theme, responsive)
- [x] Deployed to GitHub Pages: https://lodd193.github.io/daily_equity_bot/
- [x] Summary cards, positions table, equity curve, sector allocation
- [x] Candidates analysis, trade history, daily report viewer
- [x] Equity history tracking (equity_history.json)
- [x] Auto-updates after each daily Actions run

### Fixes Applied During Build
- UTF-8 encoding on all file writes (Windows cp1252 can't handle Claude's Unicode)
- Fractional shares instruction added to system prompt (£100 too small for whole shares)
- Lazy imports in bot.py so --status works without yfinance installed
- Repo made public for GitHub Pages access

## Current State
- **Portfolio**: £99.46 equity, 2 positions (AZN.L, SHEL.L), £8.79 cash
- **Bot runs daily** at 17:30 UTC via GitHub Actions
- **Dashboard live** at https://lodd193.github.io/daily_equity_bot/
- **Paper trading mode** — no real money involved

## Remaining TODO (Priority Order)

### High
- [ ] Telegram daily notifications — push trade alerts + portfolio summary to phone
- [ ] Backtesting engine — validate strategy on historical data

### Medium
- [ ] Performance analytics & weekly reports — win rate, Sharpe, sector breakdown
- [ ] Correlation matrix pipeline — better diversification (V2 spec supports it)
- [ ] Capital injection CLI — `python bot.py --deposit 50`

### Low
- [ ] Automate trading calendar — replace hardcoded holidays with exchange_calendars
- [ ] Dynamic universe management — auto-update FTSE 100 constituents

### Future
- [ ] Live broker integration (Trading 212 / IBKR)

## Key Files
| File | Purpose |
|------|---------|
| `bot.py` | Main orchestrator |
| `data_pipeline.py` | Yahoo Finance + indicators |
| `decision_engine.py` | Claude API wrapper |
| `portfolio.py` | Paper portfolio management |
| `generate_dashboard.py` | Static HTML dashboard generator |
| `config.json` | All configuration |
| `system_prompt.txt` | V2 system prompt for Claude |
| `positions.json` | Current portfolio state |
| `equity_history.json` | Daily equity snapshots |

## Links
- **Repo**: https://github.com/Lodd193/daily_equity_bot
- **Dashboard**: https://lodd193.github.io/daily_equity_bot/
- **Actions**: https://github.com/Lodd193/daily_equity_bot/actions
