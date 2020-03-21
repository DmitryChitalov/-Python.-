"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

from re import sub
from random import randint


def otgadayka(
        initialize: bool = False,
        start: str = "1",
        count: int = 10,
        secret_number: int = 0,
) -> [int, None]:
    if not initialize:
        start = sub(r"[\s]", "", input("Введите 1 для начала, или 0 для выхода из программы: "))

    if start == "0":
        return
    elif start == "1":
        if not initialize:
            secret_number = randint(0, 100)
            count = 10
            print("Попробуйте угадать число от 0 до 100 с 10 попыток")
        try:
            number = int(
                sub(r"[\s]", "", input(f"У вас осталось попыток ({count}), попробуйте угадать: "))
            )
        except ValueError:
            print("Вы ввели не целое число, попробуйте еще")
            return otgadayka(True, start, count, secret_number)

        if count > 1:
            count -= 1
            if number == secret_number:
                return f"Вы отгдали число {number} с {10 - count} попытки)"
            elif number > secret_number:
                print(f"Ваше число {number} больше загаданного числа, попробуйте еще")
                return otgadayka(True, start, count, secret_number)
            elif number < secret_number:
                print(f"Ваше число {number} меньше загаданного числа, попробуйте еще")
                return otgadayka(True, start, count, secret_number)
        else:
            print(f"У вас закончились попытки. Загаданное число было {secret_number}")
            return otgadayka(False, start, count, secret_number)
    else:
        print("Вы ввели неверное действие, попробуйте еще раз")
        return otgadayka()


print(otgadayka())
