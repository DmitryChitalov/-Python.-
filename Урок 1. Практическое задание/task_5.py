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

first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

if ord(first_letter) > 1000 and ord(second_letter) > 1000:
    print(f'Букв между: {abs(ord(first_letter) - ord(second_letter)) - 1 if first_letter != second_letter else 0}')
    print(f'Первая буква стоит на месте {ord(first_letter) - 1072 + 1}')
    print(f'Вторая буква стоит на месте {ord(second_letter) - 1072 + 1}')
elif ord(first_letter) < 123 and ord(second_letter) < 123:
    print(f'Букв между: {abs(ord(first_letter) - ord(second_letter)) - 1 if first_letter != second_letter else 0}')
    print(f'Первая буква стоит на месте {ord(first_letter) - 97 + 1}')
    print(f'Вторая буква стоит на месте {ord(second_letter) - 97 + 1}')
else:  # не учитывал язки, отличные от en, ru
    print('Вы ввели буквы из рвзных языков')
