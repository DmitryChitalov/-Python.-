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

# Laptop Windows 7 64 bit OS, Python version 3.7


from memory_profiler import profile
from sys import getrefcount
from guppy import hpy, heapy
from timeit import timeit
import random

# First example of function
# Count memory usage with memory-profile

# @profile()
# def first_function():
#     cont = True
#     while cont:
#         first_number = 123456789
#         second_number = 123456789
#         sign_operation = '*'
#
#         if sign_operation == '+':
#             return first_number + second_number
#         elif sign_operation == '-':
#             return first_number - second_number
#         elif sign_operation == '*':
#             return first_number * second_number
#         elif sign_operation == '/':
#             return first_number / second_number
#         elif sign_operation == '0':
#             return 'You entered a zero to quite. The calculation will be stopped'
#
#         elif sign_operation not in ['0', '+', '-', '*', '/']:
#             return 'You entered a wrong symbol. Try again'
#
# first_function()
"""
Использование памяти 48.7 Mib для цифр 123456789 и 123456789
Results ot memory-profile

Line #    Mem usage    Increment   Line Contents
================================================
    24     48.7 MiB     48.7 MiB   @profile()
    25                             def first_function():
    26     48.7 MiB      0.0 MiB       cont = True
    27     48.7 MiB      0.0 MiB       while cont:
    28     48.7 MiB      0.0 MiB           first_number = 123456789
    29     48.7 MiB      0.0 MiB           second_number = 123456789
    30     48.7 MiB      0.0 MiB           sign_operation = '*'
    31                             
    32     48.7 MiB      0.0 MiB           if sign_operation == '+':
    33                                         return first_number + second_number
    34     48.7 MiB      0.0 MiB           elif sign_operation == '-':
    35                                         return first_number - second_number
    36     48.7 MiB      0.0 MiB           elif sign_operation == '*':
    37     48.7 MiB      0.0 MiB               return first_number * second_number
    38                                     elif sign_operation == '/':
    39                                         return first_number / second_number
    40                                     elif sign_operation == '0':
    41                                         return 'You entered a zero to quite. The calculation will be stopped'
    42                             
    43                                     elif sign_operation not in ['0', '+', '-', '*', '/']:
    44                                         return 'You entered a wrong symbol. Try again'




"""
# @profile()
# def first_function():
#     cont = True
#     while cont:
#         first_number = 123456789123456789
#         second_number = 123456789123456789
#         sign_operation = '*'
#
#         if sign_operation == '+':
#             return first_number + second_number
#         elif sign_operation == '-':
#             return first_number - second_number
#         elif sign_operation == '*':
#             return first_number * second_number
#         elif sign_operation == '/':
#             return first_number / second_number
#         elif sign_operation == '0':
#             return 'You entered a zero to quite. The calculation will be stopped'
#
#         elif sign_operation not in ['0', '+', '-', '*', '/']:
#             return 'You entered a wrong symbol. Try again'
# first_function()

"""
Если мы берем большие числа для расчета (123456789123456789 и 123456789123456789), то использование памяти не растет. 
Те же 48.7 MiB

Line #    Mem usage    Increment   Line Contents
================================================
    78     48.7 MiB     48.7 MiB   @profile()
    79                             def first_function():
    80     48.7 MiB      0.0 MiB       cont = True
    81     48.7 MiB      0.0 MiB       while cont:
    82     48.7 MiB      0.0 MiB           first_number = 123456789123456789
    83     48.7 MiB      0.0 MiB           second_number = 123456789123456789
    84     48.7 MiB      0.0 MiB           sign_operation = '*'
    85                             
    86     48.7 MiB      0.0 MiB           if sign_operation == '+':
    87                                         return first_number + second_number
    88     48.7 MiB      0.0 MiB           elif sign_operation == '-':
    89                                         return first_number - second_number
    90     48.7 MiB      0.0 MiB           elif sign_operation == '*':
    91     48.7 MiB      0.0 MiB               return first_number * second_number
    92                                     elif sign_operation == '/':
    93                                         return first_number / second_number
    94                                     elif sign_operation == '0':
    95                                         return 'You entered a zero to quite. The calculation will be stopped'
    96                             
    97                                     elif sign_operation not in ['0', '+', '-', '*', '/']:
    98                                         return 'You entered a wrong symbol. Try again'
"""
# ======================================================================================================================

# @profile()
# def generator_function():
#     initial = [random.randint(1, 1000) for item in range(1000000)]
#     final = []
#     for num in initial:
#         if num % 2 == 0:
#             final.append(initial.index(num))
#         else:
#             continue
#     return final
#
#
# generator_function()

"""
Интересно, что в данном случае не указывается значение увеличения памяти для строки 133 и 135. Почему? 
Использование памяти 95,3 MiB
Line #    Mem usage    Increment   Line Contents
================================================
   131     48.8 MiB     48.8 MiB   @profile()
   132                             def generator_function():
   133     79.6 MiB      0.4 MiB       initial = [random.randint(1, 1000) for item in range(1000000)]
   134     79.6 MiB      0.0 MiB       final = []
   135     95.3 MiB      0.0 MiB       for num in initial:
   136     95.3 MiB      0.0 MiB           if num % 2 == 0:
   137     95.3 MiB      0.4 MiB               final.append(initial.index(num))
   138                                     else:
   139                                         continue
   140     95.3 MiB      0.0 MiB       return final

"""

# @profile()
# def cycle_function():
#     initial = [random.randint(1, 1000) for item in range(1000000)]
#     return [num for num in range(len(initial) + 1) if num % 2 == 0]
#
#
# cycle_function()

"""
Интересно, что в данном случае не указывается значение увеличения памяти для строки 157 и 158
Но в данном случае использование памяти в итоге больше за счет использования  list comprehension  в строке 158
Line #    Mem usage    Increment   Line Contents
================================================
   155     48.9 MiB     48.9 MiB   @profile()
   156                             def cycle_function():
   157     79.6 MiB      0.4 MiB       initial = [random.randint(1, 1000) for item in range(1000000)]
   158     99.0 MiB      0.4 MiB       return [num for num in range(len(initial) + 1) if num % 2 == 0]
Использование памяти 99,0 MiB

"""

# ======================================================================================================================

# @profile()
# def func_cycle_range():
#     final = []
#     for x in range(2, 100):
#         multiples = 0
#         for y in range(2, 10000):
#             if y % x == 0:
#                 multiples += 1
#         final.append(f"В диапазоне 2-9999: {multiples} чисел кратны {x}")
#     return '\n'.join(final)
# func_cycle_range()


# h = hpy()
# def func_cycle_range_2():
#     final = []
#     for x in range(2, 1000):
#         multiples = 0
#         for y in range(2, 10000):
#             if y % x == 0:
#                 multiples += 1
#         final.append(f"В диапазоне 2-9999: {multiples} чисел кратны {x}")
#     return '\n'.join(final)
#
# func_cycle_range_2()
# print(h.heap())


"""
Использование memory-profile показывает 48.9 MiB для следющих значений 
Line #    Mem usage    Increment   Line Contents
================================================
   192     48.8 MiB     48.8 MiB   @profile()
   193                             def func_cycle_range():
   194     48.8 MiB      0.0 MiB       final = []
   195     48.9 MiB      0.0 MiB       for x in range(2, 100):
   196     48.9 MiB      0.0 MiB           multiples = 0
   197     48.9 MiB      0.0 MiB           for y in range(2, 10000):
   198     48.9 MiB      0.0 MiB               if y % x == 0:
   199     48.9 MiB      0.0 MiB                   multiples += 1
   200     48.9 MiB      0.0 MiB           final.append(f"В диапазоне 2-9999: {multiples} чисел кратны {x}")
   201     48.9 MiB      0.0 MiB       return '\n'.join(final)


Использование бибилиотеки guppy3 показывает использование 28.568872452 MiB. Непонятно почему такая разница, почти в 2 
раза
Partition of a set of 247934 objects. Total size = 29956634 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  72386  29  9428243  31   9428243  31 str
     1  63853  26  4935392  16  14363635  48 tuple
     2  29209  12  2288672   8  16652307  56 bytes
     3  14621   6  2112928   7  18765235  63 types.CodeType
     4  13889   6  1888904   6  20654139  69 function
     5   1917   1  1831784   6  22485923  75 type
     6   2914   1  1261024   4  23746947  79 dict (no owner)
     7   1917   1  1022416   3  24769363  83 dict of type
     8    459   0   840720   3  25610083  85 dict of module
     9   4236   2   563656   2  26173739  87 list
<532 more rows. Type e.g. '_.more' to view.>

Process finished with exit code 0

"""


@profile()
def func_gen_range():
    final = []
    for i in range(2, 1000):
        new_list = [el for el in range(2, 100000) if el % i == 0]
        final.append(f"В диапазоне 2-100000: {len(new_list)} чисел кратны {i}")
    return '\n'.join(final)


func_gen_range()

h = hpy()


def func_gen_range_2():
    final = []
    for i in range(2, 1000):
        new_list = [el for el in range(2, 100000) if el % i == 0]
        final.append(f"В диапазоне 2-100000: {len(new_list)} чисел кратны {i}")
    return '\n'.join(final)


func_gen_range_2()
print(h.heap())
"""
Использование memory-profile показывает 48.8 MiB для следющих значений 
Line #    Mem usage    Increment   Line Contents
================================================
   256     48.8 MiB     48.8 MiB   @profile()
   257                             def func_gen_range():
   258     48.8 MiB      0.0 MiB       final = []
   259     51.0 MiB      0.0 MiB       for i in range(2, 1000):
   260     52.1 MiB      0.3 MiB           new_list = [el for el in range(2, 100000) if el % i == 0]
   261     51.0 MiB      0.0 MiB           final.append(f"В диапазоне 2-100000: {len(new_list)} чисел кратны {i}")
   262     49.9 MiB      0.0 MiB       return '\n'.join(final)

Использование бибилиотеки guppy3 показывает использование  28.573565483 MiB
Partition of a set of 247987 objects. Total size = 29961555 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  72424  29  9432252  31   9432252  31 str
     1  63861  26  4935840  16  14368092  48 tuple
     2  29213  12  2288820   8  16656912  56 bytes
     3  14623   6  2113216   7  18770128  63 types.CodeType
     4  13889   6  1888904   6  20659032  69 function
     5   1917   1  1831784   6  22490816  75 type
     6   2914   1  1261024   4  23751840  79 dict (no owner)
     7   1917   1  1022416   3  24774256  83 dict of type
     8    459   0   840720   3  25614976  85 dict of module
     9   4236   2   563656   2  26178632  87 list
<532 more rows. Type e.g. '_.more' to view.>

Process finished with exit code 0

"""
