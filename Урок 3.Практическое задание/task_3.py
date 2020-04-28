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

EXAMPLE = [random.randint(0, 100) for _ in range(20)]
print(EXAMPLE)


def replace_min_max(array):
    """ Replaces minimal and maximal items of array """
    min_i, max_i = 0, 0

    for i in range(len(array)):
        if array[i] < array[min_i]:
            min_i = i
        elif array[i] > max_i:
            max_i = i

    print(f'On index {min_i} is minimal element, {array[min_i]}')
    print(f'On index {max_i} is maximal element, {array[max_i]}')

    array[min_i], array[max_i] = array[max_i], array[min_i]

    return array


print(replace_min_max(EXAMPLE))
