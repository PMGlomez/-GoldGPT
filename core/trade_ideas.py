import random
from datetime import datetime, timedelta

def generate_trade_ideas():
    tickers = ["SPY", "AAPL", "MSFT", "NVDA"]
    strategies = ["Breakout", "Reversal"]
    ideas = []
    expiration = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    for ticker in tickers:
        ask = round(random.uniform(0.8, 3.5), 2)
        idea = {
            "ticker": ticker,
            "strategy": random.choice(strategies),
            "confidence": round(random.uniform(0.7, 0.95), 2),
            "contract_type": "call",
            "strike_price": random.choice([100, 105, 110, 115]),
            "expiration": expiration,
            "entry": ask,
            "stop": round(ask * 0.5, 2),
            "target": round(ask * 2.0, 2),
            "partial_exit": round(ask * 1.75, 2),
            "confidence_tags": ["📈 MACD Bullish", "🟢 High Call Flow", "🕵️ Insider Buying"]
        }
        ideas.append(idea)
    return {"ideas": ideas}