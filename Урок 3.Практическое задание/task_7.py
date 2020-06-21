"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

import random

START_RANGE = 1
END_RANGE = 100
SIZE_RANGE = 10

MY_LIST = [random.randint(START_RANGE, END_RANGE) for _ in range(SIZE_RANGE)]
print(MY_LIST)

min_first, min_second = (0, 1) if MY_LIST[0] < MY_LIST[1] else (1, 0)

for i in range(2, len(MY_LIST)):
    if MY_LIST[i] < MY_LIST[min_first]:
        spam = min_first
        min_first = i
        if MY_LIST[spam] < MY_LIST[min_second]:
            min_second = spam

    elif MY_LIST[i] < MY_LIST[min_second]:
        min_second = i

print(f'Первый наименьший элемент в массиве: {MY_LIST[min_first]} его индекс = {min_first}\n'
      f'Второй наименьший элемент в массиве: {MY_LIST[min_second]} его индекс = {min_second}')
