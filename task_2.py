"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@memorize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


number = 100
print(timeit.timeit("recursive_reverse(number)", setup="from __main__ import recursive_reverse, number", number=1000))
print(timeit.timeit("recursive_reverse_mem(number)", setup="from __main__ import recursive_reverse_mem, number", number=1000))

"""
0.0011725
0.0001552999999999971 - При использовании меморизации выполняется на порядок быстрее из-за сохранения части результатов.
"""
