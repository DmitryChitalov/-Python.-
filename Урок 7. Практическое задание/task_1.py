"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import timeit


def my_bubble_first(is_list):
    """Классическая реализация"""
    n = 1
    while n < len(is_list):
        for i in range(len(is_list) - 1):
            if is_list[i] < is_list[i + 1]:
                is_list[i], is_list[i + 1] = is_list[i + 1], is_list[i]
        n += 1
    return is_list


def my_bubble_second(is_list):
    """Доработанная  реализация"""
    flag = True
    while flag:
        flag = False
        for i in range(len(is_list) - 1):
            if is_list[i] < is_list[i + 1]:
                is_list[i], is_list[i + 1] = is_list[i + 1], is_list[i]
                flag = True
    return is_list


arr = [randint(-100, 100) for _ in range(10)]
arr_2 = arr[:]
# замеры 10
print(
    f'Исходный массив: {arr}\n'
    f'Отсортированный массив 1 способ: {my_bubble_first(arr_2)}\n'
    f'Отсортированный массив 2 способ: {my_bubble_second(arr_2)}\n'
    f'Классическая реализация для 10: '
    f'{timeit("my_bubble_first(arr_2)", setup="from __main__ import my_bubble_first, arr_2", number=1000)}\n'
    f'Доработанная  реализация для 10: '
    f'{timeit("my_bubble_second(arr_2)", setup="from __main__ import my_bubble_second, arr_2", number=1000)}')
print()
arr = [randint(-100, 100) for _ in range(100)]
arr_2 = arr[:]
# замеры 100
print(
    f'Исходный массив: {arr}\n'
    f'Отсортированный массив 1 способ: {my_bubble_first(arr_2)}\n'
    f'Отсортированный массив 2 способ: {my_bubble_second(arr_2)}\n'
    f'Классическая реализация для 100: '
    f'{timeit("my_bubble_first(arr_2)", setup="from __main__ import my_bubble_first, arr_2", number=1000)}\n'
    f'Доработанная  реализация для 100: '
    f'{timeit("my_bubble_second(arr_2)", setup="from __main__ import my_bubble_second, arr_2", number=1000)}')
print()
arr = [randint(-100, 100) for _ in range(1000)]
arr_2 = arr[:]
# замеры 1000
print(
    f'Исходный массив: {arr}\n'
    f'Отсортированный массив 1 способ: {my_bubble_first(arr_2)}\n'
    f'Отсортированный массив 2 способ: {my_bubble_second(arr_2)}\n'
    f'Классическая реализация для 1000: '
    f'{timeit("my_bubble_first(arr_2)", setup="from __main__ import my_bubble_first, arr_2", number=1000)}\n'
    f'Доработанная  реализация для 1000: '
    f'{timeit("my_bubble_second(arr_2)", setup="from __main__ import my_bubble_second, arr_2", number=1000)}')
print()
'''
Оптимизация алгоритма с помощью дополнительной переменной flag помогла сократить
время выполнения для массива из 1000 элементов с 108 сек до 0,08 сек, а для
100 элементов с 1,25 сек до 0,007 сек.
'''
