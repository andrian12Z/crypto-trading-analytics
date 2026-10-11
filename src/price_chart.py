
import matplotlib.pyplot as plt
from pathlib import Path


def show_price_chart(prices, coin="BTC/USDT"):
    dates = list(range(1, len(prices) + 1))

    highest = max(prices)
    lowest = min(prices)
    current = prices[-1]

    # Create chart
    fig, ax = plt.subplots(figsize=(12, 6))

    # Dark background
    fig.patch.set_facecolor("#0b1220")
    ax.set_facecolor("#111827")

    # Price line
    ax.plot(
        dates,
        prices,
        color="#00e676",
        linewidth=2.8,
        marker="o",
        markersize=7,
        markerfacecolor="#00e676",
        markeredgecolor="white",
        label="Price"
    )

    # Shaded area
    ax.fill_between(
        dates,
        prices,
        min(prices) * 0.995,
        color="#00e676",
        alpha=0.12
    )

    # Highlight highest and lowest prices
    ax.annotate(
        f"High: ${highest:,.0f}",
        xy=(dates[prices.index(highest)], highest),
        xytext=(0, 15),
        textcoords="offset points",
        color="#00e676",
        ha="center"
    )

    ax.annotate(
        f"Low: ${lowest:,.0f}",
        xy=(dates[prices.index(lowest)], lowest),
        xytext=(0, -22),
        textcoords="offset points",
        color="#ff6b6b",
        ha="center"
    )

    # Titles and labels
    ax.set_title(
        f"{coin}  |  PRICE ANALYSIS",
        color="white",
        fontsize=17,
        fontweight="bold",
        loc="left",
        pad=20
    )

    ax.set_xlabel("Data Point", color="#9ca3af")
    ax.set_ylabel("Price (USDT)", color="#9ca3af")

    # Style
    ax.tick_params(colors="#9ca3af")
    ax.grid(color="#374151", linestyle="--", linewidth=0.6, alpha=0.6)

    for spine in ax.spines.values():
        spine.set_color("#374151")

    ax.legend(
        facecolor="#1f2937",
        edgecolor="#374151",
        labelcolor="white"
    )

    # Current price information
    ax.text(
        0.98,
        0.95,
        f"Last Price: ${current:,.0f}",
        transform=ax.transAxes,
        ha="right",
        va="top",
        color="#00e676",
        fontsize=12,
        fontweight="bold"
    )

    plt.tight_layout()

    # Save chart
    output_dir = Path("reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "btc_price_chart.png"

    plt.savefig(
        output_path,
        dpi=200,
        facecolor=fig.get_facecolor(),
        bbox_inches="tight"
    )

    plt.close()
    print(f"Professional chart saved to: {output_path}")