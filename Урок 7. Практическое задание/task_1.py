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


def bubble_sort(A):
    n = 1
    while n < len(A):
        sort_num  = True
        for i in range(len(A) - n):
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sort_num = False
        if sort_num == True:
            break
        n += 1
    return A

A = [random.randint(-100, 100) for _ in range(10)]

print(f'Исходный массив: {A}')
print(f'Отсортированный по убыванию массив: {bubble_sort(A)}')
print(timeit.timeit('bubble_sort(A)', \
    setup='from __main__ import bubble_sort, A', number=1000))


A = [random.randint(-100, 100) for _ in range(100)]
# len(A) = 100
print(timeit.timeit('bubble_sort(A)', \
    setup='from __main__ import bubble_sort, A', number=1000))


A = [random.randint(-100, 100) for _ in range(1000)]
# len(A) = 1000
print(timeit.timeit('bubble_sort(A)', \
    setup='from __main__ import bubble_sort, A', number=1000))


# len(A) = 10
# с оптимизацией: 0.0034652000000000016
# без:            0.017352300000000043

# len(A) = 100
# с оптимизацией: 0.0217377
# без:            1.2617971

# len(A) = 1000
# с оптимизацией: 0.3676744
# без:            135.3131037

# Оптимизация значительно улучшила скорость выполнения программы,
# колоссальная разница при большой длине массива.
