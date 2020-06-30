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
""" Для превого примера была взята вторая задача из 3 урока"""

from memory_profiler import profile
from guppy import hpy, heapy

@profile

def SAVE(ONE_LIST):
    NEW_LIST = []
    for elem in ONE_LIST:
        if elem % 2 == 0:
            NEW_LIST.append(ONE_LIST.index(elem))
    print(f"Первый массив {ONE_LIST}, второй мвссив из первого {NEW_LIST}")

ONE_LIST = [8, 3, 15, 6, 4, 2]
SAVE(ONE_LIST)

h = hpy()
def SAVE_1(ONE_LIST):
    NEW_LIST = []
    for elem in ONE_LIST:
        if elem % 2 == 0:
            NEW_LIST.append(ONE_LIST.index(elem))
    print(f"Первый массив {ONE_LIST}, второй мвссив из первого {NEW_LIST}")

ONE_LIST = [8, 3, 15, 6, 4, 2]
SAVE_1(ONE_LIST)
print(h.heap())

"""Line #    Mem usage    Increment   Line Contents
================================================
    18     14.1 MiB     14.1 MiB   @profile
    19                             
    20                             def SAVE(ONE_LIST):
    21     14.1 MiB      0.0 MiB       NEW_LIST = []
    22     14.1 MiB      0.0 MiB       for elem in ONE_LIST:
    23     14.1 MiB      0.0 MiB           if elem % 2 == 0:
    24     14.1 MiB      0.0 MiB               NEW_LIST.append(ONE_LIST.index(elem))
    25     14.1 MiB      0.0 MiB       print(f"Первый массив {ONE_LIST}, второй мвссив из первого {NEW_LIST}")"""

"""По данным замерам можно сделать вывод, что память у нас практичемки не выделяется на выполнение"""

"""artition of a set of 89333 objects. Total size = 10445489 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  27836  31  2600443  25   2600443  25 str
     1  19390  22  1395256  13   3995699  38 tuple
     2   6213   7  1096899  11   5092598  49 types.CodeType
     3  12620  14   960208   9   6052806  58 bytes
     4   1031   1   905712   9   6958518  67 type
     5   6026   7   819536   8   7778054  74 function
     6   1031   1   532848   5   8310902  80 dict of type
     7    236   0   421696   4   8732598  84 dict of module
     8    786   1   371192   4   9103790  87 dict (no owner)
     9     94   0    95440   1   9199230  88 abc.ABCMeta
<254 more rows. Type e.g. '_.more' to view.>"""

"""guppy показал, что больше всего str объекты занимают памяти 31%. Это понятно, т.к. приемущественно их больше"""