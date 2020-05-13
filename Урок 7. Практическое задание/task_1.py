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
import timeit



def bubble_sort_original(orig_list):
    ''' простостая обратная сортировка'''
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


def list_checker(orig_list):
    """проверка массива на сортированность"""

    for i in range(len(orig_list)-1):
        if orig_list[i] < orig_list[i + 1]:
            return 1

    return 0


def bubble_sort_tuning(orig_list):
    ''' простостая обратная сортировка c проверкой массива'''
    n = 1
    k = list_checker(orig_list)

    if k == 0:
        return orig_list

    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list

# простой пузырек
orig_list =[random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_original(orig_list))

# пузырек c проверкой
orig_list =[random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_original(orig_list))

'''
прсто так ради интереса

timeit
со случайныйм списком(10)
простая             0.021763699999999997
усовершенсвованная  0.022410100000000002

со случайныйм списком(10)
простая             0.008350100000000003
усовершенсвованная  0.001541299999999999

Вывод: отсортированный массив всегда считмется быстрее чем не отсортированный.
-

'''