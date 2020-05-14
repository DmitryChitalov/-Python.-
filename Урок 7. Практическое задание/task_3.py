"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random
from statistics import median


def my_mediana(list, lenght):
    """поска медианы"""

    if len(list) == 1:
        return list[0]

    point = random.choice(list)

    left_el = [el for el in list if el < point]
    right_el = [el for el in list if el > point]
    center = [el for el in list if el == point]

    if lenght < len(left_el):
        return my_mediana(left_el, lenght)
    elif lenght < len(left_el) + len(center):
        return center[0]
    else:
        return my_mediana(right_el, lenght - len(left_el) - len(center))


m = int(input("введите m для массива: "))
orig_list = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(orig_list)

list_median = my_mediana(orig_list, len(orig_list) / 2)
print(f'Медиана в массиве: {list_median}')

print(f' проверка {median(orig_list)}')
