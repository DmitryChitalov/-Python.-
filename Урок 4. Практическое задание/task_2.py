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
import timeit


def eratosfen(i):

    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def without_eratosfen(i):
    i = int(i)
    start_num = 2
    slt = []
    s = 0
    while s != i:
        if isPrime(start_num):
            slt.append(start_num)
            s += 1
        start_num += 1
    return slt[s - 1]


i = int(input('i- '))
print(
    timeit.timeit(
        "eratosfen(i)",
        setup="from __main__ import eratosfen, i",
        number=100))
print(
    timeit.timeit(
        "without_eratosfen(i)",
        setup="from __main__ import without_eratosfen, i",
        number=100))

# 0.4782986 - 10 eratosfen()
# 0.0009734000000003462 - 10 without_eratosfen()

# 0.4783588000000001 - 100 eratosfen()
# 0.024854699999999674 - 100 without_eratosfen()

# 0.4787002 - 1000 eratosfen()
# 0.7335972000000002 - 1000 without_eratosfen()

# При работе с поиском простых чисел малого порядкового номера лучше
#  не использовать решето Эратосфена т.к данный алгоритм производителен при работе с большими индексами, а при работе с
# малыми, он уступает аналогу.
