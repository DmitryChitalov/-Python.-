#!/usr/local/bin/python3

"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d
Подсказка: используйте ф-ции chr() и ord()
"""


number_of_letter = int(input("Номер буквы: "))
if number_of_letter > 26:
    print("Значение выходит за диапозон алфавита")
else:
    position_letter_1 = number_of_letter + 96
    print(chr(position_letter_1))
