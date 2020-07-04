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

from random import randint
from timeit import timeit


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


def bubble_sort_changed(orig_list):
    n = 1
    while n < len(orig_list):
        a = True
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                a = False
        if a:
            break
        n += 1
    return orig_list


test_list = [randint(-100, 100) for _ in range(20)]
print(test_list)
l = test_list
m = test_list
print(bubble_sort(l))
print(bubble_sort_changed(m))


i = [randint(-100, 100) for _ in range(1000)]
j = [randint(-100, 100) for _ in range(1000)]
b = timeit("bubble_sort(i)", setup="from __main__ import bubble_sort, i", number=1)
c = timeit("bubble_sort_changed(j)", setup="from __main__ import bubble_sort_changed, j", number=1)
print(f'При ста элементах \n {b} - оригинальный пузырь \n {c} - измененный')

"""
При ста элементах 
 0.0010061999999999988 - оригинальный пузырь 
 0.0008992999999999987 - измененный

Даёт незначительный прирост по времени (и то не всегда), доработка не обязательна.
"""




