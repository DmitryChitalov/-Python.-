"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def check_eq(num, last_num=1, sum_nums=0):
    """

    :param num:
    :param last_num:
    :param sum_nums:
    :return:
    """
    if last_num == num:
        return sum_nums + last_num
    sum_nums = check_eq(num, last_num + 1, sum_nums)
    return sum_nums + last_num

NUM = int(input('Введите любое натуральное число, для которого '
                'выполнять проверку равенства 1+2+...+n = n(n+1)/2: '))
SUM = check_eq(NUM)
print(f'1+2+...+n = {SUM}')
print(f'n(n+1)/2 = {int(NUM * (NUM + 1) / 2)}')
if SUM == NUM * (NUM + 1) / 2:
    print(f'Для числа {NUM} выполняется равенство 1+2+...+n = n(n+1)/2')
else:
    print(f'Для числа {NUM} не выполняется равенство 1+2+...+n = n(n+1)/2')
