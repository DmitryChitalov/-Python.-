"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""
print('Введите номер буквы в алфавите от 1 до 26:')
num = int(input())
char = chr(num + 64)
print(f'Это буква "{char}"')