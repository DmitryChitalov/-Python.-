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
# Array transform function.
# Calls a function that creates a list of minimum values.


def el_in_col(args):
    i = 0
    matrix_2 = []
    while i < len(args[0]):
        tmp = []
        for el in args:
            tmp.append(el[i])
        i += 1
        matrix_2.append(tmp)
    return min_el(matrix_2)


# A function that creates a list of minimum values.
# Сalls the function of extracting the maximum among the minimum.
def min_el(args):
    min_list = []
    for el in args:
        min_el = el[0]
        for i in el:
            if i < min_el:
                min_el = i
        min_list.append(min_el)
    last_max(min_list)


# The function of extracting the maximum value.
def last_max(args):
    max = args[0]
    for el in args:
        if el > max:
            max = el
    return print(f'tThe maximum element '
                 f'among the minimum elements '
                 f'of the matrix columns is: {max}.')


matrix_1 = [
    [3, 3, 3, 9, 2],
    [4, 7, 7, 1, 3],
    [6, 8, 6, 5, 4],
    [4, 2, 6, 3, 8]
]

el_in_col(matrix_1)
