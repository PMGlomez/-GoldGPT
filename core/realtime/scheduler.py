
import asyncio
from core.daily_brief import generate_daily_brief
from datetime import datetime

async def run_scheduler():
    while True:
        now = datetime.now()
        if now.hour == 8 and now.minute == 30:
            print("Auto running 8:30AM daily brief...")
            generate_daily_brief()
        await asyncio.sleep(60)
