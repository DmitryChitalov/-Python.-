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

MAX_SIZE = int(input('Введите размер массива: '))


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


def bubble_sort_no_smart(array):
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] < array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]

print(bubble_sort(numbers))

time1 = timeit(f'bubble_sort({numbers})',
               setup='from __main__ import bubble_sort',
               number=1000)

numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]

time2 = timeit(f'bubble_sort_no_smart({numbers})',
               setup='from __main__ import bubble_sort_no_smart',
               number=1000)
print(time1)
print(time2)

"""
Время работы функции без улучшения с увеличением кол-ва элементов массива стремительно увеличивается
    на 100 элементах:
        с улучшением: 0.009916695
        без улучшения: 0.6977301520000001
    на 1000 элементов:
        с улучшением: 0.09072035
        без улучшения: 77.99184451800001
"""