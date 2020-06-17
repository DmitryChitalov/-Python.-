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


def matrix(row, col, row_idx=0):
    """Функция для построения матрицы

        row - количество строк
        col - количество колонок
        row_idx - индекс новой строки
    """
    if not row:
        for elem in MATRIX:
            print(' ', *elem)

        row_matrix = []
        for idx in range(len(MATRIX[0])):
            row_matrix.append([el_row for el in MATRIX for el_row in el if el.index(el_row) == idx])
        min_in_row = [el_row for el in row_matrix for el_row in el if el_row == min(el)]
        print(f"{min_in_row} "
              f"минимальные значения по столбцам \nМаксимальное среди них: {max(min_in_row)}")
        return
    MATRIX.append([])
    for elem in range(col):
        MATRIX[row_idx].append(randint(10, 100))

    return matrix(row - 1, col, row_idx + 1)


MATRIX = []
try:
    ROW_MATRIX = int(input("Задайте количество строк в матрице: "))
    COL_MATRIX = int(input("Задайте количество столбцов в матрице: "))

    if not ROW_MATRIX or not COL_MATRIX:
        raise ValueError

    matrix(ROW_MATRIX, COL_MATRIX)
except ValueError as exception:
    print("Необходимо вводить положительное количество")
