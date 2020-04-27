"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recur_total(n, total):
    if n == 0:
        return print(f'Сумма элементов: {total}')
    else:
        if n == 1:
            return recur_total(n=n - 1, total=1 + total)
        elif n % 2 == 0:
            return recur_total(n=n - 1, total=total - 1 / (2 ** (n - 1)))
        elif n % 2 != 0:
            return recur_total(n=n - 1, total=total + 1 / (2 ** (n - 1)))


recur_total(int(input('Введите количество элементов: ')), total=0)
