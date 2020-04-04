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
import timeit


def sieve_without_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена»
    '''

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    используя алгоритм «Решето Эратосфена»
    '''

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    '''Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Функция основана на теореме о
    распределении простых чисел, она утверждает, что функция
    распределения простых чисел. Количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    '''

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

for TEST_VALUE in [10,100,1000, 10000] :

    time1 = timeit.timeit(f'sieve_without_eratosthenes({TEST_VALUE})',
                          setup='from __main__ import sieve_without_eratosthenes',
                          number=NUMBER_EXECUTIONS)

    time2 = timeit.timeit(f'sieve_eratosthenes({TEST_VALUE})',
                          setup='from __main__ import sieve_eratosthenes',
                          number=NUMBER_EXECUTIONS)

    print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее программы с использованием алгоритма «Решето Эратосфена» в \
    {round(time2 / time1, 2)} раз для N={TEST_VALUE}'
          )
