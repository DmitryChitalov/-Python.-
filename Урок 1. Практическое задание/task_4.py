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

low = input('Enter the lower limit: ')
high = input('Enter the high limit: ')

print('Choose the option: \n1. Random integer \n2. Random float \n3. Random char')
option = int(input('Option: '))

if option == 1:
    result = int(random() * (int(high) - int(low) + 1) + int(low))
elif option == 2:
    result = random() * (float(high) - float(low)) + float(high)
elif option == 3:
    result = chr(int(random() * (ord(high) - ord(low) + 1) + ord(low)))
else:
    print('Wrong option!')
print(result)
