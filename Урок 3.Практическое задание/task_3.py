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

NUMBER_LIST = [randint(-100, 100) for i in range(randint(7, 14))]
print('Первоначальный массив', NUMBER_LIST)
MAX = 0
MIN = 0
for i, el in enumerate(NUMBER_LIST):
    if el > NUMBER_LIST[MAX]:
        MAX = i
    elif el < NUMBER_LIST[MIN]:
        MIN = i
NUMBER_LIST[MAX], NUMBER_LIST[MIN] = NUMBER_LIST[MIN], NUMBER_LIST[MAX]
print('Массив с заменой     ', NUMBER_LIST)
