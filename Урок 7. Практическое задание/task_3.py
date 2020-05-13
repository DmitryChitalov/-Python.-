"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random

# Можно отсортировать при помощи встроенной функции:
#
# def sorted_array(array):
#     ordered_list = sorted(array)
#     return ordered_list


def sorted_array(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return sorted_array(less) + [pivot] + sorted_array(greater)


m = random.randint(5, 10)
size = 2 * m + 1
array = [random.randint(0, 50) for _ in range(size)]
sort_list = sorted_array(array)

print(f'Массив размером {size} элементов : {array}')
print(f'Отсортированный массив: {sort_list}')
print(f'Медиана : {sort_list[len(sort_list) // 2 ]}')
