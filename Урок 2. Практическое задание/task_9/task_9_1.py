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

user_number = int(input('Введите количество чисел: '))
max_sum_number = 0
maximum_number = 0
while user_number != 0:
    user_input = int(input('Введите число: '))
    max_number = user_input
    max_sum = 0
    while user_input > 0:
        max_sum += user_input % 10
        user_input //= 10
    if max_sum > max_sum_number:
        max_sum_number = max_sum
        maximum_number = max_number
    user_number -= 1
print(f'Максимальная сумма введенных чисел {max_sum_number}, это число {maximum_number}')
