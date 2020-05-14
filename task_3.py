"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random
import timeit
from memory_profiler import profile


@profile
def cocktail_sort(orig_list):
    left = 0
    right = len(orig_list) - 1
    while left <= right:
        for i in range(left, right):
            if orig_list[i] > orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        right -= 1
        for i in range(right, left, -1):
            if orig_list[i - 1] > orig_list[i]:
                orig_list[i], orig_list[i - 1] = orig_list[i - 1], orig_list[i]
        left += 1
    return orig_list


def median(lst):
    ordered_list = cocktail_sort(lst)
    print(f'Отсортированный массив: {ordered_list}')
    l = len(lst)
    i = (l - 1) // 2

    if l % 2:
        return ordered_list[i]
    else:
        return (ordered_list[i] + ordered_list[i + 1]) / 2


n = random.randint(1, 10)
orig_list = [random.randint(0, 50) for _ in range(2 * n + 1)]
print(timeit.timeit("cocktail_sort(orig_list)", setup="from __main__ import cocktail_sort, orig_list", number=1000))
copy_list = orig_list.copy()

print(f'Исходный массив: {orig_list}')
m = median(copy_list)
print(f'Медиана: {m}')

# 0.014498300000000002 время работы (без учета профайлера)