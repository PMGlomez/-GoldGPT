from fastapi import FastAPI, Request
from core.trade_ideas import generate_trade_ideas
from core.trade_tracker import track_trade, get_trade_status
from core.daily_brief import generate_daily_brief

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to TradeGPT 🎯"}

@app.get("/ideas")
def ideas():
    return generate_trade_ideas()

@app.post("/track")
async def track(request: Request):
    data = await request.json()
    return track_trade(data)

@app.get("/tracker/status")
def status():
    return get_trade_status()

@app.get("/daily-brief")
def brief():
    return generate_daily_brief()