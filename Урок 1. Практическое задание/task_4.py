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
from random import randrange



LEFT = int(input("Минимальная граница: "))
RIGHT = int(input("Максимальная граница: "))
NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
print(NUMB)

LEFT = float(input("Минимальная граница: "))
RIGHT = float(input("Максимальная граница: "))
NUMB = random() * (RIGHT - LEFT) + LEFT
print(round(NUMB, 3))



#     случайный символ в интервале

LETTER_1 = input('input a 1st letter ')
LETTER_NUMB_1 = (ord(LETTER_1))
FIRST_DIFF = LETTER_NUMB_1 - 97  

LETTER_2 = input('input a second letter ')
LETTER_NUMB_2 = (ord(LETTER_2))
SECOND_DIFF = LETTER_NUMB_2 - 97 

print(chr(randrange(97+ FIRST_DIFF, 97 + SECOND_DIFF + 1)))