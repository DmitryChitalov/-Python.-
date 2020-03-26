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

try:
    ROW = 3  # int(input('Задайте количество строк в матрице: '))
    COLUMN = 4  # int(input('Задайте количество столбцов в матрице: '))
    MATRIX = [[randint(0, 100) for n in range(COLUMN)] for m in range(ROW)]
    for lst in MATRIX:
        print(lst)
    # тут передаем в map функцию min и несколько (COLUMN) массивов
    MIN_LST = list(map(min, *MATRIX))
    print(f'Минимальные значения по столбцам: {MIN_LST}')
    print(f'Максимальное среди них = {max(MIN_LST)}')
except ValueError as err:
    print(f'Ошибка ввода: {err}')
