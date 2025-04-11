from datetime import datetime

def generate_daily_brief():
    return {
        "timestamp": datetime.now().isoformat(),
        "summary": "📊 TradeBotGPT Morning Brief",
        "spy_level": "SPY resistance at 515, support at 505",
        "catalysts": ["CPI Report tomorrow", "Fed speakers today"],
        "ideas": ["SPY 510C 4/19", "AAPL 185C 4/19"]
    }