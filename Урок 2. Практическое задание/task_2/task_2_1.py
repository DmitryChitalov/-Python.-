"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


# Strictly on task
def count_evens_with_arithmetic(number):
    """ Counts odd and even ts in number """
    evens, odds = 0, 0
    while number > 0:
        if (number % 10) % 2 == 0:
            evens += 1
        else:
            odds += 1
        number //= 10
    return f'Evens: {evens}, odds: {odds}'

# More gracefully, if the number is a user input
def count_evens(str_number):
    """ Counts evens in user input number"""
    evens = 0
    for digit in str_number:
        if int(digit) in (0, 2, 4, 6, 8):
            evens += 1
    return f'Evens: {evens}, odds: {len(str_number) - evens}'


print(count_evens_with_arithmetic(12345))

USER_INPUT = '12345'
print(count_evens(USER_INPUT))

# I couldn't resist, it's so beautiful!
EVEN_ARRAY = [a for a in USER_INPUT if int(a) % 2 == 0]
print(f'Evens: {len(EVEN_ARRAY)}, odds: {len(USER_INPUT) - len(EVEN_ARRAY)}')
