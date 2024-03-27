import asyncio
import time

async def function(delay, content):
    await asyncio.sleep(delay)
    print(content)

async def main():               
    print(f"Time : {time.strftime('%X')}")
    await function(2, "helloooo")
    await function(1, "hiiii")
    print(f"Time : {time.strftime('%X')}")

asyncio.run(main())