"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
import cProfile
from random import randint


# """
# Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Пример:
# Задайте количество строк в матрице: 3
# Задайте количество столбцов в матрице: 4
#  36 20 42 38
#  46 27  7 33
#  13 12 47 15
# [13, 12, 7, 15] минимальные значения по столбцам
# Максимальное среди них = 15
# """

# from random import randint


# def matrix(row, col, row_idx=0):
#     """Функция для построения матрицы
#         row - количество строк
#         col - количество колонок
#         row_idx - индекс новой строки
#     """
#     if not row:
#         for elem in MATRIX:
#             print(' ', *elem)
#
#         row_matrix = []
#         for idx in range(len(MATRIX[0])):
#             row_matrix.append([el_row for el in MATRIX for el_row in el if el.index(el_row) == idx])
#         min_in_row = [el_row for el in row_matrix for el_row in el if el_row == min(el)]
#         print(f"{min_in_row} "
#               f"минимальные значения по столбцам \nМаксимальное среди них: {max(min_in_row)}")
#         return
#     MATRIX.append([])
#     for elem in range(col):
#         MATRIX[row_idx].append(randint(10, 100))
#
#     return matrix(row - 1, col, row_idx + 1)
#
#
# MATRIX = []
# try:
#     ROW_MATRIX = int(input("Задайте количество строк в матрице: "))
#     COL_MATRIX = int(input("Задайте количество столбцов в матрице: "))
#
#     if not ROW_MATRIX or not COL_MATRIX:
#         raise ValueError
#
#     matrix(ROW_MATRIX, COL_MATRIX)
# except ValueError as exception:
#     print("Необходимо вводить положительное количество")

MATRIX = [[]]


def func1(col=5, row_idx=0):
    """O(n) – линейная сложность"""
    for elem in range(col):
        MATRIX[row_idx].append(randint(10, 100))


MATRIX = [[]]


def func2(col=5, row_idx=0):
    """O(n) – линейная сложность"""
    MATRIX[row_idx].append([randint(10, 100) for _ in range(col)])


ROW_MATRIX = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]


def func3(row_matrix):
    """O(n^2) – квадратичная сложность"""
    min_in_row = [el_row for el in row_matrix for el_row in el if el_row == min(el)]


def func4(row_matrix):
    """O(n^2) – квадратичная сложность"""
    min_in_row = []
    for el in row_matrix:
        for el_row in el:
            if el_row == min(el):
                min_in_row.append(el_row)


def functions():
    func1()
    func2()
    func3(ROW_MATRIX)
    func4(ROW_MATRIX)


functions()


cProfile.run('functions()')
print(timeit.timeit("func1()",
                    setup="from __main__ import func1",
                    number=1000))
print(timeit.timeit("func2()",
                    setup="from __main__ import func2",
                    number=1000))
print(timeit.timeit("func3(ROW_MATRIX)",
                    setup="from __main__ import func3, ROW_MATRIX",
                    number=1000))
print(timeit.timeit("func4(ROW_MATRIX)",
                    setup="from __main__ import func4, ROW_MATRIX",
                    number=1000))


"""
Результат:
0.011439099999999994
0.012753299999999995
0.011487800000000006
0.014746699999999988

1,2. Оптимизировал код, заменив цикл for на генератор работающий быстрее 
и заменив итерируемую переменную на мусорную (_)

3,4. Обратный пример из той же функции. В квадратичной функции заменил двойной генератор на
цикл и вложенный цикл, в итоге код стал работать медленнее.

Теорема преимущества генераторов над циклами докзана)
"""