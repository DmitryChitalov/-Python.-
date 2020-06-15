"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
from random import randint

a = [randint(10, 20) for x in range(1, 11)]
print(a)
# 1 Вариант
max_number = max(a, key=lambda i: a.count(i))
print(f'Число {max_number} встречается в массиве чаще всего')
# 2 Вариант
max_cnt = 0
number = a[0]
for i in range(0, len(a)):
    cnt = 1
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        number = a[i]
print(f'Число {number} встречается в массиве чаще всего, а именно {max_cnt} раз(а)')
