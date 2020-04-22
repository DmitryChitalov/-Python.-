"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

while True:
    try:
        LETTER_1: str = input('Введите первую букву латинского алфавита: ').lower()
        LETTER_2: str = input('Введите вторую букву латинского алфавита: ').lower()
        if LETTER_1.isalpha() and LETTER_2.isalpha() and ord(LETTER_1) in range(97, 123) \
                and ord(LETTER_2) in range(97, 122):
            FIRST = (ord(LETTER_1) - 96)
            LAST = (ord(LETTER_2) - 96)
            COUNT_LETTERS = abs(LAST - FIRST) - 1
            print(f'Количество символов между указанными = {COUNT_LETTERS}')
            print(f'Место первой буквы = {FIRST}')
            print(f'Место второй буквы = {LAST}')
            break
        else:
            raise ValueError
    except ValueError or TypeError:
        print('Ошибка ввода. Необходимо ввести буквы латинского алфавита.')
