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

MASSIVE = [randint(-100, 100) for el in range(randint(0, 20))]

if len(MASSIVE) > 1:
    MAX_INDEX = MASSIVE.index(max(MASSIVE))
    MIN_INDEX = MASSIVE.index(min(MASSIVE))

    print(
        f"В данном массиве чисел максимальное число {MASSIVE[MAX_INDEX]} стоит на {MAX_INDEX + 1}"
        f" позиции, а минимальное число {MASSIVE[MIN_INDEX]} стоит на {MIN_INDEX + 1} позиции "
        f"\nЗаменяем их\n", MASSIVE)

    MASSIVE[MAX_INDEX], MASSIVE[MIN_INDEX] = MASSIVE[MIN_INDEX], MASSIVE[MAX_INDEX]
    print(
        f"В данном массиве чисел максимальное число {MASSIVE[MAX_INDEX]} стоит на {MAX_INDEX + 1} "
        f"позиции, а минимальное число {MASSIVE[MIN_INDEX]} стоит на {MIN_INDEX + 1} позиции\n",
        MASSIVE)
elif len(MASSIVE) == 1:
    print(f"В данном массиве всего 1 элемент: {MASSIVE}")
else:
    print(f"Данный массив пустой \n {MASSIVE}")
