"""
Задание_4. Определить, какое число в массиве встречается чаще всего
Подсказка: можно применить ф-цию max с параметром key
"""
import random

def NUM(LST):
    NUMBER = max(LST, key=LST.count)
    print(f"Число {NUMBER} в массиве {LST} встречается {LST.count(NUMBER)} раз")

LST = [random.randint(-100, 100) for i in range(10)]
NUM(LST)