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
from pympler import asizeof

@profile
def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

@profile
def func(n):
    b = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            b.append(i)
    return b

if __name__ == "__main__":
    func(1000)
    eratosthenes(1000)
print(asizeof.asizeof(eratosthenes(1000)))
print(asizeof.asizeof(func(1000)))


# При анализе функцией asizeof ,было выявленно что моя функция хоть и медленней ( урок 4 задание 2), но потребляет в два раза меньше
# памяти (func - 6824), чем Эратосфена ( eratosthenes 14520)
#
# Python 3.7
# Win 10 (x64)
#
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     16     16.0 MiB     16.0 MiB   @profile
#     17                             def func(n):
#     18     16.0 MiB      0.0 MiB       b = []
#     19     16.0 MiB      0.0 MiB       for i in range(2, n):
#     20     16.0 MiB      0.0 MiB           result = True
#     21     16.0 MiB      0.0 MiB           for j in range(2, i):
#     22     16.0 MiB      0.0 MiB               if i % j == 0:
#     23     16.0 MiB      0.0 MiB                   result = False
#     24     16.0 MiB      0.0 MiB           if result:
#     25     16.0 MiB      0.0 MiB               b.append(i)
#     26     16.0 MiB      0.0 MiB       return b
#
#
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      6     16.0 MiB     16.0 MiB   @profile
#      7                             def eratosthenes(n):
#      8     16.0 MiB      0.0 MiB       sieve = list(range(n + 1))
#      9     16.0 MiB      0.0 MiB       sieve[1] = 0
#     10     16.0 MiB      0.0 MiB       for i in sieve:
#     11     16.0 MiB      0.0 MiB           if i > 1:
#     12     16.0 MiB      0.0 MiB               for j in range(i + i, len(sieve), i):
#     13     16.0 MiB      0.0 MiB                   sieve[j] = 0
#     14     16.0 MiB      0.0 MiB       return sieve
#



