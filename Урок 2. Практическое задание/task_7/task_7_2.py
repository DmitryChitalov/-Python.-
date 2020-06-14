"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def check_theorem(n):
    check_n_2 = n * (n + 1) / 2
    theorem(n, check_n_2)


def theorem(n, check_n, result=1):
    if result == check_n:
        return print('Теорема доказана')
    result += n
    n -= 1
    return theorem(n, check_n, result)


check_theorem(20)
