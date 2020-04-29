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

import random

LIST_N = [random.randint(-100, 100) for i in range(10)]

print(f"Исходный массив: {LIST_N}")

INDEX_MIN, INDEX_MAX = 0, 0
NUMBER_MIN, NUMBER_MAX = LIST_N[INDEX_MIN], LIST_N[INDEX_MAX]

for i in range(1, len(LIST_N)):
    if LIST_N[i] < NUMBER_MIN:
        NUMBER_MIN = LIST_N[i]
        INDEX_MIN = i
    if LIST_N[i] > NUMBER_MAX:
        NUMBER_MAX = LIST_N[i]
        INDEX_MAX = i

LIST_N[INDEX_MIN], LIST_N[INDEX_MAX] = LIST_N[INDEX_MAX], LIST_N[INDEX_MIN]

print(f"      результат: {LIST_N}")
