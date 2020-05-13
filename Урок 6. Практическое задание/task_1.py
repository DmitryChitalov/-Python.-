"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from random import randint
import math


@profile
def foo():
    pass

@profile
def func():
    y = []
    x = [randint(1, 100) for _ in range(50000)]
    for i in x:
        if i % 2 == 0:
            y.append(math.sqrt(i))

    for i in x:
        if i % 2 != 0:
            y.append(math.sin(i))
    del y
    del x


foo()
func()

'''
Больше всего потребляет памяти сам profile видно при вызове ф-ции foo()
Функция func()  при вызове тратит 15.5 MiB на profile ,а дальше по мере 
выполнения кода заполняется списками x и y до 16.9 MiB и 18.1 соответсвенно.
по мере удаления списков память освобождается.


Line #    Mem usage    Increment   Line Contents
================================================
     6     15.5 MiB     15.5 MiB   @profile
     7                             def foo():
     8     15.5 MiB      0.0 MiB       pass

Line #    Mem usage    Increment   Line Contents
================================================
    11     15.5 MiB     15.5 MiB   @profile
    12                             def func():
    13     15.5 MiB      0.0 MiB       def f():
    14     15.5 MiB      0.0 MiB           pass
    15     15.5 MiB      0.0 MiB       f()
    16     15.5 MiB      0.0 MiB       y = []
    17     16.1 MiB      0.2 MiB       x = [randint(1, 100) for _ in range(50000)]
    18     16.9 MiB      0.1 MiB       for i in x:
    19     16.9 MiB      0.0 MiB           if i % 2 == 0:
    20     16.9 MiB      0.0 MiB               y.append(math.sqrt(i))
    21                             
    22     18.1 MiB      0.1 MiB       for i in x:
    23     18.1 MiB      0.0 MiB           if i % 2 != 0:
    24     18.1 MiB      0.2 MiB               y.append(math.sin(i))
    25     16.9 MiB      0.0 MiB       del y
    26     16.5 MiB      0.0 MiB       del x
'''
