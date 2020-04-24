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
import copy


def bubble_sort(orig_list):
    n = 1
    flag = False
    start_list = copy.deepcopy(orig_list)
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                flag = True
        if not flag:
            break
        n += 1
    return f"начальный список{start_list} конечный{orig_list}"


def bubble_sort2(orig_list):
    n = 1
    start_list = copy.deepcopy(orig_list)
    while n < len(orig_list):
        t = 0
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return f"начальный список{start_list} конечный{orig_list}"






orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10

print("замеры 10 с выходом:")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print("Без выхода")
print(timeit.timeit("bubble_sort2(orig_list)", \
    setup="from __main__ import bubble_sort2, orig_list", number=1000))


orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print("замеры 100 с выходом")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))
print("Без выхода")
print(timeit.timeit("bubble_sort2(orig_list)", \
    setup="from __main__ import bubble_sort2, orig_list", number=1000))

orig_list = [random.randint(-10000, 10000) for _ in range(1000)]

# замеры 1000

print("замеры 1000 с выходом")
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

print("Без выхода")
print(timeit.timeit("bubble_sort2(orig_list)", \
    setup="from __main__ import bubble_sort2, orig_list", number=1000))
"""
замеры 10 с выходом:
0.013286840000000001
Без выхода
0.019024961
замеры 100 с выходом
0.1004286
Без выхода
0.7062443230000001
замеры 1000 с выходом
1.199337974
Без выхода
66.694136468
функция с выходом оказалась быстрей
"""