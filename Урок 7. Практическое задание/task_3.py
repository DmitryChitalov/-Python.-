"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import random
from random import randint
from timeit import timeit


def create_list_int(list_len, l_border, r_border):
    return [randint(l_border, r_border - 1) for _ in range(list_len * 2 + 1)]


# Использую set, что дает прирост производительности
def get_median(base_list):
    for val in base_list:
        cnt1 = cnt2 = 0
        cnt3 = base_list.count(val)
        for val2 in base_list:
            if val == val2:
                continue
            if val2 < val:
                cnt1 += 1
            else:
                cnt2 += 1
        if abs(cnt1-cnt2) <= cnt3:
            return val
    return None


# Использую set, что дает прирост производительности
def get_median_opt(base_list):
    for val in set(base_list):
        cnt1 = cnt2 = 0
        cnt3 = base_list.count(val)
        for val2 in base_list:
            if val == val2:
                continue
            if val2 < val:
                cnt1 += 1
            else:
                cnt2 += 1
        if abs(cnt1-cnt2) <= cnt3:
            return val
    return None


a = create_list_int(5, 0, 10)
print(a)
print(sorted(a))
print(get_median(a))
print(get_median_opt(a))
"""
[5, 2, 0, 5, 9, 3, 3, 7, 3, 0, 2]
[0, 0, 2, 2, 3, 3, 3, 5, 5, 7, 9]
3
3
"""
print('Обычный: ',
      timeit('get_median(create_list_int(500,0,1000000))', 'from __main__ import get_median, create_list_int',
             number=100))
print('Оптимиз: ',
      timeit('get_median_opt(create_list_int(500,0,1000000))', 'from __main__ import get_median_opt, create_list_int',
             number=100))
"""
Обычный:  5.44049578999693
Оптимиз:  6.0076921620056964

"""
# Сделаем разброс возможных значений массива минимальными
print('Обычный: ',
      timeit('get_median(create_list_int(500,0,10))', 'from __main__ import get_median, create_list_int', number=100))
print('Оптимиз: ',
      timeit('get_median_opt(create_list_int(500,0,10))', 'from __main__ import get_median_opt, create_list_int',
             number=100))
"""
Обычный:  0.19541699200635776
Оптимиз:  0.15574709400243592
"""
# ВЫВОД: в зависимости от типа входных данных разные алгоритмы могут как ускорить, так и замедлить работу
