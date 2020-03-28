"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random

RANDOM_LIST = [random.randint(-100, 100) for i in range(25)]


print(f"Исходный массив: {RANDOM_LIST}\nНаименьший элемент: {min(RANDOM_LIST)}, "
      f"встречается в массиве {RANDOM_LIST.count(min(RANDOM_LIST))} раз(а)")


if RANDOM_LIST.count(min(RANDOM_LIST)) == 1:
    RANDOM_LIST.pop(RANDOM_LIST.index(min(RANDOM_LIST)))
    print(f"Второй наименьший элемент: {min(RANDOM_LIST)}")
