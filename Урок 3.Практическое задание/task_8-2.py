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


def row_enter(message):
    while True:
        break_point = True
        row = input(message).split()
        row_int = []
        for item in row:
            if item.isdecimal():
                row_int.append(int(item))
            else:
                print(f"Invalid number {item}. Repeat entry.")
                break_point = False
        if break_point:
            return row_int


matrix = [[] for j in range(0, 4)]

for row in range(0, 4):
    matrix[row] = row_enter(f"{row + 1}-я строка:\n")
    matrix[row].append(sum(matrix[row]))

for row in matrix:
    print(row)




