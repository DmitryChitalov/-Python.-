"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
"""
def recursion(length, summary, i):
    if length == 0:
        return print(f'Сумма последовательности = {summary}')
    else:
        summary += 1 / (-2) ** i
        recursion(length - 1, summary, i + 1)


print(f"Введите длину:")
recursion(int(input()), 0, 0)
