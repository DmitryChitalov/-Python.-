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
print('Ведите две прописные буквы латинского алфавита:')
char1 = input('char1 = ')
char2 = input('char2 = ')

pos_char1 = ord(char1) - 64
pos_char2 = ord(char2) - 64
distance = abs(pos_char1 - pos_char2) - 1
print(f'Буква "{char1}" {pos_char1}-я в алфавите\n'
      f'Буква "{char2}" {pos_char2}-я в алфавите\n'
      f'Между буквами {distance} букв')