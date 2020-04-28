"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random
import statistics

m = int(input('Введите число : '))
numbers = [random.randint(-100, 100) for _ in range(2 * m + 1)]




def median(nums):
    half = len(nums) // 2
    nums.sort()
    if not len(nums) % 2:
        return (nums[half - 1] + nums[half]) / 2
    return nums[half]


print('Исходный массив:', numbers)
print('Медиана:', median(numbers))
print('Медиана statistics:', statistics.median(numbers))