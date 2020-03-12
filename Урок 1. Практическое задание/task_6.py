"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""


try:
    NUMB = int(input("First number of letter: "))
    print(f"The numbers corresponds to the letter: {chr(NUMB+96)}")
except ValueError:
    print('Incorrect')
