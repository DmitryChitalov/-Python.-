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


def proc(lst):
    """ Наша процедура"""

    max_elem = max(lst)
    min_elem = min(lst)
    ind_max = lst.index(max_elem)
    ind_min = lst.index(min_elem)

    print(
        f'В данном массиве чисел максимальное число {max_elem} стоит на {ind_max} позиции, '
        f'а минимальное число {min_elem} стоит на {ind_min} позиции')

    print('Заменяем их')
    print(lst)

    lst[ind_max], lst[ind_min] = min_elem, max_elem
    ind_max = lst.index(max_elem)
    ind_min = lst.index(min_elem)
    print(
        f'В данном массиве чисел максимальное число {max_elem} стоит на {ind_max} позиции, '
        f'а минимальное число {min_elem} стоит на {ind_min} позиции')

    print(lst)


LST = [randint(-1000, 1000) for i in range(10)]
proc(LST)
