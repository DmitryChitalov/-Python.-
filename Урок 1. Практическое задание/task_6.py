"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""

NUMB = int(input('Введите номер буквы в алфавите от 1 до 26: '))
print(f"На {NUMB} месте в алфавите стоит буква {chr(NUMB + 96)}")
