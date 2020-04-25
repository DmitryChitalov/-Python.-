"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
"""Алгоритм не защищен от случаев когда в массиве есть повторяющиеся элементы
значения которых лежат в диапазоне от min до медианы"""


from random import randint
from copy import deepcopy
NUMB = 5 # int(input('Массив размером 2m + 1\nВведите m: '))
ARY = [randint(-100, 100) for _ in range(NUMB * 2 + 1)]

# выводим исходный массив и отсортированный для проверки
print(f'{ARY}\n{sorted(ARY)}')


def median(ary):
    minimal = min(ary)
    for _ in range(NUMB):  #
        nextmin = max(ary)
        for i in ary:
            # if i == minimal:
            #     continue
            if minimal < i < nextmin:
                nextmin = i
        minimal = nextmin
    return minimal


print(median(deepcopy(ARY)))
