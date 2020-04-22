"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
"""

while True:
    try:
        NUMBER = int(input('Введите трехзначное целое положительное число: '))
        # Проверка, что введено трехзначное число
        # Если число введено отличное от трехзначного,
        # вызывается обработка исключения IOError
        if NUMBER < 100 or NUMBER > 999:
            raise IOError
        # Определение цифр числа NUMBER путем
        # разбиения числа на сотни, десятки и единицы
        NUMBER_HUNDREDS = NUMBER // 100
        NUMBER_TENS = (NUMBER // 10) % 10
        NUMBER_UNITS = NUMBER % 10
        # Вычисление суммы цифр числа NUMBER
        SUM = NUMBER_HUNDREDS + NUMBER_TENS + NUMBER_UNITS
        # Вычисление произведения цифр числа NUMBER
        MULTIPLICATION = NUMBER_HUNDREDS * NUMBER_TENS * NUMBER_UNITS
        print(f'Сумма цифр числа =  {SUM}')
        print(f'Произведение цифр числа =  {MULTIPLICATION}')
        break
    except ValueError:
        print('Ошибка ввода. Необходимо ввести трехзначное целое число.')
    except IOError:
        print('Неверно введено число. Необходимо ввести трехзначное целое число')
