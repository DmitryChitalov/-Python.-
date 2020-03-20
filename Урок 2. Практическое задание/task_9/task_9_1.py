"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""

# Не смог решить без использования списков. Негде хранить числа для
# последующего сравнения

SUM_NUMBERS = []
NUMBERS = []
STEP_COUNTER = int(input('Введите количество чисел: '))
for i in range(STEP_COUNTER):
    number = int(input('Введите очередное число: '))
    NUMBERS.append(number)
    len_num = len(str(number))
    sum_num = 0
    unit = number % 10
    temp_num = number // 10
    for j in range(len_num):
        sum_num += unit
        unit = temp_num % 10
        temp_num = temp_num // 10
    SUM_NUMBERS.append(sum_num)
MAX_DIGIT = SUM_NUMBERS[0]
ELEM = 0
for i in range(len(SUM_NUMBERS)):
    if SUM_NUMBERS[i] > MAX_DIGIT:
        MAX_DIGIT = SUM_NUMBERS[i]
        ELEM = i
print(
    f'Наибольшее число по сумме цифр: {NUMBERS[ELEM]}, сумма его цифр: {MAX_DIGIT}')
