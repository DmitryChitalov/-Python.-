"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

QUANTITY = int(input('Введите количество чисел: '))
MAX_AMOUNT = 0
MAX_NUMBER = 0
while QUANTITY != 0:
    AMOUNT = 0
    NUMBER = int(input('Введите число: '))
    for i in str(NUMBER):
        AMOUNT += int(i)
    if AMOUNT > MAX_AMOUNT:
        MAX_AMOUNT = AMOUNT
        MAX_NUMBER = NUMBER
    QUANTITY -= 1
print(
    f'Наибольшее число по сумме цифр: {MAX_NUMBER}, сумма его цифр: {MAX_AMOUNT}')
