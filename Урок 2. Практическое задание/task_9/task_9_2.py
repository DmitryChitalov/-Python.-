"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

# данные
TOTAL = int(input('Введите сколько будет чисел \n'))


# тут цикл
def comparior(total, max_sum=0, i=1):
    """сравнивает сумму"""
    while total > 0:
        row = int(input(f'введите число {i} : '))
        row_sum = sum_row(row)
        total -= 1
        i += 1

        if max_sum <= row_sum:
            max_sum = row_sum
            max_row = row

    return max_sum, max_row

# тут рекурсия
def sum_row(row):
    """  сумма чисел"""
    if len(str(row)) == 1:
        summ = int(row)
        return summ
    else:
        summ = row % 10 + sum_row(row // 10)
        return summ


# поехали
MAX_SUM, ROW = comparior(TOTAL)

print(f'самое большая сумма : {MAX_SUM}, в ряду "{ROW}"')
