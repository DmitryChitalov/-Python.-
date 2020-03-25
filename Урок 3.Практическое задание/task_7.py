"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
from random import randint
BASE_LIST = []
for i in range(10):
    BASE_LIST.append(randint(-100, 100))
TEMP_LIST = BASE_LIST[:]
FIRST_MIN = TEMP_LIST.pop(TEMP_LIST.index(min(TEMP_LIST)))
print(TEMP_LIST)
SECOND_MIN = TEMP_LIST.pop(TEMP_LIST.index(min(TEMP_LIST)))
print(TEMP_LIST)
print(f'Исходный массив: {BASE_LIST}')
print(f'Первый наименьший элемент: {FIRST_MIN}')
print(f'Второй наименьший элемент: {SECOND_MIN}')
