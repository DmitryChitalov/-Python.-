"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random


A = [random.randint(1, 5) for i in range(10)]
print(A)
MAX_COUNT = 0
for i in A:
    if MAX_COUNT < A.count(i):
        MAX_COUNT = A.count(i)
        NUM = i
print(f'Число {NUM} встречается {MAX_COUNT} раз')
