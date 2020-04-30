"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import random

ARRAY1 = [int(5 * random()) for i in range(30)]
print(ARRAY1)
LS_ARR = sorted(list(set(ARRAY1)))
MAX_ELEM = []

for i in LS_ARR:
    MAX_ELEM.append(ARRAY1.count(i))

print(f"Чаще всего в массиве встречается {LS_ARR[MAX_ELEM.index(max(MAX_ELEM))]}")
