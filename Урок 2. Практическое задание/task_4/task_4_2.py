"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def sum_seq_req(number, result=0.0, start=1.0):
    """ Recursively counts the sum of numerical sequence"""
    if number == 0:
        return result
    return sum_seq_req(number - 1, result + start, start / -2)


print(sum_seq_req(3))
