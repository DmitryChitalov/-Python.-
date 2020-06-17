"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

number = int(input('Введите кол-во элементов: '))

def recursion(number, digit = 1, total = 0):
    if number == 0:
        return total
    else:
        total += digit
        digit /= -2
        number -= 1
        return recursion(number, digit, total)

print(f'Сумма элементов: {recursion(number)}')