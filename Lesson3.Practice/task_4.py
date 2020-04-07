"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

import random


def find_min_modern():
    # Наполняем массив в при помощи random.sample
    lst = sample(range(-100, 100), 10)
    cnt = 0
    min1 = min(lst)
    while cnt < 2:
        if element != min1 and el:
            cnt += 1
    if cnt > 1:
        return f'Наименьший элемент: {min1}, встречается в этом массиве {cnt} раз(а)'
    else:
        lst.remove(min1)
        min2 = min(lst)
        return f'Наименьший элемент: {min1}, встречается в этом массиве 1 раз \n' \
               f'Второй наименьший элемент: {min2}'
