"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
from timeit import timeit


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        arr1 = merge_sort(arr[:middle])
        arr2 = merge_sort(arr[middle:])
        new_arr = merge(arr1, arr2)
        return new_arr


def merge(arr1, arr2):
    arr = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            arr.append(arr1.pop(0))
        else:
            arr.append(arr2.pop(0))
    for i in arr1:
        arr.append(i)
    for i in arr2:
        arr.append(i)
    return arr


try:
    count = int(input('Enter the count of numbers - '))
    input_arr = [uniform(0, 50) for el in range(count)]
    print(f'Source array:\n'
          f'{input_arr}\n')
    print('Sorted array:\n'
          f'{merge_sort(input_arr)}\n')
    number = int(input('Enter the number of algorithm calculations to estimate time - '))
    print(f'Algorithm sort time with number of calculations = {number}:')
    print("\033[31m{}\033[0m".format('Please wait...'), end='')
    print('\r' + str(timeit(f"merge_sort(input_arr)",
                            setup=f"from __main__ import merge_sort, input_arr",
                            number=number)) + ' seconds\n')
except ValueError as err:
    print(f'Error: Invalid number.\n{err}')
