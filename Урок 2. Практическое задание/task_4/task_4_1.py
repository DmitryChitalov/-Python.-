"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

ROW_RANGE = int(input("Введите количество элементов в ряду: "))
ROW_EL = 1
ROW_SUM = 0
i = 0

while i <= ROW_RANGE - 1:
    i += 1
    ROW_SUM = ROW_SUM + ROW_EL
    ROW_EL = ROW_EL * -0.5

print(ROW_SUM)
