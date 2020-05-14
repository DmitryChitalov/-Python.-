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
from memory_profiler import profile
import timeit


def merge_sort(array):
    if len(array) <= 1:
        return array

    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


mass = [round(random.randint(1, 50, ), 2) for _ in range(10)]
print(f'Изначальный массив: {mass}')
merge_sort(mass)
print(f'Отсортированный массив: {mass}')
print(timeit.timeit("merge_sort(mass)", setup="from __main__ import merge_sort, mass", number=1000))


# 0.010421800000000002 время выполнения работы (без учета профайлера)