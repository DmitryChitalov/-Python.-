"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random

START_RANGE = 0
SIZE_RANGE = 10

MY_LIST = [random.randint(START_RANGE, SIZE_RANGE // 1.5) for _ in range(SIZE_RANGE)]
print(MY_LIST)

ELEM = MY_LIST[0]
COUNT = 1

for i in range(len(MY_LIST)):
    spam = 1
    for j in range(i + 1, len(MY_LIST)):
        if MY_LIST[i] == MY_LIST[j]:
            spam += 1
    if spam > COUNT:
        COUNT = spam
        ELEM = MY_LIST[i]

print(f'Чаще всего в списке встречается чсло {ELEM} = {COUNT} раз.')
