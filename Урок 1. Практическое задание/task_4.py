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
import random
import string as list_symbols


start = int(input('Введите первое число: '))
stop = int(input('Введите второе число: '))
step = random.randrange(start, stop, 5)
symbols_list = list(list_symbols.printable)


integer = random.randrange(start, stop, step)
float_number = random.randrange(start, stop, step) / step
print(f'Случайное целое число: {integer}')
print(f'Случайное вещественное число: {float_number}')
print(f'Случайное символ: {symbols_list[integer+9]}')
