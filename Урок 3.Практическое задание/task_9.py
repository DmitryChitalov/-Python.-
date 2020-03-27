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

matrix = []
line = int(input('Задайте количество строк в матрице: '))
column = int(input('Задайте количество столбцов в матрице: '))

for i in range(line):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(column)])


min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1


print()

min_list.sort(reverse=True)
print(
        'Максимальный элемент среди минимальных элементов матрицы: ',
        min_list[0]
            )