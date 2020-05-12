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

from memory_profiler import profile

@profile
def my_list():
    my_list = [8, 3, 15, 6, 4, 2]
    print(my_list)
    print([i for i in range(len(my_list)) if my_list[i] % 2 == 0])

my_list()

"""
[8, 3, 15, 6, 4, 2]
[0, 3, 4, 5]
Filename: /home/sergej/PycharmProjects/Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    17     10.2 MiB     10.2 MiB   @profile
    18                             def my_list():
    19     10.2 MiB      0.0 MiB       my_list = [8, 3, 15, 6, 4, 2]
    20     10.2 MiB      0.0 MiB       print(my_list)
    21     10.2 MiB      0.0 MiB       print([i for i in range(len(my_list)) if my_list[i] % 2 == 0])




Проблем с памятью нет, в пределах нормы.
"""
######################################################################################################################

from random import random
from memory_profiler import profile

@profile
def arr():
    N = int(input("Введите длину массива: "))
    my_arr = []
    for i in range(N):
        my_arr.append(int(random()*100)-50)
    print(my_arr)
    min_arr = min(my_arr)
    max_arr = max(my_arr)
    min_index = my_arr.index(min_arr)
    max_index = my_arr.index(max_arr)
    print(f"Максимальное значение массива {max_arr} c индексом {max_index}, минимальное значение - {min_arr} "
          f"с индексом {min_index}")
    my_arr[min_index], my_arr[max_index] = my_arr[max_index], my_arr[min_index]
    print(my_arr)

arr()

"""
Введите длину массива: 5
[13, -9, 35, 24, 44]
Максимальное значение массива 44 c индексом 4, минимальное значение - -9 с индексом 1
[13, 44, 35, 24, -9]
Filename: /home/sergej/PycharmProjects/Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    43     12.2 MiB     12.2 MiB   @profile
    44                             def arr():
    45     12.2 MiB      0.0 MiB       N = int(input("Введите длину массива: "))
    46     12.2 MiB      0.0 MiB       my_arr = []
    47     12.2 MiB      0.0 MiB       for i in range(N):
    48     12.2 MiB      0.0 MiB           my_arr.append(int(random()*100)-50)
    49     12.2 MiB      0.0 MiB       print(my_arr)
    50     12.2 MiB      0.0 MiB       min_arr = min(my_arr)
    51     12.2 MiB      0.0 MiB       max_arr = max(my_arr)
    52     12.2 MiB      0.0 MiB       min_index = my_arr.index(min_arr)
    53     12.2 MiB      0.0 MiB       max_index = my_arr.index(max_arr)
    54     12.2 MiB      0.0 MiB       print(f"Максимальное значение массива {max_arr} c индексом {max_index}, минимальное значение - {min_arr} "
    55                                       f"с индексом {min_index}")
    56     12.2 MiB      0.0 MiB       my_arr[min_index], my_arr[max_index] = my_arr[max_index], my_arr[min_index]
    57     12.2 MiB      0.0 MiB       print(my_arr)

Проблем с памятью нет, в пределах нормы.
"""

######################################################################################################################


from random import random
from memory_profiler import profile

@profile
def my_arr():
    N = int(input("Введите длину массива: "))
    my_arr = [int(random()*10) for i in range(N)]
    print(my_arr)
    max_arr = max(my_arr, key=my_arr.count)
    print(f"Число {max_arr} встречается чаще всего: {my_arr.count(max_arr)} раз")

my_arr()

"""
Введите длину массива: 10
[7, 5, 1, 2, 7, 3, 8, 4, 3, 8]
Число 7 встречается чаще всего: 2 раз
Filename: /home/sergej/PycharmProjects/Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    92     12.3 MiB     12.3 MiB   @profile
    93                             def my_arr():
    94     12.3 MiB      0.0 MiB       N = int(input("Введите длину массива: "))
    95     12.3 MiB      0.0 MiB       my_arr = [int(random()*10) for i in range(N)]
    96     12.3 MiB      0.0 MiB       print(my_arr)
    97     12.3 MiB      0.0 MiB       max_arr = max(my_arr, key=my_arr.count)
    98     12.3 MiB      0.0 MiB       print(f"Число {max_arr} встречается чаще всего: {my_arr.count(max_arr)} раз")


Проблем с памятью нет, в пределах нормы.
"""
######################################################################################################################

import collections
import functools
from memory_profiler import profile
from guppy import hpy

h = hpy()
@profile
def calc():
    hex_number = collections.defaultdict(list)
    for i in range (2):
        n = input("Введите шестнадцатеричное число: ")
        hex_number[f"{i + 1} - {n}"] = list(n)
    print(hex_number)

    summ = sum([int(''.join(i), 16) for i in hex_number.values()])
    print("Сумма двух чисел ", list('%X' % summ))

    mult = functools.reduce(lambda a, b: a*b, [int(''.join(i), 16) for i in hex_number.values()])
    print("Произведение двух чисел ", list('%X' % mult))

calc()
print(h.heap())

"""
Введите шестнадцатеричное число: A2
Введите шестнадцатеричное число: C4F
defaultdict(<class 'list'>, {'1 - A2': ['A', '2'], '2 - C4F': ['C', '4', 'F']})
Сумма двух чисел  ['C', 'F', '1']
Произведение двух чисел  ['7', 'C', '9', 'F', 'E']
Filename: /home/sergej/PycharmProjects/Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
   124     10.1 MiB     10.1 MiB   @profile
   125                             def calc():
   126     10.1 MiB      0.0 MiB       hex_number = collections.defaultdict(list)
   127     10.1 MiB      0.0 MiB       for i in range (2):
   128     10.1 MiB      0.0 MiB           n = input("Введите шестнадцатеричное число: ")
   129     10.1 MiB      0.0 MiB           hex_number[f"{i + 1} - {n}"] = list(n)
   130     10.1 MiB      0.0 MiB       print(hex_number)
   131
   132     10.1 MiB      0.0 MiB       summ = sum([int(''.join(i), 16) for i in hex_number.values()])
   133     10.1 MiB      0.0 MiB       print("Сумма двух чисел ", list('%X' % summ))
   134
   135     10.1 MiB      0.0 MiB       mult = functools.reduce(lambda a, b: a*b, [int(''.join(i), 16) for i in hex_number.values()])
   136     10.1 MiB      0.0 MiB       print("Произведение двух чисел ", list('%X' % mult))


Partition of a set of 103477 objects. Total size = 7205019 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  29668  29  2150545  30   2150545  30 str
     1  27102  26  1018876  14   3169421  44 tuple
     2  13471  13   780551  11   3949972  55 bytes
     3   6648   6   559824   8   4509796  63 types.CodeType
     4   1164   1   520668   7   5030464  70 type
     5   6549   6   445332   6   5475796  76 function
     6   1164   1   304624   4   5780420  80 dict of type
     7    808   1   244228   3   6024648  84 dict (no owner)
     8    241   0   227368   3   6252016  87 dict of module
     9    749   1   112560   2   6364576  88 set
<262 more rows. Type e.g. '_.more' to view.>

Проблем с памятью нет, в пределах нормы.


Python 3.6 
32 разрядная ОС Linux Mint
"""