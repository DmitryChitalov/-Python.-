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

"""Версия python 3.8, x64"""

import sys
from memory_profiler import profile
import random
from pympler import asizeof

"""sys.setrecursionlimit(10000)

I = int(input('Введите количество элементов последовательности: '))
QUANTITY = I
@profile
def sum(i, start, result):
    if i == 0:
        return print(f'Количество элементов - {QUANTITY}, их сумма {result}')
    else:
        result += start
        start = start / -2
        sum(i-1, start, result)

sum(I, 1, 0)"""

"""Filename: C:/Users/Grilyage/Documents/GitHub/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    22     13.4 MiB     13.3 MiB   @profile
    23                             def sum(i, start, result):
    24     13.4 MiB      0.0 MiB       if i == 0:
    25     13.4 MiB      0.0 MiB           return print(f'Количество элементов - {QUANTITY}, их сумма {result}')
    26                                 else:
    27     13.4 MiB      0.0 MiB           result += start
    28     13.4 MiB      0.0 MiB           start = start / -2
    29     13.4 MiB      0.0 MiB           sum(i-1, start, result)
"""



"""I = random.randint(1, 900)
@profile
def check(end, sumM=0, i=0):
    if i == end:
        if sumM == end * (end + 1) / 2:
            return print(f'Равенство верно для числа {I}')
        else:
            print('Ошибка в равенстве')
    else:
        return check(end, sumM+i+1, i+1)


check(I)"""

"""Filename: C:/Users/Grilyage/Documents/GitHub/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    36     14.3 MiB     13.4 MiB   @profile
    37                             def check(end, sumM=0, i=0):
    38     14.3 MiB      0.0 MiB       if i == end:
    39     14.4 MiB      0.0 MiB           if sumM == end * (end + 1) / 2:
    40     14.4 MiB      0.0 MiB               return print(f'Равенство верно для числа {I}')
    41                                     else:
    42                                         print('Ошибка в равенстве')
    43                                 else:
    44     14.4 MiB      0.0 MiB           return check(end, sumM+i+1, i+1)
"""

"""@profile
def count():
    for i in range(2, 10):
        q = 0
        for n in range(2, 100):
            if n % i == 0:
                q += 1
        print(f'В диапазоне 2-99: {q} чисел кратны {i}')

count()"""

"""Filename: C:/Users/Grilyage/Documents/GitHub/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    77     13.3 MiB     13.3 MiB   @profile
    78                             def count():
    79     13.3 MiB      0.0 MiB       for i in range(2, 10):
    80     13.3 MiB      0.0 MiB           q = 0
    81     13.3 MiB      0.0 MiB           for n in range(2, 100):
    82     13.3 MiB      0.0 MiB               if n % i == 0:
    83     13.3 MiB      0.0 MiB                   q += 1
    84     13.3 MiB      0.0 MiB           print(f'В диапазоне 2-99: {q} чисел кратны {i}')"""

"""@profile
def matrix():
    STRINGS = int(input('Задайте количество строк в матрице: '))
    COLUMNS = int(input('Задайте количество столбцов в матрице: '))

    matrix = []
    for i in range(STRINGS):
        matrix.append([])
        for n in range(COLUMNS):
            matrix[i].append(random.randint(0, 100))

    result = []
    for i in range(COLUMNS):
        result.append(matrix[0][i])
    for i in range(STRINGS):
        for n in range(COLUMNS):
            if matrix[i][n] < result[n]:
                result[n] = matrix[i][n]

    for i in range(len(matrix)):
        print(" ".join(map(str, matrix[i])))

    print(f'{result} минимальные значения по столбцам')
    print(f'Максимальное среди них = {max(result)}')

matrix()"""

"""Filename: C:/Users/Grilyage/Documents/GitHub/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
   103     13.5 MiB     13.5 MiB   @profile
   104                             def matrix():
   105     13.5 MiB      0.0 MiB       STRINGS = int(input('Задайте количество строк в матрице: '))
   106     13.5 MiB      0.0 MiB       COLUMNS = int(input('Задайте количество столбцов в матрице: '))
   107                             
   108     13.5 MiB      0.0 MiB       matrix = []
   109     13.5 MiB      0.0 MiB       for i in range(STRINGS):
   110     13.5 MiB      0.0 MiB           matrix.append([])
   111     13.5 MiB      0.0 MiB           for n in range(COLUMNS):
   112     13.5 MiB      0.0 MiB               matrix[i].append(random.randint(0, 100))
   113                             
   114     13.5 MiB      0.0 MiB       result = []
   115     13.5 MiB      0.0 MiB       for i in range(COLUMNS):
   116     13.5 MiB      0.0 MiB           result.append(matrix[0][i])
   117     13.5 MiB      0.0 MiB       for i in range(STRINGS):
   118     13.5 MiB      0.0 MiB           for n in range(COLUMNS):
   119     13.5 MiB      0.0 MiB               if matrix[i][n] < result[n]:
   120     13.5 MiB      0.0 MiB                   result[n] = matrix[i][n]
   121                             
   122     13.5 MiB      0.0 MiB       for i in range(len(matrix)):
   123     13.5 MiB      0.0 MiB           print(" ".join(map(str, matrix[i])))
   124                             
   125     13.5 MiB      0.0 MiB       print(f'{result} минимальные значения по столбцам')
   126     13.5 MiB      0.0 MiB       print(f'Максимальное среди них = {max(result)}')"""

"""target = int(input('Введите номер простого числа: '))

@profile
def simple_n3(target, simple=[]):
    for i in range(2, 1000000000):
        if (i > 10):
            if (i % 2 == 0) or (i % 10 == 5):
                continue
        for x in simple:
            if i % x == 0:
                break
        else:
            simple.append(i)
        if len(simple) == target:
            break
    return print(f'{target}-ое простое число: {simple[-1]}')

simple_n3(target)"""

"""Введите номер простого числа: 1000
1000-ое простое число: 7919
Filename: C:/Users/Grilyage/Documents/GitHub/Python_Algos/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
   160     13.4 MiB     13.4 MiB   @profile
   161                             def simple_n3(target, simple=[]):
   162     13.5 MiB      0.0 MiB       for i in range(2, 1000000000):
   163     13.5 MiB      0.0 MiB           if (i > 10):
   164     13.5 MiB      0.0 MiB               if (i % 2 == 0) or (i % 10 == 5):
   165     13.5 MiB      0.0 MiB                   continue
   166     13.5 MiB      0.0 MiB           for x in simple:
   167     13.5 MiB      0.0 MiB               if i % x == 0:
   168     13.5 MiB      0.0 MiB                   break
   169                                     else:
   170     13.5 MiB      0.0 MiB               simple.append(i)
   171     13.5 MiB      0.0 MiB           if len(simple) == target:
   172     13.5 MiB      0.0 MiB               break
   173     13.5 MiB      0.0 MiB       return print(f'{target}-ое простое число: {simple[-1]}')
"""

"""Не удается найти ни одной подходящей задачи, где было бы существеннное потребление памяти.
Попробуем написать код поиска простых чисел через решето Эратосфена до 10000"""


#@profile
def eratho(n):
    list = []
    for i in range(2, n):
        list.append(i)
    for num in list:
        for elem in list:
            if elem % num == 0 and elem != num:
                list.remove(elem)
    print(asizeof.asizeof(list))
    print(list)

eratho(2000)


"""Line #    Mem usage    Increment   Line Contents
================================================
   206     13.4 MiB     13.4 MiB   @profile
   207                             def eratho(n):
   208     13.4 MiB      0.0 MiB       list = []
   209     13.5 MiB      0.0 MiB       for i in range(2, n):
   210     13.5 MiB      0.1 MiB           list.append(i)
   211     13.5 MiB      0.0 MiB       for num in list:
   212     13.6 MiB      0.0 MiB           for elem in list:
   213     13.5 MiB      0.0 MiB               if elem % num == 0 and elem != num:
   214     13.5 MiB      0.0 MiB                   list.remove(elem)
   215     13.5 MiB      0.0 MiB       print(list)
   
   При создании множества от 2 до 10000 создается незначительная нагрузка на память.
   Но прирост незначительный и создание множества - особенность данного алгоритма, 
   обойтись без неё не получится.
   
   В целом по данным примерам видно, что наши объемы данных не создают нагрузки на память, рекурсии и циклы
   в наших примерах более требовательны к процессорному времени. Также понятно, 
   что профилирование в больших проектах - вещь необходимая, утечки памяти могут приводить к потере работоспособности кода.
   """
