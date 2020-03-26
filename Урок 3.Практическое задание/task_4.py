"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
# вариант 1 --- цикл/ветвления
from random import randint

LST = [0]*20
for i in range(20):
    LST[i] = randint(5, 10)
    print(LST[i], end=' ')
print()


NUM = 0
MAX_COUNT = 1
for el in LST:
    COUNT = 1
    for i in LST[1:]:
        if el == i:
            COUNT += 1
    if COUNT > MAX_COUNT:
        MAX_COUNT = COUNT
        NUM = el

print(NUM)

# вариант 2 --- модуль collection
from random import randint
import collections

LST = [0]*20
for i in range(20):
    LST[i] = randint(5, 10)
    print(LST[i], end=' ')
print()

for i in collections.Counter(LST).most_common(1):
    print(f'Самый часто встречающийся элемент массива : {i[0]}, он встречается : {i[1]} раз')
