"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
AMOUNT_OF_NUMBERS = int(input('Сколько будет чисел?'))
USER_NUMERAL = int(input('Какую цифру считать?'))


def recur_counter_2(number, user_numeral, count=0, n=1):
    numeral = number % (10 * n) // n
    if numeral == user_numeral:
        count += 1
    n *= 10
    if n > number:
        return count
    return recur_counter_2(number, user_numeral, count, n)


def recur_counter_1(amount_of_numbers, user_numeral, count=0, n=1):
    if n > amount_of_numbers:
        return count
    number = int(input(f'Введите число {n}:'))
    count = recur_counter_2(number, user_numeral, count)
    return recur_counter_1(amount_of_numbers, user_numeral, count, n + 1)


print(f'Было введено {recur_counter_1(AMOUNT_OF_NUMBERS, USER_NUMERAL)} цифр {USER_NUMERAL}')
