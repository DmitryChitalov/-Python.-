"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

import random

LEN = int(input('Введите длину массива: '))
a = [random.randint(0, 67) for k in range(LEN)]
print(a)


MAX_INDEX = a.index(max(a))
MIN_INDEX = a.index(min(a))
count = 0
if MAX_INDEX > MIN_INDEX:
    for i in range(MIN_INDEX+1, MAX_INDEX):
        count = count + a[i]
    print(count)
elif MAX_INDEX < MIN_INDEX:
    for i in range(MAX_INDEX+1, MIN_INDEX):
        count = count + a[i]
    print(count)
if (MAX_INDEX - MIN_INDEX == 1) or (MIN_INDEX - MAX_INDEX == 1):
    print('Между максимальным и минимальным числами нет чисел')

