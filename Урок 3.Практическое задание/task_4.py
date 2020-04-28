"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import random

# делаем массив
N = int(input('сколько элементов в массиве: '))
MY_LIST = [int(random()*100) for x in range(N)]

frq = 0
for x in set(MY_LIST): # уникальные циферки
    tmp_frq = 0
    for k in range(len(MY_LIST)): # сравнивам чего получилось
        if MY_LIST[k] == x:
            tmp_frq += 1
    if tmp_frq >= frq:
        MAX_NUMBER = x
        frq = tmp_frq
if frq == 1:
    print(MY_LIST)
    print(f'все числа разные')
else:
    print(MY_LIST)
print(f'самое часто число: {MAX_NUMBER} встречается: {frq}')

