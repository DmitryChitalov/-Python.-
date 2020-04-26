"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def recursion(NUMB, ROW, RESULT, PRIMERY):
    if NUMB == 1:
        return print(f'Количество элементов - {PRIMERY}, их сумма = {RESULT}')
    else:
        return recursion(NUMB - 1, (ROW / (-2)), RESULT + ((ROW / (-2))), PRIMERY)

NUMB = int(input('Введите количество элементов ряда чисел: '))
PRIMERY = NUMB
print(recursion(NUMB, 1, 1, PRIMERY))
