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

try:
    ER_STRING = 'Ошибка ввода!'
    CODE_A = 97
    CODE_Z = 122

    first_letter_code = ord(str(input('Введите первую букву: ')).lower())
    second_letter_code = ord(str(input('Введите вторую букву: ')).lower())

    if first_letter_code < CODE_A or first_letter_code > CODE_Z  or second_letter_code < CODE_A or second_letter_code > CODE_Z :
        print(ER_STRING)
    elif first_letter_code == second_letter_code:
        print('Буквы одинаковые')
    else:
        print('Букв между введенным буквами : %d ' %(abs(first_letter_code - second_letter_code)-1))
except:
    print(ER_STRING)