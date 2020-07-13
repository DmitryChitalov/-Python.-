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

import timeit
import random


def bubble_sort(orig_list, reverse=False):
    n = 1
    flag = True
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if not reverse:
                if orig_list[i] < orig_list[i + 1]:
                    orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                    flag = False
            else:
                if orig_list[i] > orig_list[i + 1]:
                    orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                    flag = False
        if flag:
            return orig_list
        n += 1
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(orig_list)
print(bubble_sort(orig_list, reverse=True))


# замеры 10
print(timeit.timeit("bubble_sort(orig_list, reverse=True)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list, reverse=True)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list, reverse=True)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

"""
Результат работы с оптимизацией:
[47, 28, 80, 47, -92, 85, -8, 13, -81, 39]
[-92, -81, -8, 13, 28, 39, 47, 47, 80, 85]
0.0028236999999999984
0.023103700000000005
0.43554410000000005

Результат работы без оптимизации:
[39, 66, -21, 72, -45, 67, 65, 26, 53, 21]
[-45, -21, 21, 26, 39, 53, 65, 66, 67, 72]
0.04387829999999998
2.8387881
143.7684148

Вывод:
С оптимизацией программа, в зависимости от исходных данных, работает быстрее до сотен раз
"""