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
    first_char = ord(input("First char - "))
    second_char = ord(input("Second char - "))

    first_char_place = first_char - ord('a') + 1
    second_char_place = second_char - ord('a') + 1

    dif = abs(first_char_place - second_char_place) - 1

    print(f"Place of first char - {first_char_place}")
    print(f"Place of second char - {second_char_place}")
    print(f"Number chars between - {dif}")
except ValueError:
    print("You entered an incorrect value.")
