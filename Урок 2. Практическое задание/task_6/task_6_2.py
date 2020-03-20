"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from random import randint

def game(rand_num, answer=1, max_answ=10):
    """
    Функция для игры в угадываеие числа. После запуска ожидает от пользователя
    ввод числа, в зависимости от ответа генерирует сообщение.

    :param rand_num: случайное число, генерируется вне функции
    :param answer: количество попыток пользователя, default - 1
    :param max_answ: максимальное количество попыток, default - 10
    :return:
    """
    if answer > max_answ:
        print('Вы не смогли угадать число. Попробуйте ещё раз.')
        return
    try:
        user_answer = int(input(f'Попытка №{answer}, введите число: '))
        if user_answer == rand_num:
            print('Поздравляю! Вы угадали!')
            return
        if user_answer > rand_num:
            if answer < max_answ:
                print(f'Вы ввели число, которое БОЛЬШЕ загаданного. '
                      f'Осталось попыток: {max_answ - answer}')
        elif user_answer < rand_num:
            if answer < max_answ:
                print(f'Вы ввели число, которое МЕНЬШЕ загаданного. '
                      f'Осталось попыток: {max_answ - answer}')
        answer += 1
    except ValueError:
        print(f'Необходимо вводить число! Осталось попыток: {max_answ - answer}')
        answer += 1
    game(rand_num, answer)


NUM = randint(0, 100)
START_GAME = game(NUM)
