"""Приложения из листингов 3 главы до 3.7 листинга"""

import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# параметр AF_INET говорит о том что адрес будет содержать в себе имя хоста и номер порта
# параметр SOCK_STREAM говорит о том что для взаимодействия приложение будет использовать протакол TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# метод setsockopt расшифровывается как: Установить опцию сокета
# параметр SOL_SOCKET, говорит ОС: Эта настройка не касается сетивых протаколов, а самого базового уровня нашего сокета
# параметр SO_REUSEADDR, просит ОС, повторно занять тот-же IP-адрес и порт
# циферка 1, говорит включить эту настройку, будь там 0 она бы не включилась
server_socket.setblocking(False) # переводим сокет в неблокирующий режим

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address) # привязываем адрес к нашемму сокету
server_socket.listen() # слушаем запросы на адрес от клиентов

connections = []

print("Сервер запущен и ждет подключения на порту 8000...")

try:
    while True:
        try:
            connection, client_address = server_socket.accept() # ждем запроса на подключение и этот метод: 
                                                                # 1. блокиреут програму до подключения; 2. возвращяет объект подключения и
                                                                # адрес подключившегостя клиента;
            connection.setblocking(False) # переводим сокет в неблокирующий режим
            print(f"УРА! Подключение успешно: {client_address}")
            connections.append(connection)
        except BlockingIOError:
            time.sleep(1)

        for connection in connections:
            try:
                buffer = b'' # b перед строкой говорит о том что в ней будут байты 

                while buffer[-2:] != b'\r\n': # пока пользователь не нажмет Enter(в telnet и PuTTY) при энтере выбрасываются типо такие символы: b'\r\n'
                    data = connection.recv(2) # забирает 2 байта данных
                    if not data: # если нету данных (чтобы не привротить в бескончный цикл)
                        break
                    else:
                        print(f"Данные получены {data}")
                        buffer += data
                print(f"Все данные: {buffer}")
                connection.sendall(buffer) # отправляем клиенту то же сообщение
            except BlockingIOError:
                time.sleep(1)
finally:
    server_socket.close() # закрываем сокет
