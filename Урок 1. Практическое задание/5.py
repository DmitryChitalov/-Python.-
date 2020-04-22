#!/usr/local/bin/python3

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


print("Введите грацины диапозона")
symbol_left = input("Левая граница: ")
symbol_right_border = input("Правая граница: ")
letters = abs(ord(symbol_left) - ord(symbol_right_border)) - 1
position_letter_1 = ord(symbol_left) - 96
position_letter_2 = ord(symbol_right_border) - 96
print(position_letter_1)
print(position_letter_2)
