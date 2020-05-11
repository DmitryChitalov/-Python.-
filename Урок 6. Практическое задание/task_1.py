"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

# python 3.7
# windows 10 x64

import random
import sys

# Подготовим вывод данных об использовании памяти

def get_size(x):
    print(f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                get_size(y)
        elif not isinstance(x, str):
            for y in x:
                get_size(y)

# Задание 9 урок 2 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.

def task9_2(num):
    max_sum = 0
    for i in num:
        digits_sum = 0
        n = i
        while i % 10 != 0 or i // 10 != 0:
            digits_sum += i % 10
            i //= 10
        if digits_sum > max_sum:
            max_sum = digits_sum
            max_num = n
    print(f'Сумма цифр = {max_sum} числа {max_num}')
    return locals()

# numbers = [random.randrange(1, 1001) for _ in range(0, 30)]
# get_size(task9_2(numbers))
# Сумма цифр = 23 числа 896
# type = <class 'dict'>, size = 204, object = {'num': [284, 614, 160, 146, 53, 962, 896, 21, 540, 707], 'max_sum': 23, 'i': 0, 'digits_sum': 14, 'n': 707, 'max_num': 896}
# type = <class 'tuple'>, size = 36, object = ('num', [284, 614, 160, 146, 53, 962, 896, 21, 540, 707])
# type = <class 'str'>, size = 28, object = num
# type = <class 'list'>, size = 100, object = [284, 614, 160, 146, 53, 962, 896, 21, 540, 707]
# type = <class 'int'>, size = 14, object = 284
# type = <class 'int'>, size = 14, object = 614
# type = <class 'int'>, size = 14, object = 160
# type = <class 'int'>, size = 14, object = 146
# type = <class 'int'>, size = 14, object = 53
# type = <class 'int'>, size = 14, object = 962
# type = <class 'int'>, size = 14, object = 896
# type = <class 'int'>, size = 14, object = 21
# type = <class 'int'>, size = 14, object = 540
# type = <class 'int'>, size = 14, object = 707
# type = <class 'tuple'>, size = 36, object = ('max_sum', 23)
# type = <class 'str'>, size = 32, object = max_sum
# type = <class 'int'>, size = 14, object = 23
# type = <class 'tuple'>, size = 36, object = ('i', 0)
# type = <class 'str'>, size = 26, object = i
# type = <class 'int'>, size = 12, object = 0
# type = <class 'tuple'>, size = 36, object = ('digits_sum', 14)
# type = <class 'str'>, size = 35, object = digits_sum
# type = <class 'int'>, size = 14, object = 14
# type = <class 'tuple'>, size = 36, object = ('n', 707)
# type = <class 'str'>, size = 26, object = n
# type = <class 'int'>, size = 14, object = 707
# type = <class 'tuple'>, size = 36, object = ('max_num', 896)
# type = <class 'str'>, size = 32, object = max_num
# type = <class 'int'>, size = 14, object = 896


# type = <class 'dict'>, size = 204, object = {'num': [8208, 8191, 8465, 8249, 1266, 4036, 8907, 3094, 4026, 6622], 'max_sum': 24, 'i': 0, 'digits_sum': 16, 'n': 6622, 'max_num': 8907}
# type = <class 'tuple'>, size = 36, object = ('num', [8208, 8191, 8465, 8249, 1266, 4036, 8907, 3094, 4026, 6622])
# type = <class 'str'>, size = 28, object = num
# type = <class 'list'>, size = 100, object = [8208, 8191, 8465, 8249, 1266, 4036, 8907, 3094, 4026, 6622]
# type = <class 'int'>, size = 14, object = 8208
# type = <class 'int'>, size = 14, object = 8191
# type = <class 'int'>, size = 14, object = 8465
# type = <class 'int'>, size = 14, object = 8249
# type = <class 'int'>, size = 14, object = 1266
# type = <class 'int'>, size = 14, object = 4036
# type = <class 'int'>, size = 14, object = 8907
# type = <class 'int'>, size = 14, object = 3094
# type = <class 'int'>, size = 14, object = 4026
# type = <class 'int'>, size = 14, object = 6622
# type = <class 'tuple'>, size = 36, object = ('max_sum', 24)
# type = <class 'str'>, size = 32, object = max_sum
# type = <class 'int'>, size = 14, object = 24
# type = <class 'tuple'>, size = 36, object = ('i', 0)
# type = <class 'str'>, size = 26, object = i
# type = <class 'int'>, size = 12, object = 0
# type = <class 'tuple'>, size = 36, object = ('digits_sum', 16)
# type = <class 'str'>, size = 35, object = digits_sum
# type = <class 'int'>, size = 14, object = 16
# type = <class 'tuple'>, size = 36, object = ('n', 6622)
# type = <class 'str'>, size = 26, object = n
# type = <class 'int'>, size = 14, object = 6622
# type = <class 'tuple'>, size = 36, object = ('max_num', 8907)
# type = <class 'str'>, size = 32, object = max_num
# type = <class 'int'>, size = 14, object = 8907

# Выводы
# type = <class 'list'>, size = 100, object = [284, 614, 160, 146, 53, 962, 896, 21, 540, 707]
# type = <class 'list'>, size = 100, object = [8208, 8191, 8465, 8249, 1266, 4036, 8907, 3094, 4026, 6622]
# type = <class 'list'>, size = 136, object = [891, 440, 162, 240, 958, 773, 723, 638, 857, 67, 488, 482, 185, 771, 998, 382, 714, 210, 521, 259]
# type = <class 'list'>, size = 176, object = [196, 525, 609, 655, 135, 472, 776, 32, 242, 558, 971, 593, 88, 338, 455, 910, 500, 933, 497, 552, 191, 75, 640, 902, 577, 982, 345, 890, 719, 504]
# Использованная памяти растет при увеличении количества элементов в list

# type = <class 'int'>, size = 14, object = 160
# type = <class 'int'>, size = 14, object = 8249
# Использованная памяти не изменяется для хранения одного и того же типа


# Задание 5 урок 3
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


def task5_3(num):
    min_el = float('-inf')
    for i, item in enumerate(num):
        if min_el < item < 0:
            min_el = item
            min_index = i
        return locals()

# numbers = [random.randrange(1, 1001) for _ in range(0, 10)]
# get_size(task5_3(numbers))

# type = <class 'dict'>, size = 136, object = {'num': [290, 865, 524, 16, 326, 409, 421, 465, 907, 267], 'min_el': -inf, 'i': 0, 'item': 290}
# type = <class 'tuple'>, size = 36, object = ('num', [290, 865, 524, 16, 326, 409, 421, 465, 907, 267])
# type = <class 'str'>, size = 28, object = num
# type = <class 'list'>, size = 100, object = [290, 865, 524, 16, 326, 409, 421, 465, 907, 267]
# type = <class 'int'>, size = 14, object = 290
# type = <class 'int'>, size = 14, object = 865
# type = <class 'int'>, size = 14, object = 524
# type = <class 'int'>, size = 14, object = 16
# type = <class 'int'>, size = 14, object = 326
# type = <class 'int'>, size = 14, object = 409
# type = <class 'int'>, size = 14, object = 421
# type = <class 'int'>, size = 14, object = 465
# type = <class 'int'>, size = 14, object = 907
# type = <class 'int'>, size = 14, object = 267
# type = <class 'tuple'>, size = 36, object = ('min_el', -inf)
# type = <class 'str'>, size = 31, object = min_el
# type = <class 'float'>, size = 16, object = -inf
# type = <class 'tuple'>, size = 36, object = ('i', 0)
# type = <class 'str'>, size = 26, object = i
# type = <class 'int'>, size = 12, object = 0
# type = <class 'tuple'>, size = 36, object = ('item', 290)
# type = <class 'str'>, size = 29, object = item
# type = <class 'int'>, size = 14, object = 290

# Выводы
# С python 3.7 на windows 10 x64 int имеет size = 14

# Задание 9 урок 3 Найти максимальный элемент среди минимальных элементов столбцов матрицы.

def task9_3(matrix):
    for i, line in enumerate(matrix):
        if i == 0:
            min_line = line.copy()
            continue
        for idx, item in enumerate(line):
            if item < min_line[idx]:
                min_line[idx] = item
    max_min = min_line[0]
    for item in min_line:
        if item > max_min:
            max_min = item
    return locals()

m = [[random.randrange(0,10) for y in range(100)] for x in range(100)]
get_size(task9_3(m))
# type = <class 'dict'>, size = 204, object = {'matrix': [[2, 5], [5, 8]], 'i': 1, 'line': [5, 8], 'min_line': [2, 5], 'idx': 1, 'item': 5, 'max_min': 5}
# type = <class 'tuple'>, size = 36, object = ('matrix', [[2, 5], [5, 8]])
# type = <class 'str'>, size = 31, object = matrix
# type = <class 'list'>, size = 52, object = [[2, 5], [5, 8]]
# type = <class 'list'>, size = 52, object = [2, 5]
# type = <class 'int'>, size = 14, object = 2
# type = <class 'int'>, size = 14, object = 5
# type = <class 'list'>, size = 52, object = [5, 8]
# type = <class 'int'>, size = 14, object = 5
# type = <class 'int'>, size = 14, object = 8
# type = <class 'tuple'>, size = 36, object = ('i', 1)
# type = <class 'str'>, size = 26, object = i
# type = <class 'int'>, size = 14, object = 1
# type = <class 'tuple'>, size = 36, object = ('line', [5, 8])
# type = <class 'str'>, size = 29, object = line
# type = <class 'list'>, size = 52, object = [5, 8]
# type = <class 'int'>, size = 14, object = 5
# type = <class 'int'>, size = 14, object = 8
# type = <class 'tuple'>, size = 36, object = ('min_line', [2, 5])
# type = <class 'str'>, size = 33, object = min_line
# type = <class 'list'>, size = 44, object = [2, 5]
# type = <class 'int'>, size = 14, object = 2
# type = <class 'int'>, size = 14, object = 5
# type = <class 'tuple'>, size = 36, object = ('idx', 1)
# type = <class 'str'>, size = 28, object = idx
# type = <class 'int'>, size = 14, object = 1
# type = <class 'tuple'>, size = 36, object = ('item', 5)
# type = <class 'str'>, size = 29, object = item
# type = <class 'int'>, size = 14, object = 5
# type = <class 'tuple'>, size = 36, object = ('max_min', 5)
# type = <class 'str'>, size = 32, object = max_min
# type = <class 'int'>, size = 14, object = 5

# Выводы
# матрица 2х2
# type = <class 'tuple'>, size = 36, object = ('matrix', [[2, 5], [5, 8]])
# матрица 5х5
# type = <class 'tuple'>, size = 36, object = ('matrix', [[0, 2, 6, 2, 6], [0, 7, 9, 8, 2], [4, 0, 1, 9, 2], [7, 7, 5, 0, 9], [7, 1, 2, 4, 2]])
# матрица 100х100
# type = <class 'tuple'>, size = 36, object = ('matrix', [[5, 1, 4, 7, 3, 1, 1, 2, 0, 8, 9, 3, 9, 2, 0, 8, 7, 8, .....
# не совсем понял, почему не изменяется размер tuple при изменении размера матрицы
# потому что list для хранения в памяти при увеличениии размера матрицы изменяется
# матрица 2х2
# type = <class 'list'>, size = 52, object = [[2, 5], [5, 8]]
# матрица 100х100
# type = <class 'dict'>, size = 204, object = {'matrix': [[5, 1, 4, 7, 3, 1, 1, ...............