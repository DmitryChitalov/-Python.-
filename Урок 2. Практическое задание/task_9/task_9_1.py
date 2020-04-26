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
quantity_numbers = int(input('Введите количество чисел: '))
max_sum_number = 0
max_number = 0
for i in range(1, quantity_numbers + 1):
    number = int(input(f'Введите очередное число: '))
    count = 0
    user_num = number
    while number > 0:
        count += number % 10
        number //= 10
    if count > max_sum_number:
        max_sum_number = count
        max_number = user_num
print(f'Наибольшее число по сумме цифр: {max_number}, сумма его цифр: {max_sum_number}')
