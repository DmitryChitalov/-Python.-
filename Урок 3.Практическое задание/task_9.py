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

# 1. Инициализируем массив

LIST_N = []

R_COUNT = int(input("Задайте количество строк в матрице: "))
C_COUNT = int(input("Задайте количество столбцов в матрице: "))

for r in range(R_COUNT):
    LIST_R = []
    for c in range(C_COUNT):
        LIST_R.append(random.randint(0, 10))
    LIST_N.append(LIST_R)

for r in range(R_COUNT):
    for c in range(C_COUNT):
        print(LIST_N[r][c], " ", end="")
    print()

# 2. Находим минимальные значения по столбцам
LIST_MIN = []
for c in range(C_COUNT):
    MIN_C = LIST_N[0][c]
    for r in range(1, R_COUNT):
        if LIST_N[r][c] < MIN_C:
            MIN_C = LIST_N[r][c]
    LIST_MIN.append(MIN_C)
print(f"{LIST_MIN} минимальные значения по столбцам")

# 3. Находим максимальное среди них
MIN_MAX_C = max(LIST_MIN)
print(f"Максимальное среди них = {MIN_MAX_C}")
