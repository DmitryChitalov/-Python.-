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

first_entered_letter = input("Enter the first letter: ").lower()
second_entered_letter = input("Enter the second letter: ").lower()

pos_left = ord(first_entered_letter) - ord("a") + 1
pos_right = ord(second_entered_letter) - ord("a") + 1
length = abs(pos_left - pos_right) - 1

print(f'The number of {first_entered_letter} is {pos_left}')
print(f'The number of {second_entered_letter} is {pos_right}')
print(f'There are {length} letters between them')
