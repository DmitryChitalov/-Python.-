"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random

ARR = [random.randint(-40, 40) for i in range(30)]
print(f'Массив {ARR}')

NUM = ARR[0]
MAX_FRQ = 1
for i in range(len(ARR) - 1):
    frq = 1
    for k in range(i + 1, len(ARR)):
        if ARR[i] == ARR[k]:
            frq += 1
    if frq > MAX_FRQ:
        MAX_FRQ = frq
        num = ARR[i]

if MAX_FRQ > 1:
    print(f'{MAX_FRQ} раз(а) встречается число {NUM}')
else:
    print(f'Все элементы уникальны')
