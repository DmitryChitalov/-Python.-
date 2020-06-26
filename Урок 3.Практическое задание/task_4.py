"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
preset_arr = [
    1, 2, 3, 3,
    4, 1, 1, 2,
    2, 2, 7, 5,
    8, 8, 5, 5,
    6, 4, 4, 4,
    1, 1, 1, 2,
    7, 5, 4, 6
]

unique_val_arr = list(set(preset_arr))
element_counter = []

for i in unique_val_arr:
    element_counter.append(preset_arr.count(i))

print(f'The most common element array: '
      f'{unique_val_arr[element_counter.index(max(element_counter))]}')
