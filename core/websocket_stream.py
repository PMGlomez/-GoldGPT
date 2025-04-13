
import asyncio
import websockets
import json
import os

SYMBOLS = ["SPY", "QQQ", "NVDA", "AAPL", "MSFT"]

async def stream_polygon_ws():
    key = os.getenv("POLYGON_WS_KEY")
    uri = f"wss://socket.polygon.io/stocks"

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                await websocket.send(json.dumps({"action": "auth", "params": key}))
                await websocket.send(json.dumps({"action": "subscribe", "params": ",".join(f"T.{sym}" for sym in SYMBOLS)}))
                print("✅ WebSocket connection established and streaming...")

                while True:
                    response = await websocket.recv()
                    print("📈 Tick:", response)
        except Exception as e:
            print("🔁 Reconnecting due to error:", e)
            await asyncio.sleep(3)
