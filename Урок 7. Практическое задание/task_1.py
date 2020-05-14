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
import timeit


def bubble_sort(orig_list):
    """Функция сортировки пузырьком массива по убыванию"""
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list

def bubble_sort_opt(orig_list):
    """Оптимизированна функция сортировки пузырьком массива по убыванию
    (если за проход по списку не совершается ни одной сортировки, то завершение)"""
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(orig_list)-1):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                swapped = True
    return orig_list

def bubble_sort_opt_2(orig_list):
    """Оптимизированна функция сортировки пузырьком массива по убыванию
    (если за проход по списку не совершается ни одной сортировки, то завершение)"""
    n = 1
    while n < len(orig_list):
        k = 0 #счетчик отсутствия замены
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
            else:
                k += 1
        if k == len(orig_list) - n:
            break
        else:
            n += 1
    return orig_list

orig_list = [random.randint(-100, 100) for _ in range(10)]
new_list_1 = bubble_sort(orig_list.copy())
new_list_2 = bubble_sort_opt(orig_list.copy())
new_list_3 = bubble_sort_opt_2(orig_list.copy())
print(f"Original list: {orig_list}")
print(f"New list: {new_list_1}")
print(f"New list: {new_list_2}")
print(f"New list: {new_list_3}")

# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]

print(timeit.timeit("bubble_sort(orig_list.copy())", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit.timeit("bubble_sort_opt(orig_list.copy())", \
    setup="from __main__ import bubble_sort_opt, orig_list", number=1000))
print(timeit.timeit("bubble_sort_opt_2(orig_list.copy())", \
    setup="from __main__ import bubble_sort_opt_2, orig_list", number=1000))

"""Результат:
обычный пузырек - 0.0122974
улучшенный пузырек - 0.012922799999999998
улучшенный пузырек 2 - 0.011853099999999998
"""

# замеры 100
orig_list = [random.randint(-100, 100) for _ in range(100)]

print(timeit.timeit("bubble_sort(orig_list.copy())", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit.timeit("bubble_sort_opt(orig_list.copy())", \
    setup="from __main__ import bubble_sort_opt, orig_list", number=1000))
print(timeit.timeit("bubble_sort_opt_2(orig_list.copy())", \
    setup="from __main__ import bubble_sort_opt_2, orig_list", number=1000))

"""Результат:
обычный пузырек - 1.0994884
улучшенный пузырек - 1.5117200000000002
улучшенный пузырек 2 - 1.1241097999999998
"""

# замеры 1000
orig_list = [random.randint(-100, 100) for _ in range(1000)]

print(timeit.timeit("bubble_sort(orig_list.copy())", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit.timeit("bubble_sort_opt(orig_list.copy())", \
    setup="from __main__ import bubble_sort_opt, orig_list", number=1000))
print(timeit.timeit("bubble_sort_opt_2(orig_list.copy())", \
    setup="from __main__ import bubble_sort_opt_2, orig_list", number=1000))

"""Результат:
обычный пузырек - 115.6596704
улучшенный пузырек - 177.5295594
улучшенный пузырек 2 - 128.2879716
"""

"""Вывод:
Оптимизированный пузырек (второй вариант через переменную счетчик) чуть быстрее обычного на небольших входных данных.
При массиве в 1000 элементов он выполняется немного дольше. Оптимизация через логическую переменную выполняется значительно дольше.
Следовательно, данная оптимизация неэффективна."""