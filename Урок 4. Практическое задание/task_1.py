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
from random import randint


# user_input = int(input('Введите число: '))


def test_func(user_input):
    new_number = 0
    while user_input > 0:
        new_number = new_number * 10 + user_input % 10
        user_input //= 10
    # print(new_number)


# test_func(user_input)

# user_input_lst = input('Введите число: ')


def test_func_2(user_input_lst):
    user_input_lst = ''.join(reversed(user_input_lst))
    # print(user_input_lst)


# test_func_2(user_input_lst)


def mirror_number(user_input, new_number=0):
    if user_input == 0:
        return  # print(f'Число наооборот {new_number}')
    new_number = new_number * 10 + user_input % 10
    user_input //= 10
    return mirror_number(user_input, new_number)


# mirror_number(int(input('Введите натуральное число: ')))

print(
    timeit.timeit("test_func(123456123456123456123456123456123456123456123456)", setup="from __main__ import test_func",
                  number=10000))
print(timeit.timeit("test_func_2('123456123456123456123456123456123456123456123456')",
                    setup="from __main__ import test_func_2", number=10000))
print(timeit.timeit("mirror_number(123456123456123456123456123456123456123456123456)",
                    setup="from __main__ import mirror_number", number=10000))
'''
Результаты при выполнение функций, которые делают обратное число,
заметно лучше показывает себя функция, которая работает со строкой 
с помощью встроенной функции reversed. Замеры времени числа 123456:
0.03188213399698725 - цикл
0.015842726003029384 - встроенная функция
0.07451771100022597 - рекурсия
Особенно это заметно на большом числе. 
Замеры времени числа 123456123456123456123456123456123456123456123456:
0.38418162999732886 - цикл
0.05222697299905121 - встроенная функция
0.4566892939983518 - рекурсия
'''

a = [randint(10, 20) for x in range(1, 110)]
print(a)


def test_1():
    max_number = max(a, key=lambda i: a.count(i))
    # print(f'Число {max_number} встречается в массиве чаще всего')


def test_2():
    max_cnt = 0
    number = a[0]
    for i in range(0, len(a)):
        cnt = 1
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            number = a[i]
    # print(f'Число {number} встречается в массиве чаще всего, а именно {max_cnt} раз(а)')


print(timeit.timeit("test_1()", setup="from __main__ import test_1", number=100))
print(timeit.timeit("test_2()", setup="from __main__ import test_2", number=100))

"""
Результаты работы функций:
7.929421408000053
20.140352697999333
Применение встроенной функции позволило сократить время работы примерно в 3 раза
"""


# Функция декоратор подсчета времени
def time_decor(func, n=100):
    start_time = timeit.default_timer()
    i = 0
    while i < n:
        func()
        i += 1
    print(timeit.default_timer() - start_time)


@time_decor
def test_decor():
    max_number = max(a, key=lambda i: a.count(i))


@time_decor
def test_decor_1():
    max_cnt = 0
    number = a[0]
    for i in range(0, len(a)):
        cnt = 1
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            number = a[i]


"""
Фунцкция декоратор на мой взгляд самый удобный вариант подсчета
"""
