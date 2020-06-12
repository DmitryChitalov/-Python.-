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
try:
    n_cnt = int(input('Введите сколько будет чисел: '))

    res_sum, res_num = 0, 0

    for _ in range(n_cnt):
        sum_n = 0
        user_number = int(input('Введите очередное число: '))
        num = user_number
        while user_number != 0:
            sum_n += user_number % 10
            user_number //= 10
        if sum_n >= res_sum:
            res_num = num
            res_sum = sum_n

    print(f'Наибольшее число по сумме цифр: {res_num}, сумма его цифр: {res_sum}')

except ValueError:
    print('Необходимо ввести число')