
import json
from urllib.request import urlopen
from urllib.parse import urlencode


BASE_URL = "https://data-api.binance.vision/api/v3"


def fetch_json(endpoint, params):
    query = urlencode(params)
    url = f"{BASE_URL}/{endpoint}?{query}"

    try:
        with urlopen(url, timeout=15) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as error:
        raise ValueError(
            f"Gagal mengambil data Binance: {error}"
        ) from error


def get_btc_market_data():
    symbol = "BTCUSDT"

    # Get live price and 24-hour statistics
    ticker = fetch_json(
        "ticker/24hr",
        {"symbol": symbol}
    )

    # Get daily candlestick data
    candles = fetch_json(
        "klines",
        {
            "symbol": symbol,
            "interval": "1d",
            "limit": 8
        }
    )

    if len(candles) < 2:
        raise ValueError("Data candle harian tidak mencukupi.")

    # Exclude the current, unfinished daily candle
    completed_candles = candles[:-1]
    latest_closed = completed_candles[-1]

    return {
        "symbol": "BTC/USDT",
        "price": float(ticker["lastPrice"]),
        "change": float(ticker["priceChangePercent"]),
        "high": float(ticker["highPrice"]),
        "low": float(ticker["lowPrice"]),
        "volume": float(ticker["quoteVolume"]),
        "daily_close": float(latest_closed[4]),
        "daily_timestamp": latest_closed[0],
        "candles": completed_candles[-7:],
    }