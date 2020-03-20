"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'
"""

# Задача решена не до конца. Не могу найти решение как возвращать из рекурсии значения и потом складывать их. Либо
# как складывать их прямо в рекурсии и потом вернуть эту сумму. А у меня получается, что возвращается только первое
# значение. Я понимаю почему - это же стек вызовов, но как сделать
# правильно я не додумался.
NUMBER_COUNTER = int(input('Сколько будет чисел? - '))
NUMBER = int(input('Какую цифру считать? - '))


def units(number):
    return number % 10


def count(number, num):
    counter = 0
    len_num = len(str(number))
    while len_num > 0:
        unit = units(number)
        number //= 10
        if unit == num:
            counter += 1
        len_num -= 1
    return counter


def count_number(steps, num, counter=0):
    if steps != 0:
        number = int(input(f'Число {steps}: '))
        counter = count(number, num)
        count_number(steps - 1, num, counter)
        counter += counter
    return counter


print(count_number(NUMBER_COUNTER, NUMBER))
