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

import cProfile
import timeit
import sys

sys.setrecursionlimit(150000)

# Первый пример
# Урок 2. Задание 3.
# Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

# Рекурсия
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

# Цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# Срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Пример №1')
enter_num = int(input('Введите целое число: '))
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)


print('Число на оборот на рекурсиях: ', timeit.timeit(f'revers({enter_num})', setup='from __main__ import revers', number=10000))
print('Число на оборот на циклах: ', timeit.timeit(f'revers_2({enter_num})', setup='from __main__ import revers_2', number=10000))
print('Число на оборот на срезах: ', timeit.timeit(f'revers_3({enter_num})', setup='from __main__ import revers_3', number=10000))

cProfile.run('revers(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

# Вывод: Я применил 3 вида реализации задачи ( рекурсия, цикл, срез). Согласно полученным результатам видно что срез наиболее быстрый в плане выполнения
# задачи. Рекурсия и цикл имеют арифмитические действия поэтому они проигрывают в скорости по сравнению со срезом в котором отсутствуют арифмитические действия.
# Следовательно в подобных задачах оптимально использовать срез.

print('--------------------------------------------------')
print('--------------------------------------------------')

# Второй пример
# Урок 2. Задание 4.
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...

def cycle(n=10, val=1, sum=0):

    for i in range(n):
        sum += val
        val = -(val / 2)

def recursion(n=10, val=1, sum=0):
    if n == 0:
        return
    else:
        sum = sum + val
        val /= -2
        n -= 1
        recursion(n, val, sum)

print('\nПримет №2')
print('Длина ряда = 10')
print(f'Время затраченное на цикл: ', timeit.timeit(cycle, number=10000))
print(f'Время затраченное на рекурсию:', timeit.timeit(recursion, number=10000))


cProfile.run('cycle(10000)')
cProfile.run('recursion(10000)')

# Вывод: Во втором задании я применил два решение ( цикл и рекурсию). Цикл оказался быстрее рекурсии
# так как рекурсия тратит дополнительное время на вызов саму себя тем самым замедляя выполнения операции.
# По сложности цикл так же опережает рекурсию.
# Следовательно в подобных задачах оптимально всего использоваь цикл.




 # Мои результаты:
 # Пример №1
# Введите целое число: 567
# Число на оборот на рекурсиях:  0.026144434999991972
# Число на оборот на циклах:  0.009701919999997699
# Число на оборот на срезах:  0.0038655270000163
#          15 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      12/1    0.000    0.000    0.000    0.000 task_1.py:14(revers)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:24(revers_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:32(revers_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# --------------------------------------------------
# --------------------------------------------------
#
# Примет №2
# Длина ряда = 10
# Время затраченное на цикл:  0.010612643000058597
# Время затраченное на рекурсию: 0.018344318999993448
#          4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_1.py:65(cycle)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          10004 function calls (4 primitive calls) in 0.009 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#   10001/1    0.009    0.000    0.009    0.009 task_1.py:71(recursion)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
