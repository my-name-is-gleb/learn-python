"""Testing optimization with asyncio, threading, multiprocessing, bisect"""
"""All examples and code assume that the user enters valid data."""
"""We use this unusual writing style due to the way the multiprocessing module works."""
"""We didn't end up needing that poor little threading module):"""
import multiprocessing
import time
import math

# 1
def first_mathematical_task():
    start = time.time()
    res1 = sum(i ** 0.5 for i in range(11_000_000))
    print(f"1. Square roots calculated in: {time.time() - start:.2f} sec. / 1. Квадратные корни вычислены за: {time.time() - start:.2f} сек.")


# 2
def second_mathematical_task(): 
    start = time.time()
    count = 0
    for n in range(2, 380_000):
        if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1)):
            count += 1
    print(f"2. Prime numbers found in: {time.time() - start:.2f} sec. / 2. Простые числа найдены за: {time.time() - start:.2f} сек.")


# 3
def third_mathematical_task():
    start = time.time()
    res3 = 0
    for i in range(1, 6_000_000):
        res3 += math.sin(i) * math.cos(i)
    print(f"3. Trigonometry calculated in: {time.time() - start:.2f} sec. / 3. Тригонометрия вычислена за: {time.time() - start:.2f} сек.")


# 4
def fourth_mathematical_task():
    start = time.time()
    res4 = 0
    for i in range(1, 6_500_000):
        res4 += (i ** 3) ** 0.1
    print(f"4. Powers calculated in: {time.time() - start:.2f} sec. / 4. Степени вычислены за: {time.time() - start:.2f} сек.")


# 5
def fifth_mathematical_task():
    start = time.time()
    res5 = 1
    for i in range(1, 15_000_000):
        res5 = (res5 + i) % 999_999_937
    print(f"5. Modular chain calculated in: {time.time() - start:.2f} sec. / 5. Модульная цепь вычислена за: {time.time() - start:.2f} сек.")


if __name__ == '__main__':
    import asyncio
    import aiohttp
    import bisect
    import requests
    import os
    from rich.console import Console
    from rich.progress import track
    from rich.table import Table
    from util import fetch_status

    print("Please wait while we generate the large list—I haven't learned how to optimize it yet. / Пожалуйста, подождите, пока мы генерируем большой список — я еще не научился его оптимизировать.")
    
    console = Console()

    with console.status("[bold green]Generating list / Генерация списка..."):
        my_list = [_ for _ in range(30_000_000)]
        
    print("finished / завершено")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear') # clear the console

    """no optimization"""
    print("For verification accuracy, it is recommended to enter identical numbers. / Для точности проверки рекомендуется вводить одинаковые числа.")
    
    user_number = int(input("Enter an integer: / Введите целое число: "))
    
    sync_total_start = time.perf_counter()

    sync_search_start = time.perf_counter()
    find_number = my_list.index(user_number)
    sync_search_duration = time.perf_counter() - sync_search_start
    print(f"Your number {user_number} was found at index {find_number} in {sync_search_duration} seconds. / Ваше число {user_number} было найдено по индексу {find_number} за {sync_search_duration} секунд.")

    list_for_requests = []
    
    sync_requests_start = time.perf_counter()
    try:
        for _ in track(range(101), description="Sending requests / Отправка запросов..."):
            request = requests.get("https://example.com")
            list_for_requests.append(request.status_code)
    except Exception as ex:
        print(f"An error occurred: {ex} / Произошла ошибка: {ex}")
    sync_requests_duration = time.perf_counter() - sync_requests_start
    print(f"100 requests were completed in {sync_requests_duration} seconds. / 100 запросов были выполнены за {sync_requests_duration} секунд.")

    """"""

    print("Solving math problems / Решение математических задач")

    """The examples were written by artificial intelligence."""

    sync_math_start = time.perf_counter()

    first_mathematical_task()
    second_mathematical_task()
    third_mathematical_task()
    fourth_mathematical_task()
    fifth_mathematical_task()

    sync_math_duration = time.perf_counter() - sync_math_start

    sync_total_duration = time.perf_counter() - sync_total_start
    
    print(f"The total execution time of the unoptimized program was {sync_total_duration} seconds. / Общее время выполнения неоптимизированной программы составило {sync_total_duration} секунд.")

    """-------------------------------------------------------------"""

    user_number_2 = int(input("Enter an integer: / Введите целое число: "))
    
    opt_total_start = time.perf_counter()

    opt_search_start = time.perf_counter()
    result = bisect.bisect_left(my_list, user_number_2)
    opt_search_duration = time.perf_counter() - opt_search_start
    print(f"We found the result in {opt_search_duration} seconds, while in the previous, non-optimized version it took {sync_search_duration}. / Мы нашли результат за {opt_search_duration} секунд, тогда как в предыдущей, неоптимизированной версии это заняло {sync_search_duration}.")

    url = "https://www.example.com"

    async def main():
        try:
            async with aiohttp.ClientSession() as session:
                list_for_task = []
                for res in track(range(101), description="Creating async tasks / Создание асинхронных задач..."):
                    res = asyncio.create_task(fetch_status(session, url))
                    list_for_task.append(res)
                
                with console.status("[bold cyan]Awaiting async tasks / Ожидание асинхронных задач..."):
                    await asyncio.gather(*list_for_task, return_exceptions=True)
        except Exception as ex:
            print(f"An error occurred: {ex} / Произошла ошибка: {ex}")

    async_requests_start = time.perf_counter()
    asyncio.run(main())
    async_requests_duration = time.perf_counter() - async_requests_start
    print(f"The result of the optimized web request is {async_requests_duration} seconds. / Результат оптимизированного веб-запроса составил {async_requests_duration} секунд.")

    opt_math_start = time.perf_counter()
    process = multiprocessing.Process(target=first_mathematical_task)
    second_process = multiprocessing.Process(target=second_mathematical_task)
    third_process = multiprocessing.Process(target=third_mathematical_task)
    fourth_process = multiprocessing.Process(target=fourth_mathematical_task)
    fifth_process = multiprocessing.Process(target=fifth_mathematical_task)

    # A list for conveniently managing all processes at once.
    all_processes = [process, second_process, third_process, fourth_process, fifth_process]

    for p in all_processes:
        p.start()
    
    with console.status("[bold blue]Calculating math tasks / Вычисление математических задач..."):
        for p in all_processes:
            p.join()
            
    opt_math_duration = time.perf_counter() - opt_math_start
    print(f"We calculated all the tasks in {opt_math_duration} seconds. / Мы вычислили все задачи за {opt_math_duration} секунд.")

    opt_total_duration = time.perf_counter() - opt_total_start

    print("\n")
    
    table = Table(title="FINAL OPTIMIZATION EFFICIENCY REPORT / ИТОГОВЫЙ ОТЧЕТ ОБ ЭФФЕКТИВНОСТИ ОПТИМИЗАЦИИ", title_style="bold green")
    
    table.add_column("Task / Задача", justify="left", style="cyan", no_wrap=True)
    table.add_column("Unoptimized / Неоптимизированный", justify="center", style="magenta")
    table.add_column("Optimized / Оптимизированный", justify="center", style="green")
    table.add_column("Speedup / Ускорение", justify="right", style="yellow")

    table.add_row(
        "1. Element index search in the list\nПоиск индекса элемента в списке",
        f"{sync_search_duration:.6f} sec",
        f"{opt_search_duration:.6f} sec",
        f"{sync_search_duration - opt_search_duration:.6f} sec"
    )
    table.add_row(
        "2. Execution of 100 network requests\nВыполнение 100 сетевых запросов",
        f"{sync_requests_duration:.2f} sec",
        f"{async_requests_duration:.2f} sec",
        f"{sync_requests_duration - async_requests_duration:.2f} sec"
    )
    table.add_row(
        "3. Heavy mathematical task computation\nВычисление тяжелых математических задач",
        f"{sync_math_duration:.2f} sec",
        f"{opt_math_duration:.2f} sec",
        f"{sync_math_duration - opt_math_duration:.2f} sec"
    )
    table.add_row(
        "TOTAL EXECUTION TIME\nОБЩЕЕ ВРЕМЯ ВЫПОЛНЕНИЯ",
        f"{sync_total_duration:.2f} sec",
        f"{opt_total_duration:.2f} sec",
        f"{sync_total_duration - opt_total_duration:.2f} sec",
        style="bold"
    )

    console.print(table)