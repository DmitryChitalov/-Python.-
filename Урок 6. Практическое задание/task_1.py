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
import random
from memory_profiler import profile


@profile
def search_1(N):     # Метод перебора
    NUMBERS = []
    for i in range(2, N + 1):
        for j in NUMBERS:
            if i % j == 0:
                break
        else:
            NUMBERS.append(i)
    return NUMBERS

@profile
def search_2(N):          # Решето Эратосфена
    a = [x for x in range(N+1)]
    a[1] = 0
    NUMBERS = []
    i = 2
    while i <= N:
        if a[i] != 0:
            NUMBERS.append(a[i])
            for j in range(i, N + 1, i):
                a[j] = 0
        i += 1
    return NUMBERS


search_1(1000)
search_2(1000)

'''Line #    Mem usage    Increment   Line Contents
================================================
    23     13.2 MiB     13.2 MiB   @profile
    24                             def search_1(N):     # Метод перебора
    25     13.2 MiB      0.0 MiB       NUMBERS = []
    26     13.2 MiB      0.0 MiB       for i in range(2, N + 1):
    27     13.2 MiB      0.0 MiB           for j in NUMBERS:
    28     13.2 MiB      0.0 MiB               if i % j == 0:
    29     13.2 MiB      0.0 MiB                   break
    30                                     else:
    31     13.2 MiB      0.0 MiB               NUMBERS.append(i)
    32     13.2 MiB      0.0 MiB       return NUMBERS


Filename: C:/Users/marin/Учеба/python/алгоритмы/Lesson 6/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    38     13.3 MiB     13.3 MiB   @profile
    39                             def search_2(N):          # Решето Эратосфена
    40     13.3 MiB      0.0 MiB       a = [x for x in range(N+1)]
    41     13.3 MiB      0.0 MiB       a[1] = 0
    42     13.3 MiB      0.0 MiB       NUMBERS = []
    43     13.3 MiB      0.0 MiB       i = 2
    44     13.3 MiB      0.0 MiB       while i <= N:
    45     13.3 MiB      0.0 MiB           if a[i] != 0:
    46     13.3 MiB      0.0 MiB               NUMBERS.append(a[i])
    47     13.3 MiB      0.0 MiB               for j in range(i, N + 1, i):
    48     13.3 MiB      0.0 MiB                   a[j] = 0
    49     13.3 MiB      0.0 MiB           i += 1
    50     13.3 MiB      0.0 MiB       return NUMBERS
'''

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

A = [random.randint(-100, 100) for i in range(100000)]


@profile
def min_1(A):
    MIN_1 = A[0]
    MIN_2 = A[0]
    for i in A:
        if i < MIN_1:
            MIN_2 = MIN_1
            MIN_1 = i
        elif i < MIN_2:
            MIN_2 = i
    return f'Наименьший элемент: {MIN_1}, Второй наименьший элемент: {MIN_2}'

@profile
def min_2(A):
    B = sorted(A)[:2]
    return f'Наименьший элемент: {B[0]}, Второй наименьший элемент: {B[1]}'


min_1(A)
min_2(A)
'''
Line #    Mem usage    Increment   Line Contents
================================================
    87     15.0 MiB     15.0 MiB   @profile
    88                             def min_1(A):
    89     15.0 MiB      0.0 MiB       MIN_1 = A[0]
    90     15.0 MiB      0.0 MiB       MIN_2 = A[0]
    91     15.0 MiB      0.0 MiB       for i in A:
    92     15.0 MiB      0.0 MiB           if i < MIN_1:
    93     15.0 MiB      0.0 MiB               MIN_2 = MIN_1
    94     15.0 MiB      0.0 MiB               MIN_1 = i
    95     15.0 MiB      0.0 MiB           elif i < MIN_2:
    96     15.0 MiB      0.0 MiB               MIN_2 = i
    97     15.0 MiB      0.0 MiB       return f'Наименьший элемент: {MIN_1}, Второй наименьший элемент: {MIN_2}'


Filename: C:/Users/marin/Учеба/python/алгоритмы/Lesson 6/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    99     15.0 MiB     15.0 MiB   @profile
   100                             def min_2(A):
   101     14.6 MiB      0.0 MiB       B = sorted(A)[:2]
   102     14.6 MiB      0.0 MiB       return f'Наименьший элемент: {B[0]}, Второй наименьший элемент: {B[1]}''''


# Суммы строк и столбцов матрицы

@profile
def fync(N,M):
    EXT_LST = []
    for i in range(N):
        b = []
        for j in range(M):
            b.append(random.randint(0, 10))
            print(f"{b[j]:4d}", end='')
        EXT_LST.append(b)
        print('   |', sum(b))

    for i in range(M):
        print(f" ---", end='')
    print()

    for i in range(M):
        s = 0
        for j in range(N):
            s += EXT_LST[j][i]
        print(f"{s:4d}", end='')
    print()

fync(5, 10)

'''
Line #    Mem usage    Increment   Line Contents
================================================
     9     13.5 MiB     13.5 MiB   @profile
    10                             def fync(N,M):
    11     13.5 MiB      0.0 MiB       EXT_LST = []
    12     13.5 MiB      0.0 MiB       for i in range(N):
    13     13.5 MiB      0.0 MiB           b = []
    14     13.5 MiB      0.0 MiB           for j in range(M):
    15     13.5 MiB      0.0 MiB               b.append(randint(0, 10))
    16     13.5 MiB      0.0 MiB               print(f"{b[j]:4d}", end='')
    17     13.5 MiB      0.0 MiB           EXT_LST.append(b)
    18     13.5 MiB      0.0 MiB           print('   |', sum(b))
    19                             
    20     13.5 MiB      0.0 MiB       for i in range(M):
    21     13.5 MiB      0.0 MiB           print(f" ---", end='')
    22     13.5 MiB      0.0 MiB       print()
    23                             
    24     13.5 MiB      0.0 MiB       for i in range(M):
    25     13.5 MiB      0.0 MiB           s = 0
    26     13.5 MiB      0.0 MiB           for j in range(N):
    27     13.5 MiB      0.0 MiB               s += EXT_LST[j][i]
    28     13.5 MiB      0.0 MiB           print(f"{s:4d}", end='')
    29     13.5 MiB      0.0 MiB       print()'''


'''Было проверено много замеров программ, в поисках чего-нибудь интересного по показателям использования памяти,
но все данные примерно одинаковые. Т.к. мы  не работали с большими обьектами и используются не затратные
операции, то проблем с памятью нет, оптимизация не требуется.'''