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
a = ord(input('Введите 1-ую букву: '))
b = ord(input('Введите 2-ую букву: '))
# Для русского алфавита заменить англ. букву А на русскую А
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'Позиции:{a} и {b} ')
print('Между буквами символов:', abs(a - b) - 1)
