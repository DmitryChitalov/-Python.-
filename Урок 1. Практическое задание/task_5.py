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

LATIN_ALPHABET = 96
FIRST_LETTER = input("Введите первый символ латинского алфавита: ")
SECOND_LETTER = input("Введите второй символ латинского алфавита: ")
# Проверка на количество букв, которые введены (не должно быть больше 1)
if len(FIRST_LETTER) != 1 or len(SECOND_LETTER) != 1:
    print('Необходимо вводить один символ!')
# Проверка, что введённые символы входят в латинский алфавит
elif ord(FIRST_LETTER) > 122 or ord(FIRST_LETTER) < 97 \
        or ord(SECOND_LETTER) > 122 or ord(SECOND_LETTER) < 97:
    print('Необходимо вводить символы латинского алфавита!')
else:
    # Приводим введённые буквы к их номеру в Юникоде
    FIRST_LETTER = ord(FIRST_LETTER)
    SECOND_LETTER = ord(SECOND_LETTER)
    # меняем местами буквы, если левая пограничная буква больше правой
    if FIRST_LETTER > SECOND_LETTER:
        FIRST_LETTER, SECOND_LETTER = SECOND_LETTER, FIRST_LETTER
        print(f'''Место в алфавите первой буквы: {FIRST_LETTER - LATIN_ALPHABET}
        Место в алфавите второй буквы {SECOND_LETTER - LATIN_ALPHABET}
        Между этими буквами {SECOND_LETTER - FIRST_LETTER - 1}''')
    else:
        print(f'''Место в алфавите первой буквы: {FIRST_LETTER - LATIN_ALPHABET}
Место в алфавите второй буквы {SECOND_LETTER - LATIN_ALPHABET}
Между этими буквами {SECOND_LETTER - FIRST_LETTER - 1}''')
