"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

CONS = 10

def sum_digits(number):
    if number < CONS:
        return number
    return number % CONS + sum_digits(number // CONS)

NUMBER = int(input('Введите натуральное число (для выхода из программы введите 0): '))

MAX_SUMM = 0
MAX_NUM = 0

while NUMBER != 0:
    num = NUMBER
    summ = sum_digits(NUMBER)
    if summ > MAX_SUMM:
        MAX_SUMM = summ
        NUMBER = num
    NUMBER = int(input('Введите натуральное число (для выхода из программы введите 0): '))

print(f'Число {MAX_NUM} имеет мксимальную сумму цифр: {MAX_SUMM}')
