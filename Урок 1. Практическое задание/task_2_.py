"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

from random import randint

nums = []
for i in range(10):
    nums.append(randint(1,99))
print(nums)


# algorithm_1 - O(n^2):

def get_min_num(lst):
    num_min = nums[0]
    for j in range(len(nums)):
        if nums[j] < num_min:
            num_min = nums[j]
    return num_min


print(get_min_num(nums))

# algorithm_2 - O(n):

def get_min(lst):
    num_min = min(lst)
    return num_min

print(get_min(nums))


















