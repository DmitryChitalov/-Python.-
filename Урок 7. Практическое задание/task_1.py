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

import time
from random import randint

def bubble(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    print(f'{array} - bubble simple')

def bubble_m(array):
    for i in range(len(array) - 1, 0, -1):
        swapped = False
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                swapped = True
        if not swapped:
            break
    print(f'{array} - bubble modernized')

NUMS = [randint(-100, 100) for i in range(10)]
print(f'{NUMS} - исходный список')

t1 = time.process_time()
bubble(NUMS)
t2 = time.process_time()
bubble_time = t2 - t1

t1 = time.process_time()
bubble_m(NUMS)
t2 = time.process_time()
bubble_m_time = t2 - t1

print(f'bubble simple - {bubble_time} s')
print(f'bubble modernized - {bubble_m_time} s')
