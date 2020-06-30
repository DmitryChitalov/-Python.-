"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
import random

def game(user_num, counter):
    if counter > 0:
        if user_num == task_num:
            return print('Congratulations, you guessed it!')
        elif user_num > task_num:
            print('The guessed number is less.')
            return game(int(input()), counter - 1)
        else:
            print('The guessed number is greater.')
            return game(int(input()), counter - 1)
    else:
        print(f'You played, the hidden number: {task_num}')

counter = 10
task_num = random.randint(1, 100)
game(int(input('The computer guessed '
               'the number, try to guess it: ')), counter)
