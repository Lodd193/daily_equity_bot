"""Paper portfolio management.

Manages positions.json state:
- Apply buy/sell paper trades
- Track cash balance with settlement simulation
- Compute equity value and drawdown
- Fractional shares allowed in paper mode
"""

import csv
import io
import json
import logging
from datetime import date, timedelta
from pathlib import Path

log = logging.getLogger(__name__)


def load_positions(path):
    """Load positions.json. Returns dict matching V2 schema."""
    with open(path) as f:
        return json.load(f)


def save_positions(positions, path):
    """Write positions.json."""
    with open(path, "w") as f:
        json.dump(positions, f, indent=2)
    log.info(
        "Saved positions: %d positions, cash=%.2f, equity=%.2f",
        len(positions["positions"]),
        positions["cash_balance_gbp"],
        positions["equity_value_gbp"],
    )


def settle_proceeds(positions, as_of_date):
    """Move unsettled_sell_proceeds_gbp to cash_balance_gbp if settlement due.

    UK T+1 settlement: sells on day T settle on T+1.
    """
    due_date_str = positions.get("settlement_due_date")
    unsettled = positions.get("unsettled_sell_proceeds_gbp", 0)

    if not due_date_str or unsettled <= 0:
        return positions

    due_date = date.fromisoformat(due_date_str)

    if as_of_date >= due_date:
        log.info(
            "Settling £%.2f (due %s, today %s)",
            unsettled, due_date_str, as_of_date.isoformat(),
        )
        positions["cash_balance_gbp"] += unsettled
        positions["unsettled_sell_proceeds_gbp"] = 0.0
        positions["settlement_due_date"] = None

    return positions


def compute_position_metrics(positions, market_data):
    """Update each position with current market values and P&L.

    Args:
        positions: positions.json dict
        market_data: dict of ticker -> row dict from market_data.csv
    """
    today = date.fromisoformat(positions["as_of_date"])

    for pos in positions["positions"]:
        ticker = pos["ticker"]
        data = market_data.get(ticker)

        if data and data.get("close_gbp") is not None:
            close = float(data["close_gbp"])
            pos["market_value_gbp"] = round(close * pos["quantity"], 4)
            pos["unrealised_pnl_gbp"] = round(
                pos["market_value_gbp"] - (pos["avg_cost_gbp"] * pos["quantity"]), 4
            )
        else:
            log.warning("No market data for position %s, keeping last values", ticker)

        # Update days_held
        entry_date = pos.get("entry_date")
        if entry_date:
            entry = date.fromisoformat(entry_date)
            pos["days_held"] = (today - entry).days
        else:
            pos["days_held"] = pos.get("days_held", 0)

    return positions


def update_equity_and_drawdown(positions, market_data):
    """Recompute equity_value_gbp and drawdown tracking."""
    cash = positions["cash_balance_gbp"]
    unsettled = positions.get("unsettled_sell_proceeds_gbp", 0)
    position_value = sum(p.get("market_value_gbp", 0) for p in positions["positions"])

    equity = round(cash + unsettled + position_value, 2)
    positions["equity_value_gbp"] = equity

    # Update peak
    peak = positions.get("portfolio_peak_equity_gbp", equity)
    if equity > peak:
        positions["portfolio_peak_equity_gbp"] = equity

    return positions


def apply_paper_trades(positions, orders_csv, market_data, config):
    """Apply orders from Claude's output to paper portfolio.

    For paper mode:
    - BUY: deduct cost from cash, add/increase position (fractional shares OK)
    - SELL: remove/reduce position, add proceeds to unsettled cash
    - Fill price = close_gbp with slippage applied
    - Stamp duty on UK equity BUYs
    """
    slippage_bps = config.get("slippage_bps", 10)
    stamp_duty_bps = config.get("stamp_duty_bps", 50)
    fee_model = config.get("fee_model", {"type": "per_trade", "value": 0})
    settlement_days = config.get("settlement_days", 1)
    today = date.fromisoformat(positions["as_of_date"])

    # Parse orders CSV
    orders = _parse_orders_csv(orders_csv)

    if not orders:
        log.info("No orders to execute")
        return positions

    total_sell_proceeds = 0.0

    for order in orders:
        ticker = order["ticker"]
        side = order["side"].upper()
        quantity = float(order["quantity"])
        data = market_data.get(ticker)

        if not data or data.get("close_gbp") is None:
            log.warning("No market data for %s, skipping order", ticker)
            continue

        close = float(data["close_gbp"])

        if side == "BUY":
            # Fill price with slippage (buy slightly higher)
            fill_price = close * (1 + slippage_bps / 10000)

            # Costs
            notional = fill_price * quantity
            fee = _compute_fee(fee_model, notional)
            stamp_duty = 0.0
            uk_flag = data.get("uk_equity_flag", "false")
            if str(uk_flag).lower() == "true":
                stamp_duty = notional * stamp_duty_bps / 10000

            total_cost = notional + fee + stamp_duty

            # Check cash
            if total_cost > positions["cash_balance_gbp"]:
                log.warning(
                    "Insufficient cash for %s BUY: need £%.2f, have £%.2f",
                    ticker, total_cost, positions["cash_balance_gbp"],
                )
                continue

            # Deduct cash
            positions["cash_balance_gbp"] = round(
                positions["cash_balance_gbp"] - total_cost, 4
            )

            # Add/update position
            _add_position(positions, ticker, quantity, fill_price, data, today)

            log.info(
                "BUY %s: qty=%.4f @ £%.4f, cost=£%.2f (fee=£%.2f, stamp=£%.2f)",
                ticker, quantity, fill_price, total_cost, fee, stamp_duty,
            )

        elif side == "SELL":
            # Fill price with slippage (sell slightly lower)
            fill_price = close * (1 - slippage_bps / 10000)

            notional = fill_price * quantity
            fee = _compute_fee(fee_model, notional)
            proceeds = notional - fee

            # Reduce/remove position
            removed = _remove_position(positions, ticker, quantity)
            if not removed:
                log.warning("No position to sell for %s", ticker)
                continue

            # Add to unsettled proceeds
            total_sell_proceeds += proceeds

            log.info(
                "SELL %s: qty=%.4f @ £%.4f, proceeds=£%.2f (fee=£%.2f)",
                ticker, quantity, fill_price, proceeds, fee,
            )

    # Settlement: sell proceeds go to unsettled
    if total_sell_proceeds > 0:
        positions["unsettled_sell_proceeds_gbp"] = round(
            positions.get("unsettled_sell_proceeds_gbp", 0) + total_sell_proceeds, 4
        )
        settle_date = today + timedelta(days=settlement_days)
        positions["settlement_due_date"] = settle_date.isoformat()
        log.info(
            "Unsettled proceeds: £%.2f, settlement due: %s",
            total_sell_proceeds, settle_date.isoformat(),
        )

    return positions


def _parse_orders_csv(orders_csv):
    """Parse orders CSV string into list of dicts."""
    if not orders_csv or not orders_csv.strip():
        return []

    reader = csv.DictReader(io.StringIO(orders_csv))
    orders = []
    for row in reader:
        # Skip empty rows or header-only
        if not row.get("ticker") or not row.get("side"):
            continue
        orders.append(row)
    return orders


def _compute_fee(fee_model, notional):
    """Compute trading fee based on fee model."""
    fee_type = fee_model.get("type", "per_trade")
    fee_value = fee_model.get("value", 0)

    if fee_type == "per_trade":
        return fee_value
    elif fee_type == "bps":
        return notional * fee_value / 10000
    return 0


def _add_position(positions, ticker, quantity, fill_price, data, today):
    """Add or increase a position."""
    # Check if position already exists
    for pos in positions["positions"]:
        if pos["ticker"] == ticker:
            # Average up/down
            old_cost = pos["avg_cost_gbp"] * pos["quantity"]
            new_cost = fill_price * quantity
            new_qty = pos["quantity"] + quantity
            pos["quantity"] = round(new_qty, 6)
            pos["avg_cost_gbp"] = round((old_cost + new_cost) / new_qty, 4)
            pos["market_value_gbp"] = round(fill_price * new_qty, 4)
            pos["unrealised_pnl_gbp"] = round(
                pos["market_value_gbp"] - (pos["avg_cost_gbp"] * new_qty), 4
            )
            return

    # New position
    positions["positions"].append({
        "ticker": ticker,
        "quantity": round(quantity, 6),
        "avg_cost_gbp": round(fill_price, 4),
        "market_value_gbp": round(fill_price * quantity, 4),
        "unrealised_pnl_gbp": 0.0,
        "sector": data.get("sector", ""),
        "entry_date": today.isoformat(),
        "days_held": 0,
        "current_stop_gbp": None,
        "status": "ACTIVE",
    })


def _remove_position(positions, ticker, quantity):
    """Reduce or remove a position. Returns True if position was found."""
    for i, pos in enumerate(positions["positions"]):
        if pos["ticker"] == ticker:
            if quantity >= pos["quantity"]:
                # Full sell
                positions["positions"].pop(i)
            else:
                # Partial sell
                pos["quantity"] = round(pos["quantity"] - quantity, 6)
                pos["market_value_gbp"] = round(
                    pos["avg_cost_gbp"] * pos["quantity"], 4
                )
            return True
    return False
