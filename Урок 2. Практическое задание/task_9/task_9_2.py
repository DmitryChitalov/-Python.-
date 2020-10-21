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


def get_digits_sum(num):
    if num == 0:
        return 0
    category = 10 ** (len(str(num)) - 1)
    cur_digit = num // category
    return cur_digit + get_digits_sum(num - cur_digit * category)


def recursion(num_count, max_num=0, max_sum=0):
    if num_count == 0:
        print(
            f'Наибольшее число по сумме цифр: {max_num}, сумма его цифр: {max_sum}')
        return
    num = int(input(f'Введите число № {str(num_count)}: '))
    cur_sum = get_digits_sum(num)
    if cur_sum > max_sum:
        recursion(num_count - 1, num, cur_sum)
    else:
        recursion(num_count - 1, max_num, max_sum)


recursion(3)
