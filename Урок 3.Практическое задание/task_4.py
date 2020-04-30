"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randint

a = []
bc = int(input('Ведите длину массива '))
for i in range(bc):
    a.append(randint(0, 9))

b = max(a, key=a.count)
print(f'Массив чисел: \n{a}')
print(f'\nМаксимальное количество раз встречается цифра: {b}')
