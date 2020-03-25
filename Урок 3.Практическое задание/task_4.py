"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint
EXAMPLE = [randint(0, 20) for i in range(0, 20)]
MAX_NUMBER = max(EXAMPLE, key=lambda el: EXAMPLE.count(el))
print(f"В массиве {EXAMPLE} \nчаще всего встречается число {MAX_NUMBER}")
