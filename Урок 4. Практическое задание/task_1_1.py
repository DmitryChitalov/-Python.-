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

'''     ИСХОДНОЕ РЕШЕНИЕ:

############   1 VARIANT  Со счетчиком   ##################
for i in range(2, 10):
    COUNT = 0
    for j in range(2, 100):
        COUNT += int(j % i == 0)
    print(f'В диапазоне 2-99: {COUNT} чисел кратны {i}')

############   2 VARIANT  Со списком   ##################

for i in range(2, 10):
    N = []
    N = [j for j in range(2, 100) if j % i == 0]
    print(f'В диапазоне 2-99: {len(N)} чисел кратны {i}')
'''

import cProfile
import timeit

def f_loop():
    '''Вложенный цикл'''
    for i in range(2, 10):
        count = 0
        for j in range(2, 100):
            count += int(j % i == 0)

def f_compr():
    '''comprehension'''
    for i in range(2, 10):
        n = []
        n = [j for j in range(2, 100) if j % i == 0]
        count = len(n)

def main():
    f_loop()
    f_compr()

print(timeit.timeit("f_loop()", setup="from __main__ import f_loop", number=1000))
print(timeit.timeit("f_compr()", setup="from __main__ import f_compr", number=1000))

cProfile.run('main()')

'''
В исходных вариантах реализованы два алгоритма:
один с вложенным цмклом, в другом используется генераторт списка.
Из исходных вариантов реализации удалены функции print(), чтобы протестировать только
сами алгоритмы. Тем более, что время выполнения этой функции будет постоянным и
не повлияет на конечный результат.
    Модуль cProfile выдает нулевые значения по затратам времени в обоих вариантах
реализации. Это говорит о том, что оба варианта отрабатывают без существенных задержек.
    Использование модуля timeit показывает двукратный выигрыш по времени во втором случае.
В обоих вариантах сложность алгоритма, видимо, квадратичная. Но поскольку метод
генерации списков отрабатывает быстрее, чем перебор, и операция многократного суммирования
заменяется однократным выводом длины списка, во втором случае получаем лучший результат.
    При больших значениях второй вариант может проигрывать по объему используемой памяти,
т.к. в первом случае используется одна перменная, а во втором - формируется список.
'''
