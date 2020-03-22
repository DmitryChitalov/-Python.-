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


def my_sum_slice(array):
    max_int_index = array.index(max(array))
    min_int_index = array.index(min(array))
    if max_int_index > min_int_index:
        return sum(array[min_int_index + 1:max_int_index]), array[max_int_index], array[min_int_index]
    return sum(array[max_int_index + 1:min_int_index]), array[max_int_index], array[min_int_index]


while True:
    try:
        LIST_SIZE = int(input(f'Введите количество элементов в массиве: '))
        MY_LIST = [randint(-100, 100) for i in range(LIST_SIZE)]
        SUM, MAX, MIN = my_sum_slice(MY_LIST)
        print(f'Массив: {MY_LIST}\nСумма элементов между минимальным ({MIN})  и максимальным ({MAX}) '
              f'элементами: {SUM}')
        break
    except ValueError:
        print(f'Ошибка ввода!')
