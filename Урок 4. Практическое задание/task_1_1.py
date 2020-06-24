"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
<<<<<<< Updated upstream
=======
from timeit import Timer
from random import randint


def switch_max_min():
    n = 100000  # Константная 1
    a = [randint(-20, 20) for el in range(n)]  # Линейная сложность n
    #print(a)
    a_max = a.index(max(a))
    a_min = a.index(min(a))
    a[a_max], a[a_min] = a[a_min], a[a_max]
    #print(a)
    #print(f'Максимальное число на позиции {a.index(max(a))}, минимальное на {a.index(min(a))}')

switch_max_min()


def maxim(lst):
    maxim = lst[0]
    i = 0
    while True:
        if i == len(lst):
            break
        elif maxim > lst[i]:
            maxim = maxim
        else:
            maxim = lst[i]
        i += 1
    return maxim


def minim(lst):
    minim = lst[0]
    i = 0
    while True:
        if i == len(lst):
            break
        elif minim < lst[i]:
            minim = minim
        else:
            minim = lst[i]
        i += 1
    return minim


def switch_2():
    n = 100000
    a = [randint(-20, 20) for el in range(n)]
    #print(a)
    a_max = a.index(maxim(a))
    a_min = a.index(minim(a))
    a[a_max], a[a_min] = a[a_min], a[a_max]
    #print(a)
    #print(f'Максимальное число на позиции {a.index(maxim(a))}, минимальное на {a.index(minim(a))}')


switch_2()

t1 = Timer("switch_max_min()", "from __main__ import switch_max_min")
print("Встроенные функции ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("switch_2()", "from __main__ import switch_2")
print("Собственные функции ", t2.timeit(number=1000), "milliseconds")

"""
Решил сравнить  производительность при использовании внутренних функций и собственных: min() и max()
Внутренние функции при n = 10 - 0.0214
Собственные функции при n = 10 - 0.025

Поскольку линейная сложность у обеих функций, то нет смысла увеличивать число n.
Но ради интереса ввёл n = 100000. 
Внутренние функции при n = 10 - 191.2
Собственные функции при n = 10 - 230.6
Достаточно ощутимая разница, доказано, что внутренние функции работают быстрее
"""