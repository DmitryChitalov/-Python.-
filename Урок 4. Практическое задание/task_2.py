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
from math import sqrt


# Не решето
def sieve3(num_cnt):
    num = cnt = 1
    while cnt <= num_cnt:
        num += 1
        cnt += 1 if len([i for i in range(2, num + 1) if num % i == 0 and num != i]) == 0 else 0
    return num


# Самое быстрое "не решето", что я придумал
def sieve4(num_cnt):
    num = cnt = 1
    while cnt <= num_cnt:
        num += 1
        for i in range(2, num // 2 + 1):
            if num % i == 0 and num != i:
                cnt -= 1
                break
        cnt += 1
    return num


# Не решето 1 вар.
def sieve1():
    my_array2 = []
    my_array = list(range(3, MAX_NUMBER + 1, 2))
    my_array.append(2)
    for ii in range(2, round(sqrt(MAX_NUMBER))):
        for iii in my_array:
            if iii % ii != 0 or iii <= ii:
                my_array2.append(iii)
        my_array = my_array2[:]
        my_array2 = []


# Решето
def sieve2():
    a = list(range(MAX_NUMBER + 1))
    m = 2
    while m < MAX_NUMBER:
        if a[m] != 0:
            j = m * 2
            while j < MAX_NUMBER:
                a[j] = 0
                j = j + m
        m += 1
    b = [i for i in a if i != 0]
    return len(b)


MAX_NUMBER = 23
t1 = timeit.timeit('sieve4(10)', 'from __main__ import sieve4', number=100)
t2 = timeit.timeit('sieve2()', 'from __main__ import sieve2', number=100)
print(10, t1, t2, t1 / t2)

MAX_NUMBER = 523
t3 = timeit.timeit('sieve4(100)', 'from __main__ import sieve4', number=100)
t4 = timeit.timeit('sieve2()', 'from __main__ import sieve2', number=100)
print(100, t3, t4, t3 / t4)

MAX_NUMBER = 7905
t5 = timeit.timeit('sieve4(1000)', 'from __main__ import sieve4', number=100)
t6 = timeit.timeit('sieve2()', 'from __main__ import sieve2', number=100)
print(1000, t5, t6, t5 / t6)

t7 = timeit.timeit('sieve4(600)', 'from __main__ import sieve4', number=100)

# ВЫВОД: при любом порядковом номере простого числа выигрывает Решето, однако если
# на сравнительно небольших порядковых номерах прочтых чисел
# < 10 разница во времени выполнения отличается в 2 раза, при 100 в 5 раз
# при 1000 в 66 раз, что явно указывает на разную сложность Алгоритмов
# решето выглядит как линейная O(n), а моя O(n**3)
