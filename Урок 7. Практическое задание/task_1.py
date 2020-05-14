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
'''
Comment:
Я попробовала для наглядности эксперимента интервал от -1000 до 1000 и различные длины массива (10, 100 и 500). 
Результаты с добавлением заметно сокращали время. Чем больше входные данные, тем сильнее эффект.
'''
import random
import timeit


def bubble(ls):
    n = 1
    while n < len(ls):
        k = 0
        for i in range(len(ls) - n):
            if ls[i] < ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                k += 1
        if k == 0:
            break
        n += 1
    return ls


# замеры 10

my_list = [random.randint(-1000, 1000) for i in range(10)]
print(my_list)
print(bubble(my_list))

print(timeit.timeit("bubble(my_list)", setup="from __main__ import bubble, my_list", number=1000))

'''
Без добавления:
0.01072485799999999

С добавлением:
0.002004884999999998
'''

# замеры 100

my_list = [random.randint(-1000, 1000) for i in range(100)]
print(my_list)
print(bubble(my_list))

print(timeit.timeit("bubble(my_list)", setup="from __main__ import bubble, my_list", number=1000))

'''
Без добавления:
0.396699641

С добавлением:
0.016689071
'''

# замеры 500

my_list = [random.randint(-1000, 1000) for i in range(500)]
print(my_list)
print(bubble(my_list))

print(timeit.timeit("bubble(my_list)", setup="from __main__ import bubble, my_list", number=1000))

'''
Без добавления:
10.223768448

С добавлением:
0.044398813999999995
'''
