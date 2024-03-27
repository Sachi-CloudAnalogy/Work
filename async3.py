# Concurrent execution

import asyncio
import time

async def function(delay, content):
    await asyncio.sleep(delay)
    print(content)

async def main():
    task1 = asyncio.create_task(function(2, "hellooo"))
    task2 = asyncio.create_task(function(1, "hiii"))

    print(f"Time : {time.strftime('%X')}")
    await task1
    await task2
    print(f"Time : {time.strftime('%X')}")

asyncio.run(main())    