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


def find_simple_number(number_simple: int) -> int:
    """ Без использования «Решета Эратосфена» """
    item_list = [2]
    if number_simple == 1:
        return item_list[-1]
    item = 3
    while len(item_list) < number_simple:
        is_simple = True
        for i in range(2, item):
            if item % i == 0:
                is_simple = False
        if is_simple:
            item_list.append(item)
        item += 1
    return item_list[-1]


def eratosfen(number_simple: int) -> int:
    """ Решето Эратосфена """
    start_list = []
    simple_list = []
    curr_val = 2
    stop_val = number_simple * 10
    if number_simple == 1:
        return curr_val

    for i in range(stop_val):
        start_list.append(i)

    while curr_val < stop_val:
        if start_list[curr_val] != 0:
            j = curr_val * 2
            while j < stop_val:
                start_list[j] = 0
                j = j + curr_val
        curr_val += 1

    for item in start_list:
        if item not in (0, 1):
            simple_list.append(item)

    return simple_list[number_simple - 1]


print('Алгоритм без решета. 10: ',
      timeit.timeit(
          'find_simple_number(10)',
          setup='from __main__ import find_simple_number',
          number=100))
print('Решето Эратосфена. 10: ',
      timeit.timeit(
          'eratosfen(10)',
          setup='from __main__ import eratosfen',
          number=100))

print('Алгоритм без решета. 100: ',
      timeit.timeit(
          'find_simple_number(100)',
          setup='from __main__ import find_simple_number',
          number=100))
print('Решето Эратосфена. 100: ',
      timeit.timeit(
          'eratosfen(100)',
          setup='from __main__ import eratosfen',
          number=100))

print('Алгоритм без решета. 1000: ',
      timeit.timeit(
          'find_simple_number(1000)',
          setup='from __main__ import find_simple_number',
          number=100))
print('Решето Эратосфена. 1000: ',
      timeit.timeit(
          'eratosfen(1000)',
          setup='from __main__ import eratosfen',
          number=100))

# >>>
# Алгоритм без решета. 10:  0.00892442199983634
# Решето Эратосфена. 10:  0.008809271996142343
# Алгоритм без решета. 100:  1.2673220820142888
# Решето Эратосфена. 100:  0.047965599020244554
# Алгоритм без решета. 1000:  216.8564294539974
# Решето Эратосфена. 1000:  0.3913069219852332

# Превосходство алгоритма на основе Решета Эратосфена отчетливо заметно уже
# при нахождении 100 простого числа
# https://yadi.sk/i/5EssPgXtwfu-bw
# При нахождении 1000 простого числа раздница в производительности состояляет
# несколько порядков

# Сложность алгоритма без решета можно оценить как O(n**2)
# Сложность алгоритма Решето Эратосфена можно оценить как O(n log n)

# Посмотрим на профилировку обоих алгоритмов

print(cProfile.run('find_simple_number(1000)'))
print(cProfile.run('eratosfen(1000)'))

# >>>
#         8921 function calls in 2.534 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    2.533    2.533    2.534    2.534 111.py:5(find_simple_number)
#        1    0.000    0.000    2.534    2.534 <string>:1(<module>)
#        1    0.000    0.000    2.534    2.534 {built-in method builtins.exec}
#     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#         11233 function calls in 0.005 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.004    0.004    0.005    0.005 111.py:22(eratosfen)
#        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#    11229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#

# В профайле фунции без решета нет  информации о вложенном цикле for, что не дает
# нам достоверной картины куда уходит так моного времени при работе алгоритма.
