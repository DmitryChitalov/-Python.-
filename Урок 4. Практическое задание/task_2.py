"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from time import time
from timeit import timeit


def timer(func):

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        timer_result = time() - start
        print(f"Executing {func.__name__} took {timer_result*1000} ms")
        return result
    return wrapper


# @timer
def ar_sieve(req_idx, lst):
    """РЕШЕТО. Проигрывает в памяти, но не плохо работает по времени"""
    for n, main_el in enumerate(lst, 1):
        for sub_el in lst[n::]:
            if sub_el % main_el == 0:
                lst.remove(sub_el)
        if n == req_idx:
            return main_el
    return "No element found"


def list_generator():
    num = 2
    while True:
        yield num
        num += 1


@timer
def find_simple_num_3(req_idx):
    """НЕРЕШЕТО. Выигрывает в памяти, но не очень хорошо работает со временем"""
    simple_nums = list()
    current_idx = 0
    gen = list_generator()
    while req_idx != current_idx:
        num = next(gen)
        is_simple = True
        for el in simple_nums:
            if num % el == 0:
                is_simple = False
        if is_simple:
            simple_nums.append(num)
            current_idx += 1
    return simple_nums.pop(-1)


if __name__ == '__main__':

    # Решето Эратосфена
    # Сложность O(n^2) (Приблизительно такая сложность, точна сложность высчитывается по матем. формулам)
    # Среднее время при нахождении:
    #                               100го простого чилса:    0.44 сек
    #                               200го простого чилса:    1.30 сек
    #                               300го простого чилса:    4.04 сек
    # lst_ = [i for i in range(10**4)][2:]
    # print(timeit("ar_sieve(1000, lst_)", setup="from __main__ import ar_sieve, lst_", number=100))

    find_simple_num_3(100)

    # НеРешето Эратосфена
    # Сложность O(n * n!) (Приблизительно такая сложность)
    # Среднее время при нахождении:
    #                               100го простого чилса:    2.50 сек
    #                               200го простого чилса:    12.30 сек
    #                               300го простого чилса:    27.44 сек
    # print(timeit("find_simple_num_3(300)", setup="from __main__ import find_simple_num_3", number=100))
