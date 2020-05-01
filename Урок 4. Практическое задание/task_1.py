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

# The first variant: cycle
# The second time
# O(n)

def first(user_input):
    result = ''
    for i in user_input:
        result = f'{i}{result}'
    return result

# "task_1.first('65748')"
# 1000 loops, best of 5: 604 nsec per loop

# "task_1.first('65748392012938475658')"
# 1000 loops, best of 5: 1.64 usec per loop

# "task_1.first('6574839201293847023874023476503274560236455658')"
# 1000 loops, best of 5: 3.67 usec per loop

cProfile.run('first("6574839201293847023874023476503274560236455658")')

# 4 function calls in 0.000 seconds for all numbers

# The second variant - recursion
# The third time
# O(n)

def second(num):
    if num == 0:
        return ""
    return str(num % 10) + (second((num // 10)))


# "task_1.second(65748)"
# 1000 loops, best of 5: 1.96 usec per loop

# "task_1.second(65748392012938475658)"
# 1000 loops, best of 5: 7.75 usec per loop

# "task_1.second(6574839201293847023874023476503274560236455658)"
# 1000 loops, best of 5: 19.5 usec per loop

cProfile.run('second(6574839201293847023874023476503274560236455658)')

# 6/1    0.000    0.000    0.000    0.000 prob_02.py:8(second) 65748
# 21/1    0.000    0.000    0.000    0.000 prob_02.py:8(second) 65748392012938475658
# 47/1    0.000    0.000    0.000    0.000 prob_02.py:8(second) 6574839201293847023874023476503274560236455658

# The third variant - slice
# The best time
# O(n)

def third (num):
    return str(num)[::-1]

# "task_1.third(65748)"
# 1000 loops, best of 5: 311 nsec per loop

# "task_1.third(65748392012938475658)"
# 1000 loops, best of 5: 369 nsec per loop

# "task_1.third(6574839201293847023874023476503274560236455658)"
# 1000 loops, best of 5: 441 nsec per loop

cProfile.run('third(65748392012938475658)')

# 4 function calls in 0.000 seconds for all numbers
