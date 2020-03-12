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

import string

try:
    LEFT = ord(input("First letter: ")) - ord('a') + 1
    RIGHT = ord(input("Second letter: ")) - ord('a') + 1
    print(f"Quantity of symbols between two letters: {abs(LEFT - RIGHT) - 1}")

except ValueError:
    print('Incorrect')
