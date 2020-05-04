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


def eratosphens_meth(n):
    size = int(n ** 1.5 + 2)
    sieve = [i for i in range(size)]
    sieve[1] = 0

    for i in range(2, size):
        if sieve[i] != 0:
            j = i + i

            while j < size:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[n - 1]


# ====================================================================================================================

def non_eratosphens(n):
    if n == 1:
        return 2
    res = [2]
    numb_list = [2]
    number = 3

    while len(res) != n:
        flag = True

        for itm in numb_list:
            if number % itm == 0:
                flag = False
                break

        if flag:
            res.append(number)

        numb_list.append(number)
        number += 1

    return res[n - 1]

# cProfile.run('eratosphens_meth(100)')
# 6 function calls in 0.008 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.008    0.008    0.008    0.008 task_2.py:18(eratosphens_meth)
#         1    0.000    0.000    0.000    0.000 task_2.py:20(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:31(<listcomp>)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('non_eratosphens(100)')
#          1182 function calls in 0.003 seconds
#
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 task_2.py:37(non_eratosphens)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       638    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('eratosphens_meth(1000)')
# 6 function calls in 0.028 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.028    0.028 <string>:1(<module>)
#         1    0.024    0.024    0.027    0.027 task_2.py:18(eratosphens_meth)
#         1    0.002    0.002    0.002    0.002 task_2.py:20(<listcomp>)
#         1    0.002    0.002    0.002    0.002 task_2.py:31(<listcomp>)
#         1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# cProfile.run('non_eratosphens(1000)')
#          16838 function calls in 0.363 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.363    0.363 <string>:1(<module>)
#         1    0.361    0.361    0.363    0.363 task_2.py:37(non_eratosphens)
#         1    0.000    0.000    0.363    0.363 {built-in method builtins.exec}
#      7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#      8916    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('eratosphens_meth(2000)')
# 6 function calls in 0.061 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.061    0.061 <string>:1(<module>)
#         1    0.053    0.053    0.060    0.060 task_2.py:18(eratosphens_meth)
#         1    0.003    0.003    0.003    0.003 task_2.py:20(<listcomp>)
#         1    0.004    0.004    0.004    0.004 task_2.py:31(<listcomp>)
#         1    0.000    0.000    0.061    0.061 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 100 -s "import task_2" "task_2.eratosphens_meth(2000)"
# 100 loops, best of 5: 28.5 msec per loop

#
# cProfile.run('non_eratosphens(2000)')
#          36778 function calls in 1.338 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.338    1.338 <string>:1(<module>)
#         1    1.333    1.333    1.338    1.338 task_2.py:37(non_eratosphens)
#         1    0.000    0.000    1.338    1.338 {built-in method builtins.exec}
#     17388    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#     19386    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 100 -s "import task_2" "task_2.non_eratosphens(2000)"
# 100 loops, best of 5: 738 msec per loop

# Поиск натурального числа c использованием решета Эратосфена работает существенно быстрее, и имеет сложность близкую к
# линейной O(n) по сравнению с алгоритмом, основанном на переборе всех элементов, со сложнсотью O(n^2)

