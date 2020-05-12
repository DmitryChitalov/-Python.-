"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random
from statistics import median


def print_sorted_array(array):
    """
    Функция вывода на экран содержимого массива
    :param array: Массив
    :return:
    """
    array = sorted(array)
    tab = 0
    for i, element in enumerate(array, 1):
        if i == len(array) // 2 + 1:
            tab = i % 10
            print(f'\n\n{element}\n')
        else:
            print(f'{element} ', end='')
            if i % (10 + tab) + 1 == 0:
                print(f'')
    print(f'')
    return None


def print_array(array):
    """
    Функция вывода на экран содержимого массива по 10 элементов
    :param array: Массив
    :return:
    """
    for i, element in enumerate(array, 1):
        print(f'{element}  ', end='')
        if i % 10 == 0:
            print(f'')
    print(f'')
    return None


def partition(array, left_el, right_el):
    middle = array[(left_el + right_el) // 2]
    while left_el <= right_el:
        while array[left_el] < middle:
            left_el += 1
        while array[right_el] > middle:
            right_el -= 1
        if left_el <= right_el:
            array[left_el], array[right_el] = array[right_el], array[left_el]
            left_el += 1
            right_el -= 1
    return right_el


def find_median(array):
    """
    :param array:
    :return:
    """
    mid, left, right = len(array) // 2, 0, len(array) - 1
    while True:
        middle = partition(array, left, right)
        if middle == mid:
            result_median = array[middle]
            break
        elif mid < middle:
            right = middle
        else:
            left = middle + 1
    return result_median


M = 22
# Инициализация массива случайными целыми числами от -100 до 100
ARRAY = [random.randint(10, 99) for _ in range(2 * M + 1)]

# Вывод на экран исходного массива
print(f'=' * 100)
print(f'Исходный массив:\n')
# Вывод на экран содержимого массива по 10 элементов
print_array(ARRAY)
print(f'=' * 100)

print(f'*' * 100)
print(f'Результат встроенной функции:\nМедиана массива: {median(ARRAY)}')
print(f'Результат собственной функции:\nМедиана массива: {find_median(ARRAY)}')
print(f'*' * 100)

# Вывод на экран отсотртированного массива с выделенной медианой для наглядности
print(f'=' * 100)
print(f'\nОтсортированный массив:\n')
print_sorted_array(ARRAY)
print(f'=' * 100)
