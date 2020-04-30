
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

num_col = int(input('Введите количество столбцов: '))
num_lin = int(input('Введите количество строк: '))
min_ran = -100
max_ran = 100
matrx = [[0] * num_col for _ in range(num_lin)]

for i in range(num_lin):
    for j in range(num_col):
        matrx[i][j] = randint(min_ran, max_ran)

print(f'Матрица случайных элементов размером {num_col};{num_lin}: ')
for line in matrx:
    print(line)

min_col = [max_ran + 1] * num_col
for j in range(num_col):
    for i in range(num_lin):
        if matrx[i][j] < min_col[j]:
            min_col[j] = matrx[i][j]

print(f'Минимальные значения столбцов:\n {min_col}')

max_lins = min_col[0]
for i in range(1, len(min_col)):
    if min_col[i] > max_lins:
        max_lins = min_col[i]
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_lins}')