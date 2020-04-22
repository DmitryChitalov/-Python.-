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

from timeit import Timer
from random import randint


def new_double_bubble_sort(array):
    array_len = len(array)
    count = 0
    while count < array_len // 2:
        is_sorted = True
        for i in range(count, array_len - 1 - count):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
            if array[array_len - 1 - i] > array[array_len - i - 2]:
                array[array_len - 1 - i], array[array_len - i - 2] = array[array_len - i - 2], array[array_len - 1 - i]
                is_sorted = False
        if is_sorted:
            break
        count += 1
    return array


def new_bubble_sort(array):
    array_len = len(array)
    count = 0
    while count < array_len:
        is_sorted = True
        for i in range(array_len - 1 - count):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
                start = i
        if is_sorted:
            break
        count += 1
    return array


def double_bubble_sort(array):
    array_len = len(array)
    count = 0
    while count < array_len // 2:
        is_sorted = True
        for i in range(array_len - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
            if array[array_len - 1 - i] > array[array_len-i-2]:
                array[array_len - 1 - i], array[array_len - i - 2] = array[array_len - i - 2], array[array_len - 1 - i]
                is_sorted = False
        if is_sorted:
            break
        count += 1
    return array


def bubble_sort_mod(array):
    array_len = len(array)
    count = 0
    while count < array_len:
        is_sorted = True
        for i in range(array_len - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        if is_sorted:
            break
        count += 1
    return array


def bubble_sort(array):

    array_len = len(array)
    count = 0
    while count < array_len:
        for i in range(array_len - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        count += 1
    return array


rand_array = [randint(-100, 100) for _ in range(1000)]
t1 = Timer(f"bubble_sort({rand_array})", "from __main__ import bubble_sort")
t2 = Timer(f"bubble_sort_mod({rand_array})", "from __main__ import bubble_sort_mod")
t3 = Timer(f"double_bubble_sort({rand_array})", "from __main__ import double_bubble_sort")
t4 = Timer(f"new_bubble_sort({rand_array})", "from __main__ import new_bubble_sort")
t5 = Timer(f"new_double_bubble_sort({rand_array})", "from __main__ import new_double_bubble_sort")
print("bubble_sort - > ", t1.timeit(number=100))
print("bubble_sort_mod - > ", t2.timeit(number=100))
print("double_bubble_sort - >", t3.timeit(number=100))
print("new_bubble_sort - >", t4.timeit(number=100))
print("new_double_bubble_sort - >", t5.timeit(number=100))
"""
bubble_sort - >  10.4284546
bubble_sort_mod - >  9.9929033
double_bubble_sort - > 10.6773859
new_bubble_sort - > 7.1422226
new_double_bubble_sort - > 9.420667200000004 
"""
# Наиболее быстрым является метод new_bubble_sort => 7.1422226
print(rand_array)
print(new_bubble_sort(rand_array))





