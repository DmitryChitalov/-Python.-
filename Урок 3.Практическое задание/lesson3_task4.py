"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint
a= []
for i in range(10):
    a.append(randint(0,5))
print(a)
print(max(a,key=a.count))