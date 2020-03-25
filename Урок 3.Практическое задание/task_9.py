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

ROW = int(input('Введите число строк матрицы: '))
COL = int(input('Введите число столбцов матрицы: '))
A = []
# A - это матрица, кот. заполняеся строками [[1,2,3],[2,3,4],[4,5,6]....[n,l,m]]

for i in range(ROW):
    b = []
    # b - это строка матирцы [n,l, .... k]
    for j in range(COL):
        b.append(randint(1, 50))
        print(f"{b[j]:4d}", end='')
        A.append(b)                     # Заполненная строка добавляется в матрицу
    print()
   
MAX_EL = 0
MIN_ARR = []

for j in range(COL):
    MIN_EL = 51
    for i in range(ROW):
        if A[i][j] < MIN_EL:
            MIN_EL = A[i][j]
    MIN_ARR.append(MIN_EL)
    if MIN_EL > MAX_EL:
        MAX_EL = MIN_EL
        
print(MIN_ARR)
print("Максимальный среди минимальных: ", MAX_EL)
