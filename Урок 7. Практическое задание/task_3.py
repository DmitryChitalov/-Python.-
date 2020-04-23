"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import randint


# Решение задания через сортировку Шелла
def shell_sort(input_list):
    """Сортировка Шелла"""
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp

        gap = gap // 2


print("Формула размера массива 2m + 1")
M = int(input("Введите m: "))
NUMS = [randint(0, 100) for _ in range(2 * M + 1)]
print(f"Изначальный массив: {NUMS}")
shell_sort(NUMS)
print(f"Отсортированный массив: {NUMS}")
print(f"Медиана: {NUMS[M]}")

