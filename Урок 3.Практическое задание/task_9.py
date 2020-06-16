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

y = int(input('Количество строк в матрице: '))
x = int(input('Количество столбцов в матрице: '))

result_matrix = []
for i in range(y):
    matrix = []
    for j in range(x):
        matrix.append(randint(0, 100))
    result_matrix.append(matrix)
print(*result_matrix, sep='\n')
result = []

for i in range(x):
    min_res = 100
    for j in range(y):
        if result_matrix[j][i] < min_res:
            min_res = result_matrix[j][i]
    result.append(min_res)
print()
print(result)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы - {max(result)}')
