# TradeBotGPT

**TradeBotGPT** is a real-time options trading assistant built with FastAPI. It generates high-confidence trade ideas using:

### 🔍 Strategy Logic
- EMA/VWAP breakout and flag patterns
- MACD/RSI momentum filters
- SPY, QQQ, NVDA, AAPL options focus

### 📡 Data Sources
- Polygon.io (REST for price, option chains)
- UnusualWhales (flow detection, dark pool)
- QuiverQuant (news sentiment, insider activity)

### ⚙️ API Endpoints
- `/ideas` – Generates real-time trade setups
- `/track` – Log manual option fills
- `/tracker/status` – View open trade logs
- `/daily-brief` – 8:30AM market breakdown & catalyst feed
- `/status` – System heartbeat check

### 💼 Trade Plans
All trade ideas include:
- Contract type, expiration, strike
- Entry premium, 50% stop, 2x target
- 75% partial exit at 75%
- Confidence tags (flow, indicators, sentiment)

---

### 🛠️ Setup Instructions

```bash
# Install requirements
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload
```

This app is configured for deployment on [Render](https://render.com) using the `Procfile`.

---
Built for serious traders. Tuned for precision.