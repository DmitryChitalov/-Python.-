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


def f_sieve(lenghth):
    empty_sieve = [0] * lenghth
    return empty_sieve


def fil_sieve(full_sieve, lenghth):
    for i in range(lenghth):
        full_sieve[i] = i
    full_sieve[1] = 0
    return full_sieve


def filter_sieve(sieve, lenghth):
    number = 2
    while number < lenghth:
        if sieve[number] != 0:
            next_number = number * 2
            while next_number < lenghth:
                sieve[next_number] = 0
                next_number = next_number + number
        number += 1
    return sieve


def eratosphen(lenghth):
    lenghth += 1
    sieve = f_sieve(lenghth)
    sieve = fil_sieve(sieve, lenghth)
    sieve = filter_sieve(sieve, lenghth)
    result = [x for x in sieve if sieve[x] != 0]
    return result


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosfen_2(i):
    """Используя алгоритм «Решето Эратосфена»"""
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


n = int(input("вывод простых чисел до числа(включительно) ...  "))

print(timeit.timeit("simple(n)", setup="from __main__ import simple, n", number=100))
print(timeit.timeit("eratosphen(n)", setup="from __main__ import eratosphen, n", number=100))
print(timeit.timeit("eratosfen_2(n)", setup="from __main__ import eratosfen_2, n", number=100))

'''
протостой (2)              - 0.00011709999999998111
эратосфен_мой (2)          - 0.00014209999999992284
эратосфен_из примера(2)    - 0.38345380000000007


протостой (10)          - 0.0019013000000001057
эратосфен_мой (10)      - 0.00040210000000051593
эратосфен_из примера    - 0.3767738000000005

протостой (100)              - 0.23605890000000018
эратосфен_мой (100)         - 0.0036259000000002928
эратосфен_из примера(100)   - 0.3768948999999999

протостой (1000)            - 38.835698
эратосфен_мой (1000)        - 0.03892820000000086
эратосфен_из примера(1000)  - 0.4883371999999966
 
 
Сложность алгоритма без решета O(n^2)
Сложность алгоритма решето Эратосфена O(n log(log n))
 
Итоги: иратосфен имеет приемуществот при любых цифрах, если выполнение алгоритма разбить на отдельные
составлюящие, могу предположить, это происходит за счет разницы обрабоки того что "под капотом у pyton-a"

При написании "кода полотном", при цифрах до 100 лучше использовать без решетовый алгорим, а выше с использованием.

'''
