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
from timeit import Timer


def non_erat(num):
    numbers = [i for i in range(2,10000)]
    counter = 0
    primal_counter = 0
    for i in numbers:
        if primal_counter == num:
            return i-1
        counter += 1
        is_primal = True
        for j in range(2, i):
            if i % j == 0:
                is_primal = False
                break
        if is_primal:
            primal_counter += 1



def erat(num):
    *primes, = [i for i in range(2,10000)]
    primes[4::2] = [0] * len(primes[4::2])
    for i in range(3, math.ceil(num), 2):
        if primes[i]:
            primes[i * i::2*i] * len(primes[i * i::2*i])
    return sorted(set(primes))[2:]


t1 = Timer("non_erat(USER_NUMBER)", "from __main__ import non_erat, USER_NUMBER")
t2 = Timer("erat(USER_NUMBER)", "from __main__ import erat, USER_NUMBER")

USER_NUMBER = 10
print(f"При поиске {USER_NUMBER} простого числа с помощью алгоритма "
      f"без решета понадобилось {t1.timeit(number=10)} сек на 10 итераций")
print(f"При поиске {USER_NUMBER} простого числа с помощью алгоритма "
      f"с решетом понадобилось {t2.timeit(number=10)} сек на 10 итераций")
USER_NUMBER = 200
print(f"При поиске {USER_NUMBER} простого числа с помощью алгоритма "
      f"без решета понадобилось {t1.timeit(number=10)} сек на 10 итераций")
print(f"При поиске {USER_NUMBER} простого числа с помощью алгоритма "
      f"с решетом понадобилось {t2.timeit(number=10)} сек на 10 итераций")
USER_NUMBER = 800
print(f"При поиске {USER_NUMBER} простого числа с помощью алгоритма "
      f"без решета понадобилось {t1.timeit(number=10)} сек на 10 итераций")
print(f"При поиске {USER_NUMBER} простого числа с помощью алгоритма "
      f"с решетом понадобилось {t2.timeit(number=10)} сек на 10 итераций")


"""
Алгоритм без решета, который последовательно проверяет числа, имеет сложность O(n^2)
работает эффективнее при малых входных значениях.
При этом решето считается на малых входных данных выходит более трудозатратным.
Но при увеличении входных данных, решето выигрывает, т.к. сложность алгоритма
логорифмическая O(n log n)
"""


