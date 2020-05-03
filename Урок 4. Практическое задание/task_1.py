"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit


def recur_method(numb=254735468768687686872, even=0, odd=0):
    if numb == 0:
        return even, odd
    else:
        cur_n = numb % 10
        numb = numb // 10
        if cur_n % 2 == 0:
            even += 1
            return recur_method(numb, even, odd)
        else:
            odd += 1
            return recur_method(numb, even, odd)


def cycle_method(numb=254735468768687686872):
    evens = 0
    odds = 0
    while numb != 0:
        cur_n = numb % 10
        numb = numb // 10
        if cur_n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds


print(timeit.timeit("recur_method()", setup="from __main__ import recur_method", number=10000))
print(timeit.timeit("cycle_method()", setup="from __main__ import cycle_method", number=10000))

"""
Результаты замеров: рекурсия - 0,175 сек.
                    цикл - 0,136 сек.

В данном случае цикл оказался производительнее рекурсии, т.к. при рработе функции с рекурсией стек вызовов разрастается
и его необходимо просматривать для получения конечного ответа. 
"""

import timeit
from random import random


def myArr():
    N = 14
    arr = []
    for i in range(N):
        arr.append(int(random() * 100))

    indexMin = arr.index(min(arr))
    indexMax = arr.index(max(arr))
    minMy = min(arr)
    maxMy = max(arr)

    arr[indexMin] = maxMy
    arr[indexMax] = minMy
    return arr


def myArr2():
    N = 14
    arr = []
    for i in range(N):
        arr.append(int(random() * 100))
    arr.sort()

    minMy = arr[0]
    maxMy = arr[-1]

    arr[0] = maxMy
    arr[-1] = minMy
    return arr


print(timeit.timeit(myArr))
print(timeit.timeit(myArr2))

"""
Результаты замеров - без функции sort: 12,199 сек., с sort - 9, 660 сек. Результат обусловлен тем, что для поиска минимального
и максимального элемента не нужно пробегать по всему массиву, так как в отсортированном массиве минимальный элемент на первой позиции
масимальный - на последней.
"""

import cProfile


# Вариант со словарём ------------------------------------------
def seasons_dictionary():
    season = int(input("Enter the month number - "))
    for i in range(len(seasons_dict)):
        if season == i + 1:
            if 3 <= season <= 5:
                return (f"This is Spring, month - {seasons_dict.get(i + 1)}")
            elif 6 <= season <= 8:
                return (f"This is Summer, month - {seasons_dict.get(i + 1)}")
            elif 9 <= season <= 11:
                return (f"This is Autumn, month - {seasons_dict.get(i + 1)}")
            else:
                print(f"This is Winter, month - {seasons_dict.get(i + 1)}")


seasons_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"}


# Вариант со списком --------------------------------------------
def seasons_l():
    season = int(input("Enter the month number - "))
    for i in range(len(seasons_list)):
        if season == i + 1:
            if 3 <= season <= 5:
                return (f"This is Spring, month - {seasons_list[i]}")
            elif 6 <= season <= 8:
                return (f"This is Summer, month - {seasons_list[i]}")
            elif 9 <= season <= 11:
                return (f"This is Autumn, month - {seasons_list[i]}")
            else:
                return (f"This is Winter, month - {seasons_list[i]}")


seasons_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]


def main():
    res_dictionary = seasons_dictionary()
    res_l = seasons_l()


cProfile.run('main()')

"""
Результаты замеров: вариант со списком - 0,777 сек:
                    вариант со словарем - 2,163 сек.
Обосновать не могу, потому что практически все операции в коде в варианте со словарем
имеют сложность константную, а в списке - линейную и словарь должнен работать быстрее,
но на деле почему-то наоборот оказалось.
"""