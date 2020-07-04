"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import random


counter = 10
task_num = random.randint(1, 100)
win_satus = False


while counter > 0:
    user_num = int(input('The computer guessed the number, try to guess it: '))
    if user_num == task_num:
        print('Congratulations, you guessed it!')
    elif user_num > task_num:
        print('The guessed number is less.')
        counter -= 1
    else:
        print('The guessed number is greater.')
        counter -= 1
print(f'You played, the hidden number: {task_num}')
