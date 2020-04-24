"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

import sys


def get_result_n(number):
    if number == 0:
        return 0
    return number + get_result_n(number-1)


try:
    NUMBER = int(input("Введите натуральное число: "))
except ValueError:
    print("Некорректные  данные, программа завершена")
    sys.exit()

if NUMBER < 1:
    print("Число должно быть натуральным")
    sys.exit()

RESULT_1 = get_result_n(NUMBER)

RESULT_2 = NUMBER * (NUMBER + 1) / 2

print(f"Результат вычисления типа 1+2+...+n = {RESULT_1}")
print(f"Результат вычисления типа n(n+1)/2  = {RESULT_2}")
