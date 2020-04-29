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

def f_matrix():
    """ делает матрицу"""
    s = 6
    r = 8
    matrix = [[randint(0, 100) for x in range(r)] for _ in range(s)]
    return matrix

# матрицы
MATRIX = f_matrix()
MIN_MATRIX = []

for i in range(len(MATRIX)):
    MIN = MATRIX[i][0]
    for j in range(len(MATRIX[i])):
        number = MATRIX[i][j]
        if MIN > number:
            MIN = number

    MIN_MATRIX.append(MIN)
MAX= MIN_MATRIX[0]
for i in range(len(MIN_MATRIX)):
    number = MIN_MATRIX[i]
    if MAX < number:
        MAX = number

# Вывод
# начальная матрица
for i in range(len(MATRIX)):
    print(MATRIX[i])
# самые маленкие значения в столбцах
print(f'\nминимальные значения по столбцам: {MIN_MATRIX}')

# Самое большое из маленьких
print(f'\n Максимальное среди них: {MAX}')
