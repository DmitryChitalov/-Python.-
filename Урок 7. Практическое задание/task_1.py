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


import random
from timeit import timeit


def bubble_sort(orig_list):
    """ Сортировка методом пузырька по убыванию без оптимизации """
    n = 1
    count_operations = 0
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            count_operations += 1
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list, count_operations


def bubble_sort_opt(orig_list):
    """ Сортировка методом пузырька по убыванию c оптимизации """
    n = 1
    count_operations = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(orig_list) - n):
            count_operations += 1
            if orig_list[i] < orig_list[i + 1]:
                is_sorted = False
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list, count_operations


def checker(func):
    """ Функция для проверки алгоритмов """
    o_list = [random.randint(-100, 100) for _ in range(1000)]
    return func(o_list)


if __name__ == '__main__':
    ORIG_LIST = [random.randint(-100, 100) for _ in range(40)]
    ORIG_LIST2 = ORIG_LIST.copy()
    print('Исходный массив:', ORIG_LIST)
    RESULT = bubble_sort(ORIG_LIST)
    print(f'Без оптимизации массив был отсортирован за {RESULT[1]} итераций.')
    print(' Отсортированный массив:', RESULT[0])
    RESULT = bubble_sort_opt(ORIG_LIST2)
    print(
        f'После оптимизации массив был отсортирован за {RESULT[1]} итераций.')
    print(' Отсортированный массив:', RESULT[0])

    print('Замеры времени для обычного алгоритма:')
    print(
        timeit(
            'checker(bubble_sort)',
            setup="from __main__ import checker, bubble_sort",
            number=100))
    print('Замеры времени для оптимизированного алгоритма:')
    print(
        timeit(
            'checker(bubble_sort_opt)',
            setup="from __main__ import checker, bubble_sort_opt",
            number=100))
