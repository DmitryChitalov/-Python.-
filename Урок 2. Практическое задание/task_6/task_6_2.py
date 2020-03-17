"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


from random import randint


def recursion_generator() -> None:
    """ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ """
    random_number = randint(0, 100)
    print('Загадано целое число от 0 до 100')

    def recursion(i, r_number) -> str:
        if i <= 0:
            return f'Было загадано число {r_number}'
        try:
            user_input = int(input(f'Осталось попыток {i}. Введите Ваш ответ: ').strip())
            if user_input == r_number:
                print('Вы угадали!')
                return recursion(0, r_number)
            if user_input > r_number:
                print('Загаданное число меньше.')
                return recursion(i - 1, r_number)

            print('Загаданное число больше.')
            return recursion(i - 1, r_number)
        except ValueError:
            print('Недопустимое значение.')
            return recursion(i - 1, r_number)

    print(recursion(10, random_number))


if __name__ == "__main__":
    recursion_generator()
