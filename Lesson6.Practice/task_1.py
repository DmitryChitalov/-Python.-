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

from random import randint, sample
import memory_profiler
from memory_profiler import profile
import time


"""
Задание_2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.

Подсказка:
Попробуйте решить эту задачу в одну строку (такое решение точно есть)

Пример:
Исходный массив: [8, 3, 15, 6, 4, 2], результат: [0, 3, 4, 5]
"""


def get_even_nums(arr):
    arr_even_nums = [i for i in arr if i % 2 == 0]
    return arr_even_nums


if __name__ == "__main__":
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    nums = get_even_nums(range(90000000))

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек, памяти выделено {memory_diff} мб')

"""
Пример, аналогичный примеру с урока, в данном случае применяется оператор return с сохранением каждой переменной
списка в памяти.
Отсюда достаточно высокие показатели расходования памяти и низка производительность.
Выполнение заняло 11.46875 сек, памяти выделено 1738.7578125 мб
"""
"""


def get_even_nums_modern(arr):
    for i in arr:
        if i % 2 == 0:
            yield i


if __name__ == "__main__":
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    nums = get_even_nums_modern(range(90000000))

    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек, памяти выделено {memory_diff} мб')
"""
"""
Использование оператора yield существенно экономит ресурсы памяти и время запуска программы, так как
переменные списка не сохраняются в памяти.

Выполнение заняло 0.0 сек, памяти выделено 0.00390625 мб
"""


"""

Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

def add_matrix(rows, cols):
    """
    Заполнение матрицы
    """
    matrix = []
    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            matrix[row].append(randint(0, 100))
    return matrix


def matrix_output(matrix, range_col=''):
    """
    Вывод матрицы в красивом виде
    """
    for row in matrix:
        for col in row:
            range_col = range_col + '%s\t' % (col)
        range_col += '\n'
    return range_col

@profile
def get_minmax(min_lst=[]):
    """
    Нахождение максимального значения
    среди минимальных по столбцам матрицы
    """
    cnt_rows = int(input("Задайте количество строк в матрице: "))
    cnt_cols = int(input("Задайте количество столбцов в матрице: "))
    matrix = add_matrix(cnt_rows, cnt_cols)
    length = len(matrix[0])
    min_el = matrix[0]
    min_el_1 = min_el[0]
    for col in range(length):
        for row in range(len(matrix)):
            if matrix[row][col] < min_el_1:
                min_el_1 = matrix[row][col]
        min_lst.append(min_el_1)
        min_el_1 = 100
    print(matrix_output(matrix))
    del matrix
    return min_lst

"""
if __name__ == '__main__':
    MIN_LST = get_minmax()
    print(f'{MIN_LST} минимальное значение по столбцам\n'
          f'Максимальное среди них = {max(MIN_LST)}')

"""
"""
В данном алгоритме выделяется дополнительная память при формировании матрицы (2.3 MiB) и при выводе матрицы в
читабельном виде (0.2 MiB), после освобождение памяти 1.6 MiB (стр. 96) прирост памяти составляет ~1 MiB (стр. 128)
которые , что не является
плохим показателем.
Начальные данные:
Количество строк в матрице: 500
Количество столбцов в матрице: 500

Line #    Mem usage    Increment   Line Contents
================================================
    64     15.7 MiB     15.7 MiB   @profile
    65                             def get_minmax(min_lst=[]):
    66                                 
    67                                 Нахождение максимального значения
    68                                 среди минимальных по столбцам матрицы
    69                               
    70     15.8 MiB      0.0 MiB       cnt_rows = int(input("Задайте количество строк в матрице: "))
    71     15.8 MiB      0.0 MiB       cnt_cols = int(input("Задайте количество столбцов в матрице: "))
    72     18.1 MiB      2.3 MiB       matrix = add_matrix(cnt_rows, cnt_cols)
    73     18.1 MiB      0.0 MiB       length = len(matrix[0])
    74     18.1 MiB      0.0 MiB       min_el = matrix[0]
    75     18.1 MiB      0.0 MiB       min_el_1 = min_el[0]
    76     18.1 MiB      0.0 MiB       for col in range(length):
    77     18.1 MiB      0.0 MiB           for row in range(len(matrix)):
    78     18.1 MiB      0.0 MiB               if matrix[row][col] < min_el_1:
    79     18.1 MiB      0.0 MiB                   min_el_1 = matrix[row][col]
    80     18.1 MiB      0.0 MiB           min_lst.append(min_el_1)
    81     18.1 MiB      0.0 MiB           min_el_1 = 100
    82     18.3 MiB      0.2 MiB       print(matrix_output(matrix))
    83     16.7 MiB      0.0 MiB       del matrix
    84     16.7 MiB      0.0 MiB       return min_lst
"""