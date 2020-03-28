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

try:
    S = int(input('Задайте количество строк в матрице: ').strip())
    C = int(input('Задайте количество столбцов в матрице: ').strip())
except ValueError:
    S = C = False

if S and C:
    A = []
    for i in range(S):
        tmp_list = []
        for j in range(C):
            item = randint(1, 100)
            tmp_list.append(item)
        A.append(tmp_list)

    MIN_LIST = []
    for j in range(C):
        tmp_list = []
        for i in range(S):
            tmp_list.append(A[i][j])
        MIN_LIST.append(min(tmp_list))

    for line in A:
        print(line, sep='/n')
    print('----' * C)
    print(f'{MIN_LIST} минимальные значения по столбцам')
    print(f'Максимальное среди них = {max(MIN_LIST)}')
