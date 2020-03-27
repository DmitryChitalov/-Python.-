"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

r = [random.randint(0, 99) for _ in range(30)]
print(f'Массив: {r}')

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)
if r.count(max_index) > 1:
    print(f'Число {r[max_index]}, встречается {r.count(max_index)} раза')
else:
    print('Все числа встречаются 1 раз')