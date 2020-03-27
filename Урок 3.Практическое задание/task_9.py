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

NUM_OF_STRINGS = int(input("Задайте количество строк в матрице: "))
NUM_OF_COLUMN = int(input("Задайте количество столбцов в матрице: "))
MATRIX = []
N = 0
# Цикл создания матрицы
while N < NUM_OF_STRINGS:
    ELEMENT = []
    i = 0
    while i < NUM_OF_COLUMN:
        ELEMENT.append(int(random() * 100))
        i += 1
    MATRIX.append(ELEMENT)
    N += 1
# Вывод матрицы
for i in MATRIX:
    for j in i:
        print(f"{j:3d}", end=' ')
    print()

NUM = []
for i in range(NUM_OF_COLUMN):
    MATRIX_2 = []
    for j in range(NUM_OF_STRINGS):
        MATRIX_2.append(MATRIX[j][i])
    NUM.append(min(MATRIX_2))

MAX_NUMBER = max(NUM)
print(f"{NUM} минимальные значения по столбцам\n"
      f"Максимальное среди них = {MAX_NUMBER}")
