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

import timeit
import random


def bubble_sort(lst):
    """Сортировка пузырьком без оптимизации по убыванию"""
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def bubble_sort_2(lst):
    """Сортировка пузырьком с оптимизацией по убыванию"""
    flag = True
    while flag:
        flag = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = True
    return lst


arr = [random.randint(-100, 100) for _ in range(10)]

# замеры на 10
print(timeit.timeit("bubble_sort(arr)",
                    setup="from __main__ import bubble_sort, arr", number=1000))
print(timeit.timeit("bubble_sort_2(arr)",
                    setup="from __main__ import bubble_sort_2, arr", number=1000))

arr = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(arr)",
                    setup="from __main__ import bubble_sort, arr", number=1000))
print(timeit.timeit("bubble_sort_2(arr)",
                    setup="from __main__ import bubble_sort_2, arr", number=1000))

arr = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(arr)",
                    setup="from __main__ import bubble_sort, arr", number=1000))
print(timeit.timeit("bubble_sort_2(arr)",
                    setup="from __main__ import bubble_sort_2, arr", number=1000))
