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


def add_matrix(rows, cols):
    """
    Заполнение матрицы
    """
    matrix = []
    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            matrix[row].append(randint(0, 100))
    return matrix


def matrix_output(matrix, range_col=''):
    """
    Вывод матрицы в красивом виде
    """
    for row in matrix:
        for col in row:
            range_col = range_col + '%s\t' % (col)
        range_col += '\n'
    return range_col


def get_minmax(min_lst=[]):
    """
    Нахождение максимального значения
    среди минимальных по столбцам матрицы
    """
    cnt_rows = int(input("Задайте количество строк в матрице: "))
    cnt_cols = int(input("Задайте количество столбцов в матрице: "))
    matrix = add_matrix(cnt_rows, cnt_cols)
    length = len(matrix[0])
    min_el = matrix[0]
    min_el_1 = min_el[0]
    for col in range(length):
        for row in range(len(matrix)):
            if matrix[row][col] < min_el_1:
                min_el_1 = matrix[row][col]
        min_lst.append(min_el_1)
        min_el_1 = 100
    print(matrix_output(matrix))
    return min_lst


if __name__ == '__main__':
    MIN_LST = get_minmax()
    print(f'{MIN_LST} минимальное значение по столбцам\n'
          f'Минимальное среди них = {max(MIN_LST)}')
