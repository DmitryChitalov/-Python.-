"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import random


def recur_method(count, numb):

    print(f'Try number - {count}')
    user_answer = int(input('Введите число от 0 до 100: '))
    if count == 10 or user_answer == numb:
        if user_answer == numb:
            print(f"You WIN!  -- Try number {count}")
        print(f'Сгенерированное число - {numb}')
    else:
        if user_answer > numb:
            print(f'Ваше число больше')
        else:
            print('Ваше число меньше')
        recur_method(count + 1, numb)


recur_method(1, random.randint(0, 100))
