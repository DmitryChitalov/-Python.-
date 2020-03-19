"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def devil_number_func(number, my_sum=1):
    if number == 1:
        return my_sum
    return devil_number_func((number - 1), my_sum / -2) + my_sum


while True:
    try:
        NUMBER = int(input('Введите количество элементов:'))
        print(f'Количество элементов - {NUMBER}, их сумма - {devil_number_func(NUMBER)}')
        break
    except ValueError:
        print(f'Ошибка ввода!')
    except RecursionError:
        print(f'Введите меньшее число элементов')
