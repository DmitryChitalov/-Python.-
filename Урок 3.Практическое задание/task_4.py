"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint

a = [randint(1, 30) for el in range(0, 10)]
print(a)
b = [a.count(el) for el in a]
print(f'Чаще всего в массиве используется число {a[b.index(max(b))]} ')
