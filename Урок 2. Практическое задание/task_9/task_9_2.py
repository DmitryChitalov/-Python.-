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

I = int(input('Введите количество чисел: '))

def sumNumbers(end, i=0, number=0, sum=0):
    if i == end:
        return print(f'Наибольшее число по сумме цифр: {number}, сумма его цифр: {sum}')
    else:
        num = int(input(f'Введите число {i+1}: '))
        numbers = str(num)
        sumN = 0
        for n in numbers:
            sumN += int(n)
        if sumN > sum:
            sum = sumN
            number = num
        sumNumbers(end, i+1, number, sum)

sumNumbers(I)