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

# Linux 64-bit, Python 3.6.9

import memory_profiler
import time
from random import randint


# Декоратор для мониторинга производительности
def performance_checker(func):
    def wrapped(*args, **kwargs):
        # левые отсечки времени и памяти
        t1 = time.process_time()
        m1 = memory_profiler.memory_usage()

        result = func(*args, **kwargs)

        # правые отсечки времени и памяти
        t2 = time.process_time()
        m2 = memory_profiler.memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")
        return result
    return wrapped

# Для начала рассмотрим программу, которая должна иметь минимальный расход по
# памяти
@performance_checker
def bit_operations(a_val: int, b_val: int) -> int:
    """ Простые битовые операции """
    result = a_val & b_val
    result = a_val | b_val
    result = a_val ^ b_val
    result = a_val >> 2
    result = a_val << 2
    result = ~a_val
    return result


print('Битовые операции. Простой мониторинг')
bit_operations(5, 6)
# >>> Битовые опарации
# >>> Выполнение заняло 0.0003523279999999851 сек and 0.0 Мб

del bit_operations

# Посмотрим подробнее на расход памяти на каждой строчке выполнения программы
@memory_profiler.profile
def bit_operations(a_val: int, b_val: int) -> int:
    """ Простые битовые операции """
    result = a_val & b_val
    result = a_val | b_val
    result = a_val ^ b_val
    result = a_val >> 2
    result = a_val << 2
    result = ~a_val
    return result


print('Битовые операции. Подробный анализ')
bit_operations(5, 6)
# Line #    Mem usage    Increment   Line Contents
# ================================================
#    60     15.3 MiB     15.3 MiB   @memory_profiler.profile
#    61                             def bit_operations(a_val: int, b_val: int) -> int:
#    62     15.3 MiB      0.0 MiB       result = a_val & b_val
#    63     15.3 MiB      0.0 MiB       result = a_val | b_val
#    64     15.3 MiB      0.0 MiB       result = a_val ^ b_val
#    65     15.3 MiB      0.0 MiB       result = a_val >> 2
#    66     15.3 MiB      0.0 MiB       result = a_val << 2
#    67     15.3 MiB      0.0 MiB       result = ~a_val
#    68     15.3 MiB      0.0 MiB       return result

# Действительно ни одна из строчек пограммы не дает инкремент по памяти.
# Хотя, по идее первоначальная инициализация переменной result должна
# давать инкремент.

del bit_operations

# Рассмотрим Решето Эратосфена
# Проведем сразу подробный анализ
@memory_profiler.profile
def eratosfen(number_simple: int) -> int:
    """ Решето Эратосфена """
    start_list = []
    simple_list = []
    curr_val = 2
    stop_val = number_simple * 10
    if number_simple == 1:
        return curr_val

    for i in range(stop_val):
        start_list.append(i)

    while curr_val < stop_val:
        if start_list[curr_val] != 0:
            j = curr_val * 2
            while j < stop_val:
                start_list[j] = 0
                j = j + curr_val
        curr_val += 1

    for item in start_list:
        if item not in (0, 1):
            simple_list.append(item)

    return simple_list[number_simple - 1]


print('Решето Эратосфена. Подробный мониторинг')
eratosfen(1000)
# >>>
'''
Line #    Mem usage    Increment   Line Contents
================================================
    95     14.7 MiB     14.7 MiB   @memory_profiler.profile
    96                             def eratosfen(number_simple: int) -> int:
    97                                 """ Решето Эратосфена """
    98     14.7 MiB      0.0 MiB       start_list = []
    99     14.7 MiB      0.0 MiB       simple_list = []
   100     14.7 MiB      0.0 MiB       curr_val = 2
   101     14.7 MiB      0.0 MiB       stop_val = number_simple * 10
   102     14.7 MiB      0.0 MiB       if number_simple == 1:
   103                                     return curr_val
   104
   105     15.3 MiB      0.3 MiB       for i in range(stop_val):
   106     15.3 MiB      0.3 MiB           start_list.append(i)
   107
   108     15.3 MiB      0.0 MiB       while curr_val < stop_val:
   109     15.3 MiB      0.0 MiB           if start_list[curr_val] != 0:
   110     15.3 MiB      0.0 MiB               j = curr_val * 2
   111     15.3 MiB      0.0 MiB               while j < stop_val:
   112     15.3 MiB      0.0 MiB                   start_list[j] = 0
   113     15.3 MiB      0.0 MiB                   j = j + curr_val
   114     15.3 MiB      0.0 MiB           curr_val += 1
   115
   116     15.3 MiB      0.0 MiB       for item in start_list:
   117     15.3 MiB      0.0 MiB           if item not in (0, 1):
   118     15.3 MiB      0.0 MiB               simple_list.append(item)
   119
   120     15.3 MiB      0.0 MiB       return simple_list[number_simple - 1]
'''
# Видим, что имеются 2 операции, создающие инкремент памяти
# 105     15.3 MiB      0.3 MiB       for i in range(stop_val):
# 106     15.3 MiB      0.3 MiB           start_list.append(i)

# Попробуем оптимизировать алгоритм
@performance_checker
def eratosfen_optimized(number_simple: int) -> int:
    """ Решето Эратосфена """
    if number_simple == 1:
        return 2

    curr_val = 2
    start_list = []
    simple_list = []
    stop_val = number_simple * 10

    for i in range(stop_val):
        start_list.append(i)

    while curr_val < stop_val:
        if start_list[curr_val] != 0:
            j = curr_val * 2
            while j < stop_val:
                start_list[j] = 0
                j = j + curr_val
        curr_val += 1

    del curr_val
    del stop_val

    for item in start_list:
        if item not in (0, 1):
            simple_list.append(item)

    del start_list

    return simple_list[number_simple - 1]


print('Решето Эратосфена после оптимизации. Простой мониторинг')
eratosfen_optimized(1000)
# >>> Решето Эратосфена после оптимизации. Простой мониторинг
# >>> Выполнение заняло 0.01314628499999948 сек and 0.0 Мб
# До оптимизации: Выполнение заняло 0.029690462 сек and 0.34765625 Мб

# Таким образом, удалив ссылки на ненужные переменные мы смогли
# оптимизировать расход памяти нашей программы


# Рассмотрим задачу нахождения индексов чётных чисел
# Немного видоизменим ее
@memory_profiler.profile()
def even_idx():
    A = [(randint(1, 100)) for x in range(1_000_000)]
    B = [x for x in range(len(A)) if A[x] % 2 == 0]
    return len(B)


print('Работа с массивами и списковыми включениями. Детальный мониторинг.')
print(even_idx())
# >>>
'''
Line #    Mem usage    Increment   Line Contents
================================================
   205     18.3 MiB     18.3 MiB   @memory_profiler.profile()
   206                             def even_idx():
   207     26.0 MiB      0.5 MiB       A = [(randint(1, 100)) for x in range(1_000_000)]
   208     45.3 MiB      0.3 MiB       B = [x for x in range(len(A)) if A[x] % 2 == 0]
   209     45.3 MiB      0.0 MiB       return len(B)
'''
# Видим прирост памяти 45.3 - 18.3 = 27 MiB

# Попробуем оптимизировать работу функции с помощью генераторов
@memory_profiler.profile()
def even_idx_gen():
    m = 1_000_000

    def generator_1(max_):
        for i in range(max_):
            yield randint(1, 100)
    A = generator_1(m)
    B = [x for x in range(m) if next(A) % 2 == 0]
    return len(B)


print('Работа с массивами используем генераторы. Детальный мониторинг.')
print(even_idx_gen())
# >>>
'''
Line #    Mem usage    Increment   Line Contents
================================================
   225     18.1 MiB     18.1 MiB   @memory_profiler.profile()
   226                             def even_idx_gen():
   227     18.1 MiB      0.0 MiB       m = 1_000_000
   228     18.1 MiB      0.0 MiB       def generator_1(max_):
   229     37.6 MiB      0.3 MiB           for i in range(max_):
   230     37.6 MiB      0.0 MiB               yield randint(1, 100)
   231     18.1 MiB      0.0 MiB       A = generator_1(m)
   232     37.6 MiB      0.3 MiB       B = [x for x in range(m) if next(A) % 2 == 0]
   233     37.6 MiB      0.0 MiB       return len(B)

'''
# Видим прирост памяти 37.6 - 18.1 = 19.5 MiB
# Таким образом использование генератора позволило оптимизировать
# использование памяти
