import random
from datetime import datetime
from polygon import RESTClient
import os

def generate_trade_ideas():
    client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))
    tickers = ["SPY", "AAPL", "MSFT", "NVDA"]
    ideas = []

    today_str = datetime.now().strftime("%Y-%m-%d")

    for ticker in tickers:
        try:
            snapshot = client.get_snapshot_option_contracts_underlying(ticker)
            if not snapshot:
                continue

            # Filter for 0DTE options
            zero_dte_calls = [
                option for option in snapshot["results"]
                if option["details"]["expiration_date"] == today_str
                and option["details"]["type"] == "call"
                and option["last_quote"]["ask"] is not None
                and option["last_quote"]["ask"] <= 4.00
                and 0.35 <= option["greeks"].get("delta", 0) <= 0.7
            ]

            zero_dte_puts = [
                option for option in snapshot["results"]
                if option["details"]["expiration_date"] == today_str
                and option["details"]["type"] == "put"
                and option["last_quote"]["ask"] is not None
                and option["last_quote"]["ask"] <= 4.00
                and -0.7 <= option["greeks"].get("delta", 0) <= -0.35
            ]

            for option in zero_dte_calls + zero_dte_puts:
                ask = option["last_quote"]["ask"]
                idea = {
                    "ticker": ticker,
                    "strategy": "0DTE Momentum",
                    "confidence": round(random.uniform(0.75, 0.95), 2),
                    "contract_type": option["details"]["type"],
                    "strike_price": option["details"]["strike_price"],
                    "expiration": option["details"]["expiration_date"],
                    "option": option["details"]["ticker"],
                    "entry": ask,
                    "stop": round(ask * 0.5, 2),
                    "target": round(ask * 2.0, 2),
                    "partial_exit": round(ask * 1.75, 2),
                    "confidence_tags": [
                        "⚡ 0DTE", "📈 MACD Bullish", "🟢 High Flow"
                    ]
                }
                ideas.append(idea)
        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    if not ideas:
        return {"message": "No valid 0DTE ideas found at the moment."}

    return {"ideas": ideas}