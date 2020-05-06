"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit

"""1.Сравниваем цикл и рекурсию:"""

# Начальный, неоптимизированный вариант через цикл
def inverted(num):
    """O(n) – линейная сложность"""
    inv_num = ''
    while num > 0:
        new_num = num % 10
        num = num // 10
        inv_num += str(new_num)
    return int(inv_num)


# Вариант с рекурсией
def invert_number(number, inverted_number):
    """O(n) – линейная сложность"""
    if number == 0:
        return inverted_number
    return invert_number(number // 10, inverted_number * 10 + number % 10)


# Улучшенный вариант через цикл
def inverted_opt(num):
    """O(n) – линейная сложность"""
    inv_num = 0
    while num > 0:
        inv_num = inv_num * 10 + num % 10
        num = num // 10
    return inv_num


print(timeit.timeit("inverted(3568)", setup="from __main__ import inverted", number=1000))
print(timeit.timeit("invert_number(5768, 0)", setup="from __main__ import invert_number", number=1000))

"""Результат 1:
неоптимизированный цикл - 0.0014969999999999983
рекурсия - 0.0009502000000000017
Вывод: неоптимизированный вариант с циклом выполняется дольше рекурсии."""

print(timeit.timeit("inverted_opt(5768)", setup="from __main__ import inverted_opt", number=1000))
print(timeit.timeit("invert_number(5768, 0)", setup="from __main__ import invert_number", number=1000))

"""Результат 2:
оптимизированный цикл - 0.0005686000000000024
рекурсия - 0.0008824000000000019
Вывод: после оптимизации (ушла от конкатенации строк, более короткий код) 
вариант с циклом стал быстрее рекурсии. Рекурсия медленнее цикла while."""

# 2.Сравниваем встроенную функцию и свой алгоритм:

# Вариант со встроенной функцией
def func1(list):
    """O(n) – линейная сложность"""
    max_i = list.index(max(list))
    min_i = list.index(min(list))
    list[max_i], list[min_i] = list[min_i], list[max_i]
    return list


# Собственный алгоритм нахождения индекса
def func2(list):
    """O(n) – линейная сложность"""
    max_i = 0
    min_i = 0
    for i in range(len(list)):
        if list[i] > list[max_i]:
            max_i = i
        elif list[i] < list[min_i]:
            min_i = i
    list[max_i], list[min_i] = list[min_i], list[max_i]
    return list

print(timeit.timeit("func1([34, 59, 0, 12, 36, 234, 92, 45])", setup="from __main__ import func1", number=1000))
print(timeit.timeit("func2([34, 59, 0, 12, 36, 234, 92, 45])", setup="from __main__ import func2", number=1000))

"""Результаты:
встроенная функция - 0.000985299999999998
свой алгоритм - 0.0018560999999999994
Вывод 2. Встроенная функция нахождения индекса почти в два раза быстрее моего алгоритма. И это неудивительно, не зря же она встроена."""
