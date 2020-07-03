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

from random import random
import timeit

def bubble(list):
    for i in range(9):
        for j in range(9 - i):
            if list[j] < list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]


N = 10
list = [0] * N

for i in range(10):
    list[i] = int(random() * 100)

print(f'Исходный массив: {list}')

bubble(list)
print(f'Отсортированный массив: {list}')

# Время выполнение функции - 0.010304400000000002

def bubble_2(list_2):
    for i in range(9):
        for j in range(9 - i):
            if list_2[j] < list_2[j + 1]:
                list_2[j + 1], list_2[j] = list_2[j], list_2[j + 1]
            else:
                break


N = 10
list_2 = [0] * N

for i in range(10):
    list_2[i] = int(random() * 100)

print(f'Исходный массив: {list_2}')

bubble(list_2)
print(f'Отсортированный массив: {list_2}')

print(timeit.timeit("bubble(list)", setup="from __main__ import bubble, list", number=1000))
print(timeit.timeit("bubble_2(list_2)", setup="from __main__ import bubble_2, list_2", number=1000))

# Время выполнения функции - 0.004216400000000002. Таким образом получаем время выполнения после доработки
# в 2 раза быстрее.
