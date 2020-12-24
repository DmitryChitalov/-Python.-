"""
Задание 1.
Докажите, что словари обрабатываются быстрее, чем списки.
Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time
import random as rnd


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(f'Execution time for {function} is {time.perf_counter() - start_time} sec')
        return res
    return wrapped

@time_of_function
def fill_list(number):
    reslist = []
    reslist = [rnd.randint(1, 5) for i in range(1, number) ]

fill_list(10000000)

@time_of_function
def fill_dict(number):
    resdict = {}
    for i in range(1, number):
        val = rnd.randint(1, 5)
        resdict.update(i = val)

fill_dict(10000000)