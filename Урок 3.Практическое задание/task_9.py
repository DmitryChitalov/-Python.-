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
STROKES = int(input('Задайте количество строк в матрице: '))
COLUMN = int(input('Задайте количество столбцов в матрице: '))
MATRIX = []
for i in range(STROKES):
    strokes = []
    for j in range(COLUMN):
        el = int(random() * 100)
        strokes.append(el)
        print(el, end=' ')
    print()
    MATRIX.append(strokes)

MINIMAL_MATRIX = []
for i in range(COLUMN):
    temp_matrix = []
    for j in range(STROKES):
        temp_matrix.append(MATRIX[j][i])
    MINIMAL_MATRIX.append(min(temp_matrix))
print(f'{MINIMAL_MATRIX} - минимальные значения по столбцам')
print(f'Максимальное среди них = {max(MINIMAL_MATRIX)}')
