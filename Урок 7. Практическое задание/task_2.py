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
from timeit import timeit

SIZE = int(input("Введите число элементов: "))
array = [random.uniform(0, 50) for i in range(SIZE)]
print(array)


def fun(a):
    if len(a) < 2:
        return a
    left = fun(a[:len(a) // 2])
    right = fun(a[len(a) // 2:len(a)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1
    return a


print(fun(array))
time1 = timeit(f'fun({array})',
              setup='from __main__ import fun',
              number=50)
print(time1)
"""Время - 0.00030460000000021026"""