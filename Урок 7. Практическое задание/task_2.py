"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
from random import random
from random import randint
from timeit import timeit

# import sys
# sys.setrecursionlimit(100000)


def create_list_int(list_len, l_border, r_border):
    return [randint(l_border, r_border - 1) for _ in range(list_len)]


def create_list_float(list_len, l_border, r_border):
    return [randint(l_border, r_border - 1) + random() for _ in range(list_len)]

# Читабельный вариант
def merge_sort2(list1, list2):
    tmp = []
    while len(list1) > 0:
        while len(list2) > 0 and list2[0] <= list1[0]:
            tmp.append(list2.pop(0))
        tmp.append(list1.pop(0))
    return tmp + list2


def merge_sort(base_list):
    if len(base_list) > 2:
        half = len(base_list) // 2
        return merge_sort2(merge_sort(base_list[:half]), merge_sort(base_list[half:]))
    else:
        if len(base_list) == 1:
            return base_list
        else:
            return base_list if base_list[0] < base_list[1] else base_list[::-1]

# НЕЕЕЕЕЕЕЕчитабельный вариант!
def merge_sort_opt2(list1, list2, tmp=[]):
    while len(list1) > 0:
        while len(list2) > 0 and list2[0] <= list1[0]:
            tmp.append(list2.pop(0))
        tmp.append(list1.pop(0))
    return tmp + list2

def merge_sort_opt(base_list):
    return merge_sort_opt2(merge_sort(base_list[:len(base_list) // 2]), merge_sort(base_list[len(base_list) // 2:])) \
        if len(base_list) > 2 else base_list if len(base_list) == 1 else base_list \
        if base_list[0] < base_list[1] else base_list[::-1]


a = create_list_float(8, 0, 50)
print(a)
print(merge_sort(a))
print(merge_sort_opt(a))
print('Обычный: ', timeit('merge_sort(create_list_float(10000, 0, 10))', 'from __main__ import merge_sort, merge_sort2, create_list_float', number=100))
print('Оптимизиров: ', timeit('merge_sort_opt(create_list_float(10000, 0, 10))', 'from __main__ import merge_sort_opt, merge_sort_opt2, create_list_float', number=100))
"""
[24.060749050634755, 5.569825488205687, 12.099656999933002, 25.489810820912094, 26.71010855578925, 20.318494463628316, 1.8343820847442003, 33.16803571517379]
[1.8343820847442003, 5.569825488205687, 12.099656999933002, 20.318494463628316, 24.060749050634755, 25.489810820912094, 26.71010855578925, 33.16803571517379]
[1.8343820847442003, 5.569825488205687, 12.099656999933002, 20.318494463628316, 24.060749050634755, 25.489810820912094, 26.71010855578925, 33.16803571517379]
Обычный:  0.30818897799326805
Оптимизиров:  0.35243779300071765

#Вывод: вроде бы более лаконичная запись, а привела к перерасходу ресурсов. Вот как бывает при "неправильной" оптимизации
# причем на более длинных массивах разница увеличивается
# Если длинна массива = 1000
# Обычный:  4.47612431399466
# Оптимизиров:  5.975955189001979
"""






"""
b = [1, 3, 8]
c = [1, 2, 7, 9]
print(b)
print(c)
print(merge_sort2(b, c))
b = [1, 3, 8]
c = [1, 2, 7, 9]
print(merge_sort_opt2(b, c))
print('-----------------------------------------')
"""