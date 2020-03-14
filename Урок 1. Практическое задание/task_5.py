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


# Ожидает на ввод латинский строчный символ. Повторяет попытку ввода, пока не введено корректно
def input_char(string):
    while True:
        char = input(f"Введите {string} латинский строчный символ\n")
        if len(char) == 1 and 'a' <= char <= 'z':
            break
        else:
            print("Введен недопустимый символ")
    return char


first_char = input_char("первый")
second_char = input_char("второй")
distance = abs(ord(first_char) - ord(second_char))
ord_first = ord(first_char) - ord('a') + 1
ord_second = ord(second_char) - ord('a') + 1
print(
    f"{first_char} - {ord_first} символ алфавита, {second_char} - {ord_second} символ алфавита, разница между ними {distance}")
