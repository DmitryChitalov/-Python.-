"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursion(RESULT_1, COUNT, N):
    if COUNT > N:
        print('Равенство выполняется') if RESULT_1 == (N * (N + 1) / 2) else print('Равенство не выполняется')
        return
    else:
        return recursion(RESULT_1 + COUNT, COUNT + 1, N)

N = int(input('Ведите натуральное число: '))
COUNT = 1
RESULT_1 = 0
recursion(RESULT_1, COUNT, N)