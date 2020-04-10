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
import random
import timeit



number = int(random.random() * pow(10, 10))
print('Число:', number)


def method_1():
    count_even = 0
    count_odd = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f'Четных {count_even}\nНечетных:{count_odd}')


def method_2(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return method_2(num, even, odd)
        else:
            odd += 1
            return method_2(num, even, odd)


def memorize(func):
    def wrapper(n, memory={}):
        value = memory.get(n)
        if value is None:
            value = func(n)
            memory[n] = value
        return value
    return wrapper


@memorize
def method_3(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return method_2(num, even, odd)
        else:
            odd += 1
            return method_2(num, even, odd)


method_1()
print(method_2(number))
time_meth_1 = timeit.timeit("method_1", setup="from __main__ import method_1")
time_meth_2 = timeit.timeit("method_2(number)", setup="from __main__ import method_2, number")
time_meth_3 = timeit.timeit("method_3(number)", setup="from __main__ import method_3, number")

print('\nЗатраченное время на исполнение с помощью'
      f'\n{"- цикла:":25} {time_meth_1}'
      f'\n{"- рекурсии:":25} {time_meth_2}'
      f'\n{"- рекурсия + мемоизация:":25} {time_meth_3}')


'''
Для вычисления четных и не четных подходит цикл, рекурсия занимает времени в 10 раз больше. '''

