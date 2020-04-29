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

N = int(input("Задайте количество строк в матрице: "))
M = int(input("Задайте количество столбцов в матрице: "))

MATRIX = []

for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 100))
        print(f"{b[j]:3d}", end=" ")
    MATRIX.append(b)
    print()

MIN_LIST = []

for j in range(M):
    MIN = 101
    for i in range(N):
        if MATRIX[i][j] < MIN:
            MIN = MATRIX[i][j]
    MIN_LIST.append(MIN)

print(f"{MIN_LIST} минимальные значения по столбцам")
print(f"Максимальное среди них = {max(MIN_LIST)}")
