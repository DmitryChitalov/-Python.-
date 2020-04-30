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


M = int(input('Задайте количество строк в матрице: '))
N = int(input('Задайте количество столбцов в матрице: '))
MATRIX = [[random.randint(0, 10) for i in range(N)] for j in range(M)]

for i in range(len(MATRIX)):
    print(MATRIX[i])

M_MIN = []

for j in range(N):
    MIN_NUM = MATRIX[0][j]
    for i in range(M):
        NUM = MATRIX[i][j]
        if NUM < MIN_NUM:
            MIN_NUM = NUM
    M_MIN.append(MIN_NUM)
print(f'Mинимальные значения по столбцам {M_MIN}')
print(f'Максимальное среди них = {max(M_MIN)}')
