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


def sort_bubble(arr):
    n = 1
    while n < len(arr):
        for element in range(len(arr) - n):
            if arr[element] > arr[element + 1]:
                arr[element], arr[element + 1] = arr[element + 1], arr[element]
        n += 1
    return arr


def sort_bubble_modern(arr):
    n = 1
    cnt = 0
    while n < len(arr):
        for element in range(len(arr) - n):
            if arr[element] > arr[element + 1]:
                arr[element], arr[element + 1] = arr[element + 1], arr[element]
                cnt += 1
        if cnt == 0:
            break
        n += 1
    return arr


NUMS = [randint(-100, 99) for _ in range(100)]
sort_bubble(NUMS)
sort_bubble_modern(NUMS)

"""
print('Замеры по пузырьковой сортировке: ')
print(timeit.timeit("sort_bubble(NUMS)", \
    setup="from __main__ import sort_bubble, NUMS", number=10))
print(timeit.timeit("sort_bubble(NUMS)", \
    setup="from __main__ import sort_bubble, NUMS", number=100))
print(timeit.timeit("sort_bubble(NUMS)", \
    setup="from __main__ import sort_bubble, NUMS", number=1000))

print('Замеры по умной пузырьковой сортировке: ')
print(timeit.timeit("sort_bubble_modern(NUMS)", \
    setup="from __main__ import sort_bubble_modern, NUMS", number=10))
print(timeit.timeit("sort_bubble_modern(NUMS)", \
    setup="from __main__ import sort_bubble_modern, NUMS", number=100))
print(timeit.timeit("sort_bubble_modern(NUMS)", \
    setup="from __main__ import sort_bubble_modern, NUMS", number=1000))
"""