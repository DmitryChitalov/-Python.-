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
import sys

BOOKVA1 = ord(input('Введите первую букву: '))
BOOKVA2 = ord(input('Введите вторую букву: '))

if BOOKVA1 == BOOKVA2:
    print("Буквы одинаковы.")
    sys.exit(0)

BOOKVA1 = BOOKVA1 - ord('a') + 1
BOOKVA2 = BOOKVA2 - ord('a') + 1

print(f"Позиции введенных букв : {BOOKVA1} и {BOOKVA2}")
print(f"Количество символов между буквами : {abs(BOOKVA1 - BOOKVA2) - 1}")
