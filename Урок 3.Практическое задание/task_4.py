"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random
a = [random.choice([i for i in range(1, 5)]) for j in range(10)]
count = [0, 0]
for i in sorted(a):
    j = sorted(a).count(i)
    if j > count[1]:
        count = [i, j]

print(f'В списке {a}\n'
      f'самое частое число {count[0]}. Оно встречается {count[1]} раз.')