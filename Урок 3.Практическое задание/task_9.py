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

aaa = []
for i in range(3):
    inter = []
    for j in range(4):
        inter.append(randint(1, 99))
    aaa.append(inter)

for i in range(len(aaa)):
    for j in range(len(aaa[i])):
        print(f'{aaa[i][j]:4}', end=' ')
    print()

min_coll_lst = []
for i in range(len(aaa[1])):
    min_coll_el = aaa[2][i]
    for j in range(len(aaa)):
        if aaa[j][i] < min_coll_el:
            min_coll_el = aaa[j][i]
    min_coll_lst.append(min_coll_el)
print(f'{min_coll_lst} минимальные значения по столбцам')

max_from_min = 0
for p in min_coll_lst:
    if max_from_min < p:
        max_from_min = p

print(f'Максимальное среди них = {max_from_min}')