"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
import timeit

max_number = 5

def sort(array):

    if len(array) < 2:
        return array


    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    left_part = sort(left_part)
    right_part = sort(right_part)

    return list(left_part, right_part)


def list(list_1, list_2):
    result = []
    x = 0
    y = 0
    while x < len(list_1) and y < len(list_2):
        if list_1[x] <= list_2[y]:
            result.append(list_1[x])
            x += 1
        else:
            result.append(list_2[y])
            y += 1

    result += list_1[x:]
    result += list_2[y:]
    return result


numbers = [random.uniform(0, 50) for _ in range(max_number)]

print('Исходный список :', numbers)
print('Отсортированный :', (sort(numbers)))


