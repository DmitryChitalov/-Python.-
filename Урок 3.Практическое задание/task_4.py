"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint


def max_counter(array):
    print(max(set(array), key=lambda x: array.count(x)))


max_counter([randint(-100, 100) for i in range(1000)])
