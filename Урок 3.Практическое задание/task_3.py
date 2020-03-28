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

ORIGIN_LIST = [random.randint(-100, 100) for i in range(5)]
MIN_INDEX = ORIGIN_LIST.index(min(ORIGIN_LIST))
MAX_INDEX = ORIGIN_LIST.index(max(ORIGIN_LIST))

print(f"{ORIGIN_LIST}\nВ данном массиве чисел максимальное число {max(ORIGIN_LIST)}"
      f" стоит на {ORIGIN_LIST.index(max(ORIGIN_LIST)) + 1} позиции,"
      f"\nа минимальное число {min(ORIGIN_LIST)} стоит на "
      f"{ORIGIN_LIST.index(min(ORIGIN_LIST)) + 1} позиции Заменяем их")


BUFFER = ORIGIN_LIST[MIN_INDEX]
ORIGIN_LIST[MIN_INDEX] = ORIGIN_LIST[MAX_INDEX]
ORIGIN_LIST[MAX_INDEX] = BUFFER


print(f"{ORIGIN_LIST}\nПосле замены максимального и минимального чисел местами,"
      f"\nмаксимальное число {max(ORIGIN_LIST)} стоит на "
      f"{ORIGIN_LIST.index(max(ORIGIN_LIST)) + 1} позиции,\nа "
      f"минимальное число {min(ORIGIN_LIST)} стоит на "
      f"{ORIGIN_LIST.index(min(ORIGIN_LIST)) + 1} позиции")
