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


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено целое
def input_number(string):
    while True:
        try:
            num = input(f"{string}\n")
            num = int(num)
            break
        except ValueError:
            print("Не удалось преобразовать в число")
    return num


# Получить сумму цифр в числе
def get_digit_sum(l_number):
    if l_number > 9:
        return l_number % 10 + get_digit_sum(l_number // 10)
    else:
        return l_number


# Считывает последовательность и возвращает число с максимальной суммой цифр
def check_sequence(l_count):
    if l_count > 0:
        number = input_number('Введите очередное число')
        tmp_max_number, tmp_max_digit_sum = check_sequence(l_count - 1)
        tmp_digit_sum = get_digit_sum(number)
        if tmp_digit_sum > tmp_max_digit_sum:
            return number, tmp_digit_sum
        else:
            return tmp_max_number, tmp_max_digit_sum
    else:
        return 0, 0


count = input_number('Введите количество чисел')
max_number, max_digit_sum = check_sequence(count)
print(f'Наибольшее число по сумме цифр: {max_number}, сумма его цифр: {max_digit_sum}')