"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
N = int(input('Введите любое натуральное число: '))
i = 1
cal_1 = 0
while i <= N:
    cal_1 += i
    i += 1

calc_2 = N*(N + 1)//2
print(f'1+2+...+n = {cal_1}, n(n+1)/2 = {calc_2}')
