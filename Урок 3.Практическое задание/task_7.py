"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
from random import random
ARRAY = [int(random() * 100) for _ in range(10)]
print(*ARRAY)
if ARRAY[0] > ARRAY[1]:
    MIN_ONE = 0
    MIN_TWO = 1
else:
    MIN_ONE = 1
    MIN_TWO = 0

for i in range(2, len(ARRAY) - 1):
    if ARRAY[i] < ARRAY[MIN_ONE]:
        b = MIN_ONE
        MIN_ONE = i
        if ARRAY[b] < ARRAY[MIN_TWO]:
            MIN_TWO = b
    elif ARRAY[i] < ARRAY[MIN_TWO]:
        MIN_TWO = i

print(
    f'Наименьший элемент: {ARRAY[MIN_ONE]}, встречается в массиве {ARRAY.count(ARRAY[MIN_ONE])} раз')
print(f'Второй наименьший элемент: {ARRAY[MIN_TWO]}')
