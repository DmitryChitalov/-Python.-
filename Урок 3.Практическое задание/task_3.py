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

from random import random

quantity = 10
list = [0] * quantity

for i in range(quantity):
    list[i] = int(random() * 100)
    print(list[i], end= ' ')
print()

min_number = min(list)
max_number = max(list)
index_min = list.index(min_number)
index_max = list.index(max_number)

list[index_min],list[index_max] = list[index_max],list[index_min]

for i in range(10):
    print(list[i],end=' ')
print()