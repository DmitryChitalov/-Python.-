"""
Задание 4. Написать программу, которая генерирует в указанных
пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random

print("Please choose:\n"
      "1. Random integer\n"
      "2. Random real number\n"
      "3. Random char")
user_choose = int(input("Your choose - "))

if user_choose == 1:
    print("\nRandom integer.")
    int_start = int(input("Start number - "))
    int_end = int(input("End number - "))

    if int_start < int_start:
        int_rand = int((int_end - int_start) * random()) + int_start
    else:
        int_rand = int((int_start - int_end) * random()) + int_end
    print(f"Your random integer number - {int_rand}")
elif user_choose == 2:
    print("\nRandom real number.")
    float_start = float(input("Start number - "))
    float_end = float(input("End number - "))

    if float_start < float_start:
        float_rand = round((float_end - float_start)
                           * random() + float_start, 5)
    else:
        float_rand = round((float_start - float_end) * random() + float_end, 5)
    print(f"Your random real number - {float_rand}")
elif user_choose == 3:
    print("\nRandom char.")
    char_start = ord(input("Start char - "))
    char_end = ord(input("End char - "))

    if char_start < char_start:
        char_rand = int((char_end - char_start) * random()) + char_start
    else:
        char_rand = int((char_start - char_end) * random()) + char_end
    print(f"Your random char - {chr(char_rand)}")
