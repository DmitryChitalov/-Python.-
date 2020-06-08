"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def letter_by_alphabet_order(number):
    try:
        letter_number = int(number) + 96
        symbol = chr(letter_number).lower()
        if symbol in LETTERS:
            return symbol
        else:
            raise Exception
    except Exception:
        return "Enter number between 1 and 26."


num = input("Enter number of letter from alphabet: ")
letter_by_number = letter_by_alphabet_order(num)
print(letter_by_number)
