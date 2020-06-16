"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

from random import randint


def create_array(arr_length):
    array = [randint(-99, 99) for i in range(arr_length)]
    return array


def find_2_min_nums(arr):
    min_1, min_2 = arr[0], arr[0]
    min_index = None
    for n, el in enumerate(arr[1:], 1):
        if el < min_1:
            min_1 = el
            min_index = n
    for n, el in enumerate(arr[1:], 1):
        if el < min_2 and n != min_index:
            min_2 = el

    return min_1, min_2


array = create_array(10)
print(f"array: {array}",
      f"2 min nums: {find_2_min_nums(array)}",
      sep="\n")

# output:
# array: [-46, -63, -13, 9, -58, 2, -8, -65, -17, -95]
# 2 min nums: (-95, -65)
