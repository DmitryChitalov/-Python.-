"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random

random_list = [random.randint(1, 9) for _ in range(8)]
dict_temp = dict.fromkeys(random_list, 0)

for num in random_list:
    dict_temp[num] += 1

max_count = 0
for key in dict_temp:
    if dict_temp[key] > max_count:
        max_key = key
        max_count = dict_temp[key]

print(f'В массиве \n{random_list} \nчаще всего встречается число - {max_key} ({max_count} раз)')