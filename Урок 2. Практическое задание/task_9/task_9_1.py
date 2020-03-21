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
    digit_sum = 0
    tmp_number = abs(l_number)
    while tmp_number:
        digit_sum += tmp_number % 10
        tmp_number //= 10
    return digit_sum


count = input_number('Введите количество чисел')
max_digit_sum = 0
max_number = 0
while count:
    number = input_number('Введите очередное число')
    number_digit_sum = get_digit_sum(number)
    if number_digit_sum > max_digit_sum:
        max_digit_sum = number_digit_sum
        max_number = number
    count -= 1
print(f'Наибольшее число по сумме цифр: {max_number}, сумма его цифр: {max_digit_sum}')