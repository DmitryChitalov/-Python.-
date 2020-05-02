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

SUM_COL = []
TMP_COL = []
N = 4
M = 6

EXT_LST = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(1, 9))
        print(f"{b[j]:3d}", end='')
    print('\n')
    EXT_LST.append(b)
for i in range(M):
    for j in range(N):
        TMP_COL.append(EXT_LST[j][i])
        if j == N-1:
            SUM_COL.append(min(TMP_COL))
            TMP_COL = []
print('', SUM_COL, 'минимальные значения по столбцам')
print(f'Максимальное среди них {max(SUM_COL)}')
