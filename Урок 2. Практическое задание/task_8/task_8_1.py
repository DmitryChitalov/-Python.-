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

AMOUNT_OF_NUMBERS = int(input('Сколько будет чисел?'))
USER_NUMERAL = int(input('Какую цифру считать?'))
NUMERAL_COUNT = 0
N = 1
for el in range(AMOUNT_OF_NUMBERS):
    NUMBER = int(input(f'Введите число {el + 1}:'))
    while True:
        NUMERAL = NUMBER % (10 * N) // N
        if NUMERAL == USER_NUMERAL:
            NUMERAL_COUNT += 1
        N *= 10
        if N > NUMBER:
            N = 1
            break
print(f'Было введено {NUMERAL_COUNT} цифр {USER_NUMERAL}')
