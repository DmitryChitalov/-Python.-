"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

COUNT_NUM = int(input('Сколько будет чисел ? '))
SUM_RESULT2 = 0
NUMBER2 = 0
for i in range(0, COUNT_NUM):
    COUNT = 1
    DIV = 10
    RESULT = 1
    SUM_RESULT = 0
    NUM_OF = int(input(f'Введите очередное число : '))
    while COUNT != 0:
        COUNT = NUM_OF // DIV
        RESULT = int((NUM_OF % DIV) // (DIV / 10))
        SUM_RESULT += RESULT
        DIV *= 10
    if SUM_RESULT > SUM_RESULT2:
        SUM_RESULT2 = SUM_RESULT
        NUMBER2 = NUM_OF
print(f'Наибольшее число по сумме цифр: {NUMBER2}, сумма его цифр: {SUM_RESULT2}')
