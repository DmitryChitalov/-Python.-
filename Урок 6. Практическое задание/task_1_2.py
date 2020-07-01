from random import randint
from memory_profiler import profile
from sys import getrefcount


@profile
def task_5():
    a = [randint(-100, 100) for i in range(100000)]
    print(a)
    b = [a[el] for el in range(len(a)) if a[el] < 0]
    c = min(b, key=abs)
    d = a.index(min(b, key=abs))
    print(f'Максимальный отрицательный элемент в данном массиве = {c}, его индекс {d}')
    print(f'Количество ссылок на первый массив  {getrefcount(a)}')
    print(f'Количество ссылок на первый массив  {getrefcount(b)}')


task_5()

"""
Line #    Mem usage    Increment   Line Contents
================================================
    14     16.1 MiB     16.1 MiB   @profile
    15                             def task_5():
    16     18.7 MiB      0.6 MiB       a = [randint(-100, 100) for i in range(100000)]
    17     18.2 MiB      0.0 MiB       print(a)
    18     18.6 MiB      0.1 MiB       b = [a[el] for el in range(len(a)) if a[el] < 0]
    19     18.6 MiB      0.0 MiB       c = min(b, key=abs)
    20     18.6 MiB      0.0 MiB       d = a.index(min(b, key=abs))
    21     18.6 MiB      0.0 MiB       print(f'Максимальный отрицательный элемент в данном массиве = {c}, 
    его индекс {d}')

По данным замера так же видно, чтобольшую часть памяти берёт на себя генератор списка, при небольших значениях массивов 
трата памяти незначительна, использовав range = 10**6 показало относительно большое использвание памяти в первом 
массиве, и незначительное во втором (во многом благодаря генератору списков).
Для оптимизации кода слеудет удалить ссылки на массив a и b командой del после выполнения кода.

Не понятно, почему начальные 16.1 приросли до 18.7 при инкременте 0.6. Тоже погрешность?

"""