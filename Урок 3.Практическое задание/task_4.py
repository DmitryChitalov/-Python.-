"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
list_a = [88, 26, 41, 75, 88, 23, 52, 88, -49, 60, 69, -18]

MAX_NUM = 0
for num, val in enumerate(list_a):
    if list_a.count(val) > MAX_NUM:
        MAX_NUM = num

print(list_a[MAX_NUM])
