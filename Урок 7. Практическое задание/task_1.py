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

import random, timeit, cProfile
#from memory_profiler import Profile

def bubble_sort(unsort_list):
    for i in range(len(unsort_list)):
        for j in range(1, len(unsort_list)):
            if unsort_list[j - 1] < unsort_list[j]:
                unsort_list[j - 1], unsort_list[j] = unsort_list[j], unsort_list[j - 1]
    return unsort_list

def bubble_sort_mod(unsort_list):
    for i in range(len(unsort_list)):
        changes_count = 0
        for j in range(1, len(unsort_list)):
            if unsort_list[j - 1] < unsort_list[j]:
                unsort_list[j - 1], unsort_list[j] = unsort_list[j], unsort_list[j - 1]
                changes_count += 1
        if changes_count == 0:
            break
    return unsort_list


list_to_sort = [random.randrange(-100, 100, 1) for i in range(20)]
print(list_to_sort)

print(timeit.timeit("bubble_sort(list_to_sort)", \
    setup="from __main__ import bubble_sort, list_to_sort", number=1000))
print(bubble_sort(list_to_sort))

list_to_sort = [random.randrange(-100, 100, 1) for i in range(20)]
print(list_to_sort)

print(timeit.timeit("bubble_sort_mod(list_to_sort)", \
    setup="from __main__ import bubble_sort_mod, list_to_sort", number=1000))
print(bubble_sort(list_to_sort))

"""
[-26, 46, -44, -53, -98, 53, 98, 20, -11, 69, -27, -76, -11, -77, -73, 75, 39, -60, -34, 38]
0.055910900000000006
[98, 75, 69, 53, 46, 39, 38, 20, -11, -11, -26, -27, -34, -44, -53, -60, -73, -76, -77, -98]
[-10, 95, -69, 91, 33, -20, -97, -12, 76, 83, -79, -10, 39, 22, 78, 84, -85, -73, 13, -9]
0.003451599999999999
[95, 91, 84, 83, 78, 76, 39, 33, 22, 13, -9, -10, -10, -12, -20, -69, -73, -79, -85, -97]

Доработанный метод пузырька примерно в 16 раз быстрее исходного

"""