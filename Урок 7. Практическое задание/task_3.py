import random
from copy import deepcopy
import timeit

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""


def median_el(orig_list, k): # нахождение медианы без сортировки
    if len(orig_list) > 1:
        choice_elem = random.choice(orig_list)
        smaller_el = [i for i in orig_list if i <= choice_elem]
        bigger_el = [i for i in orig_list if i > choice_elem]
        if len(smaller_el) >= k:
            return median_el(smaller_el, k)
        else:
            k -= len(smaller_el)
            return median_el(bigger_el, k)
    else:
        return orig_list[0]


def quick_sort(orig_list):  # сортировка массива
    if len(orig_list) > 1:
        choice_elem = random.choice(orig_list)
        smaller_el = [i for i in orig_list if i < choice_elem]
        bigger_el = [i for i in orig_list if i > choice_elem]
        equal_el = [i for i in orig_list if i == choice_elem]

        return quick_sort(smaller_el) + equal_el + quick_sort(bigger_el)
    else:
        return orig_list


def median_el2(orig_list, k):  # нахождение медианы с сортировкой
    return quick_sort(orig_list)[k]


n = 1000
mid_el_num = n // 2 + 1
mid_el_idx = n // 2
new_list1 = [random.randint(0, 99) for i in range(0, n)]
new_list2 = deepcopy(new_list1)
print(timeit.timeit("median_el(new_list1, mid_el_num)", setup="from __main__ import median_el, new_list1, mid_el_num",
                    number=1000))
print(timeit.timeit("median_el2(new_list2, mid_el_idx)", setup="from __main__ import median_el2, new_list2, mid_el_idx",
                    number=1000))
print(new_list1)
print(median_el(new_list1, mid_el_num))
median_element = median_el2(new_list2, mid_el_idx)
print(median_element)
