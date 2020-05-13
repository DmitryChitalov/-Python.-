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
"""Применил сортировку"""