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
import memory_profiler
from functools import reduce
import time
from random import random
import math
from random import randint


# Декоратор
def time_memory(func):
    def wrapped(*args, **kwargs):
        t1 = time.process_time()
        m1 = memory_profiler.memory_usage()

        result = func(*args, **kwargs)

        t2 = time.process_time()
        m2 = memory_profiler.memory_usage()
        time_process = t2 - t1
        mem_process = m2[0] - m1[0]
        print(f"время {time_process} сек память {mem_process}")
        return result
    return wrapped
rand = [(randint(1, 100)) for x in range(1000000)]



@memory_profiler.profile()
def even_gen():
    b = [indx for indx, i in enumerate([randint(1, 100) for x in range(1_000_000)], 1) if i % 2 == 0]
    return len(b)

print(even_gen())

"""
реализация с генератором
Line #    Mem usage    Increment   Line Contents
================================================
    42     40.4 MiB     40.4 MiB   @memory_profiler.profile()
    43                             def even_gen():
    44     53.8 MiB      0.2 MiB       b = [indx for indx, i in enumerate([randint(1, 100) for x in range(1_000_000)], 1) if i % 2 == 0]
    45     50.0 MiB      0.0 MiB       return len(b)

прирост памяти 9.6 Mib
"""

@memory_profiler.profile()
def even():
    m = 1_000_000

    def generator_1(max_):
        for i in range(max_):
            yield randint(1, 100)
    B = [x for x in range(m) if next(generator_1(m)) % 2 == 0]
    return len(B)

print(even())

"""
реализация с генератором
Line #    Mem usage    Increment   Line Contents
================================================
    59     40.6 MiB     40.6 MiB   @memory_profiler.profile()
    60                             def even():
    61     40.6 MiB      0.0 MiB       m = 1_000_000
    62
    63     50.0 MiB      0.0 MiB       def generator_1(max_):
    64     50.0 MiB      0.1 MiB           for i in range(max_):
    65     50.0 MiB      0.0 MiB               yield randint(1, 100)
    66     50.0 MiB      0.4 MiB       B = [x for x in range(m) if next(generator_1(m)) % 2 == 0]
    67     50.0 MiB      0.0 MiB       return len(B)
прирост 10.4 Mib
"""





@memory_profiler.profile()
def func(n):
    t = []
    for i in range(n):
        num = randint(1, 100) # здесь мы перезаписываем объект, старый удаляется и не хранится в памяти
        if num % 2 == 0:
            t.append(num)
    return len(t)

print(func(1_000_000))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    79     40.9 MiB     40.9 MiB   @memory_profiler.profile()
    80                             def func(n):
    81     40.9 MiB      0.0 MiB       t = []
    82     42.6 MiB      0.0 MiB       for i in range(n):
    83     42.6 MiB      0.0 MiB           num = randint(1, 100)
    84     42.6 MiB      0.0 MiB           if num % 2 == 0:
    85     42.6 MiB      0.4 MiB               t.append(num)
    86     42.6 MiB      0.0 MiB       return len(t)
    прирост 1.7 Mib

доработанный скрипт занимает меньше памяти,
потому что каждое число мы сразу проверяем на четность и перезаписываем новым
Нам не нужно хранить целый массив
"""




@memory_profiler.profile()
def func3(COL, ROW):
    max_num = max([min(i) for i in [[randint(1, 100) for _ in range(0, ROW)] for _ in range(0, COL)]])
    return max_num
"""
Line #    Mem usage    Increment   Line Contents
================================================
   125     32.8 MiB     32.8 MiB   @memory_profiler.profile()
   126                             def func3(COL, ROW):
   127     37.7 MiB      0.2 MiB       max_num = max([min(i) for i in [[randint(1, 100) for _ in range(0, ROW)] for _ in range(0, COL)]])
   128     33.8 MiB      0.0 MiB       return max_num

"""
# 2 ---------------------------
@memory_profiler.profile()
def func4(COL, ROW):
    a = []
    for i in range(0, COL):
        b = []
        for j in range(0, ROW):
            b.append(randint(1, 100))
        a.append(b)
    min_list = [min(i) for i in a]
    return max(min_list)
"""
Line #    Mem usage    Increment   Line Contents
================================================
   131     33.8 MiB     33.8 MiB   @memory_profiler.profile()
   132                             def func4(COL, ROW):
   133     33.8 MiB      0.0 MiB       a = []
   134     37.6 MiB      0.0 MiB       for i in range(0, COL):
   135     37.6 MiB      0.0 MiB           b = []
   136     37.6 MiB      0.0 MiB           for j in range(0, ROW):
   137     37.6 MiB      0.2 MiB               b.append(randint(1, 100))
   138     37.6 MiB      0.0 MiB           a.append(b)
   139     37.6 MiB      0.0 MiB       min_list = [min(i) for i in a]
   140     37.6 MiB      0.0 MiB       return max(min_list)
реализация c генератором более выгода по памяти 

"""


print(func3(1000, 1000))
print(func4(1000, 1000))



