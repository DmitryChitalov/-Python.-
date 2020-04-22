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

LETTER_1 = input('input a 1st letter ')
LETTER_NUMB_1 = (ord(LETTER_1))
LETTER_2 = input('input a second letter ')
LETTER_NUMB_2 = (ord(LETTER_2))
NUMB_DIFF = LETTER_NUMB_2 - LETTER_NUMB_1-1
if NUMB_DIFF < 0:
    NUMB_DIFF = LETTER_NUMB_2 - LETTER_NUMB_1+1
    NUMB_DIFF *= -1
    print('Между ',LETTER_1, ' и ',LETTER_2,' находится', NUMB_DIFF,' букв')

else:
    print('Между ',LETTER_1, ' и ',LETTER_2,' находится', NUMB_DIFF,' букв')


