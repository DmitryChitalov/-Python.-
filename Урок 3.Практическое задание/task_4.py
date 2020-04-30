"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random
LEN = int(input('Введите длину массива: '))
a = [random.randint(0, 99) for k in range(LEN)]
print(a)

b = max(a, key=a.count)
print(b)
