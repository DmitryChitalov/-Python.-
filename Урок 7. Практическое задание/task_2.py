"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import numpy
import timeit


# orig_list = [numpy.random.uniform(0.000000000000000, 50.000000000000000) for _ in range(5)]


def merge_sort(orig_list):
    to_be_sorted = orig_list[:]
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
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
        return to_be_sorted


orig_list = [numpy.random.uniform(0.000000000000000, 50.000000000000000) for _ in range(5)]
# замеры 5
print(f"Original array for 5 numbers is {orig_list}")
print(timeit.timeit("merge_sort(orig_list)", \
                    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Sorted array for 5 numbers is {merge_sort(orig_list)}")

orig_list = [numpy.random.uniform(0.000000000000000, 50.000000000000000) for _ in range(10)]

# замеры 10
print(f"Original array for 10 numbers is {orig_list}")
print(timeit.timeit("merge_sort(orig_list)", \
                    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Sorted array for 10 numbers is {merge_sort(orig_list)}")

orig_list = [numpy.random.uniform(0.000000000000000, 50.000000000000000) for _ in range(15)]
print(f"Original array for 15 numbers is {orig_list}")
# замеры 15
print(timeit.timeit("merge_sort(orig_list)", \
                    setup="from __main__ import merge_sort, orig_list", number=1000))
print(f"Sorted array for 15 numbers is {merge_sort(orig_list)}")
