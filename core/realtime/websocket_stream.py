
import asyncio
import websockets
import json

SYMBOLS = ["SPY", "QQQ", "NVDA", "AAPL"]

async def stream_polygon_ws():
    key = "YOUR_POLYGON_WEBSOCKET_KEY"
    uri = f"wss://socket.polygon.io/stocks"

    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"action": "auth", "params": key}))
        await websocket.send(json.dumps({"action": "subscribe", "params": ",".join(f"T.{sym}" for sym in SYMBOLS)}))

        while True:
            response = await websocket.recv()
            print("Live Tick:", response)
            await asyncio.sleep(0.1)
