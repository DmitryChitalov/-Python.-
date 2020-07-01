"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import randint

m = int(input('Введите число m, что бы сфрормировать массив по формуле 2m + 1: '))
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'не отсортированный массив: \n {orig_list}')


def cocktail_sort(orig_list):
    left = 0
    right = len(orig_list) - 1
    while left <= right:
        for i in range(left, right):
            if orig_list[i] > orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        right -= 1
        for i in range(right, left, -1):
            if orig_list[i - 1] > orig_list[i]:
                orig_list[i], orig_list[i - 1] = orig_list[i - 1], orig_list[i]
        left += 1
    return orig_list


cocktail_sort(orig_list)
print(f'отсортированный массив: \n {orig_list}')
print(f'Медиана заданного массива число {orig_list[m]}')
