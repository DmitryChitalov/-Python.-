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


USER_MATRIX = []
TRANS_MATRIX = []
FINAL_MATRIX = []
COLUMN_COUNT = int(input("Введите число столбцов: "))
ROW_COUNT = int(input("Введите число строк: "))


for i in range(ROW_COUNT):
    matrix_row = []
    for j in range(COLUMN_COUNT):
        matrix_row.append(random.randint(-100, 100))
    USER_MATRIX.append(matrix_row)


for i in USER_MATRIX:
    print(i)

# Транспонируем матрицу, чтобы легче было искать максимальный элемент столбца
for j in range(COLUMN_COUNT):
    tran_row = []
    for i in range(ROW_COUNT):
        tran_row.append(USER_MATRIX[i][j])
    TRANS_MATRIX.append(tran_row)


for i in TRANS_MATRIX:
    FINAL_MATRIX.append(min(i))
print(f"{FINAL_MATRIX} Минимальные значения по столбцам\n"
      f"Максимальное значение среди них: {max(FINAL_MATRIX)}")
