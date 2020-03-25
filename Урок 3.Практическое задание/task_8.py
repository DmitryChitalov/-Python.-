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


def sum_count(array):
    result = 0
    for el in array:
        result += int(el)
    return str(result)


def print_matrix(matrix):
    print("Matrix")
    for string in matrix:
        for el in string:
            print(f"{int(el):4d}", end=' ')
        print()


MATRIX = []

for i in range(0, 5):
    STRING = input(f"Введите 4 элемента {i+1}-й сроки через пробел: ").split(' ')
    STRING.append(sum_count(STRING))
    MATRIX.append(STRING)

print_matrix(MATRIX)
