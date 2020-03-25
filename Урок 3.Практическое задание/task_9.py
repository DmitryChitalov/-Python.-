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


def write_matrix(strings, columns):

    matrix = []
    for i in range(0, strings):
        string = input(f"Введите {columns} элемента {i + 1}-й сроки через пробел: ").split(' ')
        matrix.append(string)
    return matrix


def matrix_min(matrix):

    min_values = [int(el) for el in matrix[0]]
    for string in matrix:
        for i in range(len(string)):
            if int(string[i]) < min_values[i]:
                min_values[i] = int(string[i])
    return min_values


STRINGS = int(input("Задайте количество строк в матрице: "))
COLUMNS = int(input("Задайте количество столбцов в матрице: "))

MATRIX = write_matrix(STRINGS, COLUMNS)
MIN_ELEMENTS = matrix_min(MATRIX)
print(f"{MIN_ELEMENTS} минимальные значения по столбцам\n"
      f"Макисальное среди них = {max(MIN_ELEMENTS)}")
