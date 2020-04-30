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

MATR_STRINGS = int(input("Задайте количество строк в матрице: "))
MATR_ROWS = int(input("Задайте количество столбцов в матрице: "))
MIN_ELEMS = [0 for i in range(MATR_ROWS)]
MATR = [[0 for i in range(MATR_ROWS)] for j in range(MATR_STRINGS)]
for i in range(MATR_STRINGS):
    MATR[i] = [int(i) for i in input().split()]

for i in range(MATR_ROWS):
    MIN_ELEMS[i] = min([MATR[j][i] for j in range(MATR_STRINGS)])


print(f"{MIN_ELEMS}  минимальные значения по столбцам")
print(f"Максимальное среди них = {max(MIN_ELEMS)}")
