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

NUM_1 = 5
NUM_2 = 4
MATRIX = []

for i in range(NUM_1):
    my_list = []
    summ = 0

    for j in range(NUM_2 - 1):
        num = int(input(f'{i} строка, {j} элемент: '))
        summ += num
        my_list.append(my_list)

    my_list.append(summ)
    MATRIX.append(my_list)

for line in MATRIX:
    print(line)
