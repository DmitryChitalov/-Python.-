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
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
FIRST = input("Введите первую букву (латинскую, прописную): ")
SECOND = input("Введите вторую букву (латинскую, прописную): ")
FIRST_PLACE = (ALPHABET.index(FIRST)) + 1
SECOND_PLACE = (ALPHABET.index(SECOND)) + 1
print(f'Буква {FIRST} имеет {FIRST_PLACE} место в алфавите')
print(f'Буква {SECOND} имеет {SECOND_PLACE} место в алфавите')
if FIRST_PLACE < SECOND_PLACE:
    if 5 > (SECOND_PLACE - FIRST_PLACE - 1) > 1:
        print(f'Между ними {SECOND_PLACE - FIRST_PLACE - 1} буквы')
    elif (SECOND_PLACE - FIRST_PLACE - 1) > 4:
        print(f'Между ними {SECOND_PLACE - FIRST_PLACE - 1} букв')
    else:
        print(f'Между ними {SECOND_PLACE - FIRST_PLACE - 1} буква')
elif SECOND_PLACE < FIRST_PLACE:
    if 5 > (FIRST_PLACE - SECOND_PLACE - 1) > 1:
        print(f'Между ними {FIRST_PLACE - SECOND_PLACE - 1} буквы')
    elif (FIRST_PLACE - SECOND_PLACE - 1) > 4:
        print(f'Между ними {FIRST_PLACE - SECOND_PLACE - 1} букв')
    else:
        print(f'Между ними {FIRST_PLACE - SECOND_PLACE - 1} буква')
else:
    print('Между ними нет букв')