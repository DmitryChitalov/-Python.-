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

try:
    FIRST_LETTER = input("Введите первый символ\n")
    SECOND_LETTER = input("Введите второй символ\n")

    FIRST_LETTER_CODE = ord(FIRST_LETTER)
    SECOND_LETTER_CODE = ord(SECOND_LETTER)

    if FIRST_LETTER_CODE > ord('z') or FIRST_LETTER_CODE < ord('a'):
        print("Первый символ не является латинской буквой или введено с большой буквы")
    elif SECOND_LETTER_CODE > ord('z') or SECOND_LETTER_CODE < ord('a'):
        print("Второй символ не является латинской буквой или введено с большой буквы")
    else:
        FIRST_LETTER_PLACE = abs(FIRST_LETTER_CODE - ord('a')) + 1
        SECOND_LETTER_PLACE = abs(SECOND_LETTER_CODE - ord('a')) + 1
        DISTANCE = abs(SECOND_LETTER_CODE - FIRST_LETTER_CODE) - 1
        print(f"Первая буква стоит на {FIRST_LETTER_PLACE} месте")
        print(f"Вторая буква стоит на {SECOND_LETTER_PLACE} месте")
        print(f"Расстояние между буквами равно {DISTANCE}")
except TypeError:
    print("Нужно ввести символы")
