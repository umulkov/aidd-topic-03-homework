from tinkoff.invest import Client

from config.settings import TINKOFF_TOKEN, logger


def compute_trend(
    prev_price: float | None, new_price: float | None, ticker: str | None = None
) -> bool | None:
    if prev_price is None:
        logger.warning(
            "no previous price for %s, skipping trend", ticker or "<unknown>"
        )
        return None
    if new_price is None:
        return None
    return new_price >= prev_price


def get_last_data(share):
    with Client(TINKOFF_TOKEN) as client:
        resp = client.market_data.get_last_prices(figi=[share.figi])
        resp = resp.last_prices.pop()
        logger.info(f"Get last data for share with id {share.id}")
        price = resp.price.units + resp.price.nano / 1_000_000_000
        return [price, resp.time]
