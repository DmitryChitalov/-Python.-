"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random
EXAMPLE = [random.randint(0, 5) for _ in range(20)]
print(EXAMPLE)

def max_entrance(array):
    """Determine which number in the array is most common"""
    max_count = 0
    for el in set(array):
        if array.count(el) > max_count:
            max_count = array.count(el)
            max_i = array.index(el)
    return array[max_i]

print(max_entrance(EXAMPLE))

print(max(EXAMPLE, key=lambda x: EXAMPLE.count(x)))