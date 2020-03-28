"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random


RANDOM_LIST = [random.randint(1, 10) for i in range(25)]
print(f"Список: \n {RANDOM_LIST}")
print(f"Чаще всего в списке встречается число: {max(RANDOM_LIST, key=RANDOM_LIST.count)}")
