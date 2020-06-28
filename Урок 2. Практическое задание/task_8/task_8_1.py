"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


# BASE = 10
#
# num = int(input('How many numbers: '))
# digit = int(input('Which digit need to count?: '))
# counter = 0
#
# for i in range(1, num + 1):
#     ans = int(input(f'Enter number {i}: '))
#     while ans > 0:
#         if ans % BASE == digit:
#             counter += 1
#         ans //= BASE
#
# print(f'Were entered {counter} digits of {digit}')


# Solution from teacher

def cycle_method(n, b):
    count = 0
    for i in range(n, n + 1):
        try:
            m = int(input(f"Number {str(i)}: "))
            while m > 0:
                if m % 10 == b:
                    count += 1
                m = m // 10
        except ValueError:
            print("Wrong value. Try again")
    print(f"Were entered {count} digits of {b}")


try:
    N = int(input("How many numbers?: "))
    B = int(input("Which digit is calculate: "))
    cycle_method(N, B)
except ValueError:
    print("Wrong value. Try again")
