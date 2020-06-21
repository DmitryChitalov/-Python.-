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

import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                  107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
                  163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
                  227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
                  281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                  353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
                  421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479,
                  487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
                  569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
                  631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                  701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
                  773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853,
                  857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
                  937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} ok')


test_prime(prime)
print(prime(1))

cProfile.run('prime(10)')
cProfile.run('prime(100)')
cProfile.run('prime(1000)')
cProfile.run('prime(10000)')
cProfile.run('prime(100000)')

'''
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_2.py:19(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_2.py:19(prime)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.032    0.032 <string>:1(<module>)
        1    0.032    0.032    0.032    0.032 task_2.py:19(prime)
        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.723 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.723    0.723 <string>:1(<module>)
        1    0.723    0.723    0.723    0.723 task_2.py:19(prime)
        1    0.000    0.000    0.723    0.723 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



'''
