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


import sys
from math import sqrt, ceil
import numpy
from memory_profiler import profile


@profile
def prime(num):
    '''
    Моя новая версия решета.
    Return list of prime numbers up to argument num
    '''
    # распаковка range в список
    *primes_lst, = range(num)
    # print(sys.getrefcount(10)) # для проверки ПРИЧИНЫ 2 (описание ниже)
    # исключаем четные (зануляем)
    primes_lst[4::2] = [0] * len(primes_lst[4::2])
    # цикл с 3 до корня из num
    for i in range(3, ceil(sqrt(num)), 2):
        if primes_lst[i]:  # если число еще не занулено
            # зануляем кратные c шагом 2*i
            primes_lst[i * i::2 * i] = [0] * len(primes_lst[i * i::2 * i])
    # убираем нули , сортируем, возвращаем
    return list(filter(bool, primes_lst))[1:]


@profile
def prime_numpy(num):
    '''
    Немного оптимизированная версия решета с помощью NumPy
    Return list of prime numbers up to argument num
    '''
    # список единиц, потом будем их занулять
    primes_lst = numpy.ones(num, dtype=bool)
    # исключаем четные (зануляем)
    primes_lst[4::2] = [0] * len(primes_lst[4::2])
    # цикл с 3 до корня из num
    for i in range(3, ceil(sqrt(num)), 2):
        if primes_lst[i]:  # если число еще не занулено
            # зануляем кратные c шагом 2*i
            primes_lst[i * i::2 * i] = [0] * len(primes_lst[i * i::2 * i])
    # убираем нули , сортируем, возвращаем
    return numpy.nonzero(primes_lst)[0][2:]


# print(sys.getrefcount(10)) # для проверки ПРИЧИНЫ 2 (описание ниже)
prime(10000000)
# print(sys.getrefcount(10)) # для проверки ПРИЧИНЫ 2 (описание ниже)
prime_numpy(10000000)

'''
При запуске prime и prime_numpy с малыми аргументами разницы практически нет,
так как массивы чисел занимают достаточно мало места по сравнению с вызовом profiler'а.

С увеличением аргумента становится видно, что
NumPy дает значительное уменьшение памяти по сравнению с обычным решетом.

Причина 1:
В NumPy тип bool(можно было и int8), который я использовал для хранения нулей и единиц
занимает 1байт для каждого элемента, элемент целого числа обычного списка list() занимает 8 байт.
Таким образом приемущество по памяти как минимум в 8 раз.
print(sys.getsizeof([1])-sys.getsizeof([])) # вывод: 8
print(numpy.ones(1, dtype=numpy.bool).itemsize) # вывод: 1

Причина 2:
В первой функции мы используем числа 1,2,3,4....num - то есть разные объекты.
Во второй мы используем 2 объекта 0 и 1 (true и false). Python умеет оптимизировать
выполнение кода (что-то типа кэширования) - в памяти скорее всего используются
одни и те же объекты 0 и 1 новые не создаются, добавляются только ссылки на существующие

Если в первой функции заменить range(num) на [1]*num, то приемущество NumPy
по памяти стремится к 8 разам ~76MiB  против 9.6MiB, что косвенно подтверждает причину 2.
Также это предположение было подтверждено с помощью добавления print(sys.getrefcount(10))
в текст первой функции после строки с range, а также ДО и ПОСЛЕ выполнения функции.
до выполнения было 76 ссылок на объект 10
при выполнении функции стало 77 ссылок на объект 10
После выполнения снова стало 76 ссылок на объект 10


Ниже приведен результат замера памяти при запуске обеих функций с аргументом = 10 000 000.
Вывод: NumPy - круто =)

Комментарии удалены из вывода:
Line #    Mem usage    Increment   Line Contents
================================================
    20     25.9 MiB     25.9 MiB   @profile
    21                             def prime(num):
    27    413.1 MiB    387.2 MiB       *primes_lst, = range(num)
    29    413.1 MiB      0.0 MiB       primes_lst[4::2] = [0] * len(primes_lst[4::2])
    31    415.0 MiB      0.0 MiB       for i in range(3, ceil(sqrt(num)), 2):
    32    415.0 MiB      0.0 MiB           if primes_lst[i]:
    34    415.0 MiB      1.9 MiB               primes_lst[i * i::2 * i] = [0] * len(primes_lst[i * i::2 * i])
    36    420.0 MiB      5.0 MiB       return list(filter(bool, primes_lst))[1:]

Line #    Mem usage    Increment   Line Contents
================================================
    42     28.4 MiB     28.4 MiB   @profile
    43                             def prime_numpy(num):
    49     37.9 MiB      9.6 MiB       primes_lst = numpy.ones(num, dtype=bool)
    51     37.9 MiB      0.0 MiB       primes_lst[4::2] = [0] * len(primes_lst[4::2])
    53     37.9 MiB      0.0 MiB       for i in range(3, ceil(sqrt(num)), 2):
    54     37.9 MiB      0.0 MiB           if primes_lst[i]:
    56     37.9 MiB      0.0 MiB               primes_lst[i * i::2 * i] = [0] * len(primes_lst[i * i::2 * i])
    58     42.1 MiB      4.1 MiB       return numpy.nonzero(primes_lst)[0][2:]
'''
