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

str = int(input("Задайте количество строк в матрице: "))
col = int(input("Задайте количество столбцов в матрице: "))
new_arr = []
for i in range(str):
    array = []
    for j in range(col):
        array.append(random.randint(0, 100))
        print(f"{array[j]}   ", end='')
    new_arr.append(array)
    print('')

arr_min = []

for j in range(col):
    arr_col = []
    for i in range(str):
        arr_col.append(new_arr[i][j])
    min_col = min(arr_col)
    arr_min.append(min_col)

print(f'{arr_min} - минимальные значения по столбцам')

print(f'Максимальное среди них - {max(arr_min)}')
