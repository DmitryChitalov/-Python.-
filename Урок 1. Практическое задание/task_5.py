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

FIRST_LETTER = input("Введите одну букву латинского алфавита: ")
SECOND_LETTER = input("Введите другую букву латинского алфавита: ")
print("Буква", FIRST_LETTER, "стоит на", str(ord(FIRST_LETTER) - 96), "месте")
print("Буква", SECOND_LETTER, "стоит на", str(ord(SECOND_LETTER) - 96), "месте")
if ord(FIRST_LETTER) < ord(SECOND_LETTER):
    print("Между буквами", FIRST_LETTER, "и", SECOND_LETTER, ord(SECOND_LETTER) -
          ord(FIRST_LETTER) -1, "букв")
else:
    print("Между буквами", FIRST_LETTER, "и", SECOND_LETTER, ord(FIRST_LETTER) -
          ord(SECOND_LETTER) -1, "букв")
