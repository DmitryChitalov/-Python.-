"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
N = int(input())
SUMM = 0
for i in range(1, N + 1):
    SUMM += i

print(SUMM)
SUMM2 = N * (N + 1) / 2
print(int(SUMM2))
