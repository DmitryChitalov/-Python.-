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

EXAMPLE = [[random.randint(0, 100) for _ in range(5)] for _ in range(5)]

for i in EXAMPLE:
    print(*i, sep='\t')

MAX_EL = EXAMPLE[0][0]

for j in range(5):
    min_r = EXAMPLE[0][j]

    for i in range(5):
        if EXAMPLE[i][j] < min_r:
            min_r = EXAMPLE[i][j]
    if min_r > MAX_EL:
        MAX_EL = min_r

print(MAX_EL)
