"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def strange_task(number, left=0, right=1):
    """ Recursively checks the equation """
    if left == right:
        return f'{left} == {right}'
    return strange_task(number, left + 1, number * (number + 1) // 2)


print(strange_task(7))
