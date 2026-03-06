from datetime import datetime, timedelta, UTC


def within_cooldown(last_action_at: datetime | None, cooldown_seconds: int) -> bool:
    if last_action_at is None:
        return False
    return datetime.now(UTC) < (last_action_at + timedelta(seconds=cooldown_seconds))


def allowed_by_daily_limit(current_count: int, max_per_day: int) -> bool:
    return current_count < max_per_day
