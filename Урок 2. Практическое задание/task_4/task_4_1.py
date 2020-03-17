"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


a = float(input("введите число---"))
b = 1
startnumber = 1
startsum = 1
print(startnumber)
while b < a:
    startnumber /= 2
    b += 1
    if b // 2 != 0:
        startnumber *= -1
    startsum += startnumber
    print(f'{b} и {startnumber}')
print(startsum)
