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


def num_enter(message=""):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


row_count = num_enter("Задайте количество строк в матрице: ")
column_count = num_enter("Задайте количество столбцов в матрице: ")

matrix = [[randint(0, 100) for j in range(0, column_count)] for i in range(0, row_count)]

min_el = []

for j in range(0, column_count):
    temp_list = []
    for i in range(0, row_count):
        temp_list.append(matrix[i][j])
    min_el.append(min(temp_list))

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Минимальные значения по столбцам:")
print(min_el)

print(f"Максимальное среди них - {max(min_el)}")
