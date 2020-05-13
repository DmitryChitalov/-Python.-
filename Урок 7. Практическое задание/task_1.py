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


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


orig_list = [random.randint(-100, 99) for _ in range(10)]
print(orig_list)

print(bubble_sort(orig_list))
# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 99) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 99) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1000))

'''
Результаты:
[-92, -17, 35, -36, -78, 12, -5, 23, 28, -3]
[35, 28, 23, 12, -3, -5, -17, -36, -78, -92]
0.015521000000000007
1.0532005
142.0282607

Время на 1000 элементах очень большое. Неэффективно использовать этот алгоритм на большом количестве
элементов без оптимизации.
'''

def bubble_sort_2(orig_list):
    sort_el = True
    while sort_el:
        sort_el = False
        for i in range(len(orig_list)-1):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                sort_el = True

    return orig_list

orig_list_2 = [87, 60, 42, 37, 9, 0, -29, -47, -66, -77]

# замеры 10
print(timeit.timeit("bubble_sort_2(orig_list)", \
    setup="from __main__ import bubble_sort_2, orig_list", number=1000))

orig_list_2 = [100, 98, 96, 95, 94, 93, 93, 92, 91, 89, 88, 87, 86, 85, 82, 80, 79, 76, 75, 69, 68, 67, 67, 66, 63,
             62, 61, 54, 53, 50, 48, 47, 45, 43, 41, 41, 37, 36, 35, 34, 29, 28, 25, 25, 24, 24, 20, 18, 15, 15, 14,
             13, 8, 8, 7, 5, 5, 5, 5, 4, 3, 2, -11, -12, -13, -15, -15, -23, -30, -30, -33, -35, -35, -38, -40, -41,
             -42, -46, -46, -55, -57, -57, -59, -61, -66, -66, -73, -75, -76, -77, -82, -82, -83, -83, -87, -87, -95,
             -95, -98, -99]

# замеры 100
print(timeit.timeit("bubble_sort_2(orig_list)", \
    setup="from __main__ import bubble_sort_2, orig_list", number=1000))

'''
Результат проверки работы "флажка":
0.0035492999999999983 - на 10 элементах
0.029086999999999988 - на 100 элементах
Мы видим по результатам замеров времени на выполнение алгоритма с уже отсортированным списком, 
что выполнение происходит значительно быстрее, значит, "флажок" работает и можно считать эту оптимизацию эффективной. 
'''