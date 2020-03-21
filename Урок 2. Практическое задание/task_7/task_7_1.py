"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import sys


try:
    USER_N = int(input("Введите число: "))
except ValueError:
    print("Введено не число")
    sys.exit()

ROW_SUM = 0
for i in range(USER_N):
    ROW_SUM += i + 1

print(f"{USER_N} * ({USER_N} + 1) / 2 = {int(USER_N * (USER_N + 1) / 2)}")
print(f"Сумма чисел в ряду до {USER_N} = {ROW_SUM}")

if USER_N * (USER_N + 1) / 2 == ROW_SUM:
    print("Равенство верно")
else:
    print("Равенство неверно")
