"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


#Solution 1
n = int(input('Enter how many elements to sum:'))
digit = 1
summary = 0

while n > 0:
    summary += digit
    digit /= -2
    n -= 1
print(summary)


#Solution 2
# n = int(input('Enter how many elements to sum:'))
# sum_ = 1 * (1 - (-0.5)**n) / (1 - (-0.5))
# print(sum_)
