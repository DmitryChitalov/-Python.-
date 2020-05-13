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

from timeit import timeit
from random import randint


def bubble_sort_reverse(lst):
    """
    Сортировка массива пузырьком
    :param lst: массив для сортировки
    :return: отсортированный массив
    """
    num = 1
    while num < len(lst):
        for i in range(len(lst)-num):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        num += 1
    return lst


def bubble_sort_reverse_next(lst):
    """
    Сортировка массива пузырьком - улучшенная версия
    :param lst: массив для сортировки
    :return: отсортированный массив
    """
    num = 1
    while num < len(lst):
        l_ok = True  # флаг что массив отсортирован
        for i in range(len(lst)-num):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                l_ok = False  # флаг что массив отсортирован
        if l_ok:
            break
        num += 1
    return lst


# замеры 10
ORIG_LIST_10 = [randint(-100, 100) for _ in range(10)]
ORIG_LIST_10_COPY = ORIG_LIST_10[:]  # Копируем массив
print("Замер для 10 вариант 1:",
      timeit("bubble_sort_reverse(ORIG_LIST_10)",
             setup="from __main__ import bubble_sort_reverse, ORIG_LIST_10",
             number=1000))
print("Замер для 10 вариант 2:",
      timeit("bubble_sort_reverse_next(ORIG_LIST_10_COPY)",
             setup="from __main__ import bubble_sort_reverse_next, ORIG_LIST_10_COPY",
             number=1000))


# замеры 100
ORIG_LIST_100 = [randint(-100, 100) for _ in range(100)]
ORIG_LIST_100_COPY = ORIG_LIST_100[:]  # Копируем массив
print('Исходный массив:', ORIG_LIST_100)
print("Замер для 100 вариант 1:",
      timeit("bubble_sort_reverse(ORIG_LIST_100)",
             setup="from __main__ import bubble_sort_reverse, ORIG_LIST_100",
             number=1000))
print("Замер для 100 вариант 2:",
      timeit("bubble_sort_reverse_next(ORIG_LIST_100_COPY)",
             setup="from __main__ import bubble_sort_reverse_next, ORIG_LIST_100_COPY",
             number=1000))
print('Отсортированный массив 1:', ORIG_LIST_100)
print('Отсортированный массив 2:', ORIG_LIST_100_COPY)


# замеры 1000
ORIG_LIST_1000 = [randint(-100, 100) for _ in range(1000)]
ORIG_LIST_1000_COPY = ORIG_LIST_1000[:]  # Копируем массив
print("Замер для 1000 вариант 1:",
      timeit("bubble_sort_reverse(ORIG_LIST_1000)",
             setup="from __main__ import bubble_sort_reverse, ORIG_LIST_1000",
             number=1000))
print("Замер для 1000 вариант 2:",
      timeit("bubble_sort_reverse_next(ORIG_LIST_1000_COPY)",
             setup="from __main__ import bubble_sort_reverse_next, ORIG_LIST_1000_COPY",
             number=1000))


# Результаты замеров
# Замер для 10 вариант 1: 0.021842100000000003
# Замер для 10 вариант 2: 0.002727400000000005
# Исходный массив: [-41, 95, -8, -57, 11, 69, 98, -84, 23, 82, 72, 61, -30, 52, 31, ...
# Замер для 100 вариант 1: 1.0206942
# Замер для 100 вариант 2: 0.02080039999999994
# Отсортированный массив 1: [99, 98, 95, 93, 93, 87, 87, 87, 86, 85, 84, 82, 73, 72, ...
# Отсортированный массив 2: [99, 98, 95, 93, 93, 87, 87, 87, 86, 85, 84, 82, 73, 72, ...
# Замер для 1000 вариант 1: 114.47807370000001
# Замер для 1000 вариант 2: 0.48358840000000214
# Вывод: при незначительном увеличении сложности алгоритма (исключили лишние проходы)
# удалось заметно выиграть в скорости выполнения
