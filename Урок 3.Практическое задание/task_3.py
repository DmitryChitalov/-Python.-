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
max_ix = 0
min_ix = 0
list_ = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
for ix, i in enumerate(list_):
    if list_[ix] > list_[max_ix]:
        max_ix = ix
    if list_[ix] < list_[min_ix]:
        min_ix = ix

print(list_)
list_[max_ix], list_[min_ix] = list_[min_ix], list_[max_ix]
print(list_)