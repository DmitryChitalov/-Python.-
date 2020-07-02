"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randrange


def get_list(stop, length, start=1):
    return [randrange(start, stop) for _ in range(length)]


def hoare_sort(arr):
    if len(arr) <= 1:
        return
    barrier = arr[0]
    left = []
    middle = []
    right = []
    for el in arr:
        if el < barrier:
            left.append(el)
        elif el == barrier:
            middle.append(el)
        else:
            right.append(el)
    hoare_sort(left)
    hoare_sort(right)
    k = 0
    for el in left + middle + right:
        arr[k] = el
        k += 1


def find_media(arr, med):
    return arr[med]


if __name__ == "__main__":
    median_index = 48
    array_length = 2 * median_index + 1
    lst = get_list(start=-50, stop=50, length=array_length)
    hoare_sort(lst)
    median = lst[median_index]
    print(f"median = {median} \nsorted list = {lst}")
