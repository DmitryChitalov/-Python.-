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


def bubble_sort(orig_list):
    '''классический пузырек из примера'''
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i +
                                        1]:  # заменил знак, чтобы было убывание
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list


def my_bubble_sort(orig_list):
    '''
    Попытка оптимизации пузырька из примера.
    Останавливает цикл, если изменений в списке в текущей итерации
    не производилось
    '''
    n = 1
    swap = True  # флаг проверки были ли изменения в списке
    start = 0
    while swap:
        swap = False
        for i in range(start, len(orig_list) - n):
            if orig_list[i] < orig_list[i +
                                        1]:  # заменил знак, чтобы было убывание
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                # еще одна четная попытка улучшить алгоритм, начиная цикл с индекса,
                # предшествующего тому, на котором было первое изменение на предыдущей итерации
                # if not swap:
                #     start = i - 1 if i > 0 else 0
                swap = True
        if not swap:
            break
        n += 1
    return orig_list


if __name__ == '__main__':
    # замеры 10
    ORIG_LIST = [random.randint(-100, 100) for _ in range(10)]
    TIMER_1 = timeit.Timer(
        f"bubble_sort({ORIG_LIST})",
        "from __main__ import bubble_sort")
    TIMER_2 = timeit.Timer(
        f"my_bubble_sort({ORIG_LIST})",
        "from __main__ import my_bubble_sort")
    print("bubble_sort (10) - > ", TIMER_1.timeit(number=100))
    print("my_bubble_sort (10) - > ", TIMER_2.timeit(number=100))

    # замеры 100
    ORIG_LIST = [random.randint(-100, 100) for _ in range(100)]
    TIMER_1 = timeit.Timer(
        f"bubble_sort({ORIG_LIST})",
        "from __main__ import bubble_sort")
    TIMER_2 = timeit.Timer(
        f"my_bubble_sort({ORIG_LIST})",
        "from __main__ import my_bubble_sort")
    print("bubble_sort (100) - > ", TIMER_1.timeit(number=100))
    print("my_bubble_sort (100) - > ", TIMER_2.timeit(number=100))

    # замеры 1000
    ORIG_LIST = [random.randint(-100, 100) for _ in range(1000)]
    TIMER_1 = timeit.Timer(
        f"bubble_sort({ORIG_LIST})",
        "from __main__ import bubble_sort")
    TIMER_2 = timeit.Timer(
        f"my_bubble_sort({ORIG_LIST})",
        "from __main__ import my_bubble_sort")
    print("bubble_sort (1000) - > ", TIMER_1.timeit(number=100))
    print("my_bubble_sort (1000) - > ", TIMER_2.timeit(number=100))

'''
bubble_sort (10) time  0.0016441189999999994
my_bubble_sort (10) time  0.0015183619999999988
bubble_sort (100) time  0.119603735
my_bubble_sort (100) time  0.11577022999999997
bubble_sort (1000) time  12.217924481
my_bubble_sort (1000) time  12.407982775999999

Как видно по результатам измерений, добавление флага практически не приводит
к изменению скорости работы алгоритма, а в некоторых случаях, в зависимости
от входного списка, даже приводит к ухудшению скорости.
'''

'''
Также проверена эффективность всех алгоритмов
для длины списка 10,100 и 1000
Упорядочены от менее эффективных к более.

Естественно встроенные намного быстрее,
как минимум, ввиду своих сишных реализаций.
lst.sort() чуток быстрее sorted(lst) так как изменяет массив на месте,
а последняя создает новый массив.

Алгоритм шейкерной сортировки
0.015983921
1.088197159
126.859567025

Алгоритм сортировки пузырьком
0.015858164
1.144032245
124.44606054600001

Алгоритм сортировки вставками
0.009605519999999996
0.646190271
70.553488585

Алгоритм сортировки выбором
0.010239745000000001
0.463762505
45.200458996

Алгоритм сортировки слиянием
0.019773266
0.33210659
4.572674346

Алгоритм быстрой сортировки
0.013680298
0.164703089
1.535945662

Стандартная сортировка (sorted)
0.0005747060000000012
0.005047554000000003
0.080659427

Стандартная сортировка (lst.sort)
0.0004771080000000004
0.004556687
0.077863017
'''
