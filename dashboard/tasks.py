from config.celery import app
from dashboard.models import Share
from dashboard.services.market_data import compute_trend, get_last_data
from config.settings import logger
from django.utils import timezone


@app.task
def update_last_price():
    updated_shares = []

    for share in Share.objects.all():
        try:
            [last_price, detetime] = get_last_data(share)

            is_trend_high = compute_trend(share.last_price, last_price, share.ticker)

            share.last_price = last_price
            share.is_trend_high = is_trend_high
            share.updated_at = timezone.now()
            updated_shares.append(share)
        except Exception as e:
            logger.error(e)

    if updated_shares:
        try:
            Share.objects.bulk_update(
                updated_shares, ["last_price", "is_trend_high", "updated_at"]
            )
        except Exception as e:
            logger.error(e)
