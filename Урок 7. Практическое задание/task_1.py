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

from random import randrange


def get_list(stop, length, start=1):
    return [randrange(start, stop) for _ in range(length)]


def swap(i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def bubble_sort(lst_):
    for j in range(len(lst_) - 1, 0, -1):
        for i in range(j):
            if lst_[i] < lst_[i + 1]:
                swap(i, i + 1)
    return lst_


if __name__ == "__main__":
    lst = get_list(100, 1000, -100)
    bubble_sort(lst)
    print(lst)
