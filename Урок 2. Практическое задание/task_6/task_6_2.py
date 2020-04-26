"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

import random


def recursion_number(number_generate, count_try):
    if count_try == 0:
        print(f'Эх, не угадали... но ничего, в следующий раз получится :)\r\nЗагаданное число: {number_generate}')
        return 0
    print(f'Последняя попытка!') if count_try == 1 else \
        print(f'Количество оставшихся попыток {count_try}')
    while True:
        try:
            number = int(input("Какое число загадано?\r\n"))
            if number < 0:
                raise IOError
        except (ValueError, TypeError, IOError):
            print('Ошибка ввода. Загаданное число является целым и положительным.')
        else:
            if number < number_generate:
                print(f'Загаданное число больше, чем это число')
            elif number > number_generate:
                print(f'Загаданное число меньше, чем это.')
            elif number == number_generate:
                print(f'Превосходно! Вы угадали!')
                return 0
            count_try -= 1
            return recursion_number(number_generate, count_try)


print(f'Загадано число от 0 до 100. Попробуй с 10 попыток угадать какое число загадано!'
      f'\r\nСледи за подсказками на экране!')
recursion_number(random.randint(0, 100), 10)
