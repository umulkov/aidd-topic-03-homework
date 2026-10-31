from django.core.management.base import BaseCommand
from django.db import IntegrityError
from tinkoff.invest import Client

from config.settings import TINKOFF_TOKEN, logger
from dashboard.models import Share


class Command(BaseCommand):
    help = "Add shares to DB"

    def handle(self, *args, **options):
        with Client(TINKOFF_TOKEN) as client:
            shares = client.instruments.shares()
            for share in shares.instruments:
                try:
                    Share.objects.update_or_create(
                        figi=share.figi,
                        defaults={
                            "name": share.name,
                            "isin": share.isin,
                            "ticker": share.ticker,
                            "currency": share.currency,
                            "uid": share.uid,
                        },
                    )
                except IntegrityError as e:
                    logger.error(e)
                    continue


