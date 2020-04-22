"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.
"""

while True:
    try:
        LETTER = int(input('Введите число : '))
        if LETTER in range(0, 28):
            print(f'Введенный номер соотвествует букве : {chr(LETTER + 96)}')
            break
        else:
            raise ValueError
    except ValueError or TypeError:
        print('Ошибка ввода. Введите число от 1 до 26 (в соответствии с буквой латинского алфавита).')
