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

# не стал все задание переделывать, заменил только функцию суммы цифр


def sum_of_digits(number):
    """Recursion. Get number and return sum of digits"""
    number = abs(number)
    if number // 10:
        return number % 10 + sum_of_digits(number // 10)
    return number


try:
    QUANTITY = int(input('Сколько будет чисел? - '))
    if QUANTITY <= 0:
        raise ValueError('Отрицательное количество или ноль')
    MAX_SUM = 0
    MAX_SUM_NUM = 0
    # MAX_SUM_NUM_STR нужно чтобы формировать числа с равной суммой.
    # массивы не используем
    MAX_SUM_NUM_STR = ''
    while QUANTITY:
        NUM = int(input(f'Введите число: '))
        QUANTITY -= 1
        SUM = sum_of_digits(NUM)
        if SUM > MAX_SUM:
            MAX_SUM = SUM
            MAX_SUM_NUM = NUM
            MAX_SUM_NUM_STR = str(NUM)
        elif SUM == MAX_SUM and MAX_SUM_NUM != NUM:
            MAX_SUM_NUM_STR += f' {NUM} '
        elif MAX_SUM_NUM == 0:
            MAX_SUM_NUM_STR = f' {NUM} '
    print(
        f'Наибольшее число по сумме цифр: {MAX_SUM_NUM_STR}, сумма его цифр: {MAX_SUM}')
except ValueError as err:
    print(f'Ошибка ввода: {err}')
