"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
from random import randint

# Creating a mask for the matrix, for further filling
MATRIX = [[0 for j in range(5)] for i in range(5)]

for s, string in enumerate(range(5)):
    for i, el in enumerate(range(4)):
        MATRIX[s][i] = randint(1, 10)  # Quick random filling
        # As stated in the task
        # while True:
        #     try:
        #         MATRIX[s][i] = int(input(f'Введите {i+1}-й элемент {s+1}-й строки:'))
        #         break
        #     except ValueError:
        #         print('Пожалуйста, введите натуральное число, а не вот это вот')
    MATRIX[s][4] = sum(MATRIX[s][0:4])

for string in MATRIX:
    for el in string:
        print(f'{el:3d}', end=' ')
    print('')
