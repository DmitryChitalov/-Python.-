"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""


from random import random


LEFT = input("Минимальная граница: ")
RIGHT = input("Максимальная граница: ")
if LEFT.isdigit() and RIGHT.isdigit():
    NUMB = int(random() * (int(RIGHT) - int(LEFT) + 1)) + int(LEFT)
    print(NUMB)

elif LEFT.isalpha() and RIGHT.isalpha():
    if (len(LEFT) == 1) and (len(RIGHT) == 1):
        N = int(random() * (ord(RIGHT) - ord(LEFT) + 1)) + ord(LEFT)
        print(chr(N))
    else:
        print("Неверный ввод")
else:
    NUMB = random() * (float(RIGHT) - float(LEFT)) + float(LEFT)
    print(round(NUMB, 3))
