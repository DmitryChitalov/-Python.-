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


def get_arr_sum(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    return array[0] + get_arr_sum(array[1:])


def create_array(arr_length):
    array = [randint(-99, 99) for i in range(arr_length)]
    return array


def get_min_index(array):
    min_el = array[0]
    index = 0
    for n, el in enumerate(array[1:], 1):
        if el < min_el:
            min_el = el
            index = n
    return index


def get_max_index(array):
    max_el = array[0]
    index = 0
    for n, el in enumerate(array[1:], 1):
        if el > max_el:
            max_el = el
            index = n
    return index


def get_sum_between(array, from_, to_):
    if from_ > to_:
        from_, to_ = to_, from_
    sum_ = get_arr_sum(array[from_+1:to_])
    return sum_


if __name__ == '__main__':
    # arr = create_array(int(input("Введите количество элементов в массиве: ")))
    arr = create_array(10)
    min_index = get_min_index(arr)
    max_index = get_max_index(arr)
    numbers_sum = get_sum_between(arr, min_index, max_index)
    print(f"array: {arr}",
          f"Sum of numbers between {min_index} and {max_index} indexes equals => {numbers_sum}",
          sep="\n")

# output:
# array: [11, -38, -44, -9, 4, -16, 30, -46, -66, 14]
# Sum of numbers between 8 and 6 indexes equals => -46
