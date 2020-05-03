"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""


import random


def proc(lst):
    """ Наша процедура"""

    print(f"Исходный массив: {lst}")

    num = max(lst, key=lst.count)
    print(f"Число {num} встречается {lst.count(num)} раза")


LST = [random.randint(0, 1000) for i in range(50)]
proc(LST)
