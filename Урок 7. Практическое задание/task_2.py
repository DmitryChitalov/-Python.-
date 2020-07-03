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

element = int(input('Введите число элементов:'))
LST = [uniform(0, 50) for _ in range(element)]
LST1 = LST[:]
print(LST)

'''
Это первая версия. Ее я решил написать не заглядывая в ваш пример.
Она оказалась рабочая, но работала медленнее чем ваша.
Чем больше был массив, тем больше разница. При массиве
в 100 тыс она была уже в 3 раз, на 200 в 5, и дальше увеличивалась в разы
миллион было уже не дождаться.
Тогда я посмотрел вашу версию и перелелал часть своей.
Стала летать.

Возможно моя работала медленнее из-за того что использовал  extend и pop


'''


def merger_sort_1(lst):
    center = len(lst) // 2
    tmp = []
    left_list = lst[:center]
    right_list = lst[center:]
    if len(left_list) > 1:
        left_list = merger_sort_1(left_list)
    if len(right_list) > 1:
        right_list = merger_sort_1(right_list)

    while True:
        if len(left_list) == 0:
            tmp.extend(right_list)
            break
        elif len(right_list) == 0:
            tmp.extend(left_list)
            break
        if left_list[0] < right_list[0]:
            tmp.append(left_list.pop(0))
        else:
            tmp.append(right_list.pop(0))
    return tmp


def merger_sort_2(lst):
    center = len(lst) // 2
    left_list = lst[:center]
    right_list = lst[center:]
    if len(left_list) > 1:
        left_list = merger_sort_2(left_list)
    if len(right_list) > 1:
        right_list = merger_sort_2(right_list)

    i, j, k = 0, 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            lst[k] = left_list[i]
            i += 1
        else:
            lst[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        lst[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        lst[k] = right_list[j]
        j += 1
        k += 1
    return lst


print(timeit("merger_sort_1(LST1)", \
             setup="from __main__ import merger_sort_1, LST1", number=1))

print(merger_sort_1(LST1))

print(timeit("merger_sort_2(LST)", \
             setup="from __main__ import merger_sort_2, LST", number=1))

print(merger_sort_2(LST))
