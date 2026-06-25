#file = open('example.txt')
#try:
#    lines = file.readlines()
#finally:
#    file.close() # - долгая запись
#
## Контекстные менеджеры:
#with open('example.txt') as file:
#    lines = file.readlines()
#    # он позволяет абстрагировать логику освобождения ресурса с помощью try/finally и сам закрывает файл при окончании работы
#    """но он не подходит для асинхроных задач потому что преднозначен только для работы с синхроным python-кодом
#       по этой причине в яхык было введено новое средство - 'асинхронные контекстныне менеджеры'
#       синтаксиз почти такой же, только вместо with нужно писать async with"""


# import asyncio
# import socket
# from types import TracebackType
# from typing import Optional, Type
# # Optional - это указатель для аннотации типов, который говорит: «В этой переменной может лежать указанный тип данных, А МОЖЕТ лежать просто None»
# """Пример:
#    age: Optional[int] = None  # Возраст может быть числом, а может быть не указан (None)
#    # Или в новом стиле Python 3.10+:
#    age: int | None = None"""
# 
# # Класс Type (в Python 3.9+ можно писать просто с маленькой буквы type)
# # используется, когда в переменную передается не объект (экземпляр) класса, а сам класс как чертеж.
# 
# # TracebackType — это встроенный тип самого Python, который описывает «след» ошибки. 
# # Это тот самый список строк, который выводится в консоль, когда программа падает (в каком файле, на какой строчке и в какой функции всё сломалось). 
# # Трейсбек — это сложный системный объект, 
# # и TracebackType нужен исключительно для того, чтобы подсказать редактору кода: «Сюда прилетит системный слепок ошибки».
# 
# """Если внутри блока with произойдет ошибка,
#    Python передаст в __exit__ полную информацию о ней: тип ошибки, саму ошибку и след (трейсбек), где она случилась."""
# 
# class ConnectedSocket:
#     def __init__(self, server_socket):
#         self._connection = None
#         self._server_socket = server_socket
# 
#     async def __aenter__(self): # эта сопрограмма вызывается при входе в блок with 
#         print('Вход в контекстный менеджер, ожидание подключения')
#         loop = asyncio.get_event_loop()
#         connection, address = await loop.sock_accept(self._server_socket)
#         self._connection = connection
#         print('Подключение установлено')
#         return self._connection
#     
#     async def __aexit__(self,
#                          exc_type: Optional[Type[BaseException]], 
#     # В переменной exc_type может лежать (Optional) сам класс/чертеж (Type) какой-нибудь ошибки, унаследованной от базовой ошибки Python 
#     # (BaseException). Ну, либо там будет None, если код выполнился без ошибок
#                          exc_val: Optional[BaseException],
#     # В переменной exc_val может лежать конкретный пойманный объект ошибки (BaseException) с текстом внутри, либо None, если всё прошло гладко
#                          exc_tb: Optional[TracebackType]):
#     # В переменной exc_tb может лежать системный слепок (TracebackType) со списком сломанных строчек кода, либо None
#         """self — сам объект контекстного менеджера.
#            exc_type — тип ошибки (Exception Type), если код внутри with упал.
#            exc_val — значение (объект) ошибки (Exception Value).
#            exc_tb — след ошибки (Traceback), то есть номера строчек, где всё бахнуло."""
#         print('Выход из контекстного менеджера')
#         self._connection.close()
#         print("Подключение закрыто")
# 
# async def main():
#     loop = asyncio.get_running_loop()
# 
#     server_socket = socket.socket()
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_address = ('127.0.0.1', 8000)
#     server_socket.setblocking(False)
#     server_socket.bind(server_address)
#     server_socket.listen()
# 
#     async with ConnectedSocket(server_socket) as connection:
#         """Пошагово строчку выше можно объяснить так:
#             Шаг 1: Создание объекта. Вызывается ConnectedSocket(server_socket). Срабатывает обычный __init__, создается экземпляр класса, 
#             в него сохраняется твой серверный сокет.
# 
#             Шаг 2: Вход под капот (__aenter__). Python видит async with перед объектом и тут же делает await твоей функции __aenter__().
# 
#             Шаг 3: Ожидание клиента. Внутри __aenter__ программа замирает на строчке await loop.sock_accept(...). 
#             Как только реальный клиент подключился, класс сохраняет его сокет в self._connection.
# 
#             Шаг 4: Магия переменной as connection. Метод __aenter__ делает return self._connection. 
#             То, что этот метод вернул, Python автоматически записывает в переменную, которая стоит после ключевого слова as (в твой connection).
# 
#             Шаг 5: Выполнение тела. Только теперь программа заходит внутрь блока with и выполняет твой код:
#             data = await loop.sock_recv(connection, 1024)."""
#         
# 
#         """Вижу async with -> Мгновенно и автоматически вызываю корутину __aenter__ у указанного класса."""
#         data = await loop.sock_recv(connection, 1024)
#         print(data)
#         """Код внутри блока with закончился (или упал с ошибкой) -> Мгновенно и автоматически вызываю корутину __aexit__."""
# 
# asyncio.run(main())


# import asyncio
# import aiohttp
# from aiohttp import ClientSession
# 
# async def fetch_status(session: ClientSession, url: str) -> int:
#     ten_millis = aiohttp.ClientTimeout(total=1) # всего сколько может работать сесия
#     async with session.get(url, timeout=ten_millis) as result: # обязательно передаем таймаут как аргумент в метод get
#         return result.status
# 
# async def main():
#     session_timeout = aiohttp.ClientTimeout(total=1, connect=.1) # total - сколько всего может работать сесия; connect - сколько времени дано на подключение
#     async with ClientSession(timeout=session_timeout) as session:
#         url = "https://www.examle.com"
#         status = await fetch_status(session, url)
#         print(f"Состояние для {url} было равно {status}")
# 
# asyncio.run(main())

# import asyncio
# from util import delay, async_timed
# 
# @async_timed()
# async def main():
#     delay_timed = [3,3,3]
#     [await asyncio.create_task(delay(seconds)) for seconds in delay_timed]
# 
# asyncio.run(main())
"""Код выше не работает корректно из=за того что как только мы создали задачу мы сразу же ее ждем с помощью await"""
"""Исправим!:"""

# import asyncio
# from util import async_timed, delay
# 
# @async_timed
# async def main():
#     delay_timed = [3,3,3]
#     tasks = [asyncio.create_task(delay(second)) for second in delay_timed] # только регистрируем
#     [await task for task in tasks] # теперь все три конкурентно ждем
# 
# asyncio.run(main())

# import asyncio 
# import aiohttp
# from aiohttp import ClientSession
# from util import async_timed, fetch_status
# 
# @async_timed()
# async def main():
#     async with ClientSession() as session:
#         urls = ["http://example.com", "python://example.com"]
#         tasks = [fetch_status(session, url) for url in urls] # в переменной лежит список корутин
#         status_code = await asyncio.gather(*tasks, return_exceptions=True) # * - нужна потомуу что gather не принимает список, 
#                                                       # а принимает только отдельные аргументы ват мы так и сделали
#         exceptions = [res for res in status_code if isinstance(res, Exception)]
#         """isinstance(res, Exception) — это встроенная функция проверки типов в Python. Она спрашивает: «Является ли объект res ошибкой (исключением)?»."""
#         successful_result = [res for res in status_code if not isinstance(res, Exception)]
# 
#         print(f"Все результаты: {status_code}")
#         print(f"Завершились успешно: {successful_result}")
#         print(f"Завершились не успешно: {exceptions}")
# 
# asyncio.run(main())


import asyncio 
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, "https://www.example.com", timed=3)),
                    asyncio.create_task(fetch_status(session, "https://www.exa")),
                    asyncio.create_task(fetch_status(session, "https://www.example.com", timed=3))]
        try:
            done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

            print(f"Число завершившихся задач: {len(done)}")
            print(f"Число ещё работающих задач: {len(pending)}")

            for tasks in pending:
                await tasks

            for done_task in done:
                # result = await done_task возбудет исключение
                if done_task.exception() is None:
                    print(done_task.result())
                else:
                    try:
                        await done_task
                    except:
                        print("Задача завершилась исключением")

        except Exception as ex:
            print(f"Произошла ошибка {ex}")
#         for finished_task in asyncio.as_completed(fetchers, timeout=2):
#             try:
#                 print(await finished_task) # мы ждем первый выполнившейся результат 
#             except asyncio.TimeoutError:
#                 print("Произошел тайм-аут")
# 
#         for task in asyncio.tasks.all_tasks():
#             print(task)

asyncio.run(main())