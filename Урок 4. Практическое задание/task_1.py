"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

"""
# ТО, ЧТО БЫЛО ИЗНАЧАЛЬНО.
(МОДЕРНИЗАЦМЯ НИЖЕ)

import random
import timeit
import cProfile


def max_below_zero(size):
    #  START_RANGE = -999
    #  END_RANGE = -100
    #  SIZE_RANGE = 20

    MY_LIST = [random.randint(size * -10, size * 10) for _ in range(size)]
    #  print(MY_LIST)

    i = 0
    elem = -1

    while i < len(MY_LIST):
        if MY_LIST[i] < 0 and elem == - 1:
            elem = i
        elif 0 > MY_LIST[i] > MY_LIST[elem]:
            elem = i
        i += 1

    if elem != -1:
        #  print(f'Максимально отрицательное число {MY_LIST[elem]}\n'
         #     f'Его индекс = {elem}')
        return f'Максимально отрицательное число {MY_LIST[elem]}\n' \
               f'Его индекс = {elem}'


print(timeit.timeit('max_below_zero(10)', number=1000, globals=globals()))  # 0.02965811000103713
print(timeit.timeit('max_below_zero(100)', number=1000, globals=globals()))  # 0.29577122400041844
print(timeit.timeit('max_below_zero(1000)', number=1000, globals=globals()))  # 3.516053217999797
print(timeit.timeit('max_below_zero(10000)', number=1000, globals=globals()))  # 36.52958169700105


cProfile.run('max_below_zero(10)')
'''
         72 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       10    0.000    0.000    0.000    0.000 random.py:200(randrange)
       10    0.000    0.000    0.000    0.000 random.py:244(randint)
       10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 task_1.py:21(max_below_zero)
        1    0.000    0.000    0.000    0.000 task_1.py:26(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       16    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
cProfile.run('max_below_zero(10000)')
'''
         62979 function calls in 0.042 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.042    0.042 <string>:1(<module>)
    10000    0.011    0.000    0.022    0.000 random.py:200(randrange)
    10000    0.005    0.000    0.027    0.000 random.py:244(randint)
    10000    0.007    0.000    0.010    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.007    0.007    0.041    0.041 task_1.py:21(max_below_zero)
        1    0.006    0.006    0.032    0.032 task_1.py:26(<listcomp>)
        1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
    10001    0.002    0.000    0.002    0.000 {built-in method builtins.len}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12973    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
'''

"""

# МОДЕРНИЗАЦИЯ КОДА

import random
import timeit
import cProfile


def max_below_zero(my_list):
    i = 0
    elem = -1

    while i < len(my_list):
        if my_list[i] < 0 and elem == - 1:
            elem = i
        elif 0 > my_list[i] > my_list[elem]:
            elem = i
        i += 1

    if elem != -1:
        #  print(f'Максимально отрицательное число {MY_LIST[elem]}\n'
         #     f'Его индекс = {elem}')
        return f'Максимально отрицательное число {my_list[elem]}\n' \
               f'Его индекс = {elem}'


size = 1
while size != 10000:
    size *= 10
    my_list = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('max_below_zero(my_list)', number=1000, globals=globals()))


#  0.006055351999748382
#  0.07464794400038954
#  0.743875369998932
#  7.591469463000976

cProfile.run('max_below_zero(my_list)')
'''
         10005 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.006    0.006    0.008    0.008 task_1.py:104(max_below_zero)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''