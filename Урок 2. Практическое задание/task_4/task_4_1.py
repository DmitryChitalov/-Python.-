"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import sys

try:
    NUMBER = int(input("Введите количество элементов: "))
except ValueError:
    print("Некорректные  данные, программа завершена")
    sys.exit()

RESULT = 1
NUMBER_NEXT = RESULT / 2
for i in range(NUMBER-1):
    RESULT = RESULT - NUMBER_NEXT
    NUMBER_NEXT = - NUMBER_NEXT / 2

print(f"Количество элементов = {NUMBER}, их сумма = {RESULT}")
