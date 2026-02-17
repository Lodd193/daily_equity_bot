"""Daily Equity Trader — main orchestrator.

Usage:
    python bot.py              # Execute one daily trading cycle
    python bot.py --status     # Print portfolio summary
    python bot.py --dry-run    # Run pipeline + Claude but don't apply trades
"""

import argparse
import json
import logging
import sys
from datetime import date
from pathlib import Path

import portfolio
import trading_calendar

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent


def load_config():
    """Load config.json."""
    with open(BASE_DIR / "config.json") as f:
        return json.load(f)


def status():
    """Print portfolio summary to terminal."""
    pos = portfolio.load_positions(str(BASE_DIR / "positions.json"))

    print(f"\n{'='*60}")
    print(f"  Daily Equity Trader — Portfolio Status")
    print(f"{'='*60}")
    print(f"  As of:          {pos['as_of_date']}")
    print(f"  Cash:           £{pos['cash_balance_gbp']:.2f}")
    unsettled = pos.get("unsettled_sell_proceeds_gbp", 0)
    if unsettled > 0:
        print(f"  Unsettled:      £{unsettled:.2f} (due {pos.get('settlement_due_date', '?')})")
    print(f"  Equity value:   £{pos['equity_value_gbp']:.2f}")
    print(f"  Peak equity:    £{pos['portfolio_peak_equity_gbp']:.2f}")

    peak = pos["portfolio_peak_equity_gbp"]
    equity = pos["equity_value_gbp"]
    if peak > 0:
        drawdown = (peak - equity) / peak * 100
        print(f"  Drawdown:       {drawdown:.1f}%")

    if pos["positions"]:
        print(f"\n  Positions ({len(pos['positions'])}):")
        print(f"  {'Ticker':<10} {'Qty':>8} {'Avg Cost':>10} {'Mkt Val':>10} {'P&L':>10} {'Days':>5}")
        print(f"  {'-'*55}")
        for p in pos["positions"]:
            pnl = p.get("unrealised_pnl_gbp", 0)
            print(
                f"  {p['ticker']:<10} {p['quantity']:>8.4f} "
                f"£{p['avg_cost_gbp']:>8.2f} "
                f"£{p.get('market_value_gbp', 0):>8.2f} "
                f"£{pnl:>+8.2f} "
                f"{p.get('days_held', 0):>5d}"
            )
    else:
        print(f"\n  Positions:      (none)")

    print(f"{'='*60}\n")


def run(dry_run=False):
    """Execute one daily trading cycle."""
    from dotenv import load_dotenv
    import data_pipeline
    import decision_engine

    load_dotenv()
    config = load_config()
    today = date.today()

    log.info("=" * 60)
    log.info("Daily Equity Trader Run: %s", today.isoformat())
    log.info("Mode: %s | Strategy: %s | Dry-run: %s",
             config["mode"], config["strategy_profile"], dry_run)
    log.info("=" * 60)

    # Step 1: Kill switch
    if config.get("kill_switch", False):
        log.warning("Kill switch is ON. No trades.")
        _write_status("NO_TRADES", "Kill switch enabled", today)
        return

    # Step 2: Trading calendar
    cal = trading_calendar.get_trading_calendar(today)
    data_dir = BASE_DIR / "data"
    data_dir.mkdir(exist_ok=True)
    trading_calendar.save_trading_calendar(cal, str(data_dir / "trading_calendar.json"))

    if not cal["is_trading_day"]:
        log.info("Not a trading day (weekend or bank holiday). Exiting.")
        _write_status("NO_TRADES", "Non-trading day", today)
        return

    if cal["is_half_day"]:
        log.info("Half trading day — reduced liquidity expected.")

    # Step 3: Fetch market data and compute indicators
    log.info("Fetching market data and computing indicators...")
    data_ok = data_pipeline.build_market_data(
        universe_path=str(BASE_DIR / "universe.csv"),
        output_path=str(data_dir / "market_data.csv"),
    )

    if not data_ok:
        log.error("Market data fetch failed for all tickers.")
        _write_status("BLOCKED", "Market data unavailable", today)
        return

    # Step 4: Load and update positions
    pos = portfolio.load_positions(str(BASE_DIR / "positions.json"))
    pos = portfolio.settle_proceeds(pos, today)

    market_data = data_pipeline.load_market_data(str(data_dir / "market_data.csv"))
    pos = portfolio.compute_position_metrics(pos, market_data)
    pos = portfolio.update_equity_and_drawdown(pos, market_data)
    pos["as_of_date"] = today.isoformat()

    # Save updated positions before Claude call
    portfolio.save_positions(pos, str(BASE_DIR / "positions.json"))

    log.info(
        "Portfolio: cash=£%.2f, equity=£%.2f, positions=%d",
        pos["cash_balance_gbp"], pos["equity_value_gbp"], len(pos["positions"]),
    )

    # Step 5: Call Claude decision engine
    log.info("Calling Claude decision engine...")
    try:
        outputs = decision_engine.run_decision_engine(config, BASE_DIR)
    except Exception as e:
        log.error("Decision engine failed: %s", e, exc_info=True)
        _write_status("BLOCKED", f"Decision engine error: {e}", today)
        return

    # Step 6: Check run status
    run_status = outputs.get("run_status", {})
    status_code = run_status.get("status", "BLOCKED")
    reason = run_status.get("reason", "Unknown")
    log.info("Run status: %s — %s", status_code, reason)

    if dry_run:
        log.info("Dry run complete — not applying trades.")
        return

    if status_code != "OK":
        log.info("Status is %s, no trades to apply.", status_code)
        return

    # Step 7: Apply paper trades
    orders_csv = outputs.get("orders_csv", "")
    if orders_csv and orders_csv.strip():
        pos = portfolio.apply_paper_trades(pos, orders_csv, market_data, config)
        pos = portfolio.update_equity_and_drawdown(pos, market_data)

        # Update stop prices from trade plan
        trade_plan = outputs.get("trade_plan", {})
        _update_stop_prices(pos, trade_plan)

        portfolio.save_positions(pos, str(BASE_DIR / "positions.json"))
    else:
        log.info("No orders in output.")

    # Step 8: Append to trade log
    trade_log_entry = outputs.get("trade_log_update")
    if trade_log_entry and trade_log_entry.get("entries"):
        _append_trade_log(trade_log_entry)

    log.info("=" * 60)
    log.info("Run complete.")
    log.info("=" * 60)


def _write_status(status_code, reason, as_of_date):
    """Write run_status.json for non-OK outcomes."""
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)

    status_obj = {
        "status": status_code,
        "as_of_date": as_of_date.isoformat(),
        "reason": reason,
        "currency": "GBP",
    }
    with open(output_dir / "run_status.json", "w") as f:
        json.dump(status_obj, f, indent=2)

    # Write empty orders.csv
    with open(output_dir / "orders.csv", "w") as f:
        f.write("order_id,ticker,side,order_type,quantity,limit_price_gbp,"
                "time_in_force,stop_price_gbp,reason\n")


def _update_stop_prices(positions, trade_plan):
    """Update position stop prices from Claude's trade plan decisions."""
    decisions = trade_plan.get("decisions", [])
    stop_map = {}
    for d in decisions:
        ticker = d.get("ticker")
        stop = d.get("stop", {})
        if ticker and stop.get("price_gbp"):
            stop_map[ticker] = stop["price_gbp"]

    for pos in positions["positions"]:
        if pos["ticker"] in stop_map:
            pos["current_stop_gbp"] = stop_map[pos["ticker"]]


def _append_trade_log(entry):
    """Append trade log entries to logs/trade_log.json."""
    log_path = BASE_DIR / "logs" / "trade_log.json"
    log_path.parent.mkdir(exist_ok=True)

    existing = []
    if log_path.exists():
        with open(log_path) as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                existing = []

    existing.append(entry)

    with open(log_path, "w") as f:
        json.dump(existing, f, indent=2)

    log.info("Trade log updated: %d total entries", len(existing))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daily Equity Trader")
    parser.add_argument("--status", action="store_true", help="Show portfolio summary")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run pipeline + Claude without applying trades")
    args = parser.parse_args()

    if args.status:
        status()
    else:
        run(dry_run=args.dry_run)
