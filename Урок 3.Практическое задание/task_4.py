"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random

LIST_N = [random.randint(0, 10) for i in range(10)]

print(f"Исходный массив: {LIST_N}")

RESULT = max(LIST_N, key=LIST_N.count)

print(f"Число {RESULT} в массиве встречается чаще всего")
