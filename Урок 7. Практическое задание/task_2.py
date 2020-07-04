"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random


def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2   # Делим массив на два подмассива
        left = orig_list[:center]      # Левая часть от первого элеметна до центра
        right = orig_list[center:]     # Правая от центра до последнего
        # print('левая ', left)                    # С помощью принтов нагядно видно как происходит деление
        # print('правая ', right)
        merge_sort(left)            # Через рекурсию повторяем деление каждой половинки на другие половинки
        merge_sort(right)

        i, j, k = 0, 0, 0
        # print(orig_list)
        while i < len(left) and j < len(right):   # Далее поочередно заполняем половины  списков элеиентами в
            if left[i] < right[j]:                # порядке возрастания. Последним этам идёт присвоение элементам ориги
                orig_list[k] = left[i]            # нального списка значений отсортированных склееных половинок
                i += 1
                # print('основной 1 ',orig_list)
            else:
                orig_list[k] = right[j]
                j += 1
                # print('основной 2',orig_list)
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1
            # print('основной 3 ',orig_list)

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
            # print('основной 4',orig_list)
        return orig_list


a = [random()*50 for el in range(int(input("Введите число элементов: ")))]
print(f'Исходный список - {a}')
# print(merge_sort([9, 6, 41, 29, 40]))  на этом примере разбирался
print(f'Отсортированный список - {merge_sort(a)}')
