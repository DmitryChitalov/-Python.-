"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randint

COUNT_ROW = int(input('Задайте количество строк в матрице: '))
COUNT_COLUMN = int(input('Задайте количество столбцов в матрице: '))
MAX_NUM = int(input('Задайте максимальное число в матрице: '))
LIST = [[randint(0, MAX_NUM) for I in range(COUNT_COLUMN)] for J in range(COUNT_ROW)]
for itm in LIST:
    print(itm)

NEW_LIST = []
MIN_NUM = MAX_NUM
for J in range(COUNT_COLUMN):
    for I in LIST:
        if I[J] < MIN_NUM:
            MIN_NUM = I[J]
    NEW_LIST.append(MIN_NUM)
print(NEW_LIST)
