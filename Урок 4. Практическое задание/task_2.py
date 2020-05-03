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


def get_prime_number_eratosthenes(number):
    if number > 1229:
        # Функция разработана только для параметра <= 1229
        # так как решето эратосфена для целей задачи рассчитываем до 10000
        # при необходимости этот параметр можем увеличить
        return None  # Признак ошибочного завершения

    lst = [i for i in range(2, 10000)]

    for n in range(len(lst)):
        p = lst[n]
        if not p:
            continue
        k = n
        while True:
            if k + p >= len(lst):
                break
            lst[k + p] = 0
            k += p

    result = [i for i in lst if i]

    return result[number - 1]


def get_prime_number_simple(number):
    i = 1
    prime_number = 2
    while i < number:
        prime_number += 1
        for k in range(2, prime_number):
            if prime_number % k == 0:
                break
        else:
            i += 1
    return prime_number


print(get_prime_number_eratosthenes(100))
print(get_prime_number_simple(100))

# 10
print("get_prime_number_eratosthenes(10)=",
      timeit.timeit("get_prime_number_eratosthenes(10)",
                    setup="from __main__ import get_prime_number_eratosthenes",
                    number=50))
print("get_prime_number_simple(10)=",
      timeit.timeit("get_prime_number_simple(10)",
                    setup="from __main__ import get_prime_number_simple",
                    number=50))

# 100
print("get_prime_number_eratosthenes(100)=",
      timeit.timeit("get_prime_number_eratosthenes(100)",
                    setup="from __main__ import get_prime_number_eratosthenes",
                    number=50))
print("get_prime_number_simple(100)=",
      timeit.timeit("get_prime_number_simple(100)",
                    setup="from __main__ import get_prime_number_simple",
                    number=50))

# 1000
print("get_prime_number_eratosthenes(1000)=",
      timeit.timeit("get_prime_number_eratosthenes(1000)",
                    setup="from __main__ import get_prime_number_eratosthenes",
                    number=50))
print("get_prime_number_simple(1000)=",
      timeit.timeit("get_prime_number_simple(1000)",
                    setup="from __main__ import get_prime_number_simple",
                    number=50))

# Анализируем:

# get_prime_number_eratosthenes(10)= 0.6521514
# get_prime_number_simple(10)= 0.0017209000000000252
# get_prime_number_eratosthenes(100)= 0.6730517
# get_prime_number_simple(100)= 0.17253659999999993
# get_prime_number_eratosthenes(1000)= 0.6638286999999998
# get_prime_number_simple(1000)= 22.085386

# Вывод:
# При использовании решета Эратосфена время постоянно
# так как сложность алгоритма O(nlog(log n))
# Важно! в этой функции n-константа и равна 10000, а не входному параметру
# кажется на вебинаре это не обсуждалось и мне кажется это не всем было очевидно - например мне)
# таким образом, сложность алгоритма решета Эратосфена в данной реализации НЕ завитит от входящего параметра!
# Сложность простого алгорится равняется О(n^2) - квадратичная
# таким образом, сложность простого алгоритма СИЛЬНО завитит от входящего параметра!
# Вывод:
# Использование алгоритма решета Эратосфена оправдано, если предполагается его использование с большими числами
