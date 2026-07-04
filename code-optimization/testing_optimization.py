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
    print(f"1. Square roots calculated in: {time.time() - start:.2f} sec.")


# 2
def second_mathematical_task(): 
    start = time.time()
    count = 0
    for n in range(2, 380_000):
        if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1)):
            count += 1
    print(f"2. Prime numbers found in: {time.time() - start:.2f} sec.")


# 3
def third_mathematical_task():
    start = time.time()
    res3 = 0
    for i in range(1, 6_000_000):
        res3 += math.sin(i) * math.cos(i)
    print(f"3. Trigonometry calculated in: {time.time() - start:.2f} sec.")


# 4
def fourth_mathematical_task():
    start = time.time()
    res4 = 0
    for i in range(1, 6_500_000):
        res4 += (i ** 3) ** 0.1
    print(f"4. Powers calculated in: {time.time() - start:.2f} sec.")


# 5
def fifth_mathematical_task():
    start = time.time()
    res5 = 1
    for i in range(1, 15_000_000):
        res5 = (res5 + i) % 999_999_937
    print(f"5. Modular chain calculated in: {time.time() - start:.2f} sec.")


if __name__ == '__main__':
    import asyncio
    import aiohttp
    import bisect
    import requests
    from util import fetch_status

    print("Please wait while we generate the large list—I haven't learned how to optimize it yet.")
    my_list = [_ for _ in range(30_000_000)]
    print("finished")

    """no optimization"""
    print("For verification accuracy, it is recommended to enter identical numbers.")
    
    user_number = int(input("Enter an integer: "))
    
    sync_total_start = time.perf_counter()

    sync_search_start = time.perf_counter()
    find_number = my_list.index(user_number)
    sync_search_duration = time.perf_counter() - sync_search_start
    print(f"Your number {user_number} was found at index {find_number} in {sync_search_duration} seconds.")

    list_for_requests = []
    
    sync_requests_start = time.perf_counter()
    try:
        for request in range(101):
            request = requests.get("https://example.com")
            list_for_requests.append(request.status_code)
    except Exception as ex:
        print(f"An error occurred: {ex}")
    sync_requests_duration = time.perf_counter() - sync_requests_start
    print(f"100 requests were completed in {sync_requests_duration} seconds.")

    """"""

    print("Solving math problems")

    """The examples were written by artificial intelligence."""

    sync_math_start = time.perf_counter()

    first_mathematical_task()
    second_mathematical_task()
    third_mathematical_task()
    fourth_mathematical_task()
    fifth_mathematical_task()

    sync_math_duration = time.perf_counter() - sync_math_start

    sync_total_duration = time.perf_counter() - sync_total_start
    
    print(f"The total execution time of the unoptimized program was {sync_total_duration} seconds.")

    """-------------------------------------------------------------"""

    user_number_2 = int(input("Enter an integer: "))
    
    opt_total_start = time.perf_counter()

    opt_search_start = time.perf_counter()
    result = bisect.bisect_left(my_list, user_number_2)
    opt_search_duration = time.perf_counter() - opt_search_start
    print(f"We found the result in {opt_search_duration} seconds, while in the previous, non-optimized version it took {sync_search_duration}.")

    url = "https://www.example.com"

    async def main():
        try:
            async with aiohttp.ClientSession() as session:
                list_for_task = []
                for res in range(101):
                    res = asyncio.create_task(fetch_status(session, url))
                    list_for_task.append(res)
                statuses = await asyncio.gather(*list_for_task, return_exceptions=True)
                for status in statuses:
                    print(status)
        except Exception as ex:
            print(f"An error occurred: {ex}")

    async_requests_start = time.perf_counter()
    asyncio.run(main())
    async_requests_duration = time.perf_counter() - async_requests_start
    print(f"The result of the optimized web request is {async_requests_duration} seconds.")

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
        print(f"The {p} process has started running.")
    
    for p in all_processes:
        p.join()
    opt_math_duration = time.perf_counter() - opt_math_start
    print(f"We calculated all the tasks in {opt_math_duration} seconds.")

    opt_total_duration = time.perf_counter() - opt_total_start

    print("\n" + "="*60)
    print("FINAL OPTIMIZATION EFFICIENCY REPORT")
    print("="*60)
    print(f"1. Element index search in the list:")
    print(f"   Non-optimized execution took: {sync_search_duration:.6f} sec.")
    print(f"   Optimized execution (bisect) took: {opt_search_duration:.6f} sec.")
    print(f"   Difference: {sync_search_duration - opt_search_duration:.6f} sec speedup.")
    print("-"*60)
    print(f"2. Execution of 100 network requests:")
    print(f"   Non-optimized execution took: {sync_requests_duration:.2f} sec.")
    print(f"   Optimized execution (asyncio) took: {async_requests_duration:.2f} sec.")
    print(f"   Difference: {sync_requests_duration - async_requests_duration:.2f} sec speedup.")
    print("-"*60)
    print(f"3. Heavy mathematical task computation:")
    print(f"   Non-optimized execution (sequential) took: {sync_math_duration:.2f} sec.")
    print(f"   Optimized execution (multiprocessing) took: {opt_math_duration:.2f} sec.")
    print(f"   Difference: {sync_math_duration - opt_math_duration:.2f} sec speedup.")
    print("-"*60)
    print(f"TOTAL EXECUTION TIME FOR ALL TASKS (excluding user input pauses):")
    print(f"   Total synchronous code execution time: {sync_total_duration:.2f} sec.")
    print(f"   Total optimized code execution time: {opt_total_duration:.2f} sec.")
    print(f"   TOTAL DIFFERENCE: {sync_total_duration - opt_total_duration:.2f} sec speedup.")
    print("="*60)