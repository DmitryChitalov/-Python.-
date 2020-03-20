"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import random

def random_number(NUMBER, TRY_COUNT):
    if TRY_COUNT <= 10:
        try:
            USER_NUMBER = int(input('Угадайте число от 0 до 100 : '))
            if USER_NUMBER >= 0 and USER_NUMBER <= 100:
                if USER_NUMBER < NUMBER:
                    print(f'Вы ввели слишком маленькое число.У вас осталось {10 - TRY_COUNT} попыток')
                    return random_number(NUMBER, TRY_COUNT +1)
                if USER_NUMBER > NUMBER:
                    print(f'Вы ввели слишком большое число.У вас осталось {10 - TRY_COUNT} попыток')
                    return random_number(NUMBER, TRY_COUNT +1)
                print(f'Поздравляю. Вы угадали за {TRY_COUNT} попыток.')
            else:
                raise ValueError
        except ValueError:
            print('Некорректное значение.Введите целое число от 0 до 100.')
            return random_number(NUMBER, TRY_COUNT)
    else:
        print(f'Увы, количество попыток Вы исчерпали.Правильный ответ : {NUMBER}')


random_number(NUMBER=round(random() * 100), TRY_COUNT=1)
