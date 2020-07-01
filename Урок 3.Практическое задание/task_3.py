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
# initial_list = [88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
#
# in_max = 0
# in_min = 0
#
# for x in range(len(initial_list)):
#     if initial_list[x] < initial_list[in_min]:
#         in_min = x
#     elif initial_list[x] > initial_list[in_max]:
#         in_max = x
# print(f"Minimal number is: {initial_list[in_min]} index was {in_min}")
# print(f"Maximum number is: {initial_list[in_max]} index was {in_max}")
# initial_list[in_max], initial_list[in_min] = initial_list[in_min], initial_list[in_max]
# print(initial_list)

#  Solution from teacher

from random import randint


def task_3(lst):
    max_val = max(lst)
    min_val = min(lst)
    ind_max = lst.index(max_val)
    ind_min = lst.index(min_val)

    print(f"В данном массиве чисел максимальное число {max_val:4} стоит на {ind_max:4} позиции",
          f"а минимальное число {min_val:4} стоит на {ind_min:4} позиции")
    print('Заменяем их')
    print(lst)

    lst[ind_max], lst[ind_min] = min_val, max_val
    ind_max = lst.index(max_val)
    ind_min = lst.index(min_val)
    print(f"В данном массиве чисел максимальное число {max_val:4} стоит на {ind_max:4} позиции",
          f"а минимальное число {min_val:4} стоит на {ind_min:4} позиции")

    print(lst)


LST = [randint(-100, 100) for i in range(10)]
task_3(LST)
