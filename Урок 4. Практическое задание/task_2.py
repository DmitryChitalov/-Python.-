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
import cProfile


def i_prime_num(i_num):
    """Без решета"""
    lst = [2]
    i = 1

    while len(lst) < i_num:
        i += 2
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)

    return lst[-1]


def eratosfen(i):
    """Используя алгоритм «Решето Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]


I_NUM = int(input("Порядковый номер простого числа: "))


def functions():
    i_prime_num(I_NUM)
    eratosfen(I_NUM)


cProfile.run('functions()')
print(timeit.timeit("i_prime_num(I_NUM)",
                    setup="from __main__ import i_prime_num, I_NUM", number=100))
print(timeit.timeit("eratosfen(I_NUM)",
                    setup="from __main__ import eratosfen, I_NUM", number=100))


"""
При i = 10 
0.003059299999999876
2.2717021999999996

При i = 100
0.1595200000000001
2.5655628999999998

При i = 1000
3.283639599999999
2.7138814

Решето было взято из примеров к уроку, его эффективность была замечена при входных данных от 1000
и более соответсвенно оно наиболее эффективно при больших числах
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))
"""
