"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import randint, random

def merge_sort(array):

    if len(array) == 1:
        return array
    else:
        left = merge_sort(array[:len(array) // 2])
        right = merge_sort(array[len(array) // 2:])
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array


def rand_list_sort():

    numb = int(input("Введите число элементов: "))
    array = [int(randint(0, 49)) + int(random()) for _ in range(numb)]
    print(f"Исходдный - {array}")
    print(f"Отсортированный - {merge_sort(array)}")


rand_list_sort()