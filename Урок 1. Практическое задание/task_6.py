"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""
first_letter = 97
# last_letter = 122
# quantity_letters = last_letter - first_letter +1
letter_num = int(input('enter any letter_num from 1 to 26 :')) + first_letter - 1
letter_usually = chr(letter_num)

print(f'вводимая буква {letter_usually}')
