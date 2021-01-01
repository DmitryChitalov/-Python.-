"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from random import randint
import timeit

src = [randint(1, 100) for i in range(1, 10000)]
queue = deque(src)


def insert_list(indx, val):
    src.insert(indx, val)

def insert_queue(indx, val):
    queue.insert(indx, val)

indx = 123
val = 9999
print(timeit.timeit("insert_list(indx, val)", setup="from __main__ import insert_list, indx, val", number=1000))
print(timeit.timeit("insert_queue(indx, val)", setup="from __main__ import insert_queue, indx, val", number=1000))
"""
0.006530399999999999
0.00037399999999999933
"""
# Вывод вставка в deque происходит быстрее

def get_from_list(indx):
    return src[indx]

def get_from_queue(indx):
    i = 0
    for val in queue:
        if i == indx:
            return val
        else:
            i += 1    


indx = 123
print(timeit.timeit("get_from_list(indx)", setup="from __main__ import get_from_list, indx", number=1000))
print(timeit.timeit("get_from_queue(indx)", setup="from __main__ import get_from_queue, indx", number=1000))

"""
8.289999999999687e-05
0.005491299999999998
"""
# поиск по индексу в list значительно быстрее
