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
N = 3
M = 4

EXT_LST = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 10))
        print(f"{b[j]:4d}", end='')
    EXT_LST.append(b)
    print(' ')

for i in range(M):
    print(f" ---", end='')
print()

for x in range(M):
    s = [EXT_LST[i][x] for i in range(N)]
    print(f"{min(s):4d}", end='')
print()
