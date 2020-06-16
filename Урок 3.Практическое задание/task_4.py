"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

list_ = [88, 26, 41, 75, -49, 23, 52, 88, -49, 60, 69, -18, -49]
max_num = 0
for num, val in enumerate(list_):
    if list_.count(val) > max_num:
        max_num = num
print(f'Чаще всего встречается: {list_[num]}, появляется {list_.count(list_[num])} раза')