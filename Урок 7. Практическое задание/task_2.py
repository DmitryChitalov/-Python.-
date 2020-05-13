"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random


def merge_sort(A):
    if len(A) > 1:
        center = len(A) // 2
        left = A[:center]
        right = A[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return A


A = [random.uniform(0, 50) for _ in range(10)]
print(f'Исходный массив: {A}')
print(f'Отсортированный методом слияния массив: {merge_sort(A)}')
# len(A) = 10
print(timeit.timeit('merge_sort(A)', \
    setup='from __main__ import merge_sort, A', number=1000))
# 0.03248589999999999

A = [random.uniform(0, 50) for _ in range(100)]

# len(A) = 100
print(timeit.timeit('merge_sort(A)', \
    setup='from __main__ import merge_sort, A', number=1000))
# 0.3261698

A = [random.uniform(0, 50) for _ in range(1000)]

# len(A) = 1000
print(timeit.timeit('merge_sort(A)', \
    setup='from __main__ import merge_sort, A', number=1000))
# 5.5866808
