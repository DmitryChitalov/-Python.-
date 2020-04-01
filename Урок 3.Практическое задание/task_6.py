"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

from random import randint


def func(res_array):
    print(f'Твой список: {res_array}')
    min_idx = 0
    max_idx = 0
    step = 1
    res = 0

    for i in res_array:
        if res_array[min_idx] > i:
            min_idx = res_array.index(i)
        elif res_array[max_idx] < 1:
            max_idx = res_array.index(i)

    if max_idx - min_idx < 0:
        step = -1

    for i in res_array[min_idx + step:max_idx:step]:
        res += i

    print(f'сумма элементов между минимальным элементом списка {res_array[min_idx]} \n'
          f'и максимальным {res_array[max_idx]} равна {res}')


USER_ARRAY = [randint(-100, 100) for i in range(15)]
func(USER_ARRAY)
