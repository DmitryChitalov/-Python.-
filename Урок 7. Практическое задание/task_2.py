"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
n = int(input('Введите число элементов: '))

my_list = [random.uniform(0, 49) for _ in range(n)]

def merge_sort(some_list):
    if len(some_list) > 1:
        center = len(some_list) // 2
        left = some_list[:center]
        right = some_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                some_list[k] = left[i]
                i += 1
            else:
                some_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            some_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            some_list[k] = right[j]
            j += 1
            k += 1
        return some_list

print(f'Исходный - {my_list}\nОтсортированный - {merge_sort(my_list)}')