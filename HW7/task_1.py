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


# from random import randint
import random
import timeit


def bubble_sort(original_list):
    n = 1
    while n < len(original_list):
        for i in range(len(original_list) - n):
            if original_list[i] > original_list[i + 1]:
                original_list[i], original_list[i + 1] = original_list[i + 1], original_list[i]
        n += 1
    return original_list


"Доробатываем алгоритм"
def revert_bubble(original_list_2):
    n = 1
    t = 0
    while n < len(original_list_2):
        for i in range(len(original_list_2) - n):
            if original_list_2[i] < original_list_2[i + 1]:
                original_list_2[i], original_list_2[i + 1] = original_list_2[i + 1], original_list_2[i]
                t = 1
        if t == 0:
            break
        n += 1
    return original_list_2

original_list = [random.randint(-100, 100) for _ in range(100)]
print(f'Исходные массивы:\n{original_list}\n')

original_list_2 = [random.randint(-100, 100) for _ in range(100)]
print(f'Сортированные массивы:\n{original_list_2}\n')

print(timeit.timeit("bubble_sort(original_list)", setup="from __main__ import bubble_sort, original_list", number=1000))
print(timeit.timeit("revert_bubble(original_list_2)", setup="from __main__ import revert_bubble, original_list_2", number=1000))

"""Результат замеров 
original_list: 0.2859691070043482
original_list_2: 0.00576216698391363 
По этим данным можно сделать вывод, что доработка показала эффективность"""