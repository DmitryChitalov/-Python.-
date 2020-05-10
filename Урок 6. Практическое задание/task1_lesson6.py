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

"""Профилировка памяти"""


# @profile
# def revese_number():
#     number = 4394839483984395754574775848488584854858443948394839843957545747758484885848548584
#     new_number = ""
#     while number > 0:
#         value = number % 10
#         new_number += str(value)
#         number = number // 10
#     print(int(new_number))
#
#
#
# number = 4394839483984395754574775848488584854858443948394839843957545747758484885848548584
# new_number = ""
#
# @profile
# def calc(number, new_number):
#     if number > 0:
#         value = number % 10
#         new_number += str(value)
#         number = number // 10
#         return calc(number, new_number)
#     else:
#         return new_number
#
# f = calc(number, new_number)
# print(int(f))
#
# revese_number()

from memory_profiler import profile
import math
@profile
def factorial():
    n = 5
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("The factorial of 5 is : ", end="")
    print(fact)


@profile
def factorial_2():
    print("The factorial of 5 is : ", end="")
    print(math.factorial(5))


@profile
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


factorial()
factorial_2()
recurs = recur_factorial(5)
print(f'The factorial of 5 is : {recurs}')

# Проверил потребления памяти у 3 видах алгоритмов ( факториал обычный алгоритм, встроенный факториал и через рекурсию)
# во первых двух параметров Mem usage константа 34.4 MiB, а в случае с рекурсией тоже 34.4 MiB  для однои функцыеи,
# которая вызывается 5 раз ( 34.4 MiB * 5 = 175 MiB )
# mac os 64 bit, python 3.8
