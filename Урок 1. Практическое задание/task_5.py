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

first_str = input('Введите первую букву: ')
second_str = input('Введите вторую букву: ')
if len(first_str) == 1 and len(second_str) == 1:
    print(ord(first_str))
else:
    print('Эх... что-то не так с вводом')
