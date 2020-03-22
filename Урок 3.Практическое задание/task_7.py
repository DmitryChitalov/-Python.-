"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
from random import randint


def my_min(array):
    min_int_1 = min(array)
    if array.count(min_int_1) <= 1:
        array.remove(min_int_1)
        min_int_2 = min(array)
        array.append(min_int_1)
        return min_int_1, min_int_2
    min_int_2 = min_int_1
    return min_int_1, min_int_2


MY_LIST = [randint(-100, 100) for i in range(30)]
MIN_INT_1, MIN_INT_2 = my_min(MY_LIST)
print(f'Исходный массив: {MY_LIST}\nНаименьший элемент: {MIN_INT_1}, встречается в этом массиве 1 раз\n'
      f'Второй наименьший элемент: {MIN_INT_2}' if MIN_INT_1 != MIN_INT_2 else f'Исходный массив: {MY_LIST}\n'
                                                                               f'Наименьший элемент: {MIN_INT_1}, '
                                                                               f'встречается в этом массиве 2 раза')
