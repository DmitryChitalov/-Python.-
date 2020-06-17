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

rows = int(input('Задайте количество строк в матрице: '))
columns = int(input('Задайте количество столбцов в матрице: '))

# заполнение матрицы рандомными зничениями
matrix_a = [[randint(10, 100) for _ in range(columns)] for _ in range(rows)]
# print(matrix_a)

# печать матрицы
for row in matrix_a:
    for elem in row:
        print(elem, end='\t')
    print()

# поиск минимальных значений в столбцах
min_of_column = []
for column in range(columns):
    cache = 100
    for row in range(rows):
        if matrix_a[row][column] < cache:
            cache = matrix_a[row][column]
    min_of_column.append(cache)

print(f'{min_of_column} минимальные значения по столбцам')

# поиск максимального значения
max_row_num = 0
for item in min_of_column:
    if item > max_row_num:
        max_row_num = item
print(f'Максимальное среди них = {max_row_num}')
