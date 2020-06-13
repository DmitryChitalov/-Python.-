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

quantity_num = int(input('Сколько будет чисел?'))
need_num = int(input('Какую цифру считать? '))


def rec9(seq_num, need_num):
    c = 0
    if seq_num < 10:
        if seq_num == need_num:
            c += 1
        return c
    else:
        rem = seq_num % 10
        if rem == need_num:
            c += 1
        return c + rec9(seq_num // 10, need_num)


count_num = 0
for i in range(1, quantity_num + 1):
    num = int(input(f'Число {i} : '))
    count_num += rec9(num, need_num)

print(f'в рассмотреных числах {need_num} встретится {count_num} раз')
