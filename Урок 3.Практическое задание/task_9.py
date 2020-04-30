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

rows_num = int(input('Задайте количество строк в матрице: '))
columns_num = int(input('Задайте количество столбцов в матрице: '))
matrix = []  # формирование матрицы случайными числами
for i in range(rows_num):
    elements = [randint(1, 100) for j in range(columns_num)]
    matrix.append(elements)

min_elements = []

for i in range(rows_num):
    _ = []  # промежуточные результаты перебора матрицы
    for j in range(columns_num):  # перебор каждого элемента столбца
        _.append(matrix[j][i])
    min_elements.append(min(_))

for row in matrix:  # вывод результатов
    print(row)

print(f'{min_elements} - минимальные значения по столбцам\n'
      f'Максимальное среди них = {max(min_elements)}')
