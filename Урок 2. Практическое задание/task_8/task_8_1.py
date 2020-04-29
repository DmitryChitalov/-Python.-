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

COUNT_WHAT_NUM = 0
COUNT_NUM = int(input('Сколько будет чисел ? '))
WHAT_NUM = int(input('Какую чифру считать ? '))
for i in range(0, COUNT_NUM):
    COUNT = 1
    DIV = 10
    RESULT = 1
    NUM_OF = int(input(f'Число {i + 1} : '))
    while COUNT != 0:
        COUNT = NUM_OF // DIV
        RESULT = int((NUM_OF % DIV) // (DIV / 10))
        if RESULT == WHAT_NUM:
            COUNT_WHAT_NUM += 1
        DIV *= 10
        print(RESULT)

print(f'Цифра {WHAT_NUM} введена {COUNT_WHAT_NUM} раз')
