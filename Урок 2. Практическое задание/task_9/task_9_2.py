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


def input_quantity_number():
    try:
        quantity_numbers = int(input('Введите количество чисел:'))
        if quantity_numbers > 1:
            return quantity_numbers
        print('При таких значенях задача не имеет смысла, попробуйте еще раз')
        return input_quantity_number()

    except ValueError:
        print('Это не похоже на натуральное число, попробуйте еще раз')
        return input_quantity_number()


def get_sum_num(user_number, count=1, sum_numeral=0):
    if count > user_number:
        return sum_numeral
    numeral = user_number % (10 * count) // count
    sum_numeral += numeral
    return get_sum_num(user_number, count * 10, sum_numeral)


def input_number(quantity_numbers, count=1, max_number=0, max_sum=0):
    if count > quantity_numbers:
        return f'Наибольшее число по сумме цифр: {max_number}, сумма его цифр: {max_sum}'
    try:
        user_number = int(input(f'Введиите число {count}:'))
        sum_numeral = get_sum_num(user_number)
        if sum_numeral > max_sum:
            max_sum = sum_numeral
            max_number = user_number
        return input_number(quantity_numbers, count + 1, max_number, max_sum)
    except ValueError:
        print('Введите пожалуйста натуральное число:')
        return input_number(quantity_numbers, count, max_number, max_sum)


print(input_number(input_quantity_number()))
