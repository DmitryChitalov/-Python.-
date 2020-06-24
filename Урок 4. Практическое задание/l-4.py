import cProfile
from timeit import Timer
import random


def my_func():
    x = 15
    array = [1, 1, 1, 2, 2, 3, 4, 2, 8, 8, 8, 8, 8, 8, 1, 9]

    num = array[0]
    max_frq = 1
    for i in range(x - 1):
        frq = 1
        for k in range(i + 1, x):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

    print(f'number {num} will found {max_frq} times')


timeit_1 = Timer("my_func()", "from __main__ import my_func")
print("test timer 1", timeit_1.timeit(number=100), 'ms')

# test timer 0.001029947999995784 ms - with print
# test timer 0.0008337250000067797 ms - without print
# можно сделать вывод, что нативная ф-я print сильно замедляет работу алогритма

cProfile.run('my_func()')


# результаты работы
# 4 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#  1    0.000    0.000    0.000    0.000 staging.py:5(my_func)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# так же при раскомментировании ф-ии print подсчитывает ее (4 function calls in 0.000 seconds)

def my_func_g():
    for i in range(2, 10):
        new_list = [el for el in range(2, 100) if el % i == 0]
        print(f'В диапазоне 2-99 {len(new_list)} чисел кратных {i}')


my_func_g()

timeit_2 = Timer("my_func_g()", "from __main__ import my_func_g")
print("test timer 2", timeit_2.timeit(number=100), 'ms')


# test timer 2 0.00497901899984754 ms - with gen

def my_func_():
    a = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                a[j - 2] += 1
    i = 0
    while i < len(a):
        print(i + 2, ' - ', a[i])
        i += 1


timeit_3 = Timer("my_func_()", "from __main__ import my_func_")
print("test timer 3", timeit_3.timeit(number=100), 'ms')


# test timer 3 0.007557301000133521 ms - without gen

# из результатов прогонов timer 2 и timer 3 можно сделать вывод, что ф-я с генератором
# работает медленнее

def my_func_without_max():
    x = 15
    array = [1, 1, 1, 2, 2, 3, 4, 2, 8, 8, 8, 8, 8, 8, 1, 9]

    num = array[0]
    max_frq = 1
    for i in range(x - 1):
        frq = 1
        for k in range(i + 1, x):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]

    print(f'number {num} will found {max_frq} times')


def my_func_with_max(lst):
    print(f'source list - {lst}')
    numb = max(lst, key=lst.count)
    print(f'number {numb} will found {lst.count(numb)} times')


LST = [random.randint(-100, 100) for i in range(50)]
my_func_with_max(LST)

timeit_4 = Timer("my_func_without_max()", "from __main__ import my_func_without_max")
print("test timer 4", timeit_4.timeit(number=100), 'ms')

timeit_5 = Timer("my_func_with_max", "from __main__ import my_func_with_max")
print("test timer 5", timeit_5.timeit(number=100), 'ms')

# test timer 4 0.0010122999997292936 ms
# test timer 5 1.2420000530255493e-06 ms
# ф-я с ф-ей max работает значительно медленнее
#
