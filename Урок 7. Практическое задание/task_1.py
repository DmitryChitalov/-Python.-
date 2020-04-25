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
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 10_000


def bubble_smart(array):
    """Bubble sort with optimization"""
    for i in range(len(array) - 1, 0, -1):
        swapped = False
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                swapped = True

        if not swapped:
            break
    return array


def bubble_simple(array):
    """Bubble sort without optimization"""
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array


NUMS = [randint(-100, 100) for _ in range(MAX_SIZE)]
print(NUMS)
print(bubble_smart(NUMS))


TIME1 = timeit(f'bubble_simple({NUMS})',
               setup='from __main__ import bubble_simple',
               number=NUMBER_EXECUTIONS)

TIME2 = timeit(f'bubble_smart({NUMS})',
               setup='from __main__ import bubble_smart',
               number=NUMBER_EXECUTIONS)

print("Simple", TIME1)
print("Smart", TIME2)
