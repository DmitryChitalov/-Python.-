"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random

size = 10
random_range = 100

def task7_1(arr, reverse=False):
    sign = int(reverse) * 2 - 1
    n = 1
    while n < len(arr):
        is_sorted = True
        for i in range(len(arr) - n):
            if arr[i] * sign < arr[i + 1] * sign:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            break
        n += 1



rand_data = [random.randrange(-random_range, random_range) for _ in range(size)]
print('Исходный массив:', rand_data)
task7_1(rand_data, reverse=True)
print('Отсортированный:', rand_data)

#python -m timeit -n 100 -s "import random" "x = [random.randint(-100, 100) for _ in range(10)]" "import task_1" "task_1.task7_1(x)"
#100 loops, best of 5: 23.4 usec per loop
