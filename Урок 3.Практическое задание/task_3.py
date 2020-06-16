"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

from random import randint


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


def change_el_places(min_i, max_i):
    arr[min_i], arr[max_i] = arr[max_i], arr[min_i]


if __name__ == '__main__':
    arr = create_array(10)
    print(f"Массив до изменений: {arr}")
    min_index = get_min_index(arr)
    max_index = get_max_index(arr)
    change_el_places(min_index, max_index)
    print(f"Минимальный элемент = {arr[min_index]}; Максимальный = {arr[max_index]}")
    print(f"Массив после изменений: {arr}")

