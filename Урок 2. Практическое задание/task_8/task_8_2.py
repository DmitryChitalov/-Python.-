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

TOTAL = 3  # int(input('Введите сколько будет чисел \n'))
NUMBER = 3  # int(input('Введите цифру, которо будем считать \n'))
ROW = int("3")


# def counter(row, number, coinsedence):
#     """ситает количество цифер в ряд"""
#     if len(str(row)) == 1:
#         if int(row) == number:
#             coinsedence += 1
#             return coinsedence
#         else:
#             return coinsedence
#     else:
#         check = int(row % 10)
#         if check == number:
#             coinsedence += 1
#             coinsedence = coinsedence + counter(row // 10, number)
#             return coinsedence
#         else:
#             coinsedence = coinsedence + counter(row // 10, number)
#             return coinsedence


def row_maker(total, r_number=1):
    """делает ряды цифры"""
    while r_number <= total:
        row = int(input(f"Введите число {r_number}: "))
        print(row)
        r_number += 1
    return r_numbersssssssssssssssssssssssssssssssssssssssssssssss

R_NUMBER = row_maker(TOTAL)
print(f'{R_NUMBER-}')

# print(f'Было введено {COINSEDENCE} цифры "{NUMBER}"')
