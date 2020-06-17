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


def matrix(row=5, col=4, row_idx=0):
    """Функция для построения матрицы

    row - количество строк
    col - количество колонок
    row_idx - индекс новой строки
    """
    if not row:
        print()
        for elem in MATRIX:
            print(elem)
        return
    print(f"{row_idx + 1}-я строка:")
    MATRIX.append([])
    for elem in range(col):
        try:
            MATRIX[row_idx].append(int(input()))
        except ValueError as exception:
            MATRIX.pop(row_idx)
            print(f"Ошибка ввода данных: {exception}\nЗаполните строку заново")
            return matrix(row, col, row_idx)
    MATRIX[row_idx].append(sum(MATRIX[row_idx]))

    return matrix(row - 1, col, row_idx + 1)


MATRIX = []
matrix()
