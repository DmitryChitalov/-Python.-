"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def sum_n(n):
    sum_answer = 0
    for itm in range(1, n + 1):
        sum_answer += itm
    return sum_answer


def multiplication(n):
    multiplication_answer = n * (n + 1) / 2
    return multiplication_answer


def check(n):
    if multiplication(n) == sum_n(n):
        print(f'С числом {n} равенство верно')
    else:
        print(f'С числом {n} равенство неверно')


for i in range(20):
    check(i)
