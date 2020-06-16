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
line = int(input('Задайте количество строк в матрице: '))
column = int(input('Задайте количество столбцов в матрице: '))
m = []
for _ in range(line):
    l = []
    for _ in range(column):
        l += [randint(0, 50)]
    m += [l]
res = []
max_el = 0
for i in range(line):
    print(m[i])
    min_el = m[i][0]
    for j in range(1, column):
        if m[i][j] < min_el:
            min_el = m[i][j]
    res += [min_el]
    if max_el < min_el:
        max_el = min_el

print(f'{res} минимальные значения по столбцам\n'
      f'Максимальное среди них - {max_el}')
