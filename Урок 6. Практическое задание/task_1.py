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
import sys
import timeit
import cProfile
import math
from memory_profiler import profile
# без решета


@profile
def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
            else:
                count += 1

    return current_prime

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     23     10.7 MiB     10.7 MiB   @profile
#     24                             def prime(num):
#     25     10.7 MiB      0.0 MiB       count = 1
#     26     10.7 MiB      0.0 MiB       current_prime = 2
#     27
#     28     10.7 MiB      0.0 MiB       while count < num:
#     29     10.7 MiB      0.0 MiB           current_prime += 1
#     30     10.7 MiB      0.0 MiB           for i in range(2, int(current_prime ** 0.5) + 1):
#     31     10.7 MiB      0.0 MiB               if current_prime % i == 0:
#     32     10.7 MiB      0.0 MiB                   break
#     33                                         else:
#     34     10.7 MiB      0.0 MiB                   count += 1
#     35
#     36     10.7 MiB      0.0 MiB       return current_prime
#
# # c решетом Эратосфена, обнаружил данное решение, но почему-то оно менее эффектично нежели код "без решета"......


MULTIPLIER = 1.3


@profile
def prime_2(num):
    size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30

    array = [True for _ in range(size)]
    array[:2] = [False, False]
    count = 0

    for i in range(2, size):
        if array[i]:
            count += 1
            if count == num:
                return i

            for j in range(i ** 2, size, i):
                array[j] = False


if __name__ == '__main__':
    prime(10000)
    prime_2(10000)

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     60     10.7 MiB     10.7 MiB   @profile
#     61                             def prime_2(num):
#     62     10.7 MiB      0.0 MiB       size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30
#     63
#     64     10.7 MiB      0.0 MiB       array = [True for _ in range(size)]
#     65     10.7 MiB      0.0 MiB       array[:2] = [False, False]
#     66     10.7 MiB      0.0 MiB       count = 0
#     67
#     68     10.7 MiB      0.0 MiB       for i in range(2, size):
#     69     10.7 MiB      0.0 MiB           if array[i]:
#     70     10.7 MiB      0.0 MiB               count += 1
#     71     10.7 MiB      0.0 MiB               if count == num:
#     72     10.7 MiB      0.0 MiB                   return i
#     73
#     74     10.7 MiB      0.0 MiB               for j in range(i ** 2, size, i):
#     75     10.7 MiB      0.0 MiB                   array[j] = False

# Оба алгоритма как я понял вполне рабочие и не занимают лишней памяти при выполнении, при num = 1000

# А вот при увеличении num = 10000, во втором алгоритме начинает задействоваться больше памяти при пробегании по массиву

# 1 алгоритм
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     23     10.7 MiB     10.7 MiB   @profile
#     24                             def prime(num):
#     25     10.7 MiB      0.0 MiB       count = 1
#     26     10.7 MiB      0.0 MiB       current_prime = 2
#     27
#     28     10.7 MiB      0.0 MiB       while count < num:
#     29     10.7 MiB      0.0 MiB           current_prime += 1
#     30     10.7 MiB      0.0 MiB           for i in range(2, int(current_prime ** 0.5) + 1):
#     31     10.7 MiB      0.0 MiB               if current_prime % i == 0:
#     32     10.7 MiB      0.0 MiB                   break
#     33                                         else:
#     34     10.7 MiB      0.0 MiB                   count += 1
#     35
#     36     10.7 MiB      0.0 MiB       return current_prime
#
#
# 2 алгоритм
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     61     10.7 MiB     10.7 MiB   @profile
#     62                             def prime_2(num):
#     63     10.7 MiB      0.0 MiB       size = int(num * math.log(num) * MULTIPLIER) if num > 10 else 30
#     64
#     65     11.7 MiB      0.1 MiB       array = [True for _ in range(size)]
#     66     11.7 MiB      0.0 MiB       array[:2] = [False, False]
#     67     11.7 MiB      0.0 MiB       count = 0
#     68
#     69     11.7 MiB      0.0 MiB       for i in range(2, size):
#     70     11.7 MiB      0.0 MiB           if array[i]:
#     71     11.7 MiB      0.0 MiB               count += 1
#     72     11.7 MiB      0.0 MiB               if count == num:
#     73     11.7 MiB      0.0 MiB                   return i
#     74
#     75     11.7 MiB      0.0 MiB               for j in range(i ** 2, size, i):
#     76     11.7 MiB      0.0 MiB                   array[j] = False

