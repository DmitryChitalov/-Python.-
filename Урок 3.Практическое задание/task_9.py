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


def create_matrix(i, j):
    """
    :param i: вертикаль
    :param j: горизонталь
    """
    matrix = list()
    for _ in range(i):
        raw_elements = list()
        for _ in range(j):
            raw_elements.append(randint(-99, 99))
        matrix.append(raw_elements)
    return matrix


def find_min_matrix_el(matrix):
    min_elements = list()
    for i in matrix:
        min_raw_el = i[0]
        for j in i[1:]:
            if j < min_raw_el:
                min_raw_el = j
        min_elements.append(min_raw_el)
    return min_elements


def find_max_arr_el(array):
    max_el = array[0]
    for el in array[1:]:
        if el > max_el:
            max_el = el
    return max_el


if __name__ == '__main__':
    i, j = 3, 4
    matrix = create_matrix(i, j)
    min_elements_arr = find_min_matrix_el(matrix)
    max_el = find_max_arr_el(min_elements_arr)
    print(f"matrix: {matrix}",
          f"min_elements_arr: {min_elements_arr}",
          f"max_el: {max_el}",
          sep="\n"
          )

# output:
# matrix: [[7, -28, -33, -94], [-6, -53, 6, -6], [-29, -5, 24, -56]]
# min_elements_arr: [-94, -53, -56]
# max_el: -53
