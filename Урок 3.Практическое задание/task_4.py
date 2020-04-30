"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import random
ARRAY = [int(random() * 20) for _ in range(15)]
print(ARRAY)
print(sorted([(i, ARRAY.count(i))
              for i in set(ARRAY)], key=lambda t: t[1])[-1])
