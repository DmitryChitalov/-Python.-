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

START_RANGE = -300
END_RANGE = 300
SIZE_RANGE = 10

MY_LIST = [random.randint(START_RANGE, END_RANGE) for _ in range(SIZE_RANGE)]
print(MY_LIST)

ELEM_MIN = 0
ELEM_MAX = 0

for i in range(len(MY_LIST)):
    if MY_LIST[i] < MY_LIST[ELEM_MIN]:
        ELEM_MIN = i
    elif MY_LIST[i] > MY_LIST[ELEM_MAX]:
        ELEM_MAX = i

MY_LIST[ELEM_MIN], MY_LIST[ELEM_MAX] = MY_LIST[ELEM_MAX], MY_LIST[ELEM_MIN]

print(MY_LIST)
