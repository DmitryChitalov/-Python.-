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
import random

# MATRIX = []
# Количество строк в матрице
COUNT_LINES = 5
# Количество столбцов в матрице
COUNT_COLUMNS = 4
# Генерация элементов матрицы 5х3
# 4-й столбец с суммой элементов строки будет добавлен
# в цикле подсчета суммы элементов строки
MATRIX = [[random.randrange(0, 100) for x in range(COUNT_COLUMNS - 1)] for y in range(COUNT_LINES)]
# Если элементы матрицы вводятся вручную с клавиатуры
if len(MATRIX) == 0:
    for i in range(0, COUNT_LINES):
        row = []
        SUM = 0
        for j in range(0, COUNT_COLUMNS - 1):
            while True:
                try:
                    VALUE = float(input(f'Введите элемент {j+1} строки {i+1}:\r\n'))
                except (ValueError, TypeError, IOError):
                    print('Ошибка ввода. Необходимо ввести число.')
                else:
                    row.append(VALUE)
                    SUM += VALUE
                    break
        row.append(SUM)
        MATRIX.append(row)

# Если элементы матрицы сгенерированы автоматически
# Подсчет суммы элементов строки  запись результата в новый столбец той же строки матрицы
else:
    for i in range(0, COUNT_LINES):
        SUM = 0
        for j in range(0, COUNT_COLUMNS - 1):
            SUM += MATRIX[i][j]
        MATRIX[i].append(SUM)

# Вывод всех элементов матрицы
for line in MATRIX:
    for item in line:
        print(f'{item} ', end="")
    print()
