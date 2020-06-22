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
matrix = []
a = int(input('Задайте количество строк в матрице: '))
b = int(input('Задайте количество столбцов в матрице: '))
for el in range(a):
    a = []
    for i in range(b):
        a.append(randint(1, 40))
        print(f"{a[i]:4d}", end='')
    matrix.append(a)
    print('\n')

matrix_tr = []
t = 0
while t != len(matrix[0]):
    c = []
    for n in matrix:
        c.append(n[t])
    t += 1
    matrix_tr.append(c)

min_val = [min(j) for j in matrix_tr]
print(f'{min_val} минимальные значения по столбцам \n Максимальное среди них {max(min_val)}')
