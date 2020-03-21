"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import sys


try:
    USER_N = int(input("Введите число: "))
except ValueError:
    print("Введено не число")
    sys.exit()


def row_sum(row_length, cur_number=1, total=0):
    """ Сумма ряда чисел"""
    if row_length == 0:
        return total
    total += cur_number
    cur_number += 1
    row_length -= 1
    return row_sum(row_length, cur_number, total)


print(f"{USER_N} * ({USER_N} + 1) / 2 = {int(USER_N * (USER_N + 1) / 2)}")
print(f"Сумма чисел в ряду до {USER_N} = {row_sum(USER_N)}")

if USER_N * (USER_N + 1) / 2 == row_sum(USER_N):
    print("Равенство верно")
else:
    print("Равенство неверно")
