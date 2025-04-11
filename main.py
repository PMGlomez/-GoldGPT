
from fastapi import FastAPI
from core.trade_ideas import generate_trade_ideas

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to TradeGPT 🎉"}

@app.get("/ideas")
def get_trade_ideas():
    return generate_trade_ideas()

@app.get("/status")
def status():
    return {"status": "ok"}
