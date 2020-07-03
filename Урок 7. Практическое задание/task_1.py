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

LST = [randint(-100, 100) for _ in range(30)]
print(LST)


def bubble_1(old_lst, cnt=0):
    lst = old_lst[:]
    for _ in range(len(lst) - 1):
        for i in range(len(lst)):
            if lst[i] > lst[i - 1] and i > 0:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
    return lst


print(timeit("bubble_1(LST)", \
             setup="from __main__ import bubble_1, LST", number=100))
print(bubble_1(LST))


def bubble_2(old_lst, sort=1):
    lst = old_lst[:]
    while sort > 0:
        sort = 0
        for i in range(len(lst)):
            if lst[i] > lst[i - 1] and i > 0:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                sort += 1
    return lst


print(timeit("bubble_2(LST)", \
             setup="from __main__ import bubble_2, LST", number=100))

print(bubble_2(LST))

print(LST)

"""
Доработка скрипта привела к тому что в большинстве случаев скорость выполнения увеличилась
один из вариантов
0.015818744000000003 - старый вариант
0.009746643000000013 - новый
Я пробовал ставить счетчики на циклы, вышло что в наилучшем случае при списке длиной в 10 элементов
улучшеный скрипт справлялся за 5 проходов вместо 9. Но чаще это 8 или 7.
"""