"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random

array = [random.randint(0, 100) for i in range(20)]
print(array)

a = min(array)

array.remove(a)

b = min(array)

print(f"Наименьшие числа массива: {a} и {b}")
