"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import random

quantity = 10
list = [0] * quantity

for i in range(quantity):
    list[i] = int(random() * 10)
print('Случайный массив: ', list)

number = list[0]
q_repetition = 1
for i in range(quantity - 1):
    repetition = 1
    for k in range(i + 1, quantity):
        if list[i] == list[k]:
            repetition += 1
    if repetition > q_repetition:
        q_repetition = repetition
        number = list[i]

if q_repetition > 1:
    print(q_repetition, 'повторения(-ий) в массиве числа: ', number)
else:
    print('Числа массива не повторяются')
