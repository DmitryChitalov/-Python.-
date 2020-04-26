"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from random import randint
from copy import deepcopy
from timeit import timeit


def bubble_sort_before(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        for j in range(0, n - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        n -= 1
    return arr


def bubble_sort_after(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        break_point = True
        for j in range(0, n - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                break_point = False
        if break_point:
            break
        n -= 1
    return arr


count = 100
input_arr = [randint(-100, 100) for el in range(count)]
number = 1000
print(f'Source array:\n{input_arr}\n')

values = ['before', 'after']
for i in range(2):
    print(f'Sorted array {values[i]} algorithm optimization:\n'
          f'{bubble_sort_before(deepcopy(input_arr))}')
    print(f'Algorithm sort time {values[i]} optimization with number = {number}:')
    print("\033[31m{}\033[0m".format('Please wait...'), end='')
    print('\r' + str(timeit(f"bubble_sort_{values[i]}(input_arr)",
                            setup=f"from __main__ import bubble_sort_{values[i]}, input_arr",
                            number=number)) + ' seconds\n')


"""
У обоих алгоритмов сложность О(n^2). Но для алгоритма без оптимизации это справедливо всегда (каждый раз алгоритм
проходит массив n^2 раз), а для алгоритма с оптимизацией это справедливо только худшем случае. Таким образом, в среднем
алгоритм с оптимизацией выполнятеся быстрее, что подтверждается результатами замеров.
"""
