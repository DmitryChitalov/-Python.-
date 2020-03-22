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


def matrix_designer(row, column):
    matrix = []
    min_matrix_elements = []

    for i in range(row):
        spam = [randint(10, 99) for i in range(column)]
        matrix.append(spam)

    for index in range(0, column):
        spam = [matrix[i][index] for i in range(0, len(matrix))]
        min_matrix_elements.append(min(spam))

    return "\n".join([f"{matrix[i]}"    for i in range(0, len(matrix))]), min_matrix_elements


while True:
    try:
        ROW = int(input(f'Задайте количество строк в матрице: '))
        COLUMN = int(input(f'Задайте количество столбцов в матрице: '))
        MATRIX, MIN_MATRIX_ELEMENTS = matrix_designer(ROW, COLUMN)
        print(f'{MATRIX}\n{MIN_MATRIX_ELEMENTS} минимальные значения по столбцам\n'
              f'Максимальное среди них = {max(MIN_MATRIX_ELEMENTS)}')
    except ValueError:
        print(f'Ошибка ввода!')
