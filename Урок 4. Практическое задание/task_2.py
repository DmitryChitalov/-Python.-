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
from timeit import Timer


def eratosthenes(n=1000):
    sieve = list(range(n + 1))
    sieve[1] = 0  
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve


def myFunc(n=1000):
    b = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            b.append(i)
    return b


t1 = Timer("eratosthenes()", "from __main__ import eratosthenes")
print("eratosthenes_test ", t1.timeit(number=10), "milliseconds")
t2 = Timer("myFunc()", "from __main__ import myFunc")
print("myFunc_test ", t2.timeit(number=10), "milliseconds")

"""
10 элементов
eratosthenes_test  0.00010439999999999061 milliseconds
myFunc_test  0.00014409999999999423 milliseconds
при данном колличестве элементов,
разница во времени выполнения практически отсутствует

100 элементов
eratosthenes_test  0.0006730999999999959 milliseconds
myFunc_test  0.011630100000000004 milliseconds

1000 элементов
eratosthenes_test  0.007220999999999991 milliseconds
myFunc_test  1.1149781 milliseconds
При увеличении колличества элементов «Решето Эратосфена»
является наиболее эффективным вариантом для выполнения поставленной задачи
Сложность простого алгоритма О(n^2)
Сложность «Решета Эратосфена» О(n log(log n))
"""
