"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint

MASSIVE = [randint(-3, 3) for el in range(randint(10, 20))]

print(f"В массиве {MASSIVE} \nчисло {max(MASSIVE, key=lambda x: MASSIVE.count(x))}"
      f" встречается чаще всего")
