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


def bubble_while(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list

def bubble_for(orig_list):
    for i in range(len(orig_list)-1):
        for j in range(len(orig_list)-i-1):
            if orig_list[j] < orig_list[j+1]:
                buff = orig_list[j]
                orig_list[j] = orig_list[j+1]
                orig_list[j+1] = buff
    return orig_list

def shortBubbleSort(orig_list):
    exchanges = True
    passnum = len(orig_list)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if orig_list[i]<orig_list[i+1]:
               exchanges = True
               temp = orig_list[i]
               orig_list[i] = orig_list[i+1]
               orig_list[i+1] = temp
       passnum = passnum-1
    return orig_list



orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f"Исходный массив")
print(orig_list)

print(f"Отсортированный массив")
print(shortBubbleSort(orig_list))

print(f"Скорость")
t1 = timeit.Timer(f"bubble_while({orig_list})", "from __main__ import bubble_while")
t2 = timeit.Timer(f"bubble_for({orig_list})", "from __main__ import bubble_for")
t3 = timeit.Timer(f"shortBubbleSort({orig_list})", "from __main__ import shortBubbleSort")
print(f"bubble_while - > ", t1.timeit(number=1000))
print(f"bubble_for - > ", t2.timeit(number=1000))
print(f"shortBubbleSort - > ", t3.timeit(number=1000))


# Реализованно 3 вида алгоритма по убыванию методом "пузырька":
# bubble_while реализация через while
# bubble_for реализация через for
# shortBubbleSort алгоритм модифицирован, чтобы останавливаться раньше, если обнаруживает, что задача выполнена

