import functools
# встроенный модуль functools используется для работы с функциями
import time
from typing import Callable, Any
# встроенный модуль typing не меняет код, он используется для того чтобы тебе и редактору подсказывать типы данных

def async_timed():
    def wrapper(func: Callable) -> Callable:
        # Callable обозночает что объект является функцией
        @functools.wraps(func)
        # Декоратор @functools.wraps(), используется для того чтобы функция не потеряла свою идентичность, 
        # ведь далее в процессе кода декораторы меняет имя функции на ту которая записана в дкораторе
        # (внешне функция будет называтся так же, вызвать её можно через привычное имя, но для компьютера есть другое имя, 
        # которое показывается если написать так: variable.__name__)
        async def wrapped(*args, **kwargs) -> Any: # Any - обозночает что может вернутся любой тип данных
            print(f'Выполняется {func}, с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs) # - возвращяем результат работы нашей функции, и-и-и... 
                                                   # Дожидаемся её завершения с помощью await(это асинхроная функция)
            finally: # - этот блок выполнится в любом случае, и писать "finally" можно только после блока try
                end = time.time()
                print(f'{func} завершилась за {end-start:.4f}c')
        return wrapped
    return wrapper