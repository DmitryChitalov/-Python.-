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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

# Solution from teacher
COUNT = 0


def recur_method(n, b):
    global COUNT
    if n == 0:
        return (f"Were entered {COUNT} digits of {b}")
    m = int(input(f"Number: "))

    while m > 0:
        if m % 10 == b:
            COUNT += 1
        m = m // 10
    return recur_method(n - 1, b)


try:
    N = int(input("How many numbers?: "))
    B = int(input("Which digit is calculate: "))
    print(recur_method(N, B))
except ValueError:
    print("Wrong value. Try again")
