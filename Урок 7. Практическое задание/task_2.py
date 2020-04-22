"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from timeit import Timer
from random import randint, random


def merge_sort(array):

    if len(array) == 1:
        return array
    else:
        left = merge_sort(array[:len(array) // 2])
        right = merge_sort(array[-len(array) // 2:])
        j = 0
        k = 0
        for i in range(len(array)):
            if j >= len(left):
                array[i] = right[k]
                k += 1
            elif k >= len(right):
                array[i] = left[j]
                j += 1
            elif left[j] > right[k]:
                array[i] = right[k]
                k += 1
            else:
                array[i] = left[j]
                j += 1
        return array


def rand_list_sort():

    value = int(input("Введите число элементов: "))
    real_number_list = [randint(0, 49) + random() for _ in range(value)]
    print(f"Исходдный - {real_number_list}")
    print(f"Отсортированный - {merge_sort(real_number_list)}")


rand_list = [randint(-100, 100) for _ in range(1000)]
t1 = Timer(f"merge_sort({rand_list})", "from __main__ import merge_sort")
print("merge_sort -> ", t1.timeit(number=100))
"""
merge_sort ->  merge_sort ->  0.28327329999999995
"""
# По сравнению с bubble_sort выйгрыш по времени составляет примерно 7.1422226 / 0.2768055 = 25.5
rand_list_sort()

