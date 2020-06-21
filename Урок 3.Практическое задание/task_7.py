"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

# from random import random
#
# N = 10
# a = []
# for i in range(N):
#     a.append(int(random() * 100))
#     print("%3d" % a[i], end='')
# print()
from random import random

quantity = 10
list = []

for i in range(quantity):
    list.append(int(random() * 100))
print('Исходный массив: ', list)

if list[0] > list[1]:
    min_number = 0
    min2_number = 1
else:
    min_number = 1
    min2_number = 0

for i in range(2, quantity):
    if list[i] < list[min_number]:
        x = min_number
        min_number = i
        if list[x] < list[min2_number]:
            min2_number = x
    elif list[i] < list[min2_number]:
        min2_number = i

print('Первый наименьший элемент в массиве: ', list[min_number])
print('Второй наименьший элемент в массиве: ', list[min2_number])
