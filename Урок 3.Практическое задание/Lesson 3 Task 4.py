"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint
LIST = []
for i in range(10):
    LIST.append(randint(0, 10))
print(LIST)
num = LIST[0]   # элемент массива
max_entry = 0   # максимальное количество вхождений в массив
for i in range(len(LIST) - 1):
    entry = 1
    for j in range(i + 1, len(LIST)):
        if LIST[i] == LIST[j]:
            entry += 1
    if entry > max_entry:
        max_entry = entry
        LIST[i] = num
print(f'В массиве чаще всего встречается число {num} - {max_entry} раз(а).')




