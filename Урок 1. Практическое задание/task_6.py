"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""


a = "abcdefghijklmnopqrstuvwxyz"
searchuser = int(input()) - 1
userletter = a[searchuser]
print(userletter)