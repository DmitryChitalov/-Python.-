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

from random import random

ROW = int(input('Задайте количество строк в матрице: '))
COL = int(input('Задайте количество столбцов в матрице: '))

max_num = max([min(i) for i in [[int(random() * 100)
                                 for _ in range(0, ROW)] for _ in range(0, COL)]])
print(max_num)

# 2 ---------------------------
a = []
for i in range(0, COL):
    b = []
    for j in range(0, ROW):
        b.append(int(random() * 100))
    a.append(b)

min_list = [min(i) for i in a]
max_num = max(min_list)
print(a)
print('минимальные значения по столбцам ', min_list)
print('Максимальное среди них = ', max_num)
