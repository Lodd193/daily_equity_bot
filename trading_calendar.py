"""LSE trading calendar — determines if today is a trading day.

Handles UK bank holidays and LSE half-trading days.
Update the holiday lists annually or switch to the exchange_calendars package.
"""

import json
import logging
from datetime import date, timedelta

log = logging.getLogger(__name__)

# UK bank holidays (update annually)
UK_BANK_HOLIDAYS = {
    # 2025
    date(2025, 1, 1),    # New Year's Day
    date(2025, 4, 18),   # Good Friday
    date(2025, 4, 21),   # Easter Monday
    date(2025, 5, 5),    # Early May
    date(2025, 5, 26),   # Spring
    date(2025, 8, 25),   # Summer
    date(2025, 12, 25),  # Christmas
    date(2025, 12, 26),  # Boxing Day
    # 2026
    date(2026, 1, 1),    # New Year's Day
    date(2026, 4, 3),    # Good Friday
    date(2026, 4, 6),    # Easter Monday
    date(2026, 5, 4),    # Early May
    date(2026, 5, 25),   # Spring
    date(2026, 8, 31),   # Summer
    date(2026, 12, 25),  # Christmas
    date(2026, 12, 28),  # Boxing Day (substitute)
    # 2027
    date(2027, 1, 1),    # New Year's Day
    date(2027, 3, 26),   # Good Friday
    date(2027, 3, 29),   # Easter Monday
    date(2027, 5, 3),    # Early May
    date(2027, 5, 31),   # Spring
    date(2027, 8, 30),   # Summer
    date(2027, 12, 27),  # Christmas (substitute)
    date(2027, 12, 28),  # Boxing Day (substitute)
}

# LSE half trading days (close at 12:30)
LSE_HALF_DAYS = {
    date(2025, 12, 24), date(2025, 12, 31),
    date(2026, 12, 24), date(2026, 12, 31),
    date(2027, 12, 24), date(2027, 12, 31),
}


def get_trading_calendar(as_of_date=None):
    """Return trading calendar info for the given date.

    Returns dict matching V2 system prompt trading_calendar.json schema.
    """
    if as_of_date is None:
        as_of_date = date.today()

    is_weekend = as_of_date.weekday() >= 5
    is_holiday = as_of_date in UK_BANK_HOLIDAYS
    is_trading_day = not is_weekend and not is_holiday
    is_half_day = as_of_date in LSE_HALF_DAYS

    # Find next trading day
    next_day = as_of_date + timedelta(days=1)
    while next_day.weekday() >= 5 or next_day in UK_BANK_HOLIDAYS:
        next_day += timedelta(days=1)

    # Bank holidays in next 5 calendar days
    upcoming_holidays = []
    for i in range(1, 6):
        check_date = as_of_date + timedelta(days=i)
        if check_date in UK_BANK_HOLIDAYS:
            upcoming_holidays.append(check_date.isoformat())

    return {
        "as_of_date": as_of_date.isoformat(),
        "is_trading_day": is_trading_day,
        "is_half_day": is_half_day,
        "next_trading_day": next_day.isoformat(),
        "bank_holidays_next_5_days": upcoming_holidays,
    }


def save_trading_calendar(calendar_data, path):
    """Write trading_calendar.json for Claude API consumption."""
    with open(path, "w") as f:
        json.dump(calendar_data, f, indent=2)
    log.info(
        "Trading calendar saved: trading_day=%s, half_day=%s",
        calendar_data["is_trading_day"],
        calendar_data["is_half_day"],
    )
