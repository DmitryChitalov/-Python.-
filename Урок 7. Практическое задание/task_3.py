"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import statistics
from random import randint

m = int(input('Введите m: '))

numbers = [randint(0, 50) for _ in range(2*m+1)]


def median(nums):
    nums.sort()
    mid = len(nums)//2
    return nums[mid]


def no_sort(nums):
    while len(nums) >1:
        min_numb = min(nums)
        max_numb = max(nums)
        nums.remove(min_numb)
        nums.remove(max_numb)
    return nums[0]

print('Исходный массив:', numbers)
print(f'Медиана: {median(numbers)}')
print(f'Медиана statistics: {statistics.median(numbers)}')
print(f'Медиана без сортировки: {no_sort(numbers)}')