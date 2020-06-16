"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
def ar_switch(values, args):
    tmp_arr = args
    i = 0
    q = 1
    for el in values:
        tmp_arr[tmp_arr.index(values[q])] = values[i]
        i += 1
        q -= 1
    return tmp_arr


preset_arr = [
    10, 2, 45,
    78, 4, 1024,
    78, 69, 7
]


min = preset_arr[0]
max = preset_arr[0]
for el in preset_arr:
    if el > max:
        max = el
    if el <= min:
        min = el
min_max = [min, max]

print(ar_switch(min_max, preset_arr))
