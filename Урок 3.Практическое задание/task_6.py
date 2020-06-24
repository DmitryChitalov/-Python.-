"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
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
