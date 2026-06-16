import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# 1. Настройка цели
target = input("Введите IP адрес или домен (например, google.com): ")
start_port = int(input("Введите начальный порт: "))
end_port = int(input("Введите конечный порт: "))

try:
    # Превращаем имя (google.com) в IP (8.8.8.8)
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Ошибка: Не удалось распознать хост.")
    exit()

print("-" * 50)
print(f"Сканирование цели: {target_ip}")
print(f"Время начала: {datetime.now()}")
print("-" * 50)

# 2. Функция проверки одного порта
def scan_port(port):
    # AF_INET = IPv4, SOCK_STREAM = TCP протокол
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Ждем ответ не больше 0.5 сек (для скорости)
    
    # connect_ex возвращает 0, если порт открыт
    result = sock.connect_ex((target_ip, port))
    sock.close()
    
    if result == 0:
        return port, True
    return port, False

# 3. Многопоточный запуск
# max_workers=100 значит, что мы проверяем 100 портов одновременно
with ThreadPoolExecutor(max_workers=100) as executor:
    # Создаем список задач
    futures = [executor.submit(scan_port, port) for port in range(start_port, end_port + 1)]
    
    for future in futures:
        port, is_open = future.result()
        if is_open:
            print(f"[+] Порт {port} ОТКРЫТ")
        # Мы не печатаем закрытые порты, чтобы не засорять консоль

print("-" * 50)
print(f"Сканирование завершено в: {datetime.now()}")

