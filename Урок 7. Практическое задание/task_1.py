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


def create_list(list_len, l_border, r_border):
    return [randint(l_border, r_border - 1) for _ in range(list_len)]


# оригинальный
def bubble_sort(base_list):
    flag = False
    for idx in range(len(base_list[:]) - 1, 0, -1):
        if base_list[idx] > base_list[idx-1]:
            base_list[idx], base_list[idx-1], flag = base_list[idx-1], base_list[idx], True
    return bubble_sort(base_list) if flag else base_list[:]


#оптимизированный
def bubble_sort_opt(base_list, itr=0):
    flag = False
    for idx in range(len(base_list[:]) - 1, itr, -1):
        if base_list[idx] > base_list[idx-1]:
            base_list[idx], base_list[idx-1], flag = base_list[idx-1], base_list[idx], True
    return bubble_sort_opt(base_list, itr+1) if flag else base_list[:]


a = create_list(10, 0, 10)
print(a)
print(bubble_sort(a))
print(bubble_sort_opt(a))
print('Пузырьковая: ', timeit('bubble_sort(create_list(1000, 0, 10))', 'from __main__ import bubble_sort, create_list', number=100))
print('Оптимизиров: ', timeit('bubble_sort_opt(create_list(1000, 0, 10))', 'from __main__ import bubble_sort_opt, create_list', number=100))

"""
[4, 9, 6, 2, 2, 3, 5, 3, 3, 3]
[9, 6, 5, 4, 3, 3, 3, 3, 2, 2]
[9, 6, 5, 4, 3, 3, 3, 3, 2, 2]
Пузырьковая:  8.634379411007103
Оптимизиров:  6.528080139003578
# Вывод: легкая оптимизация алгоритма высвободило почти 20% ресурсов.
"""

