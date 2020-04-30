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
N = int(input('Задайте количество строк в матрице: '))
M = int(input('Задайте количество столбцов в матрице: '))
EXT_LST = []
for i in range(N):
    z = []
    for j in range(M):
        n = int(random.randint(1, 10))
        z.append(n)
        print(f"{n:4d}", end='')
    print()
    EXT_LST.append(z)
print()

def func(m):
    min_num = []
    for s in range(0, M):
        new_list = []
        for l in range(0, N):
            a = m[l][s]
            new_list.append(a)
        b = min_num.append(min(new_list))
    print(f'{min_num} - минимальные значения по столбцам.\nМаксимальное среди них = {max(min_num)}')

func(EXT_LST)







