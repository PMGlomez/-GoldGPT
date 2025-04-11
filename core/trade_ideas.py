from polygon import RESTClient
from datetime import datetime, timedelta
import os

def generate_trade_ideas():
    client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))
    tickers = ["SPY", "AAPL", "MSFT", "NVDA"]
    ideas = []

    for ticker in tickers:
        try:
            today = datetime.now().date()
            aggs = client.get_aggs(ticker, 1, "minute", today, today)
            latest_price = aggs[-1].c if aggs else None
            if latest_price:
                strike = round(latest_price * 1.05, 2)
                expiration = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                idea = {
                    "ticker": ticker,
                    "strategy": "Breakout",
                    "confidence": 0.85,
                    "contract_type": "call",
                    "strike_price": strike,
                    "expiration": expiration
                }
                ideas.append(idea)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    return ideas