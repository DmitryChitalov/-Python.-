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
def min_el(*args):
    min = args[0]
    for el in args:
        if el < min:
            min = el
    return min


def max_el(*args):
    max = args[0]
    for el in args:
        if el > max:
            max = el
    return max


def sum_maker(min, max, *args):
    summ = 0
    for el in args:
        if max > el > min:
            summ += el
    return summ

test_arr = [
    1, 2, 45,
    78, 4, 1024,
    78, 69, 7
]

if len(test_arr) > 0:
    print(f'The sum of the elements of the array, '
          f'where {max_el(*test_arr)} is the maximum '
          f'and {min_el(*test_arr)} is the minimum element '
          f'is {sum_maker(min_el(*test_arr), max_el(*test_arr), *test_arr)}')
else:
    print('Cannot calculate the amount of an empty array.')
