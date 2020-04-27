"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random


def bubble_sort(orig_list):
    num = 0
    len_list = len(orig_list)
    while num < len_list:
        flag = 0
        for i in list(range(len_list))[:num:-1]:
            if orig_list[i] > orig_list[i-1]:
                orig_list[i], orig_list[i - 1] = orig_list[i - 1], orig_list[i]
                flag = 1
        if not flag:
            break
        num += 1
    return orig_list


ORIG_LIST = [random.randint(-100, 100) for _ in range(30)]
print(ORIG_LIST)
print(bubble_sort(ORIG_LIST))
