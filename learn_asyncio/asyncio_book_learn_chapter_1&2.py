# import requests
# 
# response = requests.get()
# items = response.headers.items()
# headers = [f'{key}: {headers}' for key, headers in items]
# formatted_headers = '/n'.join(headers)
# with open("headers.txt", "w") as file:
#     file.write(formatted_headers)

# import os
# import threading
# 
# print(f"Исполняется Python-процесс с индтификатором: {os.getpid()}")
# 
# total_threads = threading.active_count()
# thread_name = threading.current_thread().name
# 
# print(f"В данный момент Python исполняет {total_threads} потоков")
# print(f"Имя текущего потока {thread_name}")

# import threading
# 
# def hello_from_thread():
#     print(f"Привет от потока {threading.current_thread()}!")
# 
# hello_thread = threading.Thread(target=hello_from_thread)
# hello_thread.start()
# 
# total_threads = threading.active_count()
# thread_name = threading.current_thread().name
# 
# print(f"В данный момент Python исполняет {total_threads} потоков")
# print(f"Имя текущего потока {thread_name}")
# hello_thread.join()
# 
# def factorial(n):
#     # 1. Базовый случай (Точка выхода)
#     if n == 1:
#         return 1
#     
#     # 2. Шаг рекурсии (Вызываем себя же, но уменьшаем число на 1)
#     else:
#         return n * factorial(n - 1)
#     
# factorial(5)

# from collections import deque
# 
# messages = deque()
# 
# while True:
#     if messages:
#         message = messages.pop()
#         process_message(message)

# import multiprocessing
# import time
# 
# def block_cod() -> None:
# #     user_block_input = input("Введи текст, а пока другая задача будет выполняься паалельно: ")
#     # Вместо инпута симулируем долгую работу (например, тяжелый расчет или ожидание)
#     print("Дочерний процесс: Я зашел в тяжелую функцию и буду «думать» 3 секунды...")
#     time.sleep(3)
#     print("Дочерний процесс: Я закончил думать!")
# 
# if __name__ == '__main__':
#     process = multiprocessing.Process(target=block_cod)
#     process.start()
# 
#     for i in range(1, 6):
#         print("Работаю(вроде)")
#         time.sleep(1)
# 
#     process.join()

"""Через input проверить не льзя потому что для ввода нужен доступ к клавиатуре,
     который есть у главного процесса, но когда мы создаем другой,
     то ОС Windows полностью изолирует его и у него нету доступ к клавиатуре."""

"""попробуем обойти"""

# print("-------------------------------------------------------------------------------------")
# 
# import multiprocessing
# import time
# 
# def block_cod():
#     for i in range(1, 6):
#         print("Работаю(вроде)")
#         time.sleep(1)
# 
# if __name__ == '__main__':
#     process = multiprocessing.Process(target=block_cod)
#     process.start()
# 
#     input("Введи чота проверим) ")
# 
#     process.join()
# 

"""но наверно будет лучше это сделать через многопоточность"""
"""проверим!"""

# import threading
# import time
# 
# def block_cod():
#     for i in range(1, 11):
#         print(f"loading: {i}/10")
#         time.sleep(1)
# 
# if __name__ == "__main__":
#     test_thread = threading.Thread(target=block_cod)
#     test_thread.start()
#     input("роботает? ")
#     test_thread.join()
# 
"""Последний варик самый лучший"""
# 
# def test() -> str:
#     return "hello"
# 
# test() # - просто хотел проверить пишет ли в консоль чтото при ретурне

"""Листинги второй главы(нужные и от 2.5)"""

# import asyncio
# 
# async def hello_world_message() -> str:
#     await asyncio.sleep(1) # - нужно подписывать await т.к. asyncio.sleep() - корутина или сопрограмма
#     return "hi"
# 
# async def main() -> None:
#     massage = await hello_world_message()
#     print(massage)
#     # если просто вызвать асинхроную функцию то не выведется в консоль не чего но тут мы явно передаем результат в переменую 
# 
# asyncio.run(main())

# async def delay(delay_seconds: int) -> int:
#     print(f"засыпаю на {delay_seconds} c")
#     await asyncio.sleep(delay_seconds)
#     print(f"сон в течении {delay_seconds}c закончился")
#     return delay_seconds


# import asyncio
# from util import delay
# 
# async def add_one(number: int) -> int:
#     return number + 1
# 
# async def hello_world_message() -> str:
#     await delay(1)
#     return "hi"
# 
# async def main() -> None:
#     massage = await hello_world_message()
#     one_plus_one = await add_one(1)
#     print(one_plus_one)
#     print(massage)
# 
# asyncio.run(main())
# 
# 
# 
# """-----------------------------------------------------------------------------------"""
# 
# def test_func():
#     return "hi mir"
# 
# new_name = test_func # мы просто дали второе имя функции переменая "new_name", хранит в себе ссылку на оригинал
# new_variable = test_func() # а сюда мы помещяем резултат(return) тоесть new_variable == "hi mir"
# 
# print(new_name)
# print(type(new_name))
# print(new_variable)
# print(type(new_variable))

# import asyncio
# from util import delay
# 
# async def main():
#     sleep_for_three = asyncio.create_task(delay(3))
#     # сопрограма уже обернулась в обертку задачи и пошла роботать в фон,
#     # поэтому сообщение снизу напечатается сразу, а не через 3 сек.
#     # а ещё как только сробатывает asyncio.create_task(), 
#     # сразу же пайтон перекидывает эту задачу списку событий и просит его выполнить ее как можно рашьше
#     print(type(sleep_for_three))
#     result = await sleep_for_three
#     # строчка выше говорит пайтону подождать завершения sleep_for_three и вернуть в переменую result результат ее работы
#     print(result)
# 
# asyncio.run(main())
"""Аналогия из жизни.
    Представь, что ты пришел в пиццерию:

    Строка sleep_for_three = asyncio.create_task(...) — это момент, когда ты оплатил пиццу на кассе. 
    Повар на кухне уже начал её готовить (задача запущена в фоне). Тебе выдали чек с номером заказа (это твоя переменная sleep_for_three).

    Ты можешь отойти от кассы, полистать ленту в телефоне, проверить гитхаб (это код, который выполняется сразу под create_task).

    Но в какой-то момент тебе нужна сама пицца (return). Ты подходишь к окну выдачи и говоришь await sleep_for_three.

    Если пицца еще печется — ты стоишь и ждешь у окна. 
    Если она уже готова — ты мгновенно забираешь её коробку в руки (result = ...) и можешь её съесть (print(result)).

    Если бы ты ушел из пиццерии сразу после шага 1, не подождав у окна выдачи, ты бы остался голодным.(за это отвечает await sleep_for_three)"""


# import time
# def one_func():
#     print("print()")
#     time.sleep(3)
#     return "return"
# 
# print(one_func())
# print("---------------------------------------------------------------------------------------------------------")
# print(one_func)
# print("---------------------------------------------------------------------------------------------------------")
# one_func()
# print("---------------------------------------------------------------------------------------------------------")
# one_func

# import asyncio
# import time
# from util import delay
# 
# async def main():
#     sleep_for_three = asyncio.create_task(delay(3))
#     sleep_again = asyncio.create_task(delay(3))
#     sleep_once_more = asyncio.create_task(delay(3))
#     print("Функция №1")
# 
#     await sleep_for_three
#     await sleep_again
#     await sleep_once_more
# 
# async def main_2():
#     sleep_for_three = asyncio.create_task(delay(3))
#     sleep_again = asyncio.create_task(delay(3))
#     sleep_once_more = asyncio.create_task(delay(3))
#     print("Функция №2")
# 
#     await sleep_for_three
#     await sleep_again
#     await sleep_once_more
# 
# async def main_3():
#     sleep_for_three = asyncio.create_task(delay(3))
#     sleep_again = asyncio.create_task(delay(3))
#     sleep_once_more = asyncio.create_task(delay(3))
#     print("Функция №3")
# 
#     await sleep_for_three
#     await sleep_again
#     await sleep_once_more
# 
# async def most_main():
#     await asyncio.gather(main(), main_2(), main_3())
# 
# start_time = time.perf_counter()
# asyncio.run(most_main())
# end_time = time.perf_counter()
# print(f"Асинхроная програма выполнялась {end_time-start_time}, вместо 27с.")


# import asyncio
# from util import delay
# 
# async def hello_every_second():
#     for i in range(2):
#         await asyncio.sleep(1)
#         print("пока я жду, исполняется другой код!")
# 
# async def main():
#     firs_delay = asyncio.create_task(delay(3))
#     second_delay = asyncio.create_task(delay(3))
#     await hello_every_second()
#     await firs_delay
#     await second_delay
# 
# asyncio.run(main())

# import asyncio
# from util import delay
# 
# async def main():
#     long_task = asyncio.create_task(delay(10))
#     second_elapsed = 0
#     while not long_task.done():
#         print("Задача не закончилась следующая проверка через секунду.")
#         await a0syncio.sleep(1)
#         second_elapsed += 1
#         if second_elapsed == 5:
#             long_task.cancel()
# 
#     try:
#         await long_task
#     except asyncio.CancelledError:
#         print('Задача была снята')
# 
# asyncio.run(main())

"""!Важно что метод cancel не останавлевает задачу принудительно, если в задаче будет робоать счетный пайтон-код - она не будет остановллена,
    а остановлена она будет в случае если задача будет на строчке await"""

# import asyncio
# from util import delay
# 
# async def main():
#     delay_task = asyncio.create_task(delay(3))
#     try:
#         result = await asyncio.wait_for(delay_task, timeout=3.01)
#         print(result)
#     except asyncio.TimeoutError:
#         print('Тайм-аут')
#         print(f"Задача была снята? {delay_task.cancelled()}")
# 
# asyncio.run(main())

# import asyncio
# from util import delay
# 
# async def main():
#     task = asyncio.create_task(delay(10))
# 
#     try:
#         result = await asyncio.wait_for(asyncio.shield(task), 5)
#         print(result)
#     except TimeoutError:
#         print('Задача заняла более 5сек., скоро она закончится!')
#         print(result)
# 
# asyncio.run(main())



# import asyncio
# from util import delay
# 
# def question() -> bool:
#     work_next = None
#     while True:
#         input_question = input("Прошло уже 5 секунд, задача обрабатывается дольше чем мы ожидали, вы готовы ждать?(да/нет)")
#         if input_question.strip().lower() == "да":
#             work_next = True
#             break
#         elif input_question.strip().lower() == "нет":
#             work_next = False
#             break
#         else:
#             print("Введите да или нет")
#             continue
#     return work_next
# 
# async def main(daley_second: float):
#     task = asyncio.create_task(delay(daley_second))
#     try:
#         timer = await asyncio.wait_for(asyncio.shield(task), 5)
#         print("Задача была завершена за устоновленое время")
#     except TimeoutError:
#         result = await asyncio.to_thread(question)
#         try:
#             if result == True:
#                 print("Принято! Подождите ещё чуть-чуть, совсем скоро задача будет выполнена!")
#                 print(await task)
#             else:
#                 print("Задача снята!")
#                 task.cancel()
#         except asyncio.CancelledError:
#             print("Задача снята!")
# 
# asyncio.run(main(11.1))


# from asyncio import Future

# my_future = Future()

# print(f"Мой future готов? {my_future.done()}")

# my_future.set_result(42)

# print(f"Мой future готов? {my_future.done()}")

# print(f"Какой результат ххранится в my_future? {my_future.result()}")

# print(my_future)

# from asyncio import Future
# import asyncio
# 
# def make_request() -> Future:
#     future = Future()
#     asyncio.create_task(set_future_value(future))
#     return future
# 
# async def set_future_value(future):
#     await asyncio.sleep(1)
#     future.set_result(42)
# 
# async def main():
#     future = make_request()
#     print(f"Будующий обьект готов? {future.done()}")
#     value = await future
#     print(f"Будующий обьект готов? {future.done()}")
#     print(value)
# 
# asyncio.run(main())


# import  asyncio    
# import time
# async def main():   
#     start = time.time()
#     await asyncio.sleep(1)  
#     end = time.time() 
#     print(f"Сон занял {end-start}с") 
# asyncio.run(main())

# import functools
# # встроенный модуль functools используется для работы с функциями
# import time
# from typing import Callable, Any
# # встроенный модуль typing не меняет код, он используется для того чтобы тебе и редактору подсказывать типы данных
# 
# def async_timed():
#     def wrapper(func: Callable) -> Callable:
#         # Callable обозночает что объект является функцией
#         @functools.wraps(func)
#         # Декоратор @functools.wraps(), используется для того чтобы функция не потеряла свою идентичность, 
#         # ведь далее в процессе кода декораторы меняет имя функции на ту которая записана в дкораторе
#         # (внешне функция будет называтся так же, вызвать её можно через привычное имя, но для компьютера есть другое имя, 
#         # которое показывается если написать так: variable.__name__)
#         async def wrapped(*args, **kwargs) -> Any: # Any - обозночает что может вернутся любой тип данных
#             print(f'Выполняется {func}, с аргументами {args} {kwargs}')
#             start = time.time()
#             try:
#                 return await func(*args, **kwargs) # - возвращяем результат работы нашей функции, и-и-и... 
#                                                    # Дожидаемся её завершения с помощью await(это асинхроная функция)
#             finally: # - этот блок выполнится в любом случае, и писать "finally" можно только после блока try
#                 end = time.time()
#                 print(f'{func} завершилась за {end-start:.4f}c')
#         return wrapped
#     return wrapper
# 
# # кстати асинхроные функции можно создовать и без библеотеки "asyncio", ключевые слова async и await - это зарезирвированные слова самого пайтона
# 
# import asyncio
# 
# @async_timed()
# async def daley(delay_seconds: int) -> int:
#     print(f"засыпаю на {delay_seconds}")
#     await asyncio.sleep(delay_seconds)
#     print(f"сон в течении {delay_seconds}c закончился")
#     return delay_seconds
# 
# @async_timed()
# async def main():
#     task_one = asyncio.create_task(daley(2))
#     task_two = asyncio.create_task(daley(3))
# 
#     await task_one
#     await task_two
# 
# # декоратор нужно писать перед созданием функции 
# asyncio.run(main())

"""Проверим как однопоточная конкурентность будет себя вести с счетной операцией"""
# import asyncio
# from util import delay, async_timed
# 
# @async_timed()
# async def cpu_bound_work() -> int:
#     counter = 0
#     for i in range(1, 1_000_000):
#         counter += 1
#     return counter
# 
# @async_timed()
# async def main():
#     task_one = asyncio.create_task(cpu_bound_work())
#     task_two = asyncio.create_task(cpu_bound_work())
#     await task_one
#     await task_two
# 
# asyncio.run(main())


"""Проверим как однопоточная конкурентность будет себя вести с блокирюующим вводом-выводом"""
# import asyncio
# import requests
# from util import async_timed
# 
# @async_timed()
# async def get_example_status() -> int:
#     return requests.get('https://www.example.com').status_code
# 
# @async_timed()
# async def main():
#     task_1 = asyncio.create_task(get_example_status())
#     task_2 = asyncio.create_task(get_example_status())
#     task_3 = asyncio.create_task(get_example_status())
#     await task_1
#     await task_2
#     await task_3
# 
# asyncio.run(main()) # Асинхроность тут не роботает из-за синхроной и блокирующей библеотеки "requests"
# # вместо блокирующей библеотеки "requests", можно использовать "aiohttp"


# import asyncio
# from util import async_timed, delay
# 
# @async_timed()
# async def main():
#     task_1 = asyncio.create_task(delay(2))
#     task_2 = asyncio.create_task(delay(3))
#     await task_1
# 
# loop = asyncio.new_event_loop() # создаем цикл событий
# 
# try:
#     loop.run_until_complete(main()) # принимает програму и исполняет ее до завершения
# finally:
#     loop.close() # закончив работу с циклом событий, мы должны закрыть его.
# 
# import asyncio
# 
# def call_later():
#     print("Меня вызовут в ближайшем будущем!")
# 
# async def main():
#     loop = asyncio.get_running_loop()
#     loop.call_soon(call_later) # принмает функцию и выполняет её на следующей итерации цикла
#     await delay(1)
# 
# # существует также функция "asyncio.get_event_loop", также позволяющая позволяющая получить доступ к циклу событий, 
# # но эта функция может создать новый цикл событий если в момент ее вызова он ещё не был создан, что ведет к страному поведению
# # рекомендуется использовать run_until_complete, поскольку она возбуждает исключение, если цикл событий не был создан
# 
# asyncio.run(main())
"""loop = asyncio.get_running_loop():
   Эта команда позволяет тебе «внедриться» в текущий, запущенный прямо сейчас цикл событий (Event Loop) и получить к нему прямой доступ. 
   Теперь в переменной loop лежит пульт управления асинхронным движком.

   loop.call_soon(call_later):
   Метод call_soon переводится как «вызови при первой же возможности».
   Важное правило: Этот метод принимает только обычные (синхронные) функции. Сюда нельзя передать корутину.
   Что он делает: Он берет функцию call_later, идет к Event Loop и говорит: 
   «Слушай, не запускай её прямо сейчас, но запиши её в очередь. 
   Как только ты закончишь текущую микрозадачу и у тебя появится свободная микросекунда на следующей итерации — сразу же выполни её!».
   
   await delay(1):
   Программа доходит до этой строчки. await — это триггер для Event Loop. Функция main как бы говорит циклу событий: «Я засыпаю на 1 секунду, я освобождаю поток, иди займись другими делами»."""


# Можно использовать откладочный режим, чтобы узнать где произошла ошибка
# Способ №1: asyncio.run(cotoutine(), debug=True)
# Способ №2: (запускаем через терминал) python3 -X dev program.py
# Способ №3: (запускаем через терминал) PYTHONASYINCIODEBUG=1 python3 program.py

"""В отладочном режиме мы будем видеть информационные сообщения, если сопрограмма работает слишком долго."""

# проверим это с счетным кодом

# import asyncio
# from util import async_timed
# 
# @async_timed()
# async def cpu_bound_work() -> int:
#     counter = 1
#     for i in range(10_000_000):
#             counter += 1
#     return counter
# 
# async def main() -> None:
#       task_one = asyncio.create_task(cpu_bound_work())
#       await task_one
# 
# asyncio.run(main(), debug=True)
# Выводится сообщения о том что задача роботает слишко долго и перекрывает поток: Выполняется <function cpu_bound_work at 0x0000023EF9C10040>, 
# с аргументами () {}
# <function cpu_bound_work at 0x0000023EF9C10040> завершилась за 1.2551c
# Executing <Task finished name='Task-2' coro=<cpu_bound_work() done, defined at c:\Users\ANDREYHOME\Desktop\test_python_go\util\async_timer.py:10> 
# result=10000001 created at C:\Python313\Lib\asyncio\tasks.py:410> took 1.257 seconds

# import asyncio
# 
# async def main():
#       lopp = asyncio.get_running_loop() # получаем объект текущего цикла событий
#       lopp.slow_callback_duration = .250 # устанавливаем кол-во секунд после которых сробатывает дебаг и мы указываем милисекунды через точку
# 
# asyncio.run(main(), debug=True)

import asyncio
from util import delay, async_timed

async def main():
    await delay(1)
    print('Проверка')

@async_timed()
async def main_2():
    task = asyncio.create_task(delay(1))
    print('Проверка')
    await asyncio.sleep(2)
    await task

asyncio.run(main_2())