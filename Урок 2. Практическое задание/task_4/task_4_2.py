"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recursive_calculation(n, result=1):

    if n == 1:
        return result
    else:
        return recursive_calculation(n-1, result + pow(-1, n+1) * 1/pow(2, n-1))


try:
    N = int(input("Введите количество элементов числового ряда n\n"))

    if N > 0:
        print(f"Количество элементов - {N} , и их сумма - {recursive_calculation(N)}")
    else:
        print("n не может быть отрицательным")
except ValueError:
    print("Нужно ввести число")
