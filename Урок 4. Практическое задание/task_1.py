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

import math
import timeit


def naive(input):
    '''O(2n^2)
    '''

    MIN_NUMBER_1 = 1000

    for J in range(len(INPUT)):
        for I in range(0, len(INPUT)):
            if INPUT[I] <= MIN_NUMBER_1:
                MIN_NUMBER_1 = INPUT[I]
                MIN_INDEX_1 = I


def optimized(input):
    '''O(n)
    '''
    MIN_NUMBER_1 = 1000

    for I in range(0, len(INPUT)):
        if INPUT[I] <= MIN_NUMBER_1:
            MIN_NUMBER_1 = INPUT[I]
            MIN_INDEX_1 = I


NUMBER_EXECUTIONS = 1000
INPUT = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73, 28, -86, 44, -37, -7, -52, -19, -3, -15, -73]

time1 = timeit.timeit(f'naive({INPUT})',
                      setup='from __main__ import naive',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'optimized({INPUT})',
                      setup='from __main__ import optimized',
                      number=NUMBER_EXECUTIONS)

print(f'O(n) Быстрее в  \
{round(time1 / time2, 2)} раз чем O(2n^2)'
      )
'''Первый алгоритм линейной сложности и второй квадратичной (во второй добавлен второй цикл для сложности)'''