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

STRINGS = int(input('Задайте количество строк в матрице: '))
COLUMNS = int(input('Задайте количество столбцов в матрице: '))

matrix = []
for i in range(STRINGS):
    matrix.append([])
    for n in range(COLUMNS):
        matrix[i].append(random.randint(0, 100))

result = []
for i in range(COLUMNS):
    result.append(matrix[0][i])
for i in range(STRINGS):
    for n in range(COLUMNS):
        if matrix[i][n] < result[n]:
            result[n] = matrix[i][n]

for i in range(len(matrix)):
    print(" ".join(map(str, matrix[i])))

print(f'{result} минимальные значения по столбцам')
print(f'Максимальное среди них = {max(result)}')
