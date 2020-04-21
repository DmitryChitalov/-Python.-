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

LOW = input('Enter the lower limit: ')
HIGH = input('Enter the high limit: ')

print('Choose the option: \n1. Random integer \n2. Random float \n3. Random char')
OPTION = int(input('Option: '))

if OPTION == 1:
    RESULT = int(random() * (int(HIGH) - int(LOW) + 1) + int(LOW))
elif OPTION == 2:
    RESULT = random() * (float(HIGH) - float(LOW)) + float(HIGH)
elif OPTION == 3:
    RESULT = chr(int(random() * (ord(HIGH) - ord(LOW) + 1) + ord(LOW)))
else:
    print('Wrong option!')
print(RESULT)
