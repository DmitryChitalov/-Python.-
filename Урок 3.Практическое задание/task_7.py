"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random


A = [random.randint(1, 5) for i in range(10)]
print(f'Массив: {A}')

MIN_1 = A[0]
MIN_2 = A[0]
for i in A:
    if i < MIN_1:
        MIN_2 = MIN_1
        MIN_1 = i
    elif i < MIN_2:
        MIN_2 = i
print(f'Наименьший элемент: {MIN_1}, Второй наименьший элемент: {MIN_2}')
