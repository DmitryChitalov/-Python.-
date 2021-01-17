"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
"""Сортировка пузырьком"""

import timeit

# исходный массив
orig_list = [71, -7, 97, -51, -76, -39, -41, -77, -21, -30, -97, -9, 12, 92, -47, 33, 79, 70, -90, -79]
def b_sort_desc(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


# тот же массив, но последние 10 элементов уже отсортированы
orig_list_presorted = [71, -7, 97, -21, -9, 12, 92, 33, 79, 70, -30, -39, -41,-47, -51, -76, -77, -79, -90, -97]
def b_sort_desc_v2(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_sorted = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                is_sorted = True
        if not is_sorted:
            break
        n += 1
    return lst_obj

print(f'Source list\n {orig_list}')
print(f'With no optimization\n {b_sort_desc(orig_list)}')
print(f'Source list partly presorted\n {orig_list_presorted}')
print(f'With optimization\n {b_sort_desc_v2(orig_list_presorted)}')


print(timeit.timeit("b_sort_desc(orig_list)", \
     setup="from __main__ import b_sort_desc, orig_list", number=100))

print(timeit.timeit("b_sort_desc_v2(orig_list_presorted)", \
     setup="from __main__ import b_sort_desc_v2, orig_list_presorted", number=100))

"""
Без оптимизации 0.0019780999999999965
С оптимизацией  0.00015790000000000248
"""