"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
import copy
from random import randint


# Вариант 1
def sort_by_selection1():
    arr = copy.deepcopy(input_list)
    N = len(arr)
    i = 0
    while i < N - 1:
        m = i
        j = i + 1
        while j < N:
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr


# Вариант 2
def find_smallest(arr):
    smalest = arr[0]
    smalest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smalest_idx = i
    return smalest_idx


def sort_by_selection2():
    arr = copy.deepcopy(input_list)
    new_arr = []
    for i in range(0, len(arr)):
        idx = find_smallest(arr)
        new_arr.append(arr.pop(idx))
    return new_arr


items = 100
input_list = [randint(0, 100) for i in range(items)]


print(sort_by_selection1())
print(sort_by_selection2())

number = 100
t1 = timeit.Timer("sort_by_selection1()", setup="from __main__ import sort_by_selection1")
print("sort_by_selection1() - ", t1.timeit(number=number), "milliseconds")
t2 = timeit.Timer("sort_by_selection2()", setup="from __main__ import sort_by_selection2")
print("sort_by_selection2() - ", t2.timeit(number=number), "milliseconds")

"""
Вариант 1
У нас есть один внешний цикл - его сложность О(n).
У нас есть вложенный цикл - его сложность О(n).
В итоге общая сложность алгоритма - О(n^2)

Вариант 2
В основной функции у нас есть цикл с максимальной сложностью О(n).
В вызываемой функции у нас есть цикл - у него сложность меняется от О(1) до О(n).
Соотвественно средняя сложность цикла - О(n/2).
В итоге общая сложность алгоритма - О(n*(n/2))

Как видно по результатам второй алгоритм действительно выполняется быстрее.
"""
