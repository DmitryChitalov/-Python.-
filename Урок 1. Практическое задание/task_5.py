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
while True:
    try:
        print('Введите две маленькие буквы')
        VAL1 = input('Первая: ')
        VAL2 = input('Вторая: ')
        RESULT = ord(VAL1) - ord(VAL2)
        if RESULT < 0:
            print(f'Растояние между буквами: {(RESULT * -1) - 1}')
            break
        print(f'Растояние между буквами: {RESULT - 1}')
        break
    except TypeError:
        print(f'Ошибка ввода')
