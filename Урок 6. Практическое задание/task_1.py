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
# --== Python 3.8; OS x64 ==--

from memory_profiler import profile
from sys import getrefcount
from pympler import asizeof
from random import randint


@profile
def create_m(x, y):
    return [[randint(10, 100) for ii in range(x)] for i in range(y)]

@profile
def create_m2(x, y):
    return tuple(tuple(randint(10, 100) for ii in range(x)) for i in range(y))


@profile
def trans_m(m):
    tmp = [[] for i in m[0]]
    for i in m:
        for idx2, ii in enumerate(i):
            tmp[idx2].append(ii)
    return tmp


@profile
def main():
    m = create_m(500, 300)
    m2 = create_m2(500, 600)
    print('Ссылок на матрицу m: ', getrefcount(m))
    print(f'Размер Матрицы m список = {asizeof.asizeof(m) // 1024} кб')
    print(f'Размер Матрицы m2 кортеж = {asizeof.asizeof(m2) // 1024} кб')
    mm = trans_m(m)
    print(f'Размер Транспонированной матрицы mm = {asizeof.asizeof(mm) // 1024} кб')
    print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', max([ii for ii in [min(i) for i in mm]]))
    print('Ссылок на матрицу m: ', getrefcount(m))
    print('Ссылок на матрицу mm: ', getrefcount(mm))

    m = 1
    mm = 1
    print()


main()

#Общий вывод - в принципе распределение памяти понятно, непонятно как это все работает конкретно тут
# или средстви измерения "шалят" или я не понял ничего:
# 1. Понятно что матрица 500*300 занимает место, но не понятно почему кортеж больше
# 2. Повторяемости нет!, то строка №54 "m = 1"  освобождает память, то нет...
# Четкая картинка на складывается...



"""
/home/nubobap/venv/bin/python "/home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py"
Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    23     14.3 MiB     14.3 MiB   @profile
    24                             def create_m(x, y):
    25     15.6 MiB      0.3 MiB       return [[randint(10, 100) for ii in range(x)] for i in range(y)]


Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    27     15.6 MiB     15.6 MiB   @profile
    28                             def create_m2(x, y):
    29     17.9 MiB      0.3 MiB       return tuple(tuple(randint(10, 100) for ii in range(x)) for i in range(y))


Ссылок на матрицу m:  3
Размер Матрицы m список = 1254 кб
Размер Матрицы m2 кортеж = 2374 кб
Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    32     17.9 MiB     17.9 MiB   @profile
    33                             def trans_m(m):
    34     17.9 MiB      0.0 MiB       tmp = [[] for i in m[0]]
    35     18.9 MiB      0.0 MiB       for i in m:
    36     18.9 MiB      0.3 MiB           for idx2, ii in enumerate(i):
    37     18.9 MiB      0.3 MiB               tmp[idx2].append(ii)
    38     18.9 MiB      0.0 MiB       return tmp


Размер Транспонированной матрицы mm = 1241 кб
Максимальный элемент среди минимальных элементов столбцов матрицы:  13
Ссылок на матрицу m:  3
Ссылок на матрицу mm:  3
Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    41     14.3 MiB     14.3 MiB   @profile
    42                             def main():
    43     15.6 MiB      1.3 MiB       m = create_m(500, 300)
    44     17.9 MiB      2.3 MiB       m2 = create_m2(500, 600)
    45     17.9 MiB      0.0 MiB       print('Ссылок на матрицу m: ', getrefcount(m))
    46     17.9 MiB      0.0 MiB       print(f'Размер Матрицы m список = {asizeof.asizeof(m) // 1024} кб')
    47     17.9 MiB      0.0 MiB       print(f'Размер Матрицы m2 кортеж = {asizeof.asizeof(m2) // 1024} кб')
    48     18.9 MiB      1.1 MiB       mm = trans_m(m)
    49     19.2 MiB      0.3 MiB       print(f'Размер Транспонированной матрицы mm = {asizeof.asizeof(mm) // 1024} кб')
    50     19.2 MiB      0.0 MiB       print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', max([ii for ii in [min(i) for i in mm]]))
    51     19.2 MiB      0.0 MiB       print('Ссылок на матрицу m: ', getrefcount(m))
    52     19.2 MiB      0.0 MiB       print('Ссылок на матрицу mm: ', getrefcount(mm))
    53                             
    54     19.2 MiB      0.0 MiB       m = 1
    55     18.7 MiB      0.0 MiB       mm = 1



Process finished with exit code 0

"""
"""

Line #    Mem usage    Increment   Line Contents
================================================
    23     14.3 MiB     14.3 MiB   @profile
    24                             def create_m(x, y):
    25     15.6 MiB      0.3 MiB       return [[randint(10, 100) for ii in range(x)] for i in range(y)]


Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    27     15.6 MiB     15.6 MiB   @profile
    28                             def create_m2(x, y):
    29     17.9 MiB      0.3 MiB       return tuple(tuple(randint(10, 100) for ii in range(x)) for i in range(y))


Ссылок на матрицу m:  3
Размер Матрицы m список = 1254 кб
Размер Матрицы m2 кортеж = 2374 кб
Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    32     17.9 MiB     17.9 MiB   @profile
    33                             def trans_m(m):
    34     17.9 MiB      0.0 MiB       tmp = [[] for i in m[0]]
    35     19.0 MiB      0.0 MiB       for i in m:
    36     19.0 MiB      0.3 MiB           for idx2, ii in enumerate(i):
    37     19.0 MiB      0.3 MiB               tmp[idx2].append(ii)
    38     19.0 MiB      0.0 MiB       return tmp


Размер Транспонированной матрицы mm = 1241 кб
Максимальный элемент среди минимальных элементов столбцов матрицы:  12
Ссылок на матрицу m:  3
Ссылок на матрицу mm:  3

Filename: /home/nubobap/Документы/GB/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    41     14.3 MiB     14.3 MiB   @profile
    42                             def main():
    43     15.6 MiB      1.3 MiB       m = create_m(500, 300)
    44     17.9 MiB      2.3 MiB       m2 = create_m2(500, 600)
    45     17.9 MiB      0.0 MiB       print('Ссылок на матрицу m: ', getrefcount(m))
    46     17.9 MiB      0.0 MiB       print(f'Размер Матрицы m список = {asizeof.asizeof(m) // 1024} кб')
    47     17.9 MiB      0.0 MiB       print(f'Размер Матрицы m2 кортеж = {asizeof.asizeof(m2) // 1024} кб')
    48     19.0 MiB      1.1 MiB       mm = trans_m(m)
    49     19.2 MiB      0.3 MiB       print(f'Размер Транспонированной матрицы mm = {asizeof.asizeof(mm) // 1024} кб')
    50     19.2 MiB      0.0 MiB       print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', max([ii for ii in [min(i) for i in mm]]))
    51     19.2 MiB      0.0 MiB       print('Ссылок на матрицу m: ', getrefcount(m))
    52     19.2 MiB      0.0 MiB       print('Ссылок на матрицу mm: ', getrefcount(mm))
    53                             
    54     19.2 MiB      0.0 MiB       m = 1
    55     19.2 MiB      0.0 MiB       mm = 1
    56     19.2 MiB      0.0 MiB       print()



"""
