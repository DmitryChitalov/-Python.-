import random

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
n = int(input('Введите колличество строк в масиве: '))
m = int(input('Введите колличество столбцов в масиве: '))
a = []
for i in range(0, n):
    a.append([random.randint(0, 100) for j in range(0, m)])
    print(a[i])
min_col = []
for j in range(0, m):
    min_c = a[0][j]
    for i in range(1, n):
        if a[i][j] < min_c:
            min_c = a[i][j]
    min_col.append(min_c)
max_min_col = max(min_col)
min_col.append(max_min_col)
print(min_col)
