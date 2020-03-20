"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import random

RAND_NUMBER = random.randrange(0, 100)


def game_numbers(attempts=10):
    user_answer = int(input('Введите ваш вариант: '))
    attempts -= 1
    if attempts == 0:
        print(
            f'Количество попыток закночилось, вы проиграли. Загаданное число - {RAND_NUMBER}')
        return
    if user_answer == RAND_NUMBER:
        print('Поздравляем! Вы угадали!')
        return
    if user_answer > RAND_NUMBER:
        print(f'Ваше число больше загаданного. Осталось {attempts} попыток')
        game_numbers(attempts)
    elif user_answer < RAND_NUMBER:
        print(f'Ваше число меньше загаданного. Осталось {attempts} попыток')
        game_numbers(attempts)


game_numbers()
