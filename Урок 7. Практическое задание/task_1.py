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
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list


def bubble_sort2(orig_list):
    for i in range(len(orig_list) - 1, 0, -1):
        flag = True
        for n in range(i):
            if orig_list[n] < orig_list[n + 1]:
                orig_list[n], orig_list[n + 1] = orig_list[n + 1], orig_list[n]
                flag = False
        if flag:
            break
    return orig_list


orig_list = [randint(-100, 100) for _ in range(1000)]
test_list = orig_list.copy()
test_list_2 = orig_list.copy()

bubble_sort(test_list)
bubble_sort2(test_list_2)

print(orig_list)
print(test_list)
print(test_list_2)

print(timeit("bubble_sort(test_list)", setup="from __main__ import bubble_sort, test_list", number=1))
print(timeit("bubble_sort(test_list_2)", setup="from __main__ import bubble_sort, test_list_2", number=1))

# Проведя замеры времени, сделал вывод, что функция с "флагом" работает немного быстрее,
# но не всегда. зависит от исходного списка
