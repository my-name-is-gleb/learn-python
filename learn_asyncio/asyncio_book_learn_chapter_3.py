"""Не работает на Windows"""
import socket
import asyncio
import logging
import signal # на Windows он не будет работать
from asyncio import AbstractEventLoop #— это большой системный чертеж, в котором разработчики Python прописали: 
                                      # «Каким именно обязан быть и какие методы должен иметь любой Цикл Событий (Event Loop) в экосистеме Python».

async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            """Конструкция data := ... (walrus operator) позволяет одновременно сделать две вещи:
               Выполнить команду справа и сохранить результат в переменную data.
               Сразу же проверить, что лежит в этой переменной. Если там есть данные, while считает это как True и запускает цикл. 
               Если там пустые байты (b''), while видит в этом False и цикл автоматически завершается."""
            if data == b"boom":
                raise Exception('Неожиданая ошибка сети')
            await loop.sock_sendall(connection, data) # забираем данные из клинтского сокета и с помощью await не закрываем эту строчку, 
                                                      # а замораживаем пока пользователь не нажмет Enter
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()

echo_tasks = []

async def listen_for_connections(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket) # ждем пока пользователь не подключится к нашему сокету
        connection.setblocking(False) # переводим клиентский сокет в неблокирующий
        print(f"Получен запрос на подключение от {address}")
        echo_task = asyncio.create_task(echo(connection, loop)) # переводим  всю прошлою конструкцию в фон чтобы дать пороботать другим клиентам
        echo_tasks.append(echo_task)

class GracefulExit(SystemExit):
    # создаем свой класс с ошибкой чтобы нашу ошибку(которую мы будем планировать) случайно не забрал другой блок try/except(даем новое имя)
    pass

def shotdown():
    """Функция add_signal_handler устроена так, что она принимает в качестве аргумента обычную (синхронную) функцию. 
       Ты не можешь передать ей напрямую ключевое слово raise, 
       потому что синтаксис Python не позволяет засунуть raise внутрь обычной переменной или сделать lambda: raise GracefulExit().
       Поэтому мы создаем маленькую функцию-обертку shotdown(). 
       Её единственная задача — лечь под танк: когда прилетит сигнал, она сработает и выбросит исключение GracefulExit наверх."""
    raise GracefulExit()

async def close_echo_tasks(echo_tasks: list[asyncio.Task]): # в аргументах echo_tasks который должен быть списком в котором будут наши задачи
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks] # в переменную waiters попадает список с результатами работы цикла
    """По другому это можно было бы написать так:
        waiters = []
        for task in echo_tasks:
            wrapped_task = asyncio.wait_for(task, 2) # Сохраняем обертку с таймером
            waiters.append(wrapped_task)             # Добавляем в список именно её"""
    try:
        for task in waiters:
            await task # ждем завершения 
    except asyncio.exceptions.TimeoutError:
        # Здесь мы ожидаем истечение тайм-аута
        pass

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address) # присваиваем адрес 
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shotdown)
    await listen_for_connections(server_socket, loop)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()