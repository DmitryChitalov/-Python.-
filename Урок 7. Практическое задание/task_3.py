"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

from random import randint

SIZE = 3


def partition(array, start, end):
    """Partition"""
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    """Quick sort"""
    if start >= end:
        return

    part = partition(array, start, end)
    quick_sort(array, start, part-1)
    quick_sort(array, part+1, end)


def mediana(numbers):
    """Finding mediana"""
    middle = len(numbers)//2
    return numbers[middle]


NUMS = [randint(-100, 100) for _ in range(SIZE * 2 + 1)]
print(NUMS)
quick_sort(NUMS, 0, len(NUMS) - 1)
print(NUMS)
print("Mediana", mediana(NUMS))
