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
COLUMN = 4
ROW = 3
ARRAY = []
for i in range(ROW):
    row = []
    for j in range(COLUMN):
        val = int(random() * 100)
        row.append(val)
        print('%4d' % val, end='')
    ARRAY.append(row)
    print()

min_val = -1
for j in range(COLUMN):
    max_val = 100
    for i in range(ROW):
        if ARRAY[i][j] < max_val:
            max_val = ARRAY[i][j]
    print(max_val, end=',')
    if max_val > min_val:
        min_val = max_val
print(' минимальные значения по столбцам')
print(f"Максимальное среди них: {min_val}")
