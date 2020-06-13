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
qunt_nut_num = int(input('Введите количество чисел: '))


# def summ(num):
#     sum_num = 0
#     for p in num:
#         sum_num += int(p)
#     return sum_num`

def rec_summ(num):
    if num < 10:
        return num
    else:
        return num % 10 + rec_summ(num // 10)


sum_max_num = 0
number_max_sum = 0

for i in range(1, qunt_nut_num + 1):
    num_num = int(input('Введите очередное число: '))
    if rec_summ(num_num) > sum_max_num:
        sum_max_num = rec_summ(num_num)
        number_max_sum = num_num
print(f'Наибольшее число по сумме цифр: {number_max_sum},'
      f' сумма его цифр: {sum_max_num}')