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

BASE = 10

num = int(input('How many numbers: '))
digit = int(input('Which digit need to count?: '))
counter = 0

for i in range(1, num + 1):
    ans = int(input(f'Enter number {i}: '))
    while ans > 0:
        if ans % BASE == digit:
            counter += 1
        ans //= BASE

print(f'Were entered {counter} digits of {digit}')
