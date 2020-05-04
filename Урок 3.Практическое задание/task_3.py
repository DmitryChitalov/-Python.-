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

def func(lst):
    max_val = max(lst)
    min_val = min(lst)
    ind_max = lst.index(max_val)
    ind_min = lst.index(min_val)

    print(
        f"В данном массиве максимальное число {max_val:3} стоит на {ind_max:3} позиции, "
        f"а минимальное число {min_val:3} стоит на {ind_min:3} позиции"
    )

    print("Заменяем их")
    print(lst)

    lst[ind_max], lst[ind_min] = min_val, max_val
    ind_max = lst.index(max_val)
    ind_min = lst.index(min_val)
    print(
        f"В данном массиве максимальное число {max_val:3} стоит на {ind_max:3} позиции, "
        f"а минимальное число {min_val:3} стоит на {ind_min:3} позиции"
    )

    print(lst)


LST = [randint(-100, 100) for i in range(10)]
func(LST)