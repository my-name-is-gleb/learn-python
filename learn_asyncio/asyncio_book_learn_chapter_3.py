import selectors
import socket
from selectors import SelectorKey # SelectorKey — это специальный объект питона, в котором хранится всё про проснувшийся сокет.
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# метод setsockopt расшифровывается как: Установить опцию сокета
# параметр SOL_SOCKET, говорит ОС: Эта настройка не касается сетивых протаколов, а самого базового уровня нашего сокета
# параметр SO_REUSEADDR, просит ОС, повторно занять тот-же IP-адрес и порт
# циферка 1, говорит включить эту настройку, будь там 0 она бы не включилась

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False) # переводим сокет в неблокирующий режим
server_socket.bind(server_address) # привязываем адрес к нашемму сокету
server_socket.listen() # слушаем запросы на адрес от клиентов

print("Сервер запущен и ждет подключения на порту 8000...")

selector.register(server_socket, selectors.EVENT_READ) # регистрируем главный сокет, параметр EVENT_READ говорит: Если кто-то подключится, 
                                                       # это будет событие EVENT_READ (готово к чтению/приему), дай мне знать
# _system_variable = None
while True:
    # if _syste_variable == True:
    #     break
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1) # Если поставить timeout=1, ты говоришь селектору: «Жди данные. 
                                                                       # Но если в течение ровно 1 секунды абсолютно ничего не произошло — 
                                                                       # всё равно проснись, верни мне пустой список и дай коду идти дальше»
    # обозначаем переменную events в которой будет что-то типа: [(SelectorKey, int), (SelectorKey, int)...], и выстовляем тайм-аут 1сек.

    if len(events) == 0:
        print("\rСобытий нет, подожду ещё...", end="", flush=True) # \r возвращает курсор в начало строки, 
                                                                   # а end="" не дает переносить строку на новую, а flush=True, 
                                                                   # принудительно заставляет Python мгновенно выплюнуть текст в консоль, 
                                                                   # не придерживая его в своей внутренней памяти (буфере).

    for event, _ in events:
        # для регистрации мы передаем имя сокета и то что он будет делать и мы тут забираем это из списка
        event_socket = event.fileobj # передаем в переменную ссылку на сокет который забрал event
    
        if event_socket == server_socket:
            connection, address = server_socket.accept() # ждем запроса на подключение и этот метод: 
                                                                    # 2. возвращяет объект подключения и
                                                                    # адрес подключившегостя клиента;
            connection.setblocking(False) # переводим сокет в неблокирующий режим
            print(f"УРА! Подключение успешно: {address}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            
            # 1. СРАЗУ проверяем, не отключился ли клиент
            if not data:
                print("\n[INFO] Клиент отключился. Начинаем уборку...")
                selector.unregister(event_socket)  # Говорим селектору: "Больше не следи за ним"
                event_socket.close()               
                print("[INFO] Сокет успешно закрыт и удален из селектора.")
                # _system_variable = True
            
            # 2. Если данные ЕСТЬ, то только тогда логируем и отправляем эхо
            else:
                print(f"Получены данные {data}")
                event_socket.send(data)