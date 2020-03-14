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


# Ожидает на ввод число. Повторяет попытку ввода, пока не введено корректно
def input_number(string):
    while True:
        try:
            number = input(f"Введите {string} целое число\n")
            number = int(number)
            break
        except ValueError:
            print("Не удалось преобразовать в число")
    return number


# Ожидает на ввод длину отрезка. Повторяет попытку ввода, пока не введено целое
def input_float(string):
    while True:
        try:
            number = input(f"Введите {string} действительное число\n")
            number = float(number)
            if 0 <= abs(number):
                break
            else:
                print("Введено некорректное число")
        except ValueError:
            print("Не удалось преобразовать в число")
    return number


# Ожидает на ввод латинский строчный символ. Повторяет попытку ввода, пока не введено корректно
def input_char(string):
    while True:
        char = input(f"Введите {string} латинский строчный символ\n")
        if len(char) == 1 and 'a' <= char <= 'z':
            break
        else:
            print("Введен недопустимый символ")
    return char


# Выводит случайное значение из диапазона, заданного пользователем. Первое значение может быть больше второго
choice = input("Для целых чисел введите 'n', для действительных 'f', для символов 'c'\n")
rand = random.random()
if choice == 'n':
    # Случайное целое число
    first = input_number("первое")
    second = input_number("второе")
    result = int((abs(first - second) + 1) * rand + min(first, second))
elif choice == 'f':
    # Случайное действительное число
    first = input_float("первое")
    second = input_float("второе")
    result = (abs(first - second)) * rand + min(first, second)
elif choice == 'c':
    # Случайный символ
    first = input_char("первый")
    second = input_char("второй")
    ord_first = ord(first)
    ord_second = ord(second)
    result = chr(int((abs(ord_first - ord_second) + 1) * rand + min(ord_first, ord_second)))
else:
    print("Некорректный ввод")
    exit(-1)
print(result)
