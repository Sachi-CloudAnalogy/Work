import asyncio
import time

async def main():                #occuring one after another
    print(time.strftime('%X'))
    print("1")
    await asyncio.sleep(2)
    print("2")
    print(time.strftime('%X'))

asyncio.run(main())    