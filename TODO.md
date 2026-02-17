# Daily Equity Trader — Refinement Roadmap

## High Priority

- [ ] **Web Dashboard** — Flask dashboard with portfolio summary, positions with P&L, equity curve chart (Chart.js), trade history table, and daily report viewer. One-click launcher batch file for easy access. (Port 5050, matching Kraken bot pattern)

- [ ] **Telegram Daily Notifications** — Push daily summary to Telegram after each bot run: status, trades executed, portfolio snapshot, P&L. Alert on stop-loss triggers and errors. Use Telegram Bot API with bot token stored as GitHub Actions secret.

- [ ] **Backtesting Engine** — Replay historical Yahoo Finance data through the strategy. Measure win rate, average R-multiple, max drawdown, Sharpe ratio, total return vs buy-and-hold FTSE 100 benchmark. Generate HTML report with charts.

## Medium Priority

- [ ] **Performance Analytics & Weekly Reports** — Auto-generate weekly/monthly summaries from trade_log.json: win/loss ratio, average holding period, best/worst trades, sector breakdown, equity curve, drawdown history. Markdown report committed to repo or shown on dashboard.

- [ ] **Correlation Matrix Pipeline** — Compute 60-day pairwise correlation matrix for all universe tickers. Output correlation_matrix.csv and add pairwise_correlation_max column to market_data.csv. Feed to Claude for portfolio diversification enforcement (V2 spec already supports this).

- [ ] **Capital Injection CLI** — Simple command to grow the paper portfolio: `python bot.py --deposit 50`. Updates cash_balance_gbp and equity_value_gbp in positions.json.

## Low Priority

- [ ] **Automate Trading Calendar** — Replace hardcoded UK bank holidays in trading_calendar.py with the `exchange_calendars` Python package. Automatic LSE holiday detection, no manual annual updates.

- [ ] **Dynamic Universe Management** — Auto-fetch current FTSE 100 constituents. Detect delistings, additions, and ticker changes. Flag suspended or delisted tickers in universe.csv.

## Future

- [ ] **Live Broker Integration** — Abstract paper trading into a broker interface. Implement real order submission via Trading 212 API or Interactive Brokers API. Gradual rollout: shadow mode first (live data, paper execution), then real execution with small capital.
