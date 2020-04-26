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


def sort_list_optimize(list_param):
    """
    Сортировка списка метод "пузырька" с оптимизацией
    :param list_param: список чисел
    :return: отсортированный список
    """

    length = len(list_param)
    for inx_1 in range(length):
        break_flag = True
        for inx_2 in range(inx_1 + 1, length):
            if list_param[inx_1] > list_param[inx_2]:
                break_flag = False
                list_param[inx_1], list_param[inx_2] = list_param[inx_2], list_param[inx_1]
        if break_flag:
            break

    return list_param


def sort_list(list_param):
    """
    Сортировка списка метод "пузырька"
    :param list_param: список чисел
    :return: отсортированный список
    """

    length = len(list_param)
    for inx_1 in range(length):
        for inx_2 in range(inx_1 + 1, length):
            if list_param[inx_1] > list_param[inx_2]:
                list_param[inx_1], list_param[inx_2] = list_param[inx_2], list_param[inx_1]

    return list_param


# Генерация списка
ARRAY_LEN = 30
ARRAY1 = [randint(-100, 99) for _ in range(ARRAY_LEN)]
ARRAY2 = ARRAY1.copy()

# Вывод на экран без опимизации
print("==Сортировка при помощи пузырька без оптимизации==")
print(
    f"""Исходный массив:       {ARRAY1}\nОтсортированный массив:{sort_list(ARRAY1)}""")
print(
    "Замер:",
    timeit(
        "sort_list(ARRAY1)",
        setup="from __main__ import sort_list, ARRAY1",
        number=1000))

# Вывод на экран c опимизации
print("==Сортировка при помощи пузырька с оптимизацией==")
print(
    f"""Исходный массив:       {ARRAY2}\nОтсортированный массив:{sort_list(ARRAY2)}""")
print(
    "Замер:",
    timeit(
        "sort_list_optimize(ARRAY2)",
        setup="from __main__ import sort_list_optimize, ARRAY2",
        number=1000))

"""
Сортировка работает намного быстрее, если мы прерываем цикл, когда список отсортирован
(не было не одной замене при полной проходе)

==Сортировка при помощи пузырька без оптимизации==
Исходный массив:       [-70, 21, 55, 4, -64, 88, -6, -48, -7, -31, -34, -4, 8, -88, -21, -66, 80, 6, -51, -56, 36, -44, -7, 11, 1, -55, 16, 16, 69, -48]
Отсортированный массив:[-88, -70, -66, -64, -56, -55, -51, -48, -48, -44, -34, -31, -21, -7, -7, -6, -4, 1, 4, 6, 8, 11, 16, 16, 21, 36, 55, 69, 80, 88]
Замер: 0.23757999999999999
==Сортировка при помощи пузырька с оптимизацией==
Исходный массив:       [-70, 21, 55, 4, -64, 88, -6, -48, -7, -31, -34, -4, 8, -88, -21, -66, 80, 6, -51, -56, 36, -44, -7, 11, 1, -55, 16, 16, 69, -48]
Отсортированный массив:[-88, -70, -66, -64, -56, -55, -51, -48, -48, -44, -34, -31, -21, -7, -7, -6, -4, 1, 4, 6, 8, 11, 16, 16, 21, 36, 55, 69, 80, 88]
Замер: 0.011198700000000006
"""
