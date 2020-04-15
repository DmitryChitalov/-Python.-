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

# python version 3.7.3
# Windows 10, 64 bit
from math import log1p
from memory_profiler import profile


@profile
def func2(k):  #
    a = [0] * k
    a[0], a[1] = 2, 3
    i = 2
    m = 3
    while i < p:
        m = m + 1
        check_div = 0
        for j in range(2, int(m ** 0.5) + 1):
            if m % j == 0:
                check_div = 1
                break
        if check_div == 0:
            a[i] = m
            i += 1
    return a[k - 1]


@profile
def func3(k):
    n = int(k * log1p(2 * k) + k)
    a = [i for i in range(n)]
    a[1] = 0
    m = 2
    while m ** 2 < n:
        if a[m] != 0:
            j = m ** 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = [a[i] for i in a if a[i] != 0]
    return b[k - 1]


p = 10000
func2(p)
func3(p)

"""
Line #    Mem usage    Increment   Line Contents
================================================
    23     13.9 MiB     13.9 MiB   @profile
    24                             def func2(k):  #
    25     13.9 MiB      0.0 MiB       a = [0] * k
    26     13.9 MiB      0.0 MiB       a[0], a[1] = 2, 3
    27     13.9 MiB      0.0 MiB       i = 2
    28     13.9 MiB      0.0 MiB       m = 3
    29     14.1 MiB      0.0 MiB       while i < p:
    30     14.1 MiB      0.0 MiB           m = m + 1
    31     14.1 MiB      0.1 MiB           check_div = 0
    32     14.1 MiB      0.0 MiB           for j in range(2, int(m ** 0.5) + 1):
    33     14.1 MiB      0.0 MiB               if m % j == 0:
    34     14.1 MiB      0.0 MiB                   check_div = 1
    35     14.1 MiB      0.0 MiB                   break
    36     14.1 MiB      0.0 MiB           if check_div == 0:
    37     14.1 MiB      0.0 MiB               a[i] = m
    38     14.1 MiB      0.0 MiB               i += 1
    39     14.1 MiB      0.0 MiB       return a[k - 1]


Line #    Mem usage    Increment   Line Contents
================================================
    42     14.1 MiB     14.1 MiB   @profile
    43                             def func3(k):
    44     14.1 MiB      0.0 MiB       n = int(k * log1p(2 * k) + k)
    45     16.1 MiB      0.2 MiB       a = [i for i in range(n)]
    46     16.1 MiB      0.0 MiB       a[1] = 0
    47     16.1 MiB      0.0 MiB       m = 2
    48     16.1 MiB      0.0 MiB       while m ** 2 < n:
    49     16.1 MiB      0.0 MiB           if a[m] != 0:
    50     16.1 MiB      0.0 MiB               j = m ** 2
    51     16.1 MiB      0.0 MiB               while j < n:
    52     16.1 MiB      0.0 MiB                   a[j] = 0
    53     16.1 MiB      0.0 MiB                   j = j + m
    54     16.1 MiB      0.0 MiB           m += 1
    55     16.1 MiB      0.0 MiB       b = [a[i] for i in a if a[i] != 0]
    56     16.1 MiB      0.0 MiB       return b[k - 1]


Из-за того что в решете  сразу генерируется большой список, памяти этот вариант решения занимает больше.
"""