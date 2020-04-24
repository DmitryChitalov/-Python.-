"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

# With arithmetic operations
def mirror_number(number):
    """ Cyclically adds the last digit to empty string """
    result = ''
    while number > 0:
        result += str(number % 10)
        number //= 10
    return result

# More gracefully
def mirror_cycle(number):
    """ Cyclically adds the last digit to empty string"""
    result = ''
    for i in number:
        result = f'{i}{result}'
    return result


# Just beautiful
def mirror_array(number):
    """ Back slice of string"""
    return number[::-1]

# Run
print(mirror_number(12345))

USER_INPUT = '12345'
print(mirror_array(USER_INPUT))
print(mirror_cycle(USER_INPUT))
