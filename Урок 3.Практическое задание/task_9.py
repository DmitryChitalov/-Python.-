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

while True:
    try:
        STRINGS = int(input('Задайте количество строк в матрице:'))
        COLUMNS = int(input('Задайте количество столбцов в матрице:'))
        break
    except ValueError:
        print('Вводите пожалуйста натуральные числа!')

MATRIX = [[randint(1, 100) for j in range(COLUMNS)] for i in range(STRINGS)]
MIN_VALUE = []

for string in MATRIX:
    for i, el in enumerate(string):
        try:
            if el < MIN_VALUE[i]:
                MIN_VALUE[i] = el
        except IndexError:
            MIN_VALUE.append(el)

for string in MATRIX:
    for el in string:
        print(f'{el:3d}', end=' ')
    print('')

print(f'Минимальные значения по столбцам {MIN_VALUE}')
print(f'Максимальное среди них = {max(MIN_VALUE)}')
