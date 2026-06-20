import socket
import asyncio
import logging
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


task = []

async def listen_for_connections(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket) # ждем пока пользователь не подключится к нашему сокету
        connection.setblocking(False) # переводим клиентский сокет в неблокирующий
        print(f"Получен запрос на подключение от {address}")
        task.append(asyncio.create_task(echo(connection, loop))) # переводим  всю прошлою конструкцию в фон чтобы дать пороботать другим клиентам

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address) # присваиваем адрес 
    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())