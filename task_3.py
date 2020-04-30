"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
from random import randint


def task_three():

    a = [randint(-100, 100) for el in range(randint(1, 15))]
    print(a)
    min_el = min(a)
    min_in = a.index(min_el)
    max_el = max(a)
    max_in = a.index(max_el)
    a.remove(min_el)
    a.remove(max_el)
    a.insert(max_in, min_el)
    a.insert(min_in, max_el)
    print(a)


task_three()
