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

import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

for row in matrix:
    print(*row, sep='\t')

max_in_min = float('-inf')

for j in range(len(matrix[0])):
    min_temp = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_temp:
            min_temp = matrix[i][j]

    if min_temp > max_in_min:
        max_in_min = min_temp

print(f'\nМаксимальное значение = {max_in_min}')