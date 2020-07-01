"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
from timeit import timeit

user_input = int(input('Введите количество чисел в массиве: '))
orig_list = [uniform(0, 50) for _ in range(user_input)]
print(orig_list)
test_list = orig_list.copy()
test_list_2 = orig_list.copy()


# вариант функции из урока
def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


# немного другой вариант сортировки слиянием
def merge_sort_2(oridgin_list):
    if len(oridgin_list) < 2:
        return oridgin_list

    mid = len(oridgin_list) // 2

    left = merge_sort(oridgin_list[:mid])
    right = merge_sort(oridgin_list[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


merge_sort(test_list)
merge_sort_2(test_list_2)
print(test_list)

print(timeit("merge_sort(test_list)", setup="from __main__ import merge_sort, test_list", number=1000))
print(timeit("merge_sort_2(test_list_2)", setup="from __main__ import merge_sort_2, test_list_2", number=1000))

'''
Провел замеры скорости работы двух функций, вариант данный на уроке работает
примерно на 20% быстрее.
'''
