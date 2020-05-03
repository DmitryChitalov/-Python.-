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


def proc(row_vol, col_vol):
    """ Наша процедура"""

    matrix = []

    for i in range(row_vol):
        newrow = []

        for j in range(col_vol):
            newrow.append(randint(0, 50))
            print(f'{newrow[j]:4}', end='')

        matrix.append(newrow)
        print()

    min_lst = []

    for i in range(col_vol):
        min_l = []

        for j in range(row_vol):
            min_l.append(matrix[j][i])

        min_lst.append(min(min_l))

    print(f"{min_lst} минимальные значения по столбцам")
    print(f"Максимальное среди них = {max(min_lst)}")


try:
    ROW_VOL = int(input("Задайте количество строк в матрице: "))
    COL_VOL = int(input("Задайте количество столбцов в матрице: "))
    proc(ROW_VOL, COL_VOL)
except ValueError:
    print("Введите число. Попробуйте еще раз.")
