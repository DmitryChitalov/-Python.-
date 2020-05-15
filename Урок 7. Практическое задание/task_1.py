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
import timeit
import random


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list

def sort(orig_list):
    a = 0
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                a = 1
        if a == 0:
            break
        n += 1
    return orig_list



orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list))
print(sort(orig_list))

print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit.timeit("sort(orig_list)", \
    setup="from __main__ import sort, orig_list", number=1000))

"""
Замер времени
1.405935388999751
0.02390589499964335
"""