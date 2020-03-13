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


print("Введите грацины диапозона")
SYMBOL_LEFT_BORDER = input("Левая граница: ")
SYMBOL_RIGHT_BORDER = input("Правая граница: ")
if SYMBOL_LEFT_BORDER.isalpha and SYMBOL_RIGHT_BORDER.isdigit():
    SYMBOL_LEFT_BORDER = int(SYMBOL_LEFT_BORDER)
    SYMBOL_RIGHT_BORDER = int(SYMBOL_RIGHT_BORDER)
    NUMB = int(random() * (SYMBOL_RIGHT_BORDER - SYMBOL_LEFT_BORDER + 1)
               + SYMBOL_LEFT_BORDER)
    print(NUMB)
elif SYMBOL_LEFT_BORDER.isalpha() and SYMBOL_RIGHT_BORDER.isalpha():
    if ord(SYMBOL_LEFT_BORDER) < 975 and ord(SYMBOL_RIGHT_BORDER) < 975:
        RAND_SYM = int(random() * (ord(SYMBOL_RIGHT_BORDER) -
                       ord(SYMBOL_LEFT_BORDER))) + ord(SYMBOL_LEFT_BORDER)
        RAND_SYM = chr(RAND_SYM)
        print(RAND_SYM)
    else:
        print("Один из символов введен на русском языке")
else:
    SYMBOL_LEFT_BORDER = float(SYMBOL_LEFT_BORDER)
    SYMBOL_RIGHT_BORDER = float(SYMBOL_RIGHT_BORDER)
    NUMB = random() * (float(SYMBOL_RIGHT_BORDER) -
                       float(SYMBOL_LEFT_BORDER)) + float(SYMBOL_LEFT_BORDER)
    print(NUMB)