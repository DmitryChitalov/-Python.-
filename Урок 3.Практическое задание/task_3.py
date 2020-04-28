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

from random import randint

my_list = [randint(0, 100) for i in range(0, 10)]
print(my_list)

# в одну строку
(my_list[my_list.index(min(my_list))], my_list[my_list.index(max(my_list))]) =\
    (my_list[my_list.index(max(my_list))], my_list[my_list.index(min(my_list))])
print(my_list)

# более понятно
max_el = max(my_list)
max_el_idx = my_list.index(max_el)
min_el = min(my_list)
min_el_idx = my_list.index(min_el)
(my_list[max_el_idx], my_list[min_el_idx]) = (my_list[min_el_idx], my_list[max_el_idx])
print(my_list)

