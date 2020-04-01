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


def user_matrix(row_num, col_num):

    # делаем матрицу
    matrix = []
    for i in range(row_num):
        string = []
        for j in range(col_num):
            string.append(randint(0, 50))
            print(f'{string[j]:3}', end='')
        matrix.append(string)
        print()
    # вносим минимальные элементы в созданый список
    min_list = []
    for i in range(col_num):
        min_l = []
        for j in range(row_num):
            min_l.append(matrix[j][i])
        min_list.append(min(min_l))
    print(f'{min_list} минимальные значения по столбцам')
    print(f'максимальное из них = {max(min_list)}')


try:
    ROW_NUM = int(input('Введите количество строк в матрице: '))
    COL_NUM = int(input('Введите количество столбцов в матрице: '))
    user_matrix(ROW_NUM, COL_NUM)
except ValueError:
    print('Вы ввели не число!!!')
