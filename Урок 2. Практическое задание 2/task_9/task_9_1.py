"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""

numbers = int(input('Сколько будет чисел? - '))
total_max = 0
sum_numbers_max = 0
while numbers != 0:
    num = int(input('Введите очередное число: '))
    total = num
    sum_numbers = 0
    while num != 0:
        num_1 = num % 10
        sum_numbers += num_1
        num = num // 10
    if sum_numbers > sum_numbers_max:
        sum_numbers_max = sum_numbers
        total_max = total

    numbers -= 1
print(f'Наибольшее число по сумме цифр {total_max} сумма его цифр "{sum_numbers_max}"')