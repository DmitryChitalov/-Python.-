from random import random


class EqualValues(Exception):
    pass


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
print('Случайное целое число')
try:
    n1 = int(input('Введите первое целое число : '))
    n2 = int(input('Введите второе целое число : '))
    if n1 > n2:
        max_n, min_n = n1, n2
    elif n2 > n1:
        max_n, min_n = n2, n1
    else:
        raise EqualValues('Введенные числа равны, '
                          'вычислить случайное число невозможно')
    result = int(random() * (max_n - min_n + 1) + min_n)
    print(result)
except EqualValues as e:
    print(e)
except ValueError:
    print('Необходимо ввести целые числа.')

print('Случайное вещественное число')
try:
    n1 = float(input('Введите первое вещественное число : '))
    n2 = float(input('Введите второе вещественное число : '))
    if n1 > n2:
        max_n, min_n = n1, n2
    elif n2 > n1:
        max_n, min_n = n2, n1
    else:
        raise EqualValues('Введенные числа равны, '
                          'вычислить случайное число невозможно')
    result = random() * (max_n - min_n) + min_n
    print(round(result, 2))
except EqualValues as e:
    print(e)
except ValueError:
    print('Необходимо ввести числа.')

print('Случайный символ')
try:
    s1 = input('Введите первый символ: ')
    pos_s1 = ord(s1)
    s2 = input('Введите второй символ: ')
    pos_s2 = ord(s2)
    if pos_s1 > pos_s2:
        left, right = pos_s2, pos_s1
    elif pos_s2 > pos_s1:
        left, right = pos_s1, pos_s2
    else:
        raise EqualValues('Введено два одинаковых символа')
    result = int(random() * (right - left + 1) + left)
    print(chr(result))
except EqualValues as e:
    print(e)
except TypeError:
    print('Необходимо ввести один символ.')
