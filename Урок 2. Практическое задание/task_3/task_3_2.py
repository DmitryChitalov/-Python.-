"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def number_reverse(number, answer=''):
    """
    _________
    """
    if len(str(number)) == 1:
        return f'{answer + str(number)}'
    answer = answer + str(number % 10)
    return number_reverse(number // 10, answer)


while True:
    try:
        NUMBER = int(input('Input integer:'))
        print(f"Result is: {number_reverse(NUMBER)}")
        break
    except ValueError:
        print(f'Error')
    except RecursionError:
        print(f'Integer must be shorter')
