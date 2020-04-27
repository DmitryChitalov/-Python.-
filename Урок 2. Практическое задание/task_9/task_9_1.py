"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""

how_many_number = int(input('Введите количество чисел:  '))
big_number = ''
for idx in range(how_many_number):
    number = input(f'Введите очередное число: ')
    if len(number) > len(big_number):
        big_number = number

sum_big_number = 0
for el in list(big_number):
    sum_big_number+=int(el)

print(f'Наибольшее число по сумме цифр: {big_number}, '
      f'сумма его цифр: {sum_big_number}')

