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

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

# ввод
TOTAL = int(input('Введите сколько будет чисел \n'))
NUMBER = int(input('Введите цифру, которо будем считать \n'))


# cчиталка
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


#  циклом
# def row_maker(total, number=NUMBER, coinsedence=0, i=1):
#     """делает ряды цифры"""
#     while i <= total:
#         row = int(input(f'введите число {i}: '))
#         coinsedence = counter(row, number, coinsedence)
#         i += 1
#     return coinsedence

#  рекурсией
def row_maker(total, number=NUMBER, coinsedence=0, i=1):
    """делает ряды цифры"""
    if i == total:
        row = int(input(f'введите число {i}: '))
        coinsedence = counter(row, number, coinsedence)
        return coinsedence
    else:
        row = int(input(f'введите число {i}: '))
        coinsedence = counter(row, number, coinsedence)
        coinsedence = row_maker(total, number, coinsedence, i + 1)
        return coinsedence


# поехали
COINSEDENCE = row_maker(TOTAL)
print(f'Было введено {COINSEDENCE} цифр "{NUMBER}"')
