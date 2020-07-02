"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randrange
import statistics


def median(lst):
    for idx in range(len(lst)):
        smaller, equal, bigger = 0, 0, 0
        for idy in range(len(lst)):
            if lst[idx] < lst[idy]:
                smaller += 1
            elif lst[idx] > lst[idy]:
                bigger += 1
            else:
                equal += 1
        equal -= 1

        if smaller == bigger or smaller == equal + bigger or bigger == smaller + equal or (
                equal > 1 and abs(bigger - smaller) < equal):
            return lst[idx]


M = 12
list_a = [randrange(0, 100) for _ in range(2 * M + 1)]
print(list_a)
print(f'Медиана списка: {median(list_a)}')
print(f'Решение разработчиков python: {statistics.median(list_a)}')  # для сравнения правильности результата
""" находил медиану без сортировки
вывод: при нахождении медианы без сортировки (это решение в тз обозначалось как наиболее сложное) полученное значение 
медианы совпало со значением встроенной функции при разных значениях (в тот числе ряде одинаковых чисел) """


