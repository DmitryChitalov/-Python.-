import random
import timeit
from copy import deepcopy

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""


def bubble1(b):
    a = deepcopy(b)
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n += 1
    return a


def bubble2(b):
    a = deepcopy(b)
    n = 1
    while n < len(a):
        f = 0
        for i in range(len(a) - n):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                f += 1
        if f == 0:
            return a
        n += 1
    return a


new_list = [random.randint(-100, 99) for i in range(0, 300)]

print(timeit.timeit("bubble1(new_list)", setup="from __main__ import bubble1, new_list", number=1000))
print(timeit.timeit("bubble2(new_list)", setup="from __main__ import bubble2, new_list", number=1000))

print(new_list)
print(bubble1(new_list))
print(bubble2(new_list))
