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
import timeit

"""
Эта команда выполнит выражение setup один раз, 
а затем возвратит время в секундах типа float, 
которое требуется что бы выполнить основное выражение number раз.
"""

def recur(n_1, even=0, odd=0):
    """
    Программа подсчета четных и нечетных цифр в числе
    """
    el_1 = n_1 % 10
    if el_1 % 2 == 0:
        even += 1
    else:
        odd += 1
    n_1 = n_1 // 10
    if n_1 == 0:
        return # print(f"Количество цифр в числе {even+odd}. Четные: {even}. Нечетные {odd}.")
    recur(n_1, even, odd)


# через строку кода
STR_CODE = '''
NUMB = 123456789

EVEN = 0
ODD = 0
M = 0
INSIDE = NUMB
while M != 1:
    EL = INSIDE % 10
    if EL % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    INSIDE = INSIDE // 10
    if INSIDE == 0:
        break
'''

n = 123456789
print(timeit.timeit("recur(n)", setup="from __main__ import recur, n", number=1000))
print(timeit.timeit(STR_CODE, number=1000))