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
MAX_EL_INDEX = 0
MIN_EL_INDEX = 0
EXAMPLE = []

for i in range(0, 10):
    EL = randint(-100, 100)
    EXAMPLE.append(EL)
    if EL > EXAMPLE[MAX_EL_INDEX]:
        MAX_EL_INDEX = i
    if EL < EXAMPLE[MIN_EL_INDEX]:
        MIN_EL_INDEX = i

print(
    f"В данном массиве чисел максимальное число {EXAMPLE[MAX_EL_INDEX]} стоит на {MAX_EL_INDEX} позиции,\n"
    f"а минимальное число {EXAMPLE[MIN_EL_INDEX]} стоит на {MIN_EL_INDEX} позиции\nЗаменяем их\n{EXAMPLE}")

EXAMPLE[MAX_EL_INDEX], EXAMPLE[MIN_EL_INDEX] = EXAMPLE[MIN_EL_INDEX], EXAMPLE[MAX_EL_INDEX]
MAX_EL_INDEX, MIN_EL_INDEX = MIN_EL_INDEX, MAX_EL_INDEX

print(
    f"В данном массиве чисел максимальное число {EXAMPLE[MAX_EL_INDEX]} стоит на {MAX_EL_INDEX} позиции,\n"
    f"а минимальное число {EXAMPLE[MIN_EL_INDEX]} стоит на {MIN_EL_INDEX} позиции\n{EXAMPLE}")
