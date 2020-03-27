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


def num_enter(message=""):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        else:
            print("Invalid number. Repeat entry.")


matrix = [[None for i in range(0, 5)] for j in range(0, 4)]
print(matrix)

for row in range(0, 4):
    print(f"{row + 1}-я строка:")
    for el in range(0, 5):
        if el == 4:
            matrix[row][el] = sum(matrix[row][0:4])
        else:
            matrix[row][el] = num_enter()

for row in matrix:
    print(row)
