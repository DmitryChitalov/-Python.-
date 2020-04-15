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

import random
from memory_profiler import profile

"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""


@profile
def max_min1(a):
    k = min(a)
    k_ind = a.index(k)
    for i, n in enumerate(a):
        if n < 0:
            if n > k:
                k = n
                k_ind = i
    print(f'max negative element {k}, with index {k_ind}')


@profile
def max_min2(a):
    lst = [el for el in a if el < 0]
    max_min_el = max(lst)
    max_min_ind = lst.index(max_min_el)
    print(f'max negative element {max_min_el}, with index {max_min_ind}')


m = 900000
a = [random.randint(-99, 99) for i in range(0, m)]
max_min1(m)
max_min2(m)

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

второй вариант функции тратит больше памяти так как в процесе выолнения создается список,
который занимает место в памяти.

Меня немного удивляют результаты работы profile. 
Во втором варианте, там где появился инкремент 0.2, не сходится:
14.1 +0.2 <> 16.1
"""

