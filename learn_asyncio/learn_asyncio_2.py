import asyncio
import time

def block_cod():
    time.sleep(4)

def block_cod_2():
    time.sleep(3)

async def cod_3():
    await asyncio.sleep(2)

async def main():
    test = asyncio.to_thread(block_cod)
    test_2 = asyncio.to_thread(block_cod_2)
    await asyncio.gather(cod_3(), test, test_2)

asyncio.run(main())
