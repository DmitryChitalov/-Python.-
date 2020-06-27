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

"""Для следующего замеря взял задание из ДЗ2 №2. Так же здесь производилась оценка сложности"""

import timeit
import cProfile

"""Решение через цикл"""

def cycle_method(NUMB):

    EVENS = 0
    ODDS = 0

    while NUMB!= 0:
        CUR_N = NUMB % 10
        NUMB = NUMB // 10
        if CUR_N % 2 == 0:
            EVENS += 1
        else:
            ODDS += 1
    return EVENS, ODDS

try:
    NUMB = int(input("Введите натуральное число: "))
    print (f"Количество четных и нечетных цифр в числе равно: {cycle_method(NUMB)}")
except ValueError:
    print("Вы ввели не цифру. Повторите")

print(
        timeit.timeit(
        "cycle_method(NUMB)",
        setup="from __main__ import cycle_method, NUMB",
        number=1000)
)

"""Вариант 1 замер времени составил: 0.0008268560050055385"""

cProfile.run('cycle_method(NUMB)')
"""4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1_2.py:19(cycle_method)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

"""Решение через рекурсию"""

def recur_method(NUMB, EVEN=0, ODDS=0):
    if NUMB ==0:
        return EVEN, ODDS
    else:
        CUR_N = NUMB % 10
        NUMB = NUMB // 10
        if CUR_N % 2 == 0:
            EVEN += 1
            return recur_method(NUMB, EVEN, ODDS)
        else:
            ODDS += 1
            return recur_method(NUMB, EVEN, ODDS)

try:
    NUMB = int(input("Введите натуральное число: "))
    print (f"Количество четных и нечетных цифр в числе равно: {recur_method(NUMB)}")
except ValueError:
    print("Вы ввели не цифру. Повторите")

print(
        timeit.timeit(
        "recur_method(NUMB)",
        setup="from __main__ import recur_method, NUMB",
        number=1000)
)

"""Вариант 2 замер времени составил: 0.0011962629796471447"""

cProfile.run('recur_method(NUMB)')
"""5 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      2/1    0.000    0.000    0.000    0.000 task_1_2.py:51(recur_method)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

"""Вывод: Решение через цикл быстрее, чем рещение через рекурсию"""