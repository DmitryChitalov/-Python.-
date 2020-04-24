"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def prove_equation(num, left=0):
    """ Counts the left part of eqaution, then the right part and prints results"""
    for i in range(1, num + 1):
        left += i
    right = num * (num + 1) // 2
    return f'{left} == {right}'


print(prove_equation(7))
