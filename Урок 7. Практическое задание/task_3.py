"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random
import statistics

M = random.randint(1, 100)

ORIGINAL = [random.randint(-100, 100) for x in range(2 * M + 1)]


def without_sort(or_list: list) -> int:
    """ Поиск медианы массива без сортировки """
    l_list = []
    m_list = []
    r_list = []
    for my_median in or_list:

        for i in or_list:
            if i < my_median:
                l_list.append(i)
            elif i > my_median:
                r_list.append(i)
            elif i == my_median:
                m_list.append(i)

        if len(l_list) == len(r_list) or \
                ((len(l_list) + len(m_list) - 1) == len(r_list)) or \
                (len(l_list) == (len(m_list) - 1 + len(r_list))):
            break

        l_list.clear()
        m_list.clear()
        r_list.clear()

    del l_list
    del m_list
    del r_list

    return my_median


MY_MEDIAN = without_sort(ORIGINAL)
TEST_MEDIAN = statistics.median(ORIGINAL)

if MY_MEDIAN == TEST_MEDIAN:
    print('Ok!')
else:
    print('Fail!')

print(ORIGINAL)
print('Медиана массива: ', MY_MEDIAN)
