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

START = 0
END = 100
SIZE = 10

MATRIX = [[random.randint(START, END) for _ in range(SIZE)] for _ in range(SIZE)]

for line in MATRIX:
    print(*line, sep='\t')


max_val = None

for j in range(len(MATRIX[0])):
    min_val = MATRIX[0][j]

    for i in range(len(MATRIX)):
        if MATRIX[i][j] < min_val:
            min_val = MATRIX[i][j]

    if max_val is None or max_val < min_val:
        max_val = min_val

print(f'Максимальный элемен среди минимальных = {max_val}')

