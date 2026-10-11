
import ccxt
import pandas as pd
from pathlib import Path


def fetch_ohlcv(
    symbol="BTC/USDT",
    timeframe="1h",
    limit=500,
):
    """Fetch historical OHLCV candles from Binance public market data."""

    exchange = ccxt.binance({
        "enableRateLimit": True,
    })

    candles = exchange.fetch_ohlcv(
        symbol,
        timeframe=timeframe,
        limit=limit,
    )

    if not candles:
        raise ValueError(f"No market data returned for {symbol}")

    df = pd.DataFrame(
        candles,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ],
    )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        unit="ms",
        utc=True,
    )

    df = df.drop_duplicates(subset="timestamp")
    df = df.sort_values("timestamp").reset_index(drop=True)

    return df


def save_market_data(df, symbol="BTC_USDT"):
    """Save market data to a CSV file."""

    output_dir = Path("data")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{symbol}_ohlcv.csv"
    df.to_csv(output_path, index=False)

    return output_path