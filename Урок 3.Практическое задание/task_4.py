"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
# Пытался разобраться, но так и не понял как в этой задаче можно было применить ф-цию max с параметром key(

from random import random

LIST_1 = [int(random()*10) for i in range(15)]
print(LIST_1)

LIST_2 = [LIST_1.count(LIST_1[i]) for i in range(0, len(LIST_1))]

print(LIST_1[LIST_2.index(max(LIST_2))])
