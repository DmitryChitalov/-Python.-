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
import timeit

original_array = [randint(-100, 100) for _ in range(10)]
# original_array = [+15, 0, 25, 36, 50, 52,56]
print(f"Original array is: {original_array}")


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] > orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list
# print(f"Sorted array is {bubble_sort(original_array)}")


def revert_bubble_sort(orig_list):
    sorted = True
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                sorted = False
        if sorted:
            break

        n += 1
    return orig_list
# print(f"Revert sorted array is {revert_bubble_sort(original_array)}")



original_array = [randint(-100, 100) for _ in range(10)]
print("buble sort for range 10 - ",timeit.timeit("bubble_sort(original_array)", setup="from __main__ import bubble_sort, original_array", number=1000))

print("revert buble sort for range 10 - ", timeit.timeit("revert_bubble_sort(original_array)", setup="from __main__ import revert_bubble_sort, original_array", number=100))

original_array = [randint(-100, 100) for _ in range(100)]
print("buble sort for range 100 - ",timeit.timeit("bubble_sort(original_array)", setup="from __main__ import bubble_sort, original_array", number=100))

print("revert buble sort for range 100 - ", timeit.timeit("revert_bubble_sort(original_array)", setup="from __main__ import revert_bubble_sort, original_array", number=100))


original_array = [randint(-100, 100) for _ in range(1000)]
print("buble sort for range 1000 - ",timeit.timeit("bubble_sort(original_array)", setup="from __main__ import bubble_sort, original_array", number=100))

print("revert buble sort for range 1000 - ", timeit.timeit("revert_bubble_sort(original_array)", setup="from __main__ import revert_bubble_sort, original_array", number=100))

"""
Original array is: [79, -32, -27, -97, -45, 25, 77, -2, 62, 48]
buble sort for range 10 -  0.008165580999999977
revert buble sort for range 10 -  0.00017421499999992207
buble sort for range 100 -  0.05334371999999998
revert buble sort for range 100 -  0.0028186460000000357
buble sort for range 1000 -  5.419853857
revert buble sort for range 1000 -  0.1485756450000002

Судя по результатам обратная сортировка но с использованием завершения, если нет ни одной сортировки, работает быстрее
"""

