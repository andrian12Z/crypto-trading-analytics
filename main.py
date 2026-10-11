
from datetime import datetime, timezone

import ccxt

from src.market_data import get_btc_market_data
from src.price_chart import show_price_chart


def main():
    print("\n=== BTC DAILY MARKET MONITOR ===")
    print("Fetching live market data...\n")

    try:
        data = get_btc_market_data()

        print("Pair:", data["symbol"])
        print(f"Latest Price: ${data['price']:,.2f} USDT")

        if data["change"] is not None:
            print(f"24h Change: {data['change']:+.2f}%")
        else:
            print("24h Change: Unavailable")

        if data["high"] is not None:
            print(f"24h High: ${data['high']:,.2f}")

        if data["low"] is not None:
            print(f"24h Low: ${data['low']:,.2f}")

        if data["volume"] is not None:
            print(f"24h Volume: ${data['volume']:,.2f} USDT")

        close_date = datetime.fromtimestamp(
            data["daily_timestamp"] / 1000,
            tz=timezone.utc
        )

        print(
            f"Last Completed Daily Close "
            f"({close_date:%Y-%m-%d} UTC): "
            f"${data['daily_close']:,.2f}"
        )

        print("\nMarket data retrieved successfully.")

        # Show the chart using completed daily closing prices
        daily_prices = [float(candle[4]) for candle in data["candles"]]
        show_price_chart(daily_prices, data["symbol"])

    except (ccxt.BaseError, ValueError) as error:
        print("Could not retrieve BTC market data.")
        print("Error:", error)
        print("Please check your internet connection and try again.")


if __name__ == "__main__":
    main()