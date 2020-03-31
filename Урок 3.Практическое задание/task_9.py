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


def fun(i_value, j_value):

    matrix = []
    for i in range(i_value):
        string = []
        for j in range(j_value):
            string.append(randint(0, 50))
            print(f'{string[j]:3}', end='')
        matrix.append(string)
        print()

    min_lst = []

    for i in range(i_value):
        min_l = []
        for j in range(j_value):
            min_l.append(matrix[j][i])
        min_lst.append(min(min_l))

    print(f"{min_lst} минимальные значения по столбцам")
    print(f"Максимальное среди них = {max(min_lst)}")



ROW_NUMB = int(input("Задайте количество строк в матрице: "))
COL_NUMB = int(input("Задайте количество столбцов в матрице: "))
fun(ROW_NUMB, COL_NUMB)
