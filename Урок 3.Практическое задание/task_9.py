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
row = int(input("Введите количество строк в матрице: "))
column = int(input("Введите количество столбцов в матрице: "))
my_arr = []
for i in range(row):
    my_arr.append([])
    s = 0
    for j in range(column):
        n = int(input(f"Введите {j + 1} число {i + 1} строки: "))
        my_arr[-1].append(n)
for i in my_arr:
    print(i)
print()

min_arr = []
for i in range(column):
    min_ar = []
    for j in range(row):
        min_ar.append(my_arr[j][i])
        n = min(min_ar)
    min_arr.append(n)
print(f"{min_arr} - минимальные значения по столбцам")
print(f"Максимальное значение из них {max(min_arr)}")