from django.utils import timezone

from config.celery import app
from config.settings import logger
from dashboard.models import Share
from dashboard.services.market_data import get_last_data


def compute_trend(prev_price, new_price, ticker=None):
    """Определить тренд по предыдущей и новой цене."""
    if prev_price is None:
        if ticker is not None:
            logger.warning(f"no previous price for {ticker}, skipping trend")
        else:
            logger.warning("no previous price, skipping trend")
        return None
    return new_price >= prev_price


@app.task
def update_last_price():
    shares = list(Share.objects.all())
    rows = []

    for share in shares:
        try:
            [last_price, detetime] = get_last_data(share)

            is_trend_high = compute_trend(
                share.last_price, last_price, share.ticker
            )

            share.last_price = last_price
            share.is_trend_high = is_trend_high
            share.updated_at = timezone.now()
            rows.append(share)
        except Exception as e:
            logger.error(e)

    if rows:
        Share.objects.bulk_update(
            rows, ["last_price", "is_trend_high", "updated_at"]
        )
