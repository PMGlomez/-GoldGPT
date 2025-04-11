
import random
from datetime import datetime, timedelta
from polygon import RESTClient

def generate_trade_ideas():
    tickers = ["SPY", "AAPL", "MSFT", "NVDA"]
    strategies = ["Breakout", "Reversal"]

    # Prioritize SPY and set fixed expiration to next Friday
    today = datetime.now()
    next_expiration = today + timedelta(days=(4 - today.weekday()) % 7 + 1)

    ideas = []
    for ticker in tickers:
        idea = {
            "ticker": ticker,
            "strategy": random.choice(strategies),
            "confidence": round(random.uniform(0.7, 0.95), 2),
            "contract_type": "call",
            "strike_price": round(random.uniform(95, 130), 1),
            "expiration": next_expiration.strftime('%Y-%m-%d')
        }
        ideas.append(idea)

    # Prioritize SPY to be the first idea
    ideas.sort(key=lambda x: 0 if x["ticker"] == "SPY" else 1)
    return ideas
