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
ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import sys
from random import randint
import timeit

sys.setrecursionlimit(10000)

# чего считаем
TOTAL = int(input('Введите сколько будет чисел \n'))
NUMBER = int(input('Введите цифру, которою будем считать \n'))

# цикл начало
def circle(total, number, coinsedence=0):
    i = 0
    row_number = 1
    while i < total:
        row = randint(0, 1000)
        row_number = row_number + 1
        row_length = len(str(row))

        k = 1
        while k <= row_length:
            check = row % 10
            if check == number:
                coinsedence = coinsedence + 1

            row = row // 10
            k = k + 1
        i = i + 1
    return coinsedence
# цикл конец
# рекурсия начало
def counter(row, number, coinsedence=0):
    """ситает количество цифер в ряд"""
    if len(str(row)) == 1:
        if row == number:
            coinsedence += 1
            return coinsedence
        else:
            return coinsedence
    else:
        check = row % 10
        if check == number:
            coinsedence += 1
            coinsedence = coinsedence + counter(row // 10, number)
            return coinsedence
        else:
            coinsedence = coinsedence + counter(row // 10, number)
            return coinsedence


def row_maker(total, number, coinsedence=0, i=1):
    """делает ряды цифры"""
    if i == total:
        row = randint(0, 1000)
        coinsedence = counter(row, number, coinsedence)
        return coinsedence
    else:
        row = randint(0, 1000)
        coinsedence = counter(row, number, coinsedence)
        coinsedence = row_maker(total, number, coinsedence, i + 1)
        return coinsedence
# рекурсия конец

# рекурсия + цикл
def row_maker_1(total, number, coinsedence=0, i=1):
    """делает ряды цифры"""
    while i <= total:
        row = randint(0, 1000)
        coinsedence = counter(row, number, coinsedence)
        i += 1
    return coinsedence


print(timeit.timeit("circle(TOTAL, NUMBER)", setup="from __main__ import circle, TOTAL, NUMBER", number=100))
print(timeit.timeit("row_maker(TOTAL, NUMBER)", setup="from __main__ import row_maker, TOTAL, NUMBER", number=100))
print(timeit.timeit("row_maker_1(TOTAL, NUMBER)", setup="from __main__ import row_maker_1, TOTAL, NUMBER", number=100))

'''
Количество чисел: 10
цикл     - 0.0021632999999994244
рекурсия - 0.0030243999999992611

Количество чисел: 100
цикл     - 0.01614460000000051
рекурсия - 0.02332409999999996

Количество чисел: 300
цикл     - 0.05277320000000074
рекурсия - 0.06728069999999953

Количество чисел: 500
цикл     - 0.08030800000000049
рекурсия - 0.1156915999999999

Количество чисел: 1000
цикл     - 0.17313890000000054
рекурсия - 0.23036679999999965

Количество чисел: 5000
цикл     - 0.8379273000000005
рекурсия - 1.25411210000000045

Количество чисел: 10000
цикл     - 1.6597231
рекурсия -  MemoryError: stack overflow( пробывал стак до 10000000 тоже самое)

сложноть и того и того O(n^2)
как можно увидеть цикл быстрее и проще, чем делать вызов рекурсии из под рекурсии.
и работает с ограниченным количестов чисел. 

Уберем рекурсию из создания списка:

Количество чисел: 10
время - 0.0027913999999995553

Количество чисел: 100
время - 0.0204062000000000

Количество чисел: 1000
время - 0.21313269999999918

Количество чисел: 10000
время - 2.112644399999999

Количество чисел: 100000
время - 21.257967100000002
(для цикла - 16.7603206)

Итог:
в данном примере рекурсия вредная.  она ограничена в использовании и требует больше времяни.

'''

