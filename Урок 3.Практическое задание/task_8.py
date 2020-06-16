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


def get_arr_sum(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + get_arr_sum(arr[1:])


matrix = list()
raws, columns = 5, 4
for _ in range(raws):
    raw = [int(input()) for _ in range(columns)]
    last_el = get_arr_sum(raw)
    raw.append(last_el)
    matrix.append(raw)

print(*matrix, sep="\n")

# output
# [3, 3, 3, 3, 12]
# [3, 3, 3, 3, 12]
# [3, 3, 3, 3, 12]
# [3, 3, 3, 3, 12]
# [3, 3, 3, 3, 12]
