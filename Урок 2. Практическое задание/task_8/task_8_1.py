"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import random

I = int(input('Введите количество элементов последовательности: '))
N = input('Введите цифру для подсчета: ')

RESULT = 0
for i in range(I):
    num = int(input(f'Введите число {i+1}: '))
    RESULT += str(num).count(N)


print(f'Было введено {RESULT} цифр "{N}"')