"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

import random

LIST_N = [random.randint(0, 100) for i in range(10)]

print(f"Массив: {LIST_N}")

if LIST_N[0] < LIST_N[1]:
    INDEX_MIN_1, INDEX_MIN_2 = LIST_N[0], LIST_N[1]
else:
    INDEX_MIN_1, INDEX_MIN_2 = LIST_N[1], LIST_N[0]

for i in range(2, len(LIST_N)):
    if LIST_N[i] < INDEX_MIN_1:
        INDEX_MIN_2 = INDEX_MIN_1
        INDEX_MIN_1 = LIST_N[i]
        continue
    if LIST_N[i] < INDEX_MIN_2:
        INDEX_MIN_2 = LIST_N[i]


if INDEX_MIN_1 == INDEX_MIN_2:
    print(f"Наименьший элемент: {INDEX_MIN_1}, встречается в этом массиве 2 раза")
else:
    print(f"Наименьший элемент: {INDEX_MIN_1}, встречается в этом массиве 1 раз")
    print(f"Второй наименьший элемент: {INDEX_MIN_2}")
