"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


# Solution from teacher

def recur_method(i, numb, n_count, common_sum):
    if i == n_count:
        print(f"Number of elements - {n_count}, their sum is - {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum + numb)


try:
    N_COUNT = int(input("Enter number of elements: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("You entered a wrong value. Try again.")
