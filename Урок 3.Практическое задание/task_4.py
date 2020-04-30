"""
Задание_4. Определить, какое число в массиве встречается чаще всего
Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint

my_list = [randint(1, 100) for i in range(20)]

print(f'В массиве:\n{my_list}\nЧаще всего встречается: {max(my_list, key=my_list.count)}')
