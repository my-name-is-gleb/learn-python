import asyncio
import time

async def one():
    print("-------------------------------------------------------------------------------------------------")
    print("Задача 1: Начала ждать 8 секунд...")
    print("-------------------------------------------------------------------------------------------------")
    await asyncio.sleep(8)
#     a = (i for i in range(100_000))
#     print(*a)
    print("Задача 1: ПРОСНУЛАСЬ!")
    # Уменьшим до 100, чтобы не вешать консоль
    a = [i for i in range(100)]
    print(f"Результат 1: {a}")

async def two():
    print("-------------------------------------------------------------------------------------------------")
    print("Задача 2: Начала ждать 6 секунд...")
    await asyncio.sleep(6)
#     a = (i for i in range(100_000))
#     print(*a)
    print("Задача 2: ПРОСНУЛАСЬ!")
    a = [i for i in range(100)]
    print(f"Результат 2: {a}")

async def three():
    print("-------------------------------------------------------------------------------------------------")
    print("Задача 3: Начала ждать 3 секунды...")
    await asyncio.sleep(3)
#     a = (i for i in range(100_000))
#     print(*a)
    print("Задача 3: ПРОСНУЛАСЬ!")
    a = [i for i in range(100)]
    print(f"Результат 3: {a}")

async def main():
    time_start = time.perf_counter()
    await asyncio.gather(one(), two(), three())
    time_end = time.perf_counter()
    print(time_end - time_start)

async def main_2():
    tasks = [one(), two(), three()]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(*f"На функции: {task}, мы уже можем упровлять результатом: {result}")

asyncio.run(main())
asyncio.run(main_2())