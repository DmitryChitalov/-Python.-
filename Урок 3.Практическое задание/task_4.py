"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint

LIST = [randint(0, 10) for i in range(20)]
print(LIST)
NUM = 0
COUNT = 0

for itm in LIST:
    if LIST.count(itm) > COUNT:
        NUM = itm
        COUNT = LIST.count(itm)
print(f'Число, которое чаще всего встречается в массиве - {NUM}, оно встречается {COUNT} раз(а).')
