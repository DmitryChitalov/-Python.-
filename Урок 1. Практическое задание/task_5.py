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
A = ord(input('1-я буква: '))
B = ord(input('2-я буква: '))
A = A - ord('A') + 1
B = B - ord('A') + 1
print('Позиции: %d и %d' % (A, B))
print('Между буквами символов:', abs(A - A) - 1)
