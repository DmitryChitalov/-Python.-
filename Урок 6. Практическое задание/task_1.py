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

from math import sqrt
from random import randint
import timeit
from memory_profiler import profile


"""Python 3.8.0, Windows 64 bit"""

@profile
def max_frq_number_1(LST):
    """Функция возвращает число, встречающееся в массиве чаще всего"""
    MAX_FRQ_NUM = LST[0]
    MAX_FRQ = 1
    for i in range(len(LST)-1):
        FRQ = 1
        for j in range(i+1, len(LST)):
            if LST[j] == LST[i]:
                FRQ += 1
        if FRQ > MAX_FRQ:
            MAX_FRQ = FRQ
            MAX_FRQ_NUM = LST[i]
    return MAX_FRQ_NUM

@profile
def max_frq_number_2(lst):
    """Функция возвращает число, встречающееся в массиве чаще всего"""
    NUMBER = max(lst, key=lst.count)
    return NUMBER

M = [5, 6, 12, 3, 3, 12, 46, 3, 3, 3, 12, 12, 3, 3, 89]
print(max_frq_number_1(M))
print(max_frq_number_2(M))

"""Результат:

Line #    Mem usage    Increment   Line Contents
================================================
    18     13.2 MiB     13.2 MiB   @profile
    19                             def max_frq_number_1(LST):
    20     13.2 MiB      0.0 MiB       MAX_FRQ_NUM = LST[0]
    21     13.2 MiB      0.0 MiB       MAX_FRQ = 1
    22     13.2 MiB      0.0 MiB       for i in range(len(LST)-1):
    23     13.2 MiB      0.0 MiB           FRQ = 1
    24     13.2 MiB      0.0 MiB           for j in range(i+1, len(LST)):
    25     13.2 MiB      0.0 MiB               if LST[j] == LST[i]:
    26     13.2 MiB      0.0 MiB                   FRQ += 1
    27     13.2 MiB      0.0 MiB           if FRQ > MAX_FRQ:
    28     13.2 MiB      0.0 MiB               MAX_FRQ = FRQ
    29     13.2 MiB      0.0 MiB               MAX_FRQ_NUM = LST[i]
    30     13.2 MiB      0.0 MiB       return MAX_FRQ_NUM


Line #    Mem usage    Increment   Line Contents
================================================
    32     13.3 MiB     13.3 MiB   @profile
    33                             def max_frq_number_2(lst):
    34     13.3 MiB      0.0 MiB       NUMBER = max(lst, key=lst.count)
    35     13.3 MiB      0.0 MiB       return NUMBER
    
Вывод:
Результат работы профилировщика памяти показывают,что в обоих алгоритмах оптимизация не требуется
(нет приращения памяти). Лучше использовать второй алгоритм. Он требует чуть больше памяти, однако
по времения выполняется значительно быстрее первого. 
Результаты замеров с использованием timeit: 
свой алгоритм - 0.0199637
фунция max с параметром key - 0.0034245.
Ну и сам код гораздо лаконичнее."""


@profile
def prime_1(n):
    """Перебор делителей"""
    m = n * 10
    primes = [2]
    for i in range(3, m + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in primes:
            if j*j - 1 > i:
                primes.append(i)
                break
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes[n - 1]

@profile
def prime_2(n):
    """Использование множеств"""
    l = 2
    m = n * 10
    my_set = set(range(2, m))
    for j in range(2, int(sqrt(m))):
        if j in my_set:
            my_set -= set(range(2*j, m, j))
    primes = sorted(list(my_set))
    return primes[n - 1]

@profile
def prime_erat(n):
    """Решето Эратосфена"""
    l = 2
    m = n * 10
    lst = [i for i in range(m)]
    lst[1] = 0
    while l < m:
        if lst[l] != 0:
            p = l * 2
            while p < m:
                lst[p] = 0
                p += l
        l += 1
    primes = [lst[i] for i in lst if lst[i] != 0]
    #del lst
    return primes[n - 1]

print(prime_1(1000))
print(prime_2(1000))
print(prime_erat(1000))

"""Результат:

Line #    Mem usage    Increment   Line Contents
================================================
    86     13.3 MiB     13.3 MiB   @profile
    87                             def prime_1(n):
    88                                 '''Перебор делителей'''
    89     13.3 MiB      0.0 MiB       m = n*10
    90     13.3 MiB      0.0 MiB       primes = [2]
    91     13.3 MiB      0.0 MiB       for i in range(3, m + 1, 2):
    92     13.3 MiB      0.0 MiB           if (i > 10) and (i % 10 == 5):
    93     13.3 MiB      0.0 MiB               continue
    94     13.3 MiB      0.0 MiB           for j in primes:
    95     13.3 MiB      0.0 MiB               if j*j -1 > i:
    96     13.3 MiB      0.0 MiB                   primes.append(i)
    97     13.3 MiB      0.0 MiB                   break
    98     13.3 MiB      0.0 MiB               if i % j == 0:
    99     13.3 MiB      0.0 MiB                   break
   100                                     else:
   101     13.3 MiB      0.0 MiB               primes.append(i)
   102     13.3 MiB      0.0 MiB       return primes[n-1]


Line #    Mem usage    Increment   Line Contents
================================================
   104     13.3 MiB     13.3 MiB   @profile
   105                             def prime_2(n):
   106                                 '''Использование множеств'''
   107     13.3 MiB      0.0 MiB       l = 2
   108     13.3 MiB      0.0 MiB       m = n*10
   109     13.8 MiB      0.4 MiB       my_set = set(range(2, m))
   110     13.9 MiB      0.0 MiB       for j in range(2, int(sqrt(m))):
   111     13.9 MiB      0.0 MiB           if j in my_set:
   112     13.9 MiB      0.1 MiB               my_set -= set(range(2*j, m, j))
   113     13.6 MiB      0.0 MiB       primes = sorted(list(my_set))
   114     13.6 MiB      0.0 MiB       return primes[n-1]


Line #    Mem usage    Increment   Line Contents
================================================
   116     13.4 MiB     13.4 MiB   @profile
   117                             def prime_erat(n):
   118                                 '''Решето Эратосфена'''
   119     13.4 MiB      0.0 MiB       l = 2
   120     13.4 MiB      0.0 MiB       m = n*10
   121     13.5 MiB      0.0 MiB       lst = [i for i in range(m)]
   122     13.5 MiB      0.0 MiB       lst[1] = 0
   123     13.5 MiB      0.0 MiB       while l < m:
   124     13.5 MiB      0.0 MiB           if lst[l] != 0:
   125     13.5 MiB      0.0 MiB               p = l * 2
   126     13.5 MiB      0.0 MiB               while p < m:
   127     13.5 MiB      0.0 MiB                   lst[p] = 0
   128     13.5 MiB      0.0 MiB                   p += l
   129     13.5 MiB      0.0 MiB           l += 1
   130     13.5 MiB      0.0 MiB       primes = [lst[i] for i in lst if lst[i] != 0]
   131                                 #del lst
   132     13.5 MiB      0.0 MiB       return primes[n - 1]
   
Вывод: 
Совсем небольшой инкремент появляется во втором алгоритме при создании множеств, 
затем при вычитании одного множества из другого память немного высвобождается.
В решете инкремент незначительный возникает при генерации списков. Оптимизация не требуется."""


@profile
def func_list_compr():
    """Функция возвращает список индексов четных элементов рандомного массива."""
    M = [randint(0, 100) for i in range(100000)]
    print(M)
    N = [i + 1 for i in range(len(M)) if M[i] % 2 == 0]
    del M
    return N

@profile
def func_iter():
    """Функция возвращает список индексов четных элементов рандомного массива."""
    M = [randint(0, 100) for i in range(100000)]
    print(M)
    N = []
    for i in range(len(M)):
        if M[i] % 2 == 0:
            N.append(i+1)
    del M
    return N

print(func_list_compr())
print(func_iter())

"""Результат:

Line #    Mem usage    Increment   Line Contents
================================================
     4     14.5 MiB     14.5 MiB   @profile
     5                             def func_list_compr():
     6     15.2 MiB      0.2 MiB       M = [randint(0, 100) for i in range(100000)]
     7     14.9 MiB      0.0 MiB       print(M)
     8     16.2 MiB      0.2 MiB       N = [i+1 for i in range(len(M)) if M[i] % 2 == 0]
     9     15.7 MiB      0.0 MiB       del M
    10     15.7 MiB      0.0 MiB       return N


Line #    Mem usage    Increment   Line Contents
================================================
    12     14.8 MiB     14.8 MiB   @profile
    13                             def func_iter():
    14     15.7 MiB      0.2 MiB       M = [randint(0, 100) for i in range(100000)]
    15     16.0 MiB      0.4 MiB       print(M)
    16     16.0 MiB      0.0 MiB       N = []
    17     16.5 MiB      0.0 MiB       for i in range (len(M)):
    18     16.5 MiB      0.0 MiB           if M[i] % 2 == 0:
    19     16.5 MiB      0.1 MiB               N.append(i+1)
    20     15.7 MiB      0.0 MiB       del M
    21     15.7 MiB      0.0 MiB       return N

Вывод:
В обоих алгоритмах инкремент появляется при создании списков. 
Немного памяти освобождается при удалении ссылки на первоначальный список. 
В целом по объему памяти оба алгоритма примерно равнозначны и не нуждаются в оптимизации."""

#Доработала задачу с решетом:
def prime_1(n):
    """Проверяем на делители, сложность O(n^2)"""
    m = n * 10
    primes = []
    for i in range(2, m + 1):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes[n - 1]

def prime_2(n):
    """Перебираем меньше делителей (только те числа, которые заканчиваются на 1, 3, 7 или 9
    и не превосходят корня из проверяемого числа), сложность O(n^2)"""
    m = n * 10
    primes = [2]
    for i in range(3, m + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in primes:
            if j > int(sqrt(i)) + 1:
                primes.append(i)
                break
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes[n - 1]

def prime_3(n):
    """Оптимизированный вариант предыдущей функции - без sqrt(), сложность O(n^2)"""
    m = n * 10
    primes = [2]
    for i in range(3, m + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in primes:
            if j*j - 1 > i:
                primes.append(i)
                break
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes[n - 1]

def prime_4(n):
    """Использование множеств, сложность O(n)"""
    m = n * 10
    my_set = set(range(2, m))
    for j in range(2, int(sqrt(m))):
        if j in my_set:
            my_set -= set(range(2 * j, m, j))
    primes = sorted(list(my_set))
    return primes[n - 1]


def prime_num_erat(n):
    """Использование решета Эратосфена, сложность O(n log(log n))"""
    l = 2
    m = n * 10
    lst = [i for i in range(m)]
    lst[1] = 0
    while l < m:
        if lst[l] != 0:
            p = l * 2
            while p < m:
                lst[p] = 0
                p += l
        l += 1
    primes = [lst[i] for i in lst if lst[i] != 0]
    del lst
    return primes[n - 1]

n = int(input('Введите порядковый номер искомого простого числа: '))
print(timeit.timeit("prime_1(n)", setup="from __main__ import prime_1, n", number=100))
print(timeit.timeit("prime_2(n)", setup="from __main__ import prime_2, n", number=100))
print(timeit.timeit("prime_3(n)", setup="from __main__ import prime_3, n", number=100))
print(timeit.timeit("prime_4(n)", setup="from __main__ import prime_4, n", number=100))
print(timeit.timeit("prime_num_erat(n)", setup="from __main__ import prime_num_erat, n", number=100))

"""Результаты:
Время работы алгоритмов для поиска 10-го простого числа 100 раз:
перебор делителей - 0.00840630000000031
оптимизированный перебор с sqrt() - 0.010825399999999874
оптимизированный перебор без sqrt() - 0.003840900000000147
через множества - 0.0019122000000000305
решето - 0.005409600000000125

Время работы алгоритмов для поиска 100-го простого числа 100 раз:
перебор делителей - 0.09069780000000005
оптимизированный перебор с sqrt() - 0.0749449000000002
оптимизированный перебор без sqrt() - 0.03248659999999992
через множества - 0.014623400000000064
решето - 0.041202699999999925

Время работы алгоритмов для поиска 1000-го простого числа 100 раз:
перебор делителей - 4.7486334
оптимизированный перебор с sqrt() - 1.2320617999999994
оптимизированный перебор без sqrt() - 0.5631740000000001
через множества - 0.17892309999999867
решето - 0.4519409999999997

Вывод: 
Решето дает выйгрыш во времени на больших числах по сравнению с перебором делителей (включая оптимизированный перебор), 
что объясняется его сложностью O(n log(log n)). Обычный перебор имеет квадратичную сложность O(n^2),
поэтому на больших n время его выполнения сильно увеличивается.

Алгоритм, использующий множества, во всех проверках оказался самым быстрым, 
потому что у него линейная сложность.

Также можно отметить, что оптимизированный перебор делителей с функцией sqrt() в цикле 
на маленьких входных данных оказался чуть медленнее неоптимизированного перебора. 
На больших входных данных он выполняется значительно быстрее"""