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
import timeit

""" Судя по проведенным замерам скорость алгоритма с "отсечкой" в случае его сортировки значительно выше, соответсвенно
алгоритм эффективней и быстрее.
"""


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        is_sorted = True
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i + 1], orig_list[i] = orig_list[i], orig_list[i+1]
                is_sorted = False

        if is_sorted:
            break

        n += 1
    return orig_list


user_list = [random.randint(-100, 100) for _ in range(10)]
# print(f'Изначальный список - {or_list}')
# print(f'Отсортированныый список - {bubble_sort(or_list)}')

# замеры 10
print(timeit.timeit("bubble_sort(user_list)", number=1000, globals=globals()))  # 0.002342854999999991

user_list_1 = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(user_list_1)", number=1000, globals=globals()))  # 0.030227458999999998

user_list_2 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(user_list_2)", number=1000, globals=globals()))  # 0.301444718


def bubble_sort_1(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


my_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("bubble_sort_1(my_list)", number=1000, globals=globals()))  # 0.02234721399999999

my_list_1 = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort_1(my_list_1)", number=1000, globals=globals()))  # 0.559923608

my_list_2 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort_1(my_list_2)", number=1000, globals=globals()))  # 53.539715445999995



