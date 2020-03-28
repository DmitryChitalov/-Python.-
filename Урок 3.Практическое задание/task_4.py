"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import random

N = 15
INPUT = [0] * N
for i in range(N):
    INPUT[i] = int(random() * 20)
print(INPUT)

NUM = INPUT[0]
MAX_FRQ = 1
for i in range(N - 1):
    FRQ = 1
    for k in range(i + 1, N):
        if INPUT[i] == INPUT[k]:
            FRQ += 1
    if FRQ > MAX_FRQ:
        MAX_FRQ = FRQ
        NUM = INPUT[i]

if MAX_FRQ > 1:
    print(MAX_FRQ, 'раз(а) встречается число', NUM)
else:
    print('Все элементы уникальны')
