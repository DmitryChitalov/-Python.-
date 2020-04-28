"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randint, choice


def median(orig_list, mid, pivot_list=choice):
    if len(orig_list) == 1:
        return orig_list[0]
    pivot = pivot_list(orig_list)
    left = [itm for itm in orig_list if itm < pivot]
    right = [itm for itm in orig_list if itm > pivot]
    pivots = [itm for itm in orig_list if itm == pivot]

    if mid < len(left):
        # если длина списка left - больше индекса медианы,
        # то рекурсивно вызвать функцию, подать на вход список left
        return median(left, mid)
    elif mid < len(left) + len(pivots):
        # если выпала медиана, то вернуть её
        return pivots[0]
    else:
        # если медиана осталась в правом списке, то необходимо скорректировать индекс,
        # с учетом того, что часть элементов остались в левом списке и списке
        # опорных элементов, соответственно вычесть из индекса лишние элементы
        return median(right, mid - len(left) - len(pivots))


NUMBER_OF_ITM = int(input('Введите число элементов: '))
if NUMBER_OF_ITM % 2 == 1:
    ORIG_LIST = [randint(0, 100) for _ in range(NUMBER_OF_ITM)]
    print(ORIG_LIST)
    print(f'Медиана данного списка: {median(ORIG_LIST, (len(ORIG_LIST) // 2))}')
    print('Для наглядности отсортированный список:')
    print(sorted(ORIG_LIST))
else:
    print('Необходимо вводить количество элементов равное 2m + 1')