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

ARRAY1 = [int(200 * random() - 100) for i in range(10)]
#ARRAY1 = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
print(ARRAY1)

MIN_ELEM = [ARRAY1[0], 0]
MAX_ELEM = [ARRAY1[0], 0]

for i in range(1, len(ARRAY1)):
    if ARRAY1[i] > MAX_ELEM[0]:
        MAX_ELEM[0] = ARRAY1[i]
        MAX_ELEM[1] = i
    elif ARRAY1[i] < MIN_ELEM[0]:
        MIN_ELEM[0] = ARRAY1[i]
        MIN_ELEM[1] = i
    else:
        continue

#print(MIN_ELEM, MAX_ELEM)
ARRAY1[MAX_ELEM[1]], ARRAY1[MIN_ELEM[1]] = MIN_ELEM[0], MAX_ELEM[0]
print(ARRAY1)
