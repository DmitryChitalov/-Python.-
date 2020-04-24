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
LETTER_A = ord(input('Введите первую букву:'))
LETTER_B = ord(input('Введите вторую букву:'))
if LETTER_A > LETTER_B:
    LETTER_A, LETTER_B = LETTER_B, LETTER_A
DISTANCE = LETTER_B - LETTER_A - 1
print(f'Буква "{chr(LETTER_A)}" в алфавите на позиции {LETTER_A - 96}')
print(f'Буква "{chr(LETTER_B)}" в алфавите на позиции {LETTER_B - 96}')
print(f'Между ними {DISTANCE} букв')
