"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


# Подсмотренное решение, не засчитывайте его


# def sum_natural(n):
#     assert n < 999, 'To big number'
#     if n == 1:
#         return n
#     sum_n = n + sum_natural(n -1)
#     return  sum_n
#
#
# n = int(input('Enter any natural number: '))
#
# left = sum_natural(n)
# right = n * (n + 1) // 2
#
# print(f'left {left}')
# print(f'right {right}')
# print('Right' if left == right else 'Wrong')


# Solution from teacher

def recur_method(numb, s=0, m=1):
    if s == m:
        print(f"Equality: {s == m}")

    elif s < m:
        return recur_method(numb, s + 1, numb * (numb + 1) // 2)


try:
    NUMB = int(input("Enter a number: "))
    recur_method(NUMB)
except ValueError:
    print("Wrong value. Try again")
