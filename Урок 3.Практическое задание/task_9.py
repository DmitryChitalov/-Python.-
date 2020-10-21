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
import random


def create_m(x, y):
    return [[random.randint(10, 100) for ii in range(x)] for i in range(y)]


def trans_m(m):
    tmp = [[] for i in m[0]]
    for i in m:
        for idx2, ii in enumerate(i):
            tmp[idx2].append(ii)
    return tmp


m = create_m(5, 3)
mm = trans_m(m)
print(m)
print(mm)
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ',
      max([ii for ii in [min(i) for i in mm]]))
