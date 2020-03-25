"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import random
NUMBER_ELEM = 20
TEST_LIST = []
for i in range(NUMBER_ELEM):
    TEST_LIST.append(int(random() * 11))
print(TEST_LIST)
DIGIT_MAX = 0
ELEM = 0
for el in TEST_LIST:
    COUNT_MAX = 0
    for item in TEST_LIST:
        if el == item:
            COUNT_MAX += 1
    if COUNT_MAX > DIGIT_MAX:
        DIGIT_MAX = COUNT_MAX
        ELEM = el
print(f'Число {ELEM} встречается в массиве чаще всего - {DIGIT_MAX} раз(a)')
