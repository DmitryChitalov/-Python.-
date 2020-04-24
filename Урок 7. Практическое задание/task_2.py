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


def my_merge_sort(orig_list):
    '''Сортировка слиянием, измененный пример'''
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]
        orig_list[:] = []  # немного память оптимизируем
        my_merge_sort(left)
        my_merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list.append(left[i])
                i += 1
            else:
                orig_list.append(right[j])
                j += 1
        # из оптимизаций придумал только как код сократить =)
        # ну и совсем немножко ускоряет алгоритм
        orig_list.extend(left[i:] or right[j:])
        return orig_list


if __name__ == '__main__':

    NUM = int(input('Введите число элементов: '))
    ORIG_LIST = [random.uniform(0, 50) for _ in range(NUM)]
    print(f'Исходный - {ORIG_LIST}')
    print(f'Отсортированный - {my_merge_sort(ORIG_LIST)}')

    TIMER = timeit.Timer(
        f"my_merge_sort({ORIG_LIST})",
        "from __main__ import my_merge_sort")
    print("merge_sort time ", TIMER.timeit(number=100))

'''
Сортировка слиянием однозначно быстрее пузырька при одинаковых параметрах
my_bubble_sort (1000) 12.407982775999999
vs
my_merge_sort (1000) 0.31437103399999966
'''
