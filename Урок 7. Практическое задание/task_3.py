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


def my_median(lst):
    '''моя медиана'''
    for reference in set(lst):
        cnt1, cnt2 = 0, 0
        for num in lst:
            if num < reference:
                cnt1 += 1
            elif num > reference:
                cnt2 += 1
        if abs(cnt1 - cnt2) < lst.count(reference):
            return reference
    raise ValueError('no median')


if __name__ == '__main__':
    M = 10
    LST = [random.randint(-100, 100) for _ in range(2 * M + 1)]
    print(f'моя медиана = {my_median(LST)}')
    print(f'медиана из модуля statistics = {statistics.median(LST)}')
    print(f'медиана сортировкой = {sorted(LST)[len(LST)//2]}')
