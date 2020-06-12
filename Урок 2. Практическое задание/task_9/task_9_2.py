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


def recursive_search_max(cnt = - 1, number = 0, res_sum = 0, res_num = 0, subtotal = 0):
    try:
        if number != 0:
            subtotal += number % 10
            if subtotal > res_sum:
                res_sum = subtotal
                res_num = number
            return recursive_search_max(cnt, number // 10, res_sum, res_num, subtotal)
        if cnt == -1:
            cnt = int(input('Введите количество чисел: '))
        if cnt == 0:
            return f'Наибольшее число по сумме цифр {res_num}, сумма его цифр: {res_sum}'
        if number == 0:
            number = int(input('Введите число: '))
            return recursive_search_max(cnt - 1, number, res_sum, res_num) # ???
    except ValueError:
        print('Необходимо ввести число')


print(recursive_search_max())
