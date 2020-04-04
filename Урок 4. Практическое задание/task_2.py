"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import math
import cProfile
import timeit

def eratosthenes1(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
# O(n+1+(1/2)n^2+1) == O(n^2)

def eratosthenes2(n):
    # число, до которого хотим найти простые числа
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    a = list(filter(lambda x: x != 0, numbers))
    return a
# O(n+(1/2)*n^2+1+n) == O((1/2)*n^2)


def eratosthenes3(n):
    s = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)] for i in sub]]
    return s
# O(n*n*n) == O((1/2)n^3)

def eratosthenes4(n):
    a = True #n - число, до которого хотим дойти
    res = []
    for x in range(1,n):
        for y in range(1,n):
            if x != y and y != 1:
                if not x % y:
                    a = False
                    break
        if a == True:
            res.append(x)
        a = True
    return res

# O(n*n + n) == O(n^2)


def eratosthenes5(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if sieve[x] != 0]
    return sieve1
# O(1 + (1/2)n*n + n) == O((1/2)n^2)


def not_eratosthenes(n):
    list_num = list(range(1, n+1))
    for i in range(1, len(list_num)):
        nod = 2
        while nod != list_num[i]:
            if list_num[i] != nod and list_num[i] % nod==0:
                list_num[i] = 0
                break
            nod += 1
    return list_num
# O(n*n + n + 1) == O(n^2)

def my_eratosthenes(n):
    list_num = list(range(n+1))
    list_num [1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in list_num:
        if i < math.sqrt(n): # проверка что делитель меньше корня из конечного числа
            if i > 1:
                for j in range(i + i, len(list_num ), i):
                    list_num [j] = 0
        else:
            return list_num
# O(1 + n*n^(1/2) + n + 1) == O(n^(3/2))

list_n = [100, 1000, 10000]
for n in list_n:
    print("Моя доработаная функция секунд:    ",timeit.timeit("my_eratosthenes(n)", setup="from __main__ import my_eratosthenes, n", number=1))
    print("Без решета, с перебром НОД секунд: ", timeit.timeit("not_eratosthenes(n)", setup="from __main__ import not_eratosthenes, n", number=1))
    print("Реализация 1 секунд :              ", timeit.timeit("eratosthenes1(n)", setup="from __main__ import eratosthenes1, n", number=1))
    print("Реализация 2 секунд :              ", timeit.timeit("eratosthenes2(n)", setup="from __main__ import eratosthenes2, n", number=1))
    print("Реализация 3 секунд :              ", timeit.timeit("eratosthenes3(n)", setup="from __main__ import eratosthenes3, n", number=1))
    print("Без решета, с перебром НОД  секунд:", timeit.timeit("eratosthenes4(n)", setup="from __main__ import eratosthenes4, n", number=1))
    print("Реализация 5 секунд :              ", timeit.timeit("eratosthenes5(n)", setup="from __main__ import eratosthenes5, n", number=1))
    print('----------------------------------')

"""
Добавил в своей реализацие проверку n < sqrt(N), тем самым ускорив ее в 2 раза.
Самой медленной оказалась реализация на генраторах, при том с увеличением n время работы уыеличивается в разы, потом идет реализация полный перебор каждого числа по его делителям. 

Моя доработаная функция секунд:     2.187999999999496e-05
Без решета, с перебром НОД секунд:  0.00025928199999999957
Реализация 1 секунд :               2.1880000000001898e-05
Реализация 2 секунд :               3.3185000000005016e-05
Реализация 3 секунд :               0.0036602170000000003
Без решета, с перебром НОД  секунд: 0.00030486600000000086
Реализация 5 секунд :               3.063199999999572e-05
----------------------------------
Моя доработаная функция секунд:     0.00012034200000000245
Без решета, с перебром НОД секунд:  0.018142818000000005
Реализация 1 секунд :               0.00023338999999999999
Реализация 2 секунд :               0.00036977800000000116
Реализация 3 секунд :               0.511081119
Без решета, с перебром НОД  секунд: 0.019372857999999993
Реализация 5 секунд :               0.0003004899999999866
----------------------------------
Моя доработаная функция секунд:     0.0014896869999999618
Без решета, с перебром НОД секунд:  1.441759078
Реализация 1 секунд :               0.002377298999999944
Реализация 2 секунд :               0.0038782910000003668
Реализация 3 секунд :               66.119807293
Без решета, с перебром НОД  секунд: 1.5127947149999983
Реализация 5 секунд :               0.002951658999990059
----------------------------------

"""