from polygon import RESTClient
from datetime import datetime, timedelta
import os

def generate_trade_ideas():
    client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))
    tickers = ["SPY", "AAPL", "MSFT", "NVDA"]
    ideas = []

    today = datetime.now()
    weekday = today.weekday()
    market_day = today if weekday < 5 else today - timedelta(days=weekday - 4)

    from_date = market_day.date()
    to_date = market_day.date()

    for ticker in tickers:
        try:
            aggs = client.get_aggs(ticker, 1, "minute", from_date, to_date)
            if not aggs:
                continue
            latest_price = aggs[-1].c
            strike = round(latest_price * 1.05, 2)
            expiration = (today + timedelta(days=7)).strftime("%Y-%m-%d")
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

    if not ideas:
        return [{"message": "Market is closed or no data available — check back during market hours."}]
    return ideas