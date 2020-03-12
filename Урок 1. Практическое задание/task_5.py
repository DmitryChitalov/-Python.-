"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""


def char_distance() -> None:
    """ Определяет количество букв между 2-мя введенными """
    try:
        left_char = ord(input('Введите первую букву: ').strip())
        right_char = ord(input('Введите вторую букву: ').strip())
        if left_char == right_char:
            distance = 0
        elif left_char < right_char:
            distance = right_char - left_char - 1
        else:
            distance = left_char - right_char - 1
        print(
            f'Буква "{chr(left_char)}" стоит на {left_char - 96} месте, '
            f'а буква "{chr(right_char)}" стоит на {right_char - 96} месте в алфавите')
        print(
            f'Между буквами "{chr(left_char)}" и "{chr(right_char)}" находится {distance} символов')
    except TypeError as err:
        print('Введенное Вами значение не является корректным символом')
        print('Ошибка: ', err)


if __name__ == "__main__":
    char_distance()
