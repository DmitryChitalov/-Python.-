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
# Анализировать будем задание 2-9-2
# Слегка модифицируем решение для того что бы избежать ручного ввода

import os
import random
import timeit
import cProfile
import sys

sys.setrecursionlimit(100000)
MIN_DIG = 1
MAX_DIG = 1000000


def get_digits_sum(num):
    if num == 0:
        return 0
    category = 10 ** (len(str(num)) - 1)
    cur_digit = num // category
    return cur_digit + get_digits_sum(num - cur_digit * category)


def recursion(num_count, max_num=0, max_sum=0):
    if num_count == 0:
        # print(
        #     f'Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max_sum}')
        return
    num = random.randint(MIN_DIG, MAX_DIG)
    # num = int(input(f'Введите число № {str(num_count)}: '))
    cur_sum = get_digits_sum(num)
    if cur_sum > max_sum:
        recursion(num_count - 1, num, cur_sum)
    else:
        recursion(num_count - 1, max_num, max_sum)


cProfile.run('recursion(7000)')

"""
Наибольшее число по сумме цифр: 699898, сумма его цифр: 49
         124923 function calls (80144 primitive calls) in 0.055 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.055    0.055 <string>:1(<module>)
     7000    0.004    0.000    0.008    0.000 random.py:200(randrange)
     7000    0.002    0.000    0.011    0.000 random.py:244(randint)
     7000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
44779/7000   0.032    0.000    0.035    0.000 task_1.py:25(get_digits_sum)
   7001/1    0.009    0.000    0.055    0.055 task_1.py:33(recursion)
        1    0.000    0.000    0.055    0.055 {built-in method builtins.exec}
    37779    0.003    0.000    0.003    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     7000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     7360    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

"""


# Видно, главное узкое место в представленном коде: Вызов функции get_digits_sum
# Попробуем оптимизировать код этой функции - сделаем без рекурсии

def get_digits_sum2(num):
    return sum((int(i) for i in str(num)))


def recursion2(num_count, max_num=0, max_sum=0):
    if num_count == 0:
        # print(
        #    f'Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max_sum}')
        return
    num = random.randint(MIN_DIG, MAX_DIG)
    # num = int(input(f'Введите число № {str(num_count)}: '))
    cur_sum = get_digits_sum2(num)
    if cur_sum > max_sum:
        recursion2(num_count - 1, num, cur_sum)
    else:
        recursion2(num_count - 1, max_num, max_sum)


cProfile.run('recursion2(7000)')

"""
Наибольшее число по сумме цифр: 898988, сумма его цифр: 50
         104613 function calls (97613 primitive calls) in 0.039 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
     7000    0.005    0.000    0.010    0.000 random.py:200(randrange)
     7000    0.003    0.000    0.012    0.000 random.py:244(randint)
     7000    0.003    0.000    0.005    0.000 random.py:250(_randbelow_with_getrandbits)
     7000    0.004    0.000    0.018    0.000 task_1.py:76(get_digits_sum2)
    48244    0.008    0.000    0.008    0.000 task_1.py:77(<genexpr>)
   7001/1    0.009    0.000    0.039    0.039 task_1.py:79(recursion2)
        1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     7000    0.006    0.000    0.014    0.000 {built-in method builtins.sum}
     7000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     7364    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

"""

# отказ от рекурсии в данной функции принес ощутимый прирост скорости.
# А не замахнться ли нам на мемоизацию?
memory = {}


def mem_me(func):
    def q(n):
        tmp = memory.get(n)
        if tmp is None:
            tmp = func(n)
            memory[n] = tmp
        return tmp

    return q


@mem_me
def get_digits_sum3(num):
    return sum((int(i) for i in str(num)))


def recursion3(num_count, max_num=0, max_sum=0):
    if num_count == 0:
        # print(
        #    f'Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max_sum}')
        return
    num = random.randint(MIN_DIG, MAX_DIG)
    # num = int(input(f'Введите число № {str(num_count)}: '))
    cur_sum = get_digits_sum3(num)
    if cur_sum > max_sum:
        recursion3(num_count - 1, num, cur_sum)
    else:
        recursion3(num_count - 1, max_num, max_sum)


cProfile.run('recursion3(7000)')

"""
Наибольшее число по сумме цифр: 977899, сумма его цифр: 49
         118312 function calls (111312 primitive calls) in 0.041 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.041    0.041 <string>:1(<module>)
     7000    0.004    0.000    0.009    0.000 random.py:200(randrange)
     7000    0.002    0.000    0.011    0.000 random.py:244(randint)
     7000    0.003    0.000    0.005    0.000 random.py:250(_randbelow_with_getrandbits)
     7000    0.003    0.000    0.022    0.000 task_1.py:125(q)
     6973    0.004    0.000    0.017    0.000 task_1.py:134(get_digits_sum3)
    48018    0.008    0.000    0.008    0.000 task_1.py:136(<genexpr>)
   7001/1    0.008    0.000    0.041    0.041 task_1.py:138(recursion3)
        1    0.000    0.000    0.041    0.041 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     6973    0.005    0.000    0.013    0.000 {built-in method builtins.sum}
     7000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     7000    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     7343    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

# Эффект нулевой - ну это собственно и предполагалось т.к. словарь просто не успевает набраться
# из-за большого кол-ва вариантов
# Уменьшим разброс исходных данных

MIN_DIG = 99999900
MAX_DIG = 99999999
memory = {}

cProfile.run('recursion(7000)')
cProfile.run('recursion2(7000)')
cProfile.run('recursion3(7000)')

"""
Наибольшее число по сумме цифр: 99999999, сумма его цифр: 72
         160210 function calls (98568 primitive calls) in 0.062 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.062    0.062 <string>:1(<module>)
     7000    0.004    0.000    0.008    0.000 random.py:200(randrange)
     7000    0.002    0.000    0.010    0.000 random.py:244(randint)
     7000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
61642/7000    0.041    0.000    0.045    0.000 task_1.py:27(get_digits_sum)
   7001/1    0.007    0.000    0.062    0.062 task_1.py:35(recursion)
        1    0.000    0.000    0.062    0.062 {built-in method builtins.exec}
    54642    0.004    0.000    0.004    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     7000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     8921    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


Наибольшее число по сумме цифр: 99999999, сумма его цифр: 72
         121005 function calls (114005 primitive calls) in 0.035 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.035    0.035 <string>:1(<module>)
     7000    0.004    0.000    0.008    0.000 random.py:200(randrange)
     7000    0.002    0.000    0.010    0.000 random.py:244(randint)
     7000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
     7000    0.003    0.000    0.018    0.000 task_1.py:76(get_digits_sum2)
    63000    0.009    0.000    0.009    0.000 task_1.py:77(<genexpr>)
   7001/1    0.007    0.000    0.035    0.035 task_1.py:79(recursion2)
        1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
     7000    0.006    0.000    0.015    0.000 {built-in method builtins.sum}
     7000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     9000    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


Наибольшее число по сумме цифр: 99999999, сумма его цифр: 72
         59044 function calls (52044 primitive calls) in 0.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
     7000    0.004    0.000    0.008    0.000 random.py:200(randrange)
     7000    0.002    0.000    0.010    0.000 random.py:244(randint)
     7000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
     7000    0.001    0.000    0.003    0.000 task_1.py:123(q)
      100    0.000    0.000    0.000    0.000 task_1.py:132(get_digits_sum3)
      900    0.000    0.000    0.000    0.000 task_1.py:134(<genexpr>)
   7001/1    0.007    0.000    0.019    0.019 task_1.py:136(recursion3)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      100    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
     7000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     7000    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     8939    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# Очевиден прирост скорости при многократном обращении к словарю


# Далее оценим прирост производительности в 3-х модификациях одного решения:
# рекурсия, без рекурсии, момоизация
# Оценку будем производить с помощью модуля timeit
# уберем вывод на экран


print(timeit.timeit('recursion(7000)', 'from __main__ import recursion', number=100))
print(timeit.timeit('recursion2(7000)', 'from __main__ import recursion2', number=100))
print(timeit.timeit('recursion3(7000)', 'from __main__ import recursion3', number=100))

'''
5.6138591449998785
3.0018758950027404
1.5230963450012496
'''
# Выгода очевидна и в абсолютных цифрах

# Проверим отсутствие выгоды от мемоизации при невозможности заполнить словарь и соответственно обращаться к нему
memory = {}
MIN_DIG = 1
MAX_DIG = 1000000

my_str = 'memory = {};recursion3(7000)'

print(timeit.timeit('recursion(7000)', 'from __main__ import recursion', number=100))
print(timeit.timeit('recursion2(7000)', 'from __main__ import recursion2', number=100))
print(timeit.timeit(my_str, 'from __main__ import recursion3', number=100))
"""
4.0876929460064275
2.973920817996259
3.471149841992883
"""
# Как видно из результатов в данном примере мемоизация приносит дополнительные вычисления вместо снижения нагрузки

# Вывод: мемоизация предпочтительна в случае большого числа повторяемости входных данных функции
# при условии, однозначного и единственного их соответствия выходным данным.
